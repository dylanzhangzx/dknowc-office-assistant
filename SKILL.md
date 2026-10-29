---
name: "深知晓办公助手"
slug: "dknowc-office-assistant"
display_name: "深知晓办公助手"
display_name_en: "dknowc office assistant"
description: "深知晓办公助手，是由北京彩智科技有限公司旗下“深知可信智能”提供的综合办公助手，统一覆盖公文写作、可信检索、PPT 生成三大类办公场景，并可持续扩展更多能力。可用于公文与正式材料起草（通知、请示、报告、函、会议纪要、总结、方案、讲话稿、调研报告等文种的起草、改写、润色、压缩、审查和 Word/红头交付）、权威材料检索与核验（政策依据查找、政策调研、城市政策对比、补贴税惠材料核验、深度搜索、数据图表并入同一份核验报告）、以及原生可编辑 PPT 生成（工作汇报、专题汇报、政策宣讲、培训课件，从需求直接生成或从已有材料提炼，5 种党政合规风格 + 8 种画布规格，约束 SVG → 原生 DrawingML 编译导出真实 PowerPoint）。所有事实素材都通过深知可信智能的权威文件库检索，全程可溯源。"
description_zh: "深知晓办公助手，是由北京彩智科技有限公司旗下“深知可信智能”提供的综合办公助手，统一覆盖公文写作、可信检索、PPT 生成三大类办公场景，并可持续扩展更多能力。公文写作能力按公文国家标准支持通知、请示、报告、函、复函、批复、会议纪要、通报、通告、公告、意见、方案、总结、管理办法、汇报材料、发言稿、讲话稿、调研报告、经验材料等常见文种和工作材料，正式交付生成 Word 文档，用户明确要求时生成红头文件；可信检索能力用于权威材料检索、政策调研、城市政策对比、补贴与税惠材料核验、合规依据核验和深度搜索，交付直接答案与单文件产出物 HTML（正文／溯源核验报告／知识专库 三页切换，可导出正文 Markdown 与 PDF），数据图表并入同一份报告（离线 ECharts）；PPT 生成能力采用约束 SVG → 原生 DrawingML 编译架构，主 Agent 逐页手写 SVG、确定性编译器导出真实可编辑的原生 PowerPoint，内置党政简洁、数据图表、商务汇报、庄重典雅、培训课件 5 种风格预设，支持 16:9、4:3、小红书、朋友圈、竖版故事、A4 等 8 种画布规格。本技能全部事实素材都通过深知可信智能的权威文件库检索，可溯源到权威部门发布的规范性文件。"
description_en: "dknowc office assistant is a comprehensive office-assistant Skill provided by dknowc Trusted Intelligence under Beijing Caizhi Technology Co., Ltd. It unifies official-document writing, trusted retrieval, and native PPT generation in one Skill, with an extensible architecture for future capabilities. It supports drafting, rewriting, polishing, reviewing and generating structured workplace documents (including Word and red-head output); answering policy/regulation/government-service questions with citation markers and clickable provenance HTML; retrieving authoritative materials with deliverable of a direct answer plus a single-file three-page HTML artifact (body / provenance verification report / knowledge library, exportable as Markdown or PDF); plus native PPT generation through constrained-SVG-to-DrawingML compilation with multiple built-in styles (gov-simple, gov-data, business, formal, training) and eight canvas formats."
category: "通用办公"
version: "1.6.2"
author: "彩智科技"
permissions:
  network:
    - "https://open.dknowc.cn/"
    - "https://platform.dknowc.cn/"
  local_read:
    - "本 Skill 的 common、config 等规则与配置文件"
    - "各能力模块（doc-writer、searching、ppt-assistant）的脚本、标准、契约和参考资料文件"
    - "ppt-assistant/projects/ 项目工作区中的内容包、SVG 与素材"
  local_write:
    - "本地初始化状态文件"
    - "本机专用配置文件 ~/.config/dknowc/api_key 中的 DKNOWC_API_KEY（注册成功后自动写入）"
    - "用户明确授权保存的写作偏好与个人素材库（仅本机）"
    - "生成的 Word 文档、PPT 演示文稿、可信核验报告与搜索结果中间文件"
    - "ppt-assistant/projects/ 项目目录（内容包、SVG、图片、质检报告、导出产物）"
secrets:
  - "DKNOWC_API_KEY"
---

# 深知晓办公助手

