# Mode-specific Prompt Templates

Use only the selected template. Actual task data belongs in the placeholders.
Evaluator criteria and previous answers are not execution inputs.

## Draft

```text
Task: Write {section} in {language} for {discipline and study type}.
Inputs: {actual supplied materials and locators}
Author position: {supplied argument or interpretation, or none}
Terms: {relevant established terms}
Source policy: supplied material only, unless external research is requested.

Choose a central point that advances the requested section.
Privately distinguish source observations, capacities, possible interpretations and proposals before composition.
Select and order supplied evidence by its relation to that point. Explain the inference rather than list facts.
Connect the question, author claim, evidence, analysis and limits as the section requires.
For literature synthesis, compare relevant dimensions and explain how the comparison informs the author's question.
Invent no findings, references, mechanisms, methods or author decisions.
Keep textual observations, calculations, interpretations, synthesis and hypotheses distinct.
Preserve direct quotation wording and internal punctuation exactly.
Qualify proposed readings without treating every interpretation as missing empirical proof.
Show calculation inputs, denominator, formula, units and relevant assumptions.
Keep justified statistical conclusions. Do not infer significance or causality from arithmetic.
Before delivery, compare sentence meanings across the passage. State each conclusion once unless another occurrence serves a distinct section function.
For one central contrast, choose one explicit statement of the contrast and keep the evidence and needed inference.
Make a separate deletion pass; "this answers" or "therefore" does not make a repeated conclusion a new reasoning step.
Keep the reasoning from evidence to the conclusion. End when the paragraph has done its job.
Omit a closing paraphrase that does no new job; keep a warranted synthesis or a requested summary.
Use qualifications for actual claims that need them. Do not list absent studies for outcomes the prose does not assert.
Check each final clause against the material. A capacity or prepared action is not a completed act; a possible explanation remains possible.
Preserve commitment in both directions. Do not weaken an asserted capacity or the stated consequence of an uncertain condition by adding another possibility marker.
Check premises, relative clauses and abstract summaries too. Name the measured construct or coded actions needed to understand the result.
Keep the check private; use modal wording in prose rather than a report of what the source does not prove.

Before delivery, complete the default review loop from SKILL.md unless the user explicitly changes its depth.
Return the requested prose. Add key claim links and unresolved issues when relevant or requested.
For mapped claims, give Claim_ID, Claim_kind, Support and specific evidence locators.
Record any Derivation separately from Support.
Link each claim to source provenance, author attestation and actual session inspection.
Keep mapping outside the manuscript unless inline IDs are requested.
```

## Edit expression

```text
Task: Improve the expression of {section} in {language}.
Depth: {light editing or deep meaning-preserving rewriting, as requested}
Draft: {existing text}
Evidence: {available source material or access limits}
Terms: {established terms}
Author sample: {supplied sample, if any}

For light editing, keep effective wording and order. For deep rewriting, reconstruct sentences or paragraphs when needed.
Before reconstruction, identify protected claim states, conditions and distinct limits privately.
Diagnose empty framing, repeated propositions, unclear referents, weak connections, and voice mismatch.
Revise around the same supported point. Do not add research content to make the expression concrete.
Use the author sample's register and directness without importing its unrelated assertions.

Preserve quantities, uncertainty, negation, conditions, exceptions, scope and logical relations.
Preserve quotation wording and internal punctuation. Do not silently shorten quotes.
Do not replace unsupported numbers with unsupported qualitative claims.
Do not change a factual claim merely to clear a style finding.
Retain already clear prose, useful transitions, genuine parallel statements and disciplinary terms.
If evidence conflicts with the draft, preserve its status and list a separate correction proposal.
Evidence corrections may enter the revision only when the task requests them.

Compare the revision with the original for meaning, argument progression, expression, and author voice.
Compare nonadjacent sentence meanings. Merge or remove a repeated proposition that does no new job, while keeping evidence and needed reasoning.
Try removing suspected repeats after composition. Keep the part needed for evidence, inference, a distinct boundary, or a section connection.
Then compare each surviving clause with the original. Restore lost possibility, condition or scope at the affected claim.
Do not add uncertainty to a supplied assertion or conditional consequence. Keep uncertainty about a condition separate from what follows if it holds.
Do not turn a possible explanation, capacity, prepared action or proposal into a fact or completed act.
Keep the uncertainty of premises and limitations. Check abstract summaries for implied completion.
Use appropriate modal wording; do not insert the private source-check procedure into manuscript prose.
Before delivery, complete the default review loop from SKILL.md; a small edit uses proportionate checks, not an exemption.
Preserve each distinct supplied boundary. Combine duplicated limits only when their scope stays clear.
Repeat a boundary where separate claims or independently readable sections need it.
Do not replace a redundant ending with another paraphrase or an unrelated disclaimer.
Return the prose, with useful change reasons and material unresolved issues when requested or needed.
For prose-only requests, keep the output to the prose unless a material conflict requires a separate note.
Do not append unrelated source-check disclaimers to an expression edit.
Do not require a full evidence ledger for a small edit.
```

## Audit evidence and manuscript

```text
Task: Audit {requested claims and available manuscript parts}.
Inputs: {text, tables, source materials and precise locators}
Access limits: {unavailable materials}

For each substantial claim, identify its type, support degree and evidence relation.
Keep calculation or formal derivation separate from support.
Retain every relevant conflict, version, condition and access limit.
For citations, separate existence, metadata, content support and update checks.
State what material was actually read. Do not claim full-paper inspection from an excerpt.
For cross-part review, compare counts, denominators, units, design, outcomes, terms and conclusions.
Check quotation fidelity, overgeneralization, unsupported causality and misplaced author interpretation.
A source record or author assertion does not certify study validity.

Review the audit report through the default loop from SKILL.md; retained source defects are not defects in an accurate audit report.
Return Claim_ID, Claim_kind, Support, source locator, check limit and proposed correction.
Give Derivation when applicable. Link source provenance, author attestation and session inspection.
State checked parts, unseen parts and unresolved author decisions.
Do not certify submission readiness while required checks remain open.
```
