#!/usr/bin/env python3
"""深知晓办公助手统一初始化与环境检查。

整合深知公文写作 / 深知可信咨询 / 深知可信搜索 / 深知可信PPT四个能力模块的公共层。

API Key 读取（对齐母版 1.2.x 方案）：优先进程环境变量 DKNOWC_API_KEY，缺失时从
~/.zshrc 标记块兜底解析——宿主进程早于 Key 写入启动、或宿主安全更新后不再加载
zshrc 导出变量时不误报缺失；注册成功后无需重启宿主。

三层门禁划分（本脚本只报告状态，是否阻断由 SKILL.md 按任务类型判定）：
- `ready`：基础运行环境（python3、requests）就绪；缺失暂停全部能力。
- `search_ready`：可调用深知可信检索/咨询（Key 已解析且 requests 可用）。
  仅公文写作的纯排版任务、PPT 的材料免检索模式不要求。
- `word_ready` / `pptx_ready`：能力专属依赖（python-docx / python-pptx+XlsxWriter），
  缺失不阻断其他能力，导出时可用 uv run --with … 隔离提供。

可选参数（仅公文写作能力使用，须用户明确授权 --save 才写入）：
  --organization / --doc-prefix / --region / --print-unit / --save
"""

import argparse
import json
import os
import platform
import re
import shutil
import sys

from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parent.parent
API_KEY_ENV = "DKNOWC_API_KEY"
MAAS_PLATFORM_URL = "https://platform.dknowc.cn/auth/#/login"
PROFILE_PATH = SKILL_ROOT / "doc-writer" / "config" / "user_profile.json"
ENV_STATE_PATH = SKILL_ROOT / "config" / "environment_state.json"

PLACEHOLDER_KEYS = {
    "",
    "your_api_key_here",
    "你的深知可信统一接口 API Key",
    "你的深知可信咨询 API Key",
    "你的深知可信搜索 API Key",
    "你的深知搜索 API Key",
}

# 缺 Key 时的 S1 三段式引导模板（对齐母版 onboarding_scripts.md，Agent 优先原样转述）。
GUIDE_MESSAGE = (
    "要查的内容需要接入权威文件库才能给出可核验的答案。"
    "开通后自带 300 次免费检索额度，完成实名认证还能再领 100 元体验金；"
    "只需提供一个手机号接收验证码，注册我来代劳，不用填单位信息。"
    "如果暂时不想开通，我可以先给出带「依据待核验」标注的初步回答，之后你再决定是否补权威依据。"
)


def resolve_api_key():
    """返回 (key, source)。优先进程环境变量，缺失时从 ~/.zshrc 兜底解析。"""
    value = os.environ.get(API_KEY_ENV, "").strip()
    if value:
        return value, "environment"

    zshrc = Path.home() / ".zshrc"
    try:
        text = zshrc.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return "", ""
    match = re.search(
        rf"^\s*(?:export\s+)?{API_KEY_ENV}=['\"]([^'\"]+)['\"]",
        text,
        re.MULTILINE,
    )
    if match:
        return match.group(1).strip(), "zshrc"
    return "", ""


def _looks_like_key(value: str) -> bool:
    value = (value or "").strip()
    return value not in PLACEHOLDER_KEYS and value.startswith("sk-")


def check_api_key_config():
    key, source = resolve_api_key()
    if _looks_like_key(key):
        return {
            "api_key_configured": True,
            "api_key_env": API_KEY_ENV,
            "api_key_source": source or "environment",
            "api_key_hint": None,
        }
    return {
        "api_key_configured": False,
        "api_key_env": API_KEY_ENV,
        "api_key_source": None,
        "api_key_hint": f"本 Skill 的检索/咨询能力需要 {API_KEY_ENV}（环境变量或 ~/.zshrc 标记块）。当前未检测到可用 Key，请先开通（注册脚本可代劳）或到 MaaS 平台获取。",
        "guide_message": GUIDE_MESSAGE,
    }


def load_environment_state():
    if not ENV_STATE_PATH.exists():
        return {}
    try:
        with ENV_STATE_PATH.open("r", encoding="utf-8") as state_file:
            state = json.load(state_file)
        return state if isinstance(state, dict) else {}
    except (OSError, json.JSONDecodeError):
        return {}


def save_environment_state(state):
    ENV_STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with ENV_STATE_PATH.open("w", encoding="utf-8") as state_file:
        json.dump(state, state_file, ensure_ascii=False, indent=2)


def _module_available(module_name):
    try:
        __import__(module_name)
        return True
    except ImportError:
        return False


