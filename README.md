# Factual Academic Writing · 事实驱动学术写作

**当前正式版：0.1.0。** 据所给研究材料组织学术论证、编辑表达或审查证据。
保留作者立场、数字、条件、否定、结论强度和直接引文；不补造数据、来源、方法或作者决定。

## 三种模式

| 模式 | 交付 |
| --- | --- |
| 转写 | 所需正文、关键论断与来源对应、未决事项 |
| 保义编辑 | 清晰表达、重要修改理由、单列的证据问题 |
| 证据审查 | 有位置的支持判断、冲突、修订建议和检查范围 |

论断类型、支持程度、计算过程、作者报告和本次核验分别记录。
文献核查分为存在性、元数据、内容支持和更新情况；读取节选不等于核验全文或底层数据。
可按量化、质性、综述、解释/理论和计算研究选择章节要点，不强制所有论文采用同一结构。
小型润色无需完整事实台账；文学解释可据文本有条件成立。

## 安装

本仓库根目录即完整技能目录，包含 [SKILL.md](SKILL.md)、参考资料和扫描脚本。
复制整个目录到所用代理的技能目录，命名为 `factual-academic-writing`。
若已有同名安装，先备份旧目录。

Codex 用户可在 PowerShell 中安装指定版本：

```powershell
git clone --branch v0.1.0 https://github.com/airpot/factual-academic-writing.git "$env:USERPROFILE\.codex\skills\factual-academic-writing"
```

也可下载 [0.1.0 源码 ZIP](https://github.com/airpot/factual-academic-writing/archive/refs/tags/v0.1.0.zip)，解压并按上述名称放入技能目录。
在新会话中调用 `$factual-academic-writing`，提供所需模式、材料和输出范围。

## 使用示例

- “请据这些数据和来源转写结果部分，列出关键论断的来源，不补写未做的实验。”
- “仅润色这一段，保留数字、否定、条件和引文；证据问题另列。”
- “审查摘要、方法、表格和结论的口径，标出样本数、分母、单位及结论强度冲突。”

默认只使用提供的材料。需要外部检索时明确提出，输出应说明实际访问了哪些资料。
未见部分与作者待决问题必须保留；最终学术判断和作者审阅仍需完成。

## 可选中文扫描器

Python 3.9 或以上，仅用标准库。写作和证据审查不依赖该脚本。
在本技能目录运行：

```text
python scripts/scan_ai_patterns.py manuscript.txt
python scripts/scan_ai_patterns.py --text "待检查文本" --format json
python scripts/scan_ai_patterns.py --help
```

返回码 0 表示扫描完成；输入错误返回 2。
显式 `--fail-on review` 在有命中时返回 1，只用于语言模式提示。
命中可修订、说明理由后保留或交作者决定，无需清零。

扫描器采用有限语法规则，可能误判复杂引号、公式及 Markdown。
它不能判断 AI 作者身份、引用真伪或论文是否可提交。
本版已做有限案例观察，尚未证明普遍写作提效或真实论文全文的可靠性。

## 维护

本仓库分发该技能的独立安装树；开发规格、测试和评测证据保留在统一源码工作区。
变更见 [CHANGELOG](CHANGELOG.md)，执行入口见 [SKILL.md](SKILL.md)。
