# Default Review Loop

Use for draft, expression-edit and audit delivery unless the user explicitly changes the review depth.
At least three complete rounds within five attempts are practical defaults, not a proven optimal count or a guarantee of error-free prose.
The coordinating assistant owns this one loop for the requested artifact. A reviewer invoked for a round performs one complete review and returns its findings; it does not start a nested loop or recruit more reviewers.
Use only reviewer facilities authorized for this task. If the approved facility is unavailable, use the self-review fallback; review permission does not authorize creating separate application tasks or messaging other conversations as a substitute.

## Start from the actual task

Keep the requested mode, current raw material, author decisions and output constraints as the review scope.
Record the current input/scope and artifact identities privately. For saved work, hashes or immutable versioned files are useful; a small edit can keep the same record in working context.
Keep three separate counts: attempts used, completed full rounds, and consecutive clean reviews. Starting a review uses one attempt. Count a completed round only after its full coverage and completion are confirmed.
For a delegated round, confirm that the reviewer finished its assigned review; a saved partial result or a still-running reviewer is not completion. For self-review, record the actual end of the separate full pass. It does not require the coordinating assistant to stop running. Use the same three counts.
Identify protected quantities, quotations, conditions, modality, capacities, completed actions and author judgments before writing.
Do not replace an author judgment with only its evidence or only its limitation.

An initial generation is a draft, not a completed review round.
Review the whole requested available artifact. For long work, cover its parts and their connections; mark unseen parts.
A review of one repaired sentence cannot establish whole-section or whole-manuscript coverage.

## Perform each round

1. Review the current artifact against the raw material and task. Check meaning and support relations, argument and author voice, repeated propositions, qualifications, exact quotations, terminology and output constraints.
2. When available and authorized, use a fresh independent reviewer with only the current artifact, raw material and requested scope. Give no preferred answer or previous review opinions. Otherwise make a separate self-review using the same checks; do not call it independent.
3. Locate each issue and compare it with the material. Classify it as accepted for correction, rejected with a source-grounded reason, or pending evidence/author decision. Keep real boundary distinctions and evidence-to-inference steps.
4. Correct accepted issues within the user's mode and recheck affected claims and connections. Keep effective unaffected wording. In expression-only work, restore meanings lost by rewriting; corrections to unsupported original assertions remain separate proposals.
5. Record coverage, reviewed artifact/input identity, findings, dispositions, changed spans and the next action privately. Save files for substantial work or when requested; a small edit needs no formal log.

Each complete round checks all dimensions. Its main focus can change, but meaning, argument, voice and expression still need coverage.
Do not divide three rounds into isolated checks that never re-examine the whole final artifact.

For a substantial finding, keep these useful fields:

| Field | Required information |
| --- | --- |
| Location | Exact clause, paragraph or artifact range. |
| Basis | Source item, author decision or functional reasoning that demonstrates the problem. |
| Difference | Lost or added meaning, inferential gap, or failed reader function. |
| Correction | The smallest change that repairs it within the requested mode. |
| Recheck | Affected meaning, neighboring inference and full-review status. |

“Make it more natural” alone supplies no demonstrated defect and cannot compel a rewrite.
An expression finding can use an explained rhetorical basis. It need not pretend to be an externally measured fact.
Fresh reviewers can share model preferences and blind spots. Fresh context does not establish statistical independence or human validation.

### Supported feedback example

Synthetic source item 2: a team has prepared a label for returning an object. No completed return is reported.
Draft: “The label records the object's completed return.”
Finding: the completed action exceeds the preparation described in source item 2.
Accepted correction: “The team prepared a label for the object's return.”
Recheck: compare the action state with item 2 and check nearby claims about possession.
The corrected sentence still needs the next complete artifact review. Its local check does not increase the clean streak.

Rejected style finding: “Replace ‘此外’ because it sounds generated.”
Reason: the sentence adds a separate supplied observation. The connector has an actual additive function.
Retain it unless another located problem makes revision useful.

### Self-review fallback

When no authorized reviewer facility is available, perform the same full checks in a separate pass.
Start from the current text and raw material. Reconstruct claim relations rather than merely reread an earlier quality judgment.
Record actual issues and decisions. An unchanged artifact can be valid, but only after its required checks occur.
Do not describe self-review as independent. Do not fabricate tool use, completed rounds or a clean result from a policy explanation.

Do not equate a reviewer opinion with a verified fact. Rejecting a finding requires its actual source or reasoning basis.
In expression-only work, separately reported problems in the original assertions belong to an evidence-correction status outside the editing scope. They do not block the expression artifact's clean streak when the required meaning is preserved and the problem is accurately disclosed; unresolved defects in the edit or decisions needed to preserve its meaning still block it.
Distinguish expression-review convergence from factual validation of those assertions. Do not call the source manuscript factually clean because its expression loop converged.
If a review or required check cannot be completed, retain the incomplete status; an execution failure is not a completed round.
Repair a recoverable execution problem. If it remains unavailable, return the affected provisional work and validation limit rather than fabricate completion or retry indefinitely.
An interrupted or failed attempt stays in the five-attempt budget and does not increase completed rounds. Starting its replacement uses another attempt. A local correction check is part of its current attempt, not a new full review.

## Decide whether to continue

The clean streak increases only when a complete review of the current full scope has no accepted or pending issue, makes no artifact change, and checks the same artifact and input scope as the preceding clean round.
The first such round starts the streak at one.
Any accepted or pending issue, incomplete coverage, correction, new input, changed author decision or later style rewrite resets it to zero.
Rejected findings with verified reasons do not themselves reset the streak.
Changing inputs never refreshes the five-attempt budget automatically; record the changed scope and any resulting incomplete validation.

| State after a round | Next action |
| --- | --- |
| Gate met: at least three completed full rounds, two consecutive clean complete reviews, no open required decision/check | Deliver the reviewed artifact; freeze its wording. |
| Gate not met and five attempts used | Stop. Deliver provisional work with located unresolved items or incomplete convergence status, even if fewer than three full rounds completed. |
| Gate not met and required material or an author decision prevents meaningful correction | Preserve the uncertainty, return useful provisional work and name the required decision. |
| Gate not met, fewer than five attempts used, correction/review remains possible | Continue with the current artifact. Count a replacement review as a new attempt. |

Apply the rows in order. At the cap, do not continue to satisfy the minimum, relabel an interrupted attempt as complete, or restart the same loop under a new cycle name. Further review needs an explicit new user instruction; preserve the previous provisional result.

A round with a correction never counts as a clean full review of the corrected artifact, even if its changed spans pass a local check.
Do not shorten the loop merely because the task is small, the final wording looks polished, or a scanner has zero matches.
Do not add a rewrite to fill the round count. Several reviewers can agree while missing an issue; convergence is a bounded review result, not proof of correctness.
For an audit, review the audit report as the artifact. It may accurately retain defects in the source manuscript; a converged audit does not make that manuscript clean.

## Deliver with the right status

Return the requested prose or audit. Keep process records outside prose-only output.
If the default gate is met, report the actual scope and review type only when useful or requested.
If the gate is not met, provide a brief provisional-status note and located remaining issues; do not label the output clean or submission-ready.
For an explicit single-draft or reduced-round request, honor that depth and state that the default loop was not completed.
Do not claim source access, factual verification, human review or independent review that did not occur.