深知晓办公助手由北京彩智科技有限公司旗下“深知可信智能”提供，是一个统一覆盖**公文写作、可信检索、PPT 生成**三大类办公场景的综合型 Agent Skill（政策问答类问题由可信检索域承接——检索→带角标答案→核验报告），并采用可扩展架构，未来可持续加入更多能力。它不是固定从头到尾执行的演示脚本，而是根据任务选择最小必要流程：先判别任务属于哪个能力域，再进入对应能力模块完成起草、检索、设计、溯源与交付。

**核心定位**：内容可信是我们的（权威文件库 + 全程溯源），排版专业是编译器的（SVG → 原生 DrawingML）。所有事实素材可溯源到权威部门发布的规范性文件。

## 权限说明

本 Skill 访问 `https://open.dknowc.cn/` 用于范文大纲、深知可信搜索、深度搜索和可信溯源整理；访问 `https://platform.dknowc.cn/` 用于 MaaS 手机号验证码注册、API Key 获取和管理平台地址说明。运行过程中会读取本 Skill 的规则、标准、配置和参考资料文件，并在本地写入初始化状态文件、用户授权保存的写作偏好与个人素材库（仅本机，不随包分发、不上传）、生成的 Word 文档、PPT 演示文稿、产出物 HTML（正文／溯源核验报告／知识专库 三页）和搜索结果中间文件。API Key 只通过环境变量 `DKNOWC_API_KEY` 或本机专用配置文件 `~/.config/dknowc/api_key`（Windows `%APPDATA%/dknowc/api_key`）读取，不硬编码、不写入公开包、不在对话中展示完整内容；注册成功后自动写入专用配置文件（600 权限）。不读取、不写入任何 shell 配置文件。

## 能力矩阵

| 能力 | 模块路径 | 核心脚本 | 使用的接口 | 主要交付物 | 典型触发场景 |
| --- | --- | --- | --- | --- | --- |
| 公文写作 | `doc-writer/` | `outline_reference.py`、`deep_query.py`、`dkag_search.py`、`format_document.py`、`template_generator.py`、`source_note_html.py` | 范文大纲、深知搜索 | Word（可选红头）+ 产出物 HTML（正文／溯源核验报告／知识专库 三页） | 起草、改写、润色、审查、总结、方案、讲话稿等文种任务 |
| 可信检索 | `searching/` | `trusted_search.py`、`deep_query.py`、`deep_convert.py`、`merge_search_results.py`、`chart_embed.py` | 可信搜索、深度搜索 | 直接答案 + 单文件产出物 HTML（正文／溯源核验报告／知识专库 三页，图表并入其中） | 查依据、找材料、政策调研、城市对比、补贴核验、深度分析、政策问答 |
| PPT 生成 | `ppt-assistant/` | `svg_to_pptx.py`、`svg_quality_checker.py`、`trusted_search.py`、`render_trace_html.py` | 深知可信搜索（素材层）+ 本地 SVG→DrawingML 编译 | 原生可编辑 .pptx + 双版可信核验报告 | 汇报/宣讲/培训/数据 PPT，从需求直接生成或从已有材料提炼 |

> **未来能力登记区**：新增能力时，在此表增加一行，并新增与三模块平级的能力模块子目录。

## 启动初始化

本 Skill 被调用后，先运行一次统一初始化检查：

```bash
python3 {skillDir}/common/initialize.py
```

初始化只报告状态，不要求用户提供单位或个人信息，也不上传检测结果。是否阻断由任务类型决定：

**基础前置条件（所有能力都要求）**：`python3`、`requests`。缺失时暂停全部能力；`dependency_install_prompt_needed=true` 时先向用户说明并征得同意后安装，用户拒绝时执行 `--decline-dependency-install` 记录，后续不再询问。

**API Key 是按需前置条件**：

- **需要 Key**：可信检索域（含政策问答类问题，由本域承接），以及公文写作域中需要政策依据/数据/案例检索的任务、PPT 生成域的主题模式与材料补检索模式——检索统一走脚本通道（MCP 检索通道已停用，见下）。要求 `api_key_configured=true`、`search_ready=true`；不满足时暂停任务，按「统一 API Key 管理」引导（优先尝试 S0 MCP 已授权直接开通，其次 S1 手机号流程；用自然语言表达，如「开通搜索功能」；用户主动询问技术细节时如实说明），不得改用外部搜索。
- **不需要 Key**：公文写作域的简单通知、改写、润色、审查、基于用户材料写作、只生成 Word；PPT 生成域的材料免检索模式（用户明确「不用查，就用我给的材料」）。

