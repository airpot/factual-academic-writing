# Evidence and Claim Model

Use the smallest record that makes the requested work auditable. Existing author records are acceptable.
Keep IDs stable. They locate evidence and do not certify truth.
In an audit, copy each quoted locator exactly, including limiting words or quantities within it. If you shorten it by restating the idea, present that wording as an unquoted paraphrase. For parallel language versions that express the same item, compare their scope, quantities and status with each other as well as with their cited support.

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

## Give a usable decision under conflict

- Locate the disagreement and its scope. Check authority, version, date and applicability. Use established precedence; recency, format or confidence alone does not create it. When applicability turns on edition or effective date or time, carry the relevant edition and exact effective boundary (with any supplied time zone) into the delivered locator, alongside the action it supports. For overlapping sources, make the date or time visibly apply to each source it governs. Use one shared locator when its coverage is clear; omit metadata that has no role in the decision.
- If one record better supports a provisional operational judgment, state which record and why. Keep the contrary evidence and the confirmation that could change the decision. When the evidence does not support a judgment, state what is unresolved and any supported hold or verification step. Do not invent a hold, permission or owner.
- Give the action for each material condition the evidence supports. Distinguish the status of a release, permit or instruction from proof that a person or site has met its conditions. An unknown local state does not erase a supported conditional decision, and a conflict in one branch does not suspend independent actions. Test what the reader does both while a decision is pending and once it arrives. Give the next step if the record supports it. If the designated decision-maker will set it, instruct the reader to follow that decision without assuming an outcome or granting release. When messages are forwarded separately, include the applicable decision authority and the record that makes the rule apply in each message that relies on them. For example, an accession sheet may establish both the box count for dispatch and a restricted status for reading-room use. Citing it only for the count in the dispatch note does not give the reading-room recipient a basis for the restriction. A title or heading can identify the recipient’s own duties, but it cannot identify a different decision-maker unless it names that role. When a signed entry approves delivery to the front desk and a separate schedule names the desk attendant, cite the entry for approval and destination and the schedule for coverage. The heading may address the attendant without implying that the signed entry appoints them. If the documents leave the actual mover open, keep it open.

Example: A measurement report lists a passed routine recheck for unit T8; a summary note says the recheck is pending without identifying a unit. If the local identifier is T8, the itemized report supports treating that routine recheck as already done for planning; it does not support repeating it just because of the summary. Ask the record owner to reconcile the status before closing the discrepancy. If the unit cannot be matched, verify the identifier and the applicable result. Neither record establishes permission to operate the unit.

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
