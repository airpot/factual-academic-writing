# Factual Academic Writing · 事实驱动写作

**正式版：0.8.0。** 将准确、论证、连贯和结构要求用于 AI 文字输出。起草时区分事实、推断、建议和假设；编辑时保留原意；审查时指出问题、依据和已检查范围。

新版增加正式稿件的模板确认和英文句法审校，完善中英混排、保义和逐项依据检查。对要分别转发的交接稿，逐份核对读者能否识别裁定方、执行人、规则为何适用，以及现在和获知裁定后该怎么做。

## 安装与默认规范

从 [v0.8.0 发布页](https://github.com/airpot/factual-academic-writing/releases/tag/v0.8.0) 下载 `factual-academic-writing-0.8.0.zip`，按同页 `.zip.sha256` 核对。备份旧版，把解压后的完整 `factual-academic-writing/` 放入宿主实际使用的技能目录；在 Codex 中可使用 `%USERPROFILE%\.agents\skills\`。如现有入口是符号链接，先核对实际目录并保留链接；备份放在技能发现目录之外。

可显式调用 `$factual-academic-writing`，提供任务、材料与所需形式。只有希望每次会话默认采用此规范时，才需要以下配置。

1. 找到 Codex 配置目录：未设置 `CODEX_HOME` 时使用 `~/.codex`。已有非空的 `AGENTS.override.md` 时，编辑该文件；否则使用 `AGENTS.md`。备份要编辑的现有文件。[OpenAI 官方说明](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
2. 将 ZIP 内 `references/default-policy.md` 的完整正文写入该文件。文件不存在时新建；文件存在但没有这项规范时，在末尾另起一段追加。用 `<!-- factual-academic-writing-default:0.8.0 -->` 和 `<!-- /factual-academic-writing-default -->` 分别标记正文的起止，各占一行。已有旧规范时，在原位置替换整段规范及其版本标记（如有）。保留其他设置，只保留一份该规范。
3. 启动新会话，确认已加载这份写作规范；单独测试技能时，可显式调用技能名称。

## 资料与验证范围

见 [技能入口](SKILL.md)、[模板确认](references/manuscript-format.md)、[英文审校](references/english-review.md)、[标点审查](references/punctuation-review.md) 和 [变更记录](CHANGELOG.md)。可选扫描器只依赖 Python 标准库：`python scripts/scan_ai_patterns.py manuscript.txt`。扫描结果不能核实事实或判断作者身份。

正式 ZIP 包含 19 个运行文件。指定修复有原题回归记录；正式版本源码的 65 项相关技术测试通过。此次发布交付已核验的修复，现有评测没有证明它普遍优于 0.7.1。

ZIP SHA-256: `4f1f00f82970c1457022bc38d927ee7d7cb8e5f28f8bc9bc41ebdcfeb70ea0d3`
