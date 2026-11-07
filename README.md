# Factual Academic Writing · 事实驱动写作

**正式版：0.7.1。** 将准确、论证、连贯和结构要求用于各类 AI 文字输出。起草时区分事实、推断、建议和假设；编辑时保留原意；审查时指出问题、依据和已检查范围。

草拟、编辑和审查均核对中英及混排标点。首次提交标点诊断前，核对原文符号、位置和问题；引用已登记的标准时，核对条款与实际提交的链接。

## 安装与默认规范

从 [v0.7.1 发布页](https://github.com/airpot/factual-academic-writing/releases/tag/v0.7.1)下载 `factual-academic-writing-0.7.1.zip`，按同页 `.zip.sha256` 核对。备份旧版，把解压后的完整 `factual-academic-writing/` 放入宿主实际使用的技能目录；在 Codex 中可使用 `%USERPROFILE%\.agents\skills\`。如现有入口是符号链接，先核对实际目录并保留链接；备份应放在技能发现目录之外。

显式调用 `$factual-academic-writing`，提供任务、材料与所需形式。若设为 Codex 的全局默认规范，先备份 `%USERPROFILE%\.codex\AGENTS.md`，再将包内 `references/default-policy.md` 的完整正文写入现有受管块；没有该块时可追加。保留块外设置，如有 `AGENTS.override.md`，先核对宿主实际使用的文件。安装和配置写入后，另行确认宿主是否加载。

## 资料与验证范围

见 [技能入口](SKILL.md)、[标点审查与示例](references/punctuation-review.md)、[默认规范](references/default-policy.md)及[变更记录](CHANGELOG.md)。可选扫描器只依赖 Python 标准库：`python scripts/scan_ai_patterns.py manuscript.txt`。扫描结果不判断作者身份或核实事实。

正式 ZIP 含 17 个运行文件。固定候选的 55 项相关测试和四个指定的修复后模型案例通过；未运行该候选的全仓测试。指定案例不能证明普遍可靠性。

ZIP SHA-256: `cc179b2a782d7d00497702646ee1411181300da026acc2dca562787f39b28491`