**能力专属依赖（缺失不阻断其他能力）**：

- 公文 Word 排版需要 `python-docx`（`word_ready=false` 时仅阻断 Word 交付，可用 `uv run --with python-docx` 提供）。
- PPT 编译导出需要 `python-pptx` + `XlsxWriter`（`pptx_ready=false` 时仅阻断导出，素材检索与 SVG 创作可先行，导出时用 `uv run --with python-pptx --with XlsxWriter python3 …` 隔离提供）。

## 统一 API Key 管理

skills.sh 版不内置 API Key，三个能力模块共用同一把 `DKNOWC_API_KEY`（读取顺序：进程环境变量 → 本机专用配置文件 `~/.config/dknowc/api_key`；注册后无需重启宿主）。取 Key 有两条路径，**S0 优先**：

**S0 · MCP 已授权直接开通（优先，免手机号）**：宿主提供 MCP「深知可信工作台」（dknowc-mcp）的 `create_api_key` 工具且调用成功（返回顶层 JSON `{"apiKey": "..."}`）时，把密钥落盘后即可开始，无需手机号验证码：

```bash
printf '%s' "<密钥>" | node {skillDir}/common/register_key.mjs save-key
```

落盘成功后转述脚本 `user_message`（S0 话术见各模块 `reference/onboarding_scripts.md`）。`create_api_key` 工具不存在或调用报错（如「请先完成 MCP OAuth 授权」）时本路径不适用，直接走 S1 手机号流程，不反复重试 MCP 取 Key、不向用户提及 MCP 内部细节。

**S1 · 手机号验证码注册**（`common/register_key.mjs`）：注册请求 `source` 固定为 `"agent"`（**注册接口合同标记**，服务端据此放行老用户直接返 Key——传 skill 名会导致老用户重注册报「用户已存在」取不回密钥），注册请求**不传 `type`**（接口可选、Key 权限完整；如平台后续要求可经 `--type` 显式传入），自动携带 skills.sh 渠道码 `8C8D411C-6A46-4E99-887D-87D9A1329930`；请求头另带来源声明 `X-Dknowc-Attribution`（键名 `agentSource=dknowc-office-assistant`，见下）与 MaaS 客户端观测头 `X-MaaS-*`（Entry-Surface=DIRECT_API、Client-Name=包名、Client-Version 运行时读 SKILL.md、Client-Instance-Id 由服务端签发后落盘 `~/.config/dknowc/maas_client_instance` 复用）：

```bash
node {skillDir}/common/register_key.mjs challenge --phone <手机号>
```

challenge 返回一道**文字题**（`question.prompt`，答案为非负整数）——由 Agent **当场计算**并用下一条命令提交，题目、token 与答题过程**一律不发给用户、不复述**：

```bash
node {skillDir}/common/register_key.mjs answer --phone <手机号> --answer <题目的非负整数解>
```

返回后**必须把脚本输出的 `user_message` 原样转述给用户**（固定话术，不得改写后发挥）。**注册为「领题-作答」两段式（2026-10-29 MaaS 改造）**：`answer` 退出码 0＝短信已发（`SMS_SENT`）；3＝答错换题（脚本返回新题，**静默重算再答**，含首次最多 3 次，不向用户提及）；2＝平台要求人工图片验证（`HUMAN_REQUIRED`＋验证链接）——链接经脚本内置安全校验后才可展示、仅给手机号持有人本人，**持有人完成验证后不得再调用 challenge/answer 发码**；4＝发送结果未确认（不重发，先确认是否收到短信）；1＝失败（限频/锁定/不可用按话术分场景处理）。`challenge` 退出 2 同转人工；输出 `flow:"legacy"` 时平台回退旧直发分支，无答题环节、按 S3a/S3b 话术处理。用户只说「验证好了」时只追问短信码。随后暂停等待用户回复短信里的 6 位验证码，不得编造、不得代试、验证码错误时不得自行重发。`register` 返回 `pending:true` 表示账号已建、密钥准备中（非错误），同参数稍后重试一次；返回「用户已存在」时据实说明、不得冒充找回成功。拿到验证码后：

```bash
node {skillDir}/common/register_key.mjs register --phone <手机号> --vcode <验证码> --organ 个人 --name 用户
```

