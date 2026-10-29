# 深知晓办公助手（skills.sh 版）

深知晓办公助手由北京彩智科技有限公司旗下“深知可信智能”提供，是统一覆盖**公文写作、可信检索、PPT 生成**三大类办公场景的综合型 Agent Skill，并采用可扩展架构，未来可持续加入更多能力。三大能力共用同一套权威检索与可信溯源体系：公文写作交付 Word（可选红头）与三页产出物 HTML；可信检索交付直接答案与单文件三页 HTML（正文／溯源核验报告／知识专库，图表并入其中）；PPT 生成交付原生可编辑 .pptx 与双版核验报告。所有事实素材均来自深知权威文件库检索，正文引用逐处带角标、可点击回看原文原段，交付前经脚本五项核验。注册采用「领题-作答」两段式（对用户仅需手机号与验证码；人工图片验证为兜底），注册即赠 10 万积分、完成实名认证再送 10 万积分。

## 架构

综合 Skill 采用「公共能力层 + 模块化能力」结构：

```
dknowc-office-assistant/
├── SKILL.md              # 主入口：能力矩阵 + 任务路由 + 综合规则
├── attribution.json     # 调用来源声明（X-Dknowc-Attribution；渠道差异打包期改此文件）
├── common/               # 统一公共层（初始化 / 注册取 Key / 发布检查）
├── doc-writer/           # 能力一：公文写作（v3.9.4）
├── searching/            # 能力二：可信检索（v1.6.2，V2 接口）
└── ppt-assistant/        # 能力三：PPT 生成（v1.5.2，含 ppt-master MIT 组件）
```

- **公共能力层（common/）**：`initialize.py`（多层门禁：基础依赖 / 检索凭证 / Word 排版 / PPT 编译）、`register_key.mjs`（统一 MaaS 注册取 Key，不传 type；含 `save-key` 子命令承接 MCP 授权取 Key）。三个能力模块共用一套初始化与注册；发布检查在项目级 tools/ 维护。
- **能力模块**：每个能力一个平级子目录，内部按「脚本 + 参考文件 + 工作区」自包含组织，脚本以 `__file__` 定位本模块根目录，互不干扰、可独立运行。
- **未来扩展**：新增能力 = 新增平级模块子目录 + 在 `SKILL.md` 能力矩阵登记 + 复用 `common/`。

## 能力总览

| 能力 | 模块 | 来源版本 | 主要交付物 |
| --- | --- | --- | --- |
| 公文写作 | `doc-writer/` | 深知公文写作 v3.9.4 | Word（可选红头）+ 产出物 HTML（正文／溯源核验报告／知识专库 三页） |
| 可信检索 | `searching/` | 深知可信搜索 v1.6.2 | 直接答案 + 单文件产出物 HTML（三页，图表并入其中） |
| PPT 生成 | `ppt-assistant/` | 深知可信PPT v1.5.2 | 原生可编辑 .pptx + 双版可信核验报告 |

- **公文写作**：支持通知、请示、报告、函、会议纪要、总结、方案、讲话稿、调研报告等文种的起草、改写、润色、审查；两阶段检索（深度广度召回 + 可信精准补搜）、研究资料写作底稿、范文大纲、自由搜索（文风体例参考，全网非官方材料仅学写法、不进正文事实层与溯源报告）、GB/T 9704 排版、红头生成、本地素材库与写作偏好。
- **可信检索**：权威材料检索、政策调研、城市政策对比、深度搜索（多对象/地域对比或明确深度意图）、政策问答（v1.4.0 起承接原咨询场景）、数据图表并入同一份核验报告（离线 ECharts）；交付直接答案与单文件三页产出物 HTML，正文 Markdown/PDF 由用户在 HTML 顶栏自助导出。
- **PPT 生成**：约束 SVG → 原生 DrawingML 编译（抽取自 ppt-master，MIT，声明见 `ppt-assistant/THIRD_PARTY_NOTICES.md`）；主题/材料/材料免检索三种模式，双确认门工作流，5 种党政合规风格 + 8 种画布，素材层深知可信检索全程溯源；链接原样进报告（不做活性探测），无源网址材料以存档快照回看。

## 依赖

```bash
pip3 install python-docx requests
```

- `Python`、`requests` 是所有能力的运行基础前置条件。
- 公文 Word 排版需要 `python-docx`；PPT 编译导出需要 `python-pptx` + `XlsxWriter`。两者缺失仅阻断对应能力环节，可用隔离环境提供：

```bash
uv run --with python-docx python3 doc-writer/scripts/format_document.py ...
uv run --with python-pptx --with XlsxWriter python3 ppt-assistant/scripts/svg_to_pptx.py ...
```

- 有效 API Key（环境变量 `DKNOWC_API_KEY`）只对需要检索的任务是前置条件；公文纯排版、PPT 材料免检索模式无需 Key。

## 首次启动初始化

只要调用本 Skill，Agent 必须先运行：

```bash
python3 common/initialize.py
```

初始化报告基础环境、API Key、Word 排版依赖与 PPT 编译依赖四层状态；是否阻断按任务类型判定（详见 `SKILL.md`「启动初始化」）。

## API Key 配置

统一通过 `DKNOWC_API_KEY` 注入（读取顺序：进程环境变量 → `~/.config/dknowc/api_key` 配置文件，注册后无需重启宿主；不读取、不写入任何 shell 配置文件），三个能力模块共用。未配置时优先尝试 **S0 MCP 已授权直接开通**（宿主 dknowc-mcp 的 `create_api_key` 工具取 Key 后 `save-key` 落盘，免手机号），否则用 `common/register_key.mjs` 注册/查回（「领题-作答」两段式：challenge 申请文字题由 Agent 当场作答、answer 提交并发码，题目与答题过程不向用户展示；注册请求不传 `type`、body `source` 固定 `"agent"` 合同标记；各分支输出 `user_message` 固定话术须原样转述；**注册成功自动把 Key 写入配置文件**）；MaaS 管理平台（登录页）：`https://platform.dknowc.cn/auth/#/login`。MCP 检索通道已停用（统一脚本通道），详见 `SKILL.md`「MCP 通道状态」。
