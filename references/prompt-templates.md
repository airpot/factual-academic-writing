# Mode-specific Prompt Templates

Use only when a task card helps. These templates require the complete shared policy and applicable references from SKILL.md; they are not standalone replacements for that policy. Fill fields from the actual request without a universal intake form. Evaluator criteria and previous answers are not execution inputs.

## Shared contract for every template

Apply the existing mode authority, meaning preservation and finite review gate. Reuse confirmed reader/format decisions, ask only for material gaps, keep local preferences local and preserve protected spans. Use [response layers](response-layers.md) and, for a genuine required-format gap, [manuscript format](manuscript-format.md). Chinese tasks also use contextual language review and source/example limits. Templates add neither host-setting authority nor another loop.

Select detail and explain necessary concepts for the reader. Keep facts, inference, assumptions, recommendations and hypothetical examples distinct. Use [meaning preservation](meaning-preservation.md), [expression review](ai-pattern-library.md), [academic review](academic-review.md) for substantial structure, and [evidence model](evidence-model.md) for traceability when useful. Keep private records outside requested prose, with material unresolved issues and relevant technical access/execution status reported accurately.

## General answer

```text
Answer {actual question} in {language and format} for {reader knowledge and purpose}.
Use {context, appropriate knowledge, supplied material and source limits}.
Apply the shared contract. Correct the assistant's own errors rather than preserving them as a source-edit target.
Make the useful answer, necessary concepts, relations and supported next action findable.
Return the requested answer and decision-changing limits.
```

## Explanation or teaching

```text
Explain {question or concept} for {reader knowledge and purpose}.
Establish prerequisites, stable terms and actual connections. Use helpful examples and understanding checks.
Mark task-authorized invented teaching examples hypothetical, not observed evidence.
Apply the General answer contract without forcing a lesson format onto a short explanation.
```

## Draft

For bounded academic composition from supplied material; use General answer for other new prose.

```text
Write {section} for {discipline, study type, readers and purpose} in {language/format/length}.
Inputs: {supplied evidence and locators}; author position: {argument or necessary open decision}.
Terms and voice: {established terms and applicable sample}.
Source policy: supplied material only unless external research is requested.
Apply the shared contract and the section's function, evidence relations and inferential steps.
Keep the reverse outline and claim mapping private. Return the prose and necessary unresolved matters.
```

## Edit expression

```text
Improve {passage} for {readers} in {language/length/format}.
Intent: {polish/compress/expand/change register/reorganize}; depth: {light or deep}.
Source: {existing text}; evidence/access: {available material}; voice/terms: {sample and stable terms}.
The original is the meaning target. Apply the shared contract and each compatible intent check.
Keep effective prose and every required distinct meaning; report evidence corrections separately unless authorized to apply them.
Return the prose and any necessary material conflict note, not private process records.
```

## Optional edit task cards

These requests select an outcome within Edit. Use the shared Edit safeguards and intent checks above.
Fill useful fields from the actual request. Do not require the user to complete every field.

### Compression

```text
Compress {passage} to {requested size} for {readers}.
Keep {required content within the requested scope}. Remove repeated meaning and empty wording.
If the size conflicts with required content, state the conflict rather than silently omit it.
```

### Expansion

```text
Develop {passage} to {requested size} for {readers} using {available material}.
Expand explanations and supported connections. Identify missing support instead of inventing additions.
```

### Register change

```text
Rewrite {passage} for {readers and genre}, with {requested register or applicable voice sample}.
Keep essential technical terms and explain their meaning for these readers. Do not infer unreported method details.
Keep the underlying claims and author commitment.
```

### Reorganization

```text
Reorganize {section} so readers can follow {the intended argument or comparison}.
Improve paragraph order and connections while keeping required content and its attribution.
```

## Audit

```text
Audit {claims and available manuscript parts} using {text/tables/material and precise locators}.
Scope and limits: {requested checks and unavailable material}.
Apply the shared contract; distinguish support, derivation, provenance, author attestation and actual inspection.
Return located issues, proposals, inspected parts and necessary unresolved decisions.
Review this audit report itself. An accurate source-defect finding does not make that source true or authorize editing it.
```