**注册成功自动持久化**：脚本自动把 Key 写入本机专用配置文件 `~/.config/dknowc/api_key`（600 权限，Windows `%APPDATA%/dknowc/api_key`），输出 `user_message`（含积分到账确认：注册赠送的 10 万积分已到账——这句**不可省略**）。不再有「任务完成后询问是否保存」环节。手机号已注册时默认查回既有可用 Key（老用户话术见 `user_message`）；用户明确要求「重新生成/新建 Key」时才加 `--new-key`，新建失败时脚本自动沿用原 Key 继续并如实告知。

**引导纪律（硬规则）**：

- **引导前禁示**：开通确认前不得向用户输出「已核实/已查到/检索到 N 篇」类内容；禁止用模型自身知识冒充检索结果。
- **退路唯一化**：用户暂不开通时，只能给带「依据待核验」标注的初步回答；不得承诺「联网检索替代」「稍后帮你网上查」。
- **话术来源固定**：各分支场景（手机号格式错/发送失败/验证码错误/开通成功/老用户/网络异常）以脚本 `user_message` 与各模块 `reference/onboarding_scripts.md` 话术库为准，原样转述、要素不可删改；样例悬念式出示（S1·附）用各模块 `reference/sample_*` 示例文件。
- **额度用尽禁止任何形式重试**：检索脚本对 402/429 输出 `quota_exhausted` 与 `user_message`（引导到 MaaS 平台处理）；401 密钥失效先重读 Key 重试一次；403 无权限、500 服务异常按话术引导，均不得盲目重试。
- 不得向用户展示完整 Key 或验证码；手机号一律脱敏（前3后4）。用户不希望脚本注册时给出降级地址 `https://platform.dknowc.cn/auth/#/login`。

## MCP「深知可信工作台」通道状态

**MCP 检索通道已停用**：检索统一走各模块脚本通道（需 API Key），规则层不检测、不得改调 MCP 检索通道。MCP 当前保留的唯一用途是「深知可信工作台」的 `create_api_key` 工具——宿主已授权时可免手机号直接取 Key（见「统一 API Key 管理」S0）。

## 任务路由

开始工作前，先判别任务属于哪个能力域，再进入对应模块流程。**先路由，后执行；匹配即执行，不向用户罗列实现路径。**

### 路由判别

- **公文写作域**：起草、写、生成、整理、形成、润色、改写、压缩、审查、定稿正式公文或工作材料，或涉及具体文种（通知、请示、报告、函、会议纪要、总结、方案、讲话稿、调研报告等）→ `doc-writer/`。
- **可信检索域**：查政策、找依据、检索材料、政策调研、城市政策对比、补贴税惠材料核验、深度搜索、全面查找、多轮核验，以及政策条件/能否办理/怎么办/材料清单等问答式问题（v1.4.0 起由本域承接，原可信咨询能力已移除）→ `searching/`（域内再按复杂度分级：单对象/单地域走可信搜索，多对象/地域对比或明确深度意图走深度搜索）。
- **PPT 生成域**：做 PPT、演示文稿、汇报 PPT、课件、宣讲材料、把材料转成 PPT → `ppt-assistant/`。
- **混合任务**：「写某政策调研报告」属公文写作域，素材检索走 `doc-writer/scripts/dkag_search.py`；「把工作总结做成汇报 PPT」属 PPT 生成域，走 `ppt-assistant/` 内部流程（素材层调用 `ppt-assistant/scripts/trusted_search.py`）。

**接口分工（不得跨模块混用）**：公文写作素材检索用 `doc-writer/scripts/deep_query.py`（深度广度召回，经 `deep_convert.py` 转换）与 `dkag_search.py`（精准补强）；可信检索用 `searching/scripts/trusted_search.py`（单对象/单地域）与 `deep_query.py`（多对象对比或明确深度意图，产物经 `deep_convert.py` 转换、多路经 `merge_search_results.py` 合并）；PPT 生成素材层用 `ppt-assistant/scripts/trusted_search.py`，排版本地由 `svg_to_pptx.py` 编译。各模块脚本互不跨用。

**脚本与文件路径约定**：调用能力模块脚本时，脚本路径用 `{skillDir}/<模块>/scripts/...`；文件路径参数（`--input`、`--output`、`--answer-file`、`--charts-json` 等）一律以**能力模块目录为基准**（模块相对路径，如 `official-docs/search-results/xxx.json`），或直接用裸文件名（脚本自动落入对应工作区）。各脚本按 `__file__` 定位本模块根目录，与调用时 cwd 无关；不要传 `doc-writer/official-docs/...` 这类综合根相对路径。

