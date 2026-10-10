# Readability Review Reference

The historical filename is retained for continuity. This file defines readability judgments, not an AI-origin test.
The purpose is clear academic prose with faithful evidence and relations.

## Review candidates

| Observation | Review question | Valid disposition |
| --- | --- | --- |
| Empty promotion, such as 全面赋能 or 颠覆性创新 | Does evidence support this evaluation? Does it add necessary meaning? | Remove empty evaluation or retain a supported, attributed usage. |
| Broad attribution, such as 大量研究表明 | Which accessible sources support the exact claim and scope? | Give real source details or mark missing support. |
| A transition, such as 此外 | Does it express an actual additive or contrasting relation? | Retain the relation when useful. No automatic replacement is required. |
| Parallel clauses or a numbered sequence | Are the underlying statements parallel or sequential? | Preserve genuine parallel facts and necessary process steps. |
| A technical term, such as 城市空间格局 | Is it the established term for this field? | Keep the accepted term. Do not replace it to avoid a keyword. |
| An exact quotation | Does its wording come from the cited speaker or source? | Preserve wording and attribution. Audit its factual claim separately. |
| A short or uniform sentence sequence | Is the text clear and logically connected? | Leave clear prose alone. Do not manufacture variance. |
| A rhetorical question | Does it obscure the actual research question, mechanism, or evidence? | Prefer a direct statement when it improves the requested section. |

Do not turn parallel, sequential, or correlational facts into a causal narrative.
Do not hide a real baseline comparison to make a contribution appear more novel.
No sentence-length threshold, perplexity measure, or paragraph-symmetry score establishes writing quality or AI authorship here.

## Same-fact revision example

Synthetic teaching fixture; no actual system or study is asserted.

Input evidence:

```yaml
Source_ID: S1
Reference: "Supplied fictional functionality note"
Locator: "item 1"
Author_attestation: reported_by_author
Session_verification: not_checked
Fact_ID: F1
Statement: "The prototype records audit logs to review manual changes."
Scope: "prototype system"
```

Before:

> 此外，原型系统还构建了审计日志，用于回看人工修改记录。

After:

> 原型系统记录审计日志，用于回看人工修改记录。

Claim C1 maps to F1, S1, item 1. The change removes redundant expression and retains the supplied mechanism and purpose.
Hash storage, XML parsing and tamper resistance are not supplied facts and must not appear in this rewrite.

## Quotation example

Synthetic teaching fixture:

> 受访者甲将该政策称为“全面赋能的里程碑”。

The attributed words remain verbatim. They support the participant's stated opinion.
They do not establish that the policy achieved a measured improvement.
The scanner can exclude common quotation spans. Human review must still check attribution and source fidelity.

## Resolve a finding

Record its disposition as `revise`, `retain with reason`, or `needs author decision`.
The scanner only identifies configured text patterns. It cannot judge all discourse, evidence, or disciplinary terms.
After a justified edit, one rescan can confirm the match changed. Repeated matches do not justify distortion of the source.
