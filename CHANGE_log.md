# 变更日志

## v1.0.0（2026-08-28）

创建深知晓办公助手综合 Skill（首次整合版本）。

- 统一覆盖公文写作、可信咨询、可信检索、PPT 生成四大类办公场景，作为深知系列办公能力的综合入口。
- 四个能力模块取自对应独立 Skill 的最新发布包，保持各模块脚本、标准和参考文件自包含、可独立运行：
  - `doc-writer/` ← 深知公文写作 v3.4.5（含本地素材库/写作偏好 local_memory.py、修订工作流）
  - `consulting/` ← 深知可信咨询 v1.0.5
  - `searching/` ← 深知可信搜索 v1.1.4
  - `ppt-assistant/` ← 深知可信PPT v1.0.3（约束 SVG → 原生 DrawingML 编译架构，含 ppt-master MIT 组件与 THIRD_PARTY_NOTICES.md）
- 统一公共能力层 `common/`：`initialize.py`（基础依赖 / 检索凭证 / Word 排版 / PPT 编译多层状态报告）、`register_key.mjs`（统一注册，注册请求不传 `type`——实测接口可选参数，不传可正常注册且返回 Key 对可信搜索/统一问答接口权限完整）、`check_release.py`（多模块工作区与第三方声明白名单的发布检查）。
- 统一 API Key：四个能力模块共用 `DKNOWC_API_KEY`，模块内不再各自维护注册与初始化脚本。
- 采用「公共层 + 模块化能力」可扩展架构，未来新增能力按 `SKILL.md`「未来能力扩展指南」登记接入。
