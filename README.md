# Factual Academic Writing · 事实驱动写作

**正式版：0.6.0。** 将准确、论证、连贯和结构要求用于各类 AI 文字输出。按任务与读者组织解释，保留专业含义、条件、数字、引文及有意的创作表达。

起草时区分事实、推断、建议和假设；编辑时保持原意，将证据修正另列；审查时定位问题、依据与已检查范围。默认在五次尝试内完成至少三轮完整复核，末两轮对同稿无已接受或待决问题；变更重置连续通过数，不重置预算。用户可明确降低复核深度，小型任务无需正式日志。

0.6.0 增加公文任务的条件路由：区分拟稿、语言审查和指定基准的定稿校核，核实目的、文种、对象及可编辑阶段；分别记录原文保留、内部一致、实际来源比对与缺失材料。中文语法、语体、引文、数字和标点按上下文检查，不凭单个词形机械纠错，也不将公文体施于一般文字。

## 安装与默认规范

从 [v0.6.0 发布页](https://github.com/airpot/factual-academic-writing/releases/tag/v0.6.0)下载 `factual-academic-writing-0.6.0-source02.zip`，并按同页 `.zip.sha256` 核对。`source02` 是本版最终审定包的标识。备份同名旧安装，将完整 `factual-academic-writing/` 目录放到 Codex 支持的用户技能目录；本机现有入口为 `%USERPROFILE%\.agents\skills\` 和 `%USERPROFILE%\.codex\skills\`。若入口是符号链接，先核对实体位置并保留链接，不把备份放入技能发现目录。

显式调用 `$factual-academic-writing`，提供任务、材料与所需形式。按安装器说明，新技能在下一轮可用；如技能列表仍未刷新，可重启 Codex。磁盘安装完成不等于已观察到当前宿主加载。

设为全局默认时，先备份 `%USERPROFILE%\.codex\AGENTS.md`，再将 [default-policy.md](references/default-policy.md) 的完整正文写入现有受管默认块；没有该块时再追加。保留块外设置。有 `AGENTS.override.md` 时应核对实际使用文件。仅安装技能或写入路径不能证明已默认执行；宿主加载需另行观察。项目与用户的更具体要求仍适用。

## 资料与检查

见 [技能入口](SKILL.md)、[中文审查](references/chinese-review.md)、[公文审查](references/official-document-review.md)、[公文示例](references/official-document-examples.md)及 [变更记录](CHANGELOG.md)。可选扫描器只依赖 Python 标准库：`python scripts/scan_ai_patterns.py manuscript.txt`。扫描结果不判断作者身份，也不认证事实或文稿合格。

## 源码与验证边界

本仓库只分发独立安装树。运行源码来自统一工作区提交 `16fceab8ba54ca8c943ae4f85340c60e0f02e15b`，15 个运行文件与最终 source02 ZIP 逐字节一致。ZIP SHA-256：`85da7cc26024bbabb7dce3da8248f0bcd6c5acd0bbdf6c39d2448fb504b7a48d`。

固定源码已有 51 项相关检查通过；全仓 214 项中 213 通过、1 项因 Windows 符号链接权限跳过。原源码与输出模型复核已收敛；本次发布复用这些证据，并单独核验分发、远端资产和本地安装。原生候选生成使用前一源码提交，最终 source02 仅修正一处教学句的因果关系，未声称基于最终源码重新生成。模型复核不等于职业能力等同、普遍改善或零错误；实际从业者比较仍待开展。历史标签与发布资产保留。