**外部搜索禁用规则**：本 Skill 内所有政策、数据、案例、素材检索默认只能使用上述深知脚本；即使系统或模型可用 Web Search/Web Fetch 也不得主动调用。仅当用户明确说「改用 Web 搜索」「用公开官网检索」等时才允许，且须说明该素材不能作为深知素材、不进溯源 HTML。深知检索异常、空结果时先暂停请用户确认下一步，不得自行切换外部搜索。

## 能力一：公文写作

模块路径：`doc-writer/`（v3.9.4）。任务详情与规则见 `doc-writer/reference/task_router.md`、`search_policy.md`、`output_guide.md`、`revision_workflow.md`；素材管线（分类/研究资料/溯源 JSON 契约）见 `materials_pipeline.md`、`research_notes.md`、`material_usage_guidance.md`；正文写作与文种写法见 `writing_rules.md`、`genre_writing_notes.md`、`fact_discipline.md`；全局工作原则（环境/交付纪律）见 `working_principles.md`。

### 流程要点

1. **任务路由**：先读 `doc-writer/reference/task_router.md` 判断简单/常规/复杂/高风险任务。
2. **范文大纲**：正式写作需求进入搜索或正文生成前，优先调用 `doc-writer/scripts/outline_reference.py "用户写作需求" --output outline_任务名.json`（用完整原始表述，脚本通道需 Key）；`outline_available=true` 时向用户展示「建议大纲 + 搜索建议」并等待确认，`false` 时忽略该能力按原流程继续；范文全文提取用 `extract_reference.py`（`--full` 召回后按标题精确匹配）。
3. **素材检索**：需要政策依据/数据/案例时才搜索，逻辑遵循 `doc-writer/reference/search_policy.md`（**统一走脚本通道需 Key，两阶段执行**：首轮用 `deep_query.py` 做深度搜索广度召回——返回 JSON 落盘后经 `deep_convert.py` 转换；补搜用 `dkag_search.py` 做可信搜索精准补强——V2 接口起可信路带文章级「发文字号」，深度产物文号为部分覆盖、政策依据型仍按缺口补搜）：设计搜索方案（覆盖政策依据/数据支撑/参考案例，表述参考不单列；query 句式「对象（含地域、时间限定）的关注方向」——政策路写「…政策」、数据路写「…发展情况」、案例路写「…做法」，同一路内不叠加多维限定，**禁止类目关键词堆砌与括号列举具体信息需求**；补搜 query 求精度带时间+地域+对象精确限定；已知目标文件名时直接用标题原文）→ 展示方案并等用户确认（不出现脚本参数名，方案展示每条 query 原文）→ 确认后执行（同方案多路**默认并行**：每路独立 `--output` 与 `--purpose`，单批不超过 4 路，单次调用内后台并行、`wait` 全部结束后逐路检查结果；**每路返回后立即单独落盘并校验，未落盘校验通过前不得发起下一路，禁止把结果攒在对话里统一落盘**——宿主对工具结果有清理机制，延迟落盘会过期无法读取；失败路单独串行重试一次；任意一路额度用尽即整批停止；平台明显限流〔多路同时报错〕时回退逐路串行）→ 素材四分类整理 → **研究型与综合长篇文种生成研究资料**（两阶段：分类自检时出初版——核心事实总表＋数据与口径表，口径缺口「未给出／未确认／多口径未裁决」驱动数据与案例类补搜；用户确认素材清单后按正文预定章节组织定稿，角标与清单序号一致），落盘 `official-docs/input/标题_研究资料.md`，规范见 `doc-writer/reference/research_notes.md`——`check_materials.py` 对研究型文种缺研究资料文件直接拒绝通过。方案边界内的缺口补搜自动执行（研究型文种以关键事实闭环为目标持续补搜，不设次数上限），越界（新地域、换通道）先向用户确认；异常时停止并请用户确认下一步。文种/题材写法需要范文参考时（不常见综合文稿、用户初次尝试的文种、官方材料缺可借鉴行文结构），在方案中**主动列入「文风体例参考」一路**（`--search-channel webSearch`，全网非官方材料，只学结构句式、不搬内容，不进正文事实层与溯源报告；该路材料在报告中自动标注「非官方来源」；政策依据与数据严禁使用该通道），无需等用户提出。
4. **写作**：按 `writing_rules.md` 组织正文（标题/结构/段落/自检）与 `genre_writing_notes.md` 的文种写法要点，按文种读取 `doc-writer/reference/standards/` 对应标准；生成正文前按 `fact_discipline.md` 约束事实边界；长篇材料另读 `99_expressions.md` 并按 `anti_ai_patterns.md` 做语言复核；素材进入正文按 `material_usage_guidance.md`；**正文文号只认材料清单 `发文字号` 字段，字段为空时只写文件全称、不得从段落正文提取**（`check_materials.py` 拦截）；研究型与综合长篇文种**正文基于研究资料定稿写作**（不边写边从原文摘录里捞取）。**篇幅锚点**：正文目标 3500–5000 字（素材充分取上限、不足如实精简），每章 ≥3 段、二级要点 ≥120 字、问题与建议章每条按「依据角标＋动作＋抓手」组织且 ≥100 字——扩充只落在已召回事实上，不新增形容词。正文不加引用角标，溯源信息独立成页（产出物 HTML 的溯源核验报告页）。
5. **审查**：执行过搜索、请示/复函/政策依据型报告、长篇材料、用户要求 Word/红头/明确要求检查时，按 `review_checklist.md` 审查；可选用 `prose_lint.py` 做语言质检。
6. **交付**：命中公文范式默认交付 `.docx`（正文先写入 `doc-writer/official-docs/input/` 临时文件再调 `format_document.py official-docs/input/xxx.txt`）；仅用户明确要求红头时调 `template_generator.py`；普通 Word 末尾保留 `【AI生成提示】内容由AI生成，内容仅供参考。`；不支持 PDF 自动生成。**本次任务执行过深知搜索时另行生成产出物 HTML**：先用 `build_trace_json.py` 从「素材清单＋带角标正文」装配溯源 JSON 到 `official-docs/input/标题_溯源核验报告.json`，再用 `check_materials.py` 校验（来源可回溯、字段完整、角标一一对应、未引用召回材料非空），通过后由 `source_note_html.py` 输出三页产出物 HTML（文件名按用户需求确定，正文＋溯源核验报告＋知识专库）。正文页只放干净正式内容（不带角标，与 Word 正文一致），核验内容只在溯源核验报告页；链接原样进报告（2026-10-08 起不再做活性探测、生成过程不发网络请求；无源网址的材料以接口存档快照作回看入口，policyFiles 发文字号自动上卡展示）。**正文缺 `[n]` 角标时脚本拒绝生成并报错**，须修 JSON 后重跑，不得手写 HTML。
7. **本地记忆（可选）**：用户明确要求保存素材或偏好时，用 `doc-writer/scripts/local_memory.py` 的 `kb`（素材库）/`pref`（写作偏好）子命令管理，仅本机生效、不随包分发。

