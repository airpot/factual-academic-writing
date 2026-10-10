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

Connect the question, author claim, evidence, analysis and limits as the section requires.
Invent no findings, references, mechanisms, methods or author decisions.
Keep textual observations, calculations, interpretations, synthesis and hypotheses distinct.
Preserve direct quotation wording and internal punctuation exactly.
Qualify proposed readings without treating every interpretation as missing empirical proof.
Show calculation inputs, denominator, formula, units and relevant assumptions.
Keep justified statistical conclusions. Do not infer significance or causality from arithmetic.

Return requested prose, key claim links, and unresolved issues.
For mapped claims, give Claim_ID, Claim_kind, Support and specific evidence locators.
Record any Derivation separately from Support.
Link each claim to source provenance, author attestation and actual session inspection.
Keep mapping outside the manuscript unless inline IDs are requested.
```

## Edit expression

```text
Task: Improve the expression of {section} in {language}, with minimal necessary changes.
Draft: {existing text}
Evidence: {available source material or access limits}
Terms: {established terms}

Preserve quantities, uncertainty, negation, conditions, exceptions, scope and logical relations.
Preserve quotation wording and internal punctuation. Do not silently shorten quotes.
Do not replace unsupported numbers with unsupported qualitative claims.
Do not change a factual claim merely to clear a style finding.
Retain already clear prose, useful transitions, genuine parallel statements and disciplinary terms.
If evidence conflicts with the draft, preserve its status and list a separate correction proposal.
Evidence corrections may enter the revision only when the task requests them.

Return the prose, useful change reasons, and material unresolved issues.
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

Return Claim_ID, Claim_kind, Support, source locator, check limit and proposed correction.
Give Derivation when applicable. Link source provenance, author attestation and session inspection.
State checked parts, unseen parts and unresolved author decisions.
Do not certify submission readiness while required checks remain open.
```
