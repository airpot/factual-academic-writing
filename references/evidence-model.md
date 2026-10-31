# Evidence and Claim Model

Use the smallest record that makes the requested work auditable. Existing author records are acceptable.
Keep IDs stable. They locate evidence and do not certify truth.

## Proportionate evidence and status reporting

Apply these distinctions to general answers as well as manuscripts. A short explanation needs no formal claim ledger.
Distinguish facts, inferences, assumptions, recommendations and hypothetical examples in wording appropriate to the task.
Use the records below when traceability or an audit needs them. Do not force research fields into every reply.
Keep bounded source work within its agreed materials. General answers use sources as required by the task and governing verification rules.

In technical answers, state relevant access, execution and validation status. A proposed command is not an executed command.
A file read does not establish that the described system ran. A successful local check establishes only its actual checked scope.
Keep `not run`, `blocked`, `failed` and `passed` distinct. Name an important uninspected dependency or missing check when it limits the result.
Report only actions and outcomes that occurred. Keep useful status in the answer while private editorial records remain private.
In creative work, a fictional event needs no empirical source. A real-world factual assertion outside that frame still needs an appropriate basis.

## Source record

```yaml
Source_ID: S1
Reference: "Author's supplied prototype record"
Locator: "file A, item 1"
Provenance: author_supplied_record
Author_attestation: reported_by_author
Session_verification: not_checked
Checked_material: none
Check_limit: "No independent source-file or system inspection."
```

Keep provenance, author attestation, and session inspection independent.

| Field | Values and meaning |
| --- | --- |
| Author_attestation | `not_stated` or `reported_by_author`. A report is not an independent check. |
| Session_verification | `not_checked`, `source_checked`, or `unresolved`. Record the actual check and its limit. |
| Checked_material | Actual file, version, excerpt, abstract, full text, table, or dataset inspected. Use `none` when nothing was inspected. |

Receiving a draft assertion does not inspect its underlying source.
Reading a local excerpt can establish its wording. It does not inspect the original publication or authenticate the excerpt.
For a checked source, record the available locator and what the check established.
Keep publication identity, content support, and underlying study validity separate.
Use an actual version or hash when needed. If the locator is unavailable, record that limit.

## Claim record

```yaml
Claim_ID: C1
Text: "The prototype records audit logs to review manual changes."
Claim_kind: observation
Support: supported
Evidence:
  - Source_ID: S1
    Locator: "file A, item 1"
    Supports: "The reported function and purpose, within the prototype scope."
Scope: "Author's reported prototype."
Inspection: "See S1 for author attestation and session inspection."
```

| Claim_kind | Meaning |
| --- | --- |
| observation | A reported event, measurement, method, or textual feature. |
| calculation | A numerical result with named inputs and a formula. |
| interpretation | An author's reading or explanation supported to a stated degree. |
| synthesis | A comparison or argument across sources. |
| hypothesis | A proposition for future examination, not a completed finding. |

| Support | Meaning |
| --- | --- |
| supported | The available evidence supports this wording, claim type, and stated scope. |
| partial | Evidence supports only identified parts or conditions. Split claims when useful. |
| missing | Necessary evidence is unavailable or inadequate. State what is missing. |
| conflicting | Accessible evidence contradicts the claim or gives unresolved alternatives. Preserve each locator. |

Support describes the evidence relation. It does not certify source truth, data integrity, or methodological validity.
A supplied research record can support a reported result within its scope while session inspection remains `not_checked`.
A draft alone supports that its author made an assertion, not that the asserted result occurred.
A quotation supports the speaker's words. Do not treat the quoted opinion as a measured outcome.
For each link, identify what it supports. A reference attached to one clause need not support the whole sentence.

## Calculations and conflicting inputs

Synthetic fixture, not an actual study:

```yaml
Claim_ID: C2
Text: "The final endpoint rate is 40%."
Claim_kind: calculation
Support: conflicting
Evidence:
  - {Source_ID: A, Locator: "line 1", Supports: "32 of 80, version A"}
  - {Source_ID: B, Locator: "line 1", Supports: "24 of 80, version B"}
Derivation:
  Inputs: {A: "32 of 80", B: "24 of 80"}
  Formula: "A gives 32/80=40%. B gives 24/80=30%."
  Assumptions: "No confirmed version precedence."
Limit: "Both calculations are correct. The final rate is not established."
```

Keep denominator, units, assumptions, input uncertainty, and rounding visible.
A percentage-point difference is not the relative percentage change.
Do not infer a paired change from different aggregate samples.
Do not infer significance, causation, or practical importance from a difference alone.
If valid statistical evidence is supplied, preserve it with its method, scope, and uncertainty.
Formal derivations require their assumptions and reasoning. A category label alone does not establish a proof.

## Interpretations and synthesis

An interpretation can be supported as a qualified reading without being uniquely proven.
Link the reading to textual features, the author's stated position, and relevant counterevidence.
Do not label every literary interpretation as missing empirical proof.
Do not treat an author's supplied interpretation as evidence of a character's established motive or historical author intent.
A new reading needs appropriate qualification and an author-decision note when it changes the argument.
A hypothesis remains a hypothesis even when it has a plausible rationale.
For synthesis, preserve source differences, methods, populations, and conditions. Do not manufacture agreement.

## Transition from rc.1 records

Do not rewrite raw historical records.
Map `supported_by_supplied_source` to `supported` with its original scope and inspection limit.
Map `needs_evidence` to `missing`. Map `contradicted` to `conflicting` and retain the contradiction details.
For `Support: derived`, retain inputs and formula under `Derivation`.
Select `Claim_kind: calculation` for numerical results and reassess support separately.
For a formal inference, select the applicable claim kind and preserve its proof or reasoning.
Do not invent a supported status when the old record omits a necessary check.

For legacy `Verification: reported_by_author`, retain author attestation and use `Session_verification: not_checked` unless a check is documented.
Retain both fields when author reporting and session inspection coexist.