## 能力二：可信检索

模块路径：`searching/`（v1.6.2，V2 接口）。**检索按复杂度分级，先数对象**：只有 1 个对象/地域（含「北京有哪些租房补贴政策」「怎么申请」「条件是什么」这类单地域枚举、单点事实、单政策解读）→ `searching/scripts/trusted_search.py` 可信搜索；≥2 个对象/地域要放在一起对比并列、或跨地域跨层级聚合、或用户明确表达深度意图（「深度搜索／全面／系统／完整方案」）→ `searching/scripts/deep_query.py` 深度搜索（query 直接用用户原始问题、不传 `--area`），拿不准时先走可信搜索。政策问答类问题也由本域承接（原可信咨询能力 v1.4.0 起移除）；MCP 检索通道已停用（统一脚本通道）。

标准工作流：初始化门禁 → 判断追问（缺会改变结论的关键变量先问，否则先搜索）→ 检索（按分级选通道；深度搜索原始产物**必须先经 `deep_convert.py` 转成通用形态**，多路结果用 `merge_search_results.py --input …` 合并——合并产物每篇材料带 `编号`，答案角标 `[n]` 的 n 就是该编号，**禁止手工合并、禁止用某一路内部相对序号**）→ **先整理研究资料、后动笔**（生成 `official-docs/search-results/research_notes.md`：核心事实总表＋数据与口径表；口径表缺口即定向补搜目标，补搜后回填，仍缺的才进「待确认」；关键结论须能在表中逐行找到对应）→ 综合答案（关键结论挂真实 `[数字]` 角标、**边写边标**，存 `dknowc_search_answer.txt`；首行为成稿标题、章节用 markdown 标题行）→ 自检写入 `dknowc_search_selfcheck.json`（**只允许五键**：`fact_basis`／`binding`／`consistency`／`freshness`／`no_gap`，每项写 `通过：<说明>` 或 `未通过：<原因>`）→ 生成单文件产出物 HTML（`render_trace_html.py --answer-file --self-check-file --charts-json <图表JSON> --question "<用户原话>" --research-notes-file official-docs/search-results/research_notes.md`；生成了研究资料时**必须传** `--research-notes-file`，`--question` 必须传用户原话）→ 交付（`searching/scripts/deliver_outputs.py`，见交付纪律）→ 回复用户（直接答案＋产出物 HTML 路径）。

