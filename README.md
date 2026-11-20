# Factual Academic Writing · 事实驱动写作

**正式版：0.8.4。** 将准确、论证、连贯和结构要求用于 AI 文字输出。起草时区分事实、推断、建议和假设；编辑时保留原意；审查时指出问题、依据和已检查范围。

0.8.4 明确三层规范：通用质量约束所有文字；日常协作默认清楚、简洁、具体；交付正文从初稿起依读者、用途和已有要求选择表达与格式。保留公文、学术写作、工程技术、调研与决策、项目申报五个场景。用途不明时先问用途；缺少必用表格时，同时保留可先准备的事实工作。

## 安装与默认规范

从 [v0.8.4 发布页](https://github.com/airpot/factual-academic-writing/releases/tag/v0.8.4) 下载 `factual-academic-writing-0.8.4.zip`，按同页 `.zip.sha256` 核对。备份旧版，把解压后的完整 `factual-academic-writing/` 放入宿主实际使用的技能目录；在 Codex 中可使用 `%USERPROFILE%\.agents\skills\`。如现有入口是符号链接，先核对实际目录并保留链接；备份放在技能发现目录之外。

可显式调用 `$factual-academic-writing`，提供任务、材料与所需形式。只有希望每次会话默认采用此规范时，才需要以下配置。

1. 找到 Codex 配置目录：未设置 `CODEX_HOME` 时使用 `~/.codex`。已有非空的 `AGENTS.override.md` 时，编辑该文件；否则使用 `AGENTS.md`。备份要编辑的现有文件。[OpenAI 官方说明](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
2. 将 ZIP 内 `references/default-policy.md` 的完整正文写入该文件。文件不存在时新建；文件存在但没有这项规范时，在末尾另起一段追加。用 `<!-- factual-academic-writing-default:0.8.4 -->` 和 `<!-- /factual-academic-writing-default -->` 分别标记正文的起止，各占一行。已有旧规范时，在原位置替换整段规范及其版本标记（如有）。保留其他设置，只保留一份该规范。
3. 启动新会话，确认已加载这份写作规范；单独测试技能时，可显式调用技能名称。

## 资料与验证范围

见 [技能入口](SKILL.md)、[三层规范与正反例](references/response-layers.md)、[五类写作场景](references/writing-scenes.md)、[模板确认](references/manuscript-format.md)、[英文审校](references/english-review.md)、[标点审查](references/punctuation-review.md)、[表文数值核验](references/meaning-preservation.md#verify-table-numbers-before-delivery)和 [变更记录](CHANGELOG.md)。可选扫描器只依赖 Python 标准库：`python scripts/scan_ai_patterns.py manuscript.txt`。扫描器只提示部分宣传用语和修辞模式。引文归属和证据支持由正文审校核对；网址检查器只比对地址。扫描结果不能核实事实或判断作者身份。

正式 ZIP 含 21 个运行文件。本轮 18 道用例和 16 道原有回归用例的修正版首答通过，同一冻结稿连续通过两轮独立完整复核。正式包只更新两处版本标记；验证覆盖指定用例与运行文件，统一开发仓全仓测试未完成。

ZIP SHA-256: `c1bdf07013853b05587c7e02090ad74194775c612d43d357d4f906b942a14063`
