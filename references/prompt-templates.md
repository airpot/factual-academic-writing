# Mode-specific Prompt Templates

Use the selected template. Fill fields from the actual task without a universal intake form.
Evaluator criteria and previous answers are not execution inputs.
The linked resources define shared safeguards. Templates do not replace them.

## General answer

```text
Task: Answer {actual question} in {requested language and format} for {intended readers}.
Context: {relevant conversation, available knowledge, materials and access limits}.
Purpose: {useful result and constraints}.

Use the shared standard in SKILL.md and select the applicable task route.
Explain necessary concepts and the actual relations between ideas.
Select detail needed for the requested result. State the answer or action directly, introduce unfamiliar labels, and group shared conditions once.
Remove repeated explanations and cautions after checking that every required meaning and decision-changing limit remains.
Check sentence meaning, sentence relations, paragraph purpose and whole-document structure with ai-pattern-library.md.
For substantial prose, use academic-review.md to check the actual paragraph order. Select study-specific details only when relevant.
Distinguish facts, inferences, assumptions, recommendations and hypothetical examples.
Correct the assistant's own answer errors. Do not apply expression-only source preservation to new composition.
Use sources as required by this task and governing verification rules. Keep explicit source limits.
Use evidence-model.md when traceability is useful. Retain relevant access and execution status in technical answers.
Complete review-loop.md at its default depth unless the user explicitly changes it.
Return the useful answer and necessary limits. Keep private editorial records outside it.
```

## Explanation or teaching

```text
Explain {question or concept} for {reader knowledge and purpose}.
Start from necessary prerequisites. Connect each new idea to the point it develops.
Use an example when it helps. Identify invented teaching content as hypothetical, not observed evidence.
Keep stable technical terms and explain them at the required level.
Use a check for understanding only when it helps the actual learning task.
Apply the General answer safeguards and the complete default review loop. Do not force a lesson format on a short explanation.
```

## Draft

Use this template for academic composition from supplied material. Use General answer for other new prose.

```text
Task: Write {section} in {language} for {discipline, study type and intended readers}.
Purpose: {what this section should help those readers understand}
Inputs: {supplied material and locators}
Author position: {supplied argument or interpretation, or an essential unresolved decision}
Terms and voice: {established terms and applicable sample, if available}
Constraints: {requested length, structure and delivery format}
Source policy: supplied material only unless external research is requested.

Use meaning-preservation.md for shared safeguards and a two-direction comparison.
Use academic-review.md to select the section's function, evidence relations and inferential steps.
For substantial work, check the draft's paragraph functions with a private reverse outline.
Use ai-pattern-library.md for reader progression and sample-grounded voice decisions.
Use evidence-model.md when claim mapping is useful. Keep mappings outside manuscript prose.
Complete review-loop.md at its default depth unless this request explicitly changes it.
Return the requested prose and necessary unresolved matters, not the private checking procedure.
```

## Edit expression

```text
Task: Improve {section} in {language} for {intended readers}.
Intent: {requested outcome, such as polish, compression, expansion, register change or reorganization}
Depth: {light editing or deep meaning-preserving rewriting}
Draft: {existing text}
Evidence: {available materials or access limits}
Terms and voice: {established terms and applicable author sample, if any}
Constraints: {requested length and delivery format}

Use meaning-preservation.md. The original is the meaning target in expression-only work.
Report evidence corrections separately unless applying them is requested.
Use ai-pattern-library.md for the selected intent and its acceptance checks.
Decide whether each suspected repeat or qualification has a useful function.
Use academic-review.md when structural reconstruction is needed.
Keep effective unaffected prose. Check both newly asserted meanings and omitted required meanings after rewriting.
Complete review-loop.md with proportionate checks. Small edits retain its default round count.
Return the prose and any necessary material conflict note. Keep private records outside prose-only output.
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
Task: Audit {claims and available manuscript parts}.
Inputs: {text, tables, materials and precise locators}
Scope and limits: {requested checks and unavailable material}

Use evidence-model.md for claim type, support, provenance, author attestation and actual inspection.
Use academic-review.md for argument, cross-part checks and separate citation checks.
Use meaning-preservation.md to check quantities, quotations, conditions and author judgments.
Keep derivation separate from support and a completed check separate from a successful finding.
Return located issues, proposed corrections, inspected parts and necessary unresolved decisions.
Review the audit report with review-loop.md. Accurate retained source defects are not defects in the report.
```