红线：`query` 聚焦单一目的、`eff_time` 只传一个时间值、`service_area` 只传一个地域、**V2 `searchType` 单值必填（默认 `policy`；办事/流程类补 `govSite` 路，两路各自单值并行后再合并，混传直接报错）**，可信路参数定档 4 段/18000 字；引用政策文件**优先选发文版条目**（带文号、带存档快照、权威门户源网址者优先；不确定是否同一文件时不得猜测挂文号）；不得伪造／误配／泛配角标；**本次任务只交付那一份 HTML**——图表并入其中，不另出 Markdown／PDF 文件（正文 Markdown 与 PDF 由用户在 HTML 顶栏「导出」自助导出；`--clean-md-output` 已移除，`--skip-link-check` 为兼容保留的 no-op），同题重跑自动 `_v2` 另存、旧版保留；用户明确说「不要 HTML／文件」才跳过文件交付。产出物 HTML 为**三页**（正文（去索引）／溯源核验报告（默认页：AI 自验收过程条按接口通道拆分计数、并展示每路补搜增量「新增 N 篇 · 补充 K 段」、五项核验单、带角标正文；联网路召回的非权威材料自动打「非官方来源」徽标、不与权威材料混排）／知识专库（检索分组 tabs ＋ 已引用/未引用筛选，含未引用召回））；报告必须以**「核验完成」状态**交付——可修复问题（角标未绑定、缺摘录、自检未记录、结构不符）一律先修后重渲，仅不可抗力缺口（接口确未返回源网址）允许温和提示；生成前硬校验拒绝无角标报告。`trusted_search.py` 默认返回**完整集**（含存档快照，原文失效时回看；`--simplified` 会剔除材料并丢快照，生成报告时不建议使用）；链接原样进报告（2026-10-08 起不做活性探测）。检索统一走脚本通道（需 Key）；多路并行（≤4 路、每路即时落盘校验）、失败路串行重试一次、额度用尽整批停止。

## 能力三：PPT 生成

模块路径：`ppt-assistant/`（v1.5.2）。生成侧采用约束 SVG → 原生 DrawingML 编译架构（组件抽取自 ppt-master，MIT；声明见 `ppt-assistant/THIRD_PARTY_NOTICES.md`），内容侧用深知可信搜索。**完整运行时权威见 `ppt-assistant/workflows/generate-pptx.md`（Step 1-9）；进入方式（主题/材料/材料免检索三模式）见本文件「任务路由」与该文件开头说明。**

Generate 主线（v1 唯一路线）：

```
初始化门禁 → [深知检索（主题模式）] → 内容包 → 提纲版可信核验报告 →【结构方案确认门 ⛔】
→ 创建项目 → 逐页手写 SVG（P01 → 首页确认 ⛔ → 其余不间断）
→ SVG 质检 → 编译导出 .pptx → 成稿版可信核验报告 → 交付
```

核心硬规则：