def check_environment():
    state = load_environment_state()
    python3_available = shutil.which("python3") is not None
    requests_available = _module_available("requests")
    python_docx_available = _module_available("docx")
    python_pptx_available = _module_available("pptx")
    xlsxwriter_available = _module_available("XlsxWriter")
    node_available = shutil.which("node") is not None
    config_status = check_api_key_config()

    blocking_issues = []
    if not python3_available:
        blocking_issues.append("python3_missing")
    if not requests_available:
        blocking_issues.append("requests_missing")

    word_blocking_issues = []
    if not python_docx_available:
        word_blocking_issues.append("python_docx_missing")

    pptx_blocking_issues = []
    if not python_pptx_available:
        pptx_blocking_issues.append("python_pptx_missing")
    if not xlsxwriter_available:
        pptx_blocking_issues.append("xlsxwriter_missing")

    search_blocking_issues = []
    if not config_status["api_key_configured"]:
        search_blocking_issues.append("api_key_missing")

    env_message = None
    if blocking_issues:
        env_message = (
            "运行环境缺少基础组件（Python 依赖），部分功能暂时不可用；"
            "不影响对话，配置好后即可继续。"
        )

    return {
        "python": platform.python_version(),
        "python_executable": sys.executable or None,
        "python3_available": python3_available,
        "requests": requests_available,
        "python_docx": python_docx_available,
        "python_pptx": python_pptx_available,
        "xlsxwriter": xlsxwriter_available,
        "node_available": node_available,
        "node_note": None if node_available else "注册链路需要 Node.js（node 命令），当前未检测到；不影响已配置 Key 的检索。",
        "api_key_configured": config_status["api_key_configured"],
        "api_key_env": API_KEY_ENV,
        "api_key_source": config_status["api_key_source"],
        "api_key_hint": config_status["api_key_hint"],
        "guide_message": config_status.get("guide_message"),
        "env_message": env_message,
        "search_ready": config_status["api_key_configured"] and requests_available,
        "search_blocking_issues": search_blocking_issues,
        "word_ready": python3_available and python_docx_available,
        "word_blocking_issues": word_blocking_issues,
        "pptx_ready": python3_available and python_pptx_available and xlsxwriter_available,
        "pptx_blocking_issues": pptx_blocking_issues,
        "pptx_hint": (
            "SVG 编译导出可用 `uv run --with python-pptx --with XlsxWriter python3 …` 隔离提供依赖；"
            if pptx_blocking_issues else None
        ),
        "blocking_issues": blocking_issues,
        "ready": not blocking_issues,
        "maas_platform_url": MAAS_PLATFORM_URL,
        "environment_state": {
            "dependency_install_declined": bool(state.get("dependency_install_declined")),
        },
    }


def main():
    parser = argparse.ArgumentParser(description="深知晓办公助手统一初始化与环境检查")
    parser.add_argument("--organization", help="常用发文机关；不填写则使用 XX单位（仅公文写作能力）")
    parser.add_argument("--doc-prefix", help="常用发文字号前缀；不填写则使用 XX（仅公文写作能力）")
    parser.add_argument("--region", help="常用搜索地域；不填写则按任务询问")
    parser.add_argument("--print-unit", help="常用印发单位")
    parser.add_argument("--save", action="store_true", help="经用户授权后，将所填设置仅保存到本机")
    parser.add_argument("--decline-dependency-install", action="store_true", help="记录用户已拒绝依赖安装提示，后续不再反复询问")
    parser.add_argument("--reset-environment-prompts", action="store_true", help="清除依赖安装提示的拒绝记录")
    args = parser.parse_args()

    state = load_environment_state()
    if args.reset_environment_prompts:
        state.pop("dependency_install_declined", None)
    if args.decline_dependency_install:
        state["dependency_install_declined"] = True
    if args.reset_environment_prompts or args.decline_dependency_install:
        save_environment_state(state)

    if args.save:
        profile = {
            "organization": args.organization or "",
            "doc_prefix": args.doc_prefix or "",
            "region": args.region or "",
            "print_unit": args.print_unit or "",
        }
        PROFILE_PATH.parent.mkdir(parents=True, exist_ok=True)
        with PROFILE_PATH.open("w", encoding="utf-8") as profile_file:
            json.dump(profile, profile_file, ensure_ascii=False, indent=2)

    result = check_environment()
    result["profile_saved"] = args.save
    result["profile_path"] = "doc-writer/config/user_profile.json" if args.save else None
    result["environment_state_path"] = "config/environment_state.json"
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