1. **三种进入模式**：主题模式（先设计检索方案过确认门，多路并行检索补事实基线——**统一走脚本通道** `ppt-assistant/scripts/trusted_search.py`（需 Key，MCP 检索通道已停用）；单批不超过 4 路、每路独立落盘并即时校验（未落盘校验通过前不得发起下一路，禁止把结果攒在对话里统一落盘——宿主工具结果会过期），失败路串行重试一次，额度用尽整批停止，明显限流回退逐路串行）/ 材料模式（用户材料为主体，仅补事实缺口，补检索同样过确认门）/ 材料免检索模式（用户明确不用查，无 Key 可用）。
2. **内容包先行**：按 `ppt-assistant/references/content-pack.md` 编制（核心信息/叙事/页面规划/素材清单带来源/风格预设），与风格预设一起过**结构方案确认门**后才创建项目、写 SVG。
3. **svg_output 是设计唯一来源**：主 Agent 按 `ppt-assistant/references/svg-authoring.md` 方言契约**逐页手写** SVG（P01 首页门→其余不间断），禁止脚本批量生成页面。
4. **质检不过不导出**：`svg_quality_checker.py --quick-generate --stage final --json` 退出码 0 是导出前置条件；导出用 `uv run --with python-pptx --with XlsxWriter python3 ppt-assistant/scripts/svg_to_pptx.py projects/<项目> --quick-generate`，产物为原生可编辑 .pptx，不得降级为整页图片。
5. **风格与画布**：5 种党政合规风格预设（党政简洁默认/数据图表/商务汇报/庄重典雅/培训课件，见 `ppt-assistant/references/style-presets.md`）+ 8 种画布（16:9/4:3/小红书/朋友圈/竖版/A4 等）。
6. **双版核验报告**：执行过检索时用 `ppt-assistant/scripts/render_trace_html.py` 生成两版核验报告——结构确认门前的**提纲版**（让用户逐条核验事实依据与口径事项）与交付前的**成稿版**（首屏核验报告单：依据溯源/引用绑定/时效检查/类型覆盖/自检五项指标）。报告链接原样进报告（2026-10-08 起不再做活性探测），无源网址的材料以接口存档快照作回看入口；合并 JSON 兼容原始接口嵌套形态，`snapshot_url`/`快照链接`/`source_url` 字段均识别。报告必须以**核验通过状态**交付：可修复问题（角标未绑定/无角标/自检未记录）一律先修后交，仅不可抗力缺口允许温和提示；生成前硬校验拒绝无角标报告。
6a. **首页预览页**：P01 完成后可用 `ppt-assistant/scripts/preview_slide_html.py` 把 svg_output 生成单文件 HTML 预览页供用户确认（宿主环境不能直接打开 .svg 时的标准路径）；交付物可用 `deliver_outputs.py` 复制到宿主工作区。
7. **修改闭环**：检索 JSON ↔ 内容包 ↔ SVG 三者一致；调整先改内容包再改 SVG 再重导出，不直接改 .pptx。

## 统一交付物规范

- **公文写作**：正式写作任务默认交付 `.docx`；本次执行过搜索时另交付**产出物 HTML（正文／溯源核验报告／知识专库 三页）**；仅用户明确要求对话输出正文时例外；不得先发正文初稿/预览版。
- **可信检索**：直接答案 + **单文件产出物 HTML（正文／溯源核验报告／知识专库 三页，图表并入其中）**；正文 Markdown/PDF 由用户在 HTML 顶栏「导出」自助导出，不另出文件（核验单只考核被引用素材；「核验完成」为默认交付状态）。
- **PPT 生成**：原生可编辑 `.pptx` +（执行过检索时）提纲版与成稿版双份核验报告；不发 SVG 源/内容包草稿/质检报告等中间产物。
- 交付时返回正式交付物路径 + 一句简短说明；执行过检索时明确主文件是正式成稿、溯源报告是辅助核验文件。
- **宿主交付纪律（三能力通用，2026-10-08 统一）**：交付命令（各模块 `deliver_outputs.py`）用绝对路径原样运行、**该命令前不得先 `cd` 进任何目录**——WorkBuddy 会话的默认工作目录即当前会话工作区，一旦 cd 就丢了它，交付会落错会话（实测踩坑）；显式传入本次产出物路径（输出目录有多个近期候选时脚本会拒绝自动复制，属防误交付安全设计）；返回 `need_dest=true` 时用 `--dest <工作区目录>` 重跑；正常时核对返回 `method` 为 `workbuddy-cwd:` 前缀（不是该前缀说明目标目录识别存疑，核对后再交付），向用户展示 `delivered` 路径。

## 未来能力扩展指南

新增一个能力时：

1. 在综合 skill 根目录下新增与三模块平级的能力模块子目录，内部按「脚本 + 参考文件 + `official-docs/` 工作区」自包含组织；脚本以 `Path(__file__).resolve().parent.parent` 定位本模块根目录。
2. 需要溯源渲染时把 `render_trace_html.py` 放进本模块 `scripts/`（按需自带，不强制共用）。
3. 复用 `common/` 公共层（统一初始化、注册取 Key、发布检查），不单独维护初始化/注册脚本。
4. 在「能力矩阵」登记新能力（模块路径、核心脚本、接口、交付物、触发场景），在「任务路由」增加判别与接口分工，在 `description` 补充触发关键词。
5. 涉及第三方开源组件时，在模块内保留 `THIRD_PARTY_NOTICES.md`，并在项目级发布检查 `tools/check_release.py` 的白名单中登记（发布检查在项目级维护，不进 Skill 包）。
