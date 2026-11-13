# Punctuation review

Use this reference in the existing Draft, Edit or Audit review. A quick private check is enough for routine text. For substantial copy, mixed passages, publication or final-copy work, inspect doubtful marks in context and locate material findings. Check the rendered medium when the question concerns layout.

1. **Function.** Identify the sentence force, the clauses or list items a mark joins, and the scope of modifiers, conditions, negation, quotations and asides. A different pause or enclosure can select a different group or change what the source says. A title, label or list fragment may need no terminal mark. Retain purposeful literary punctuation.
2. **Form.** Identify the actual character and the convention for that part of the text. Check spacing, pairing, nesting and consistency. A mark's code point and its rendered advance are different: font, orientation, line breaks and compression can change the appearance without changing the text.
3. **Disposition.** Repair a confirmed defect within the task's authority. Keep valid alternatives unless the destination or user chooses a style. If a repair would choose an unresolved meaning, or alter a protected or designated text, locate the decision. In Audit, report the defect or difference without changing the source. Before submitting a diagnosis or a conditional repair, check that the reader can find the original mark and understand the defect without inferring it from the alternatives. Keep this check private in routine output-only edits. For official drafts and final copies, use the authority and comparison rules in [official-document review](official-document-review.md).

Preserve exact quotations, commands, code, URLs and link destinations, markup syntax, paths, JSON and schemas, identifiers and versions, formulae and protected numeric notation. Review editable visible text in its own role, such as a link label; validate structured syntax separately. Do not apply blanket ASCII or fullwidth substitution, or NFKC. After editing, compare affected claims in both directions: what changed, and where each required meaning remains. Check exact spans against the input, including punctuation; separately check attribution and the surrounding text. See [meaning preservation](meaning-preservation.md). The optional Chinese readability scanner does not validate punctuation.

## Chinese prose

[GB/T 15834-2011 is a current recommended national standard](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=22EA6D162E4110E752259661E1A0D0A8). In the registered standard text, §1 covers modern Chinese, including Chinese portions of mixed Chinese and foreign-language layout. Apply the relevant provision and destination requirements; see [Chinese review](chinese-review.md) and [its source notes](chinese-sources.md). Annex A supplements the rules; Annex B explains usage.

- Use sentence force to distinguish a question from a statement containing a question word (§§4.1–4.3, Annex A.2). Check the hierarchy before choosing commas, enumeration commas or semicolons (§§4.4–4.6). Adjacent numerals expressing an approximation usually take no enumeration comma; a shortened enumeration generally takes one (§4.5.3.4). Adjacent quoted items or work titles usually take no enumeration comma; an intervening annotation can warrant one (§4.5.3.5). Semicolons can also separate first-level clauses in some nonparallel complex sentences (§4.6.3.2).
- A colon can introduce, explain or summarize (§4.7). Check where its scope ends. Avoid nesting colons within one sentence in ordinary prose; separate levels in a list or provisions if nesting is necessary (§4.7.3.5).
- Check the reach of quotes, brackets and title marks. Under the standard, nested quotes use double outside and single inside (§4.8.3.4). In a set-off quotation spanning several paragraphs, start each paragraph with an opening quote and close only the last one (§4.8.3.5). Distinguish a complete, independent quotation from a fragment integrated into the host sentence before placing terminal marks (Annex B.2.1). Check whether a parenthesis annotates a sentence part or stands outside the sentence (Annex A.8). Check the scope of omissions rather than inserting an ellipsis mechanically.

## English prose

- In ordinary expository prose, avoid a bare comma joining independent clauses. Choose a period, semicolon or conjunction that fits the relation and the edit authority. Commas around a nonrestrictive clause signal supplementary information; adding them to a restrictive clause can change the group described. A medial supplement needs a closing boundary before the main clause resumes; a sentence-final supplement needs no comma before the terminal mark. If only the intended group is unknown, locate the clause and explain the possible scopes without calling the uncertainty a punctuation defect. If the context independently establishes a medial supplement and the main clause resumes without its closing comma, locate the missing boundary and explain the defect before or with any author query.
- Check apostrophes for possession or omission, and distinguish abbreviation and decimal points from sentence ends. Keep numbers and exact tokens intact. Check ellipses for actual omission or intentional trailing off. Distinguish hyphens joining words from dashes setting off material or marking ranges according to the applicable style. Check spaces around prose punctuation, including dashes, against that style.
- Check quote pairing, nesting and what each terminal mark belongs to. Follow the requested or evidenced house style. For example, the [Australian Government Style Manual](https://www.stylemanual.gov.au/grammar-punctuation-and-conventions/punctuation/quotation-marks) normally uses single outer quotes and places a host mark outside an integrated quoted phrase. Chicago generally places periods and commas inside; [a CMOS editor's explanation](https://cmosshoptalk.com/2020/10/20/commas-and-periods-with-quotation-marks/) illustrates when outside placement can keep an exact string unambiguous. No house rule authorizes a change to a protected literal.

## Mixed passages and width

Assign each mark to the host sentence, embedded passage or protected syntax. A foreign term does not govern its surrounding sentence; a complete embedded passage can keep its own punctuation. Curly quotes, curly apostrophes and dashes are ordinary forms in some English styles. Non-ASCII does not mean fullwidth, and ASCII does not mean the mark is correct.

Use an exact character comparison when similar forms matter (for example, U+002C `,` versus U+FF0C `，`). Use the actual output for questions about spacing and line placement. When citing GB/T 15834-2011 for line-end width and typesetting compression, link the registered standard text and give both plain locators: §5.1.10 calls for a fullwidth mark at a line end to occupy half a character's space; §5.1.11 allows appropriate space compression in typesetting. These provisions concern layout, so narrow appearance alone does not establish the underlying character or the cause of the width. Cite [W3C Chinese Layout Requirements](https://www.w3.org/TR/clreq/) separately under its own name for typography. See [Unicode UAX #15](https://www.unicode.org/reports/tr15/#Norm_Forms) for compatibility normalization and the distinctions it can erase.

## Check a registered link

For a link you add to the GB/T 15834-2011 standard text, use authority ID `gbt-15834-2011` and the exact URL in the [checker](../scripts/check_registered_citation.py). From the skill directory, run `python scripts/check_registered_citation.py gbt-15834-2011` to get the URL. Check each authored occurrence in the actual submission text, and recheck each changed occurrence before submission.

Resolve the one visible link in the actual authored occurrence, including any reference definition it uses. Compare its exact href with `python scripts/check_registered_citation.py gbt-15834-2011 --destination URL` and require exit 0. Pass only the resolved href. If no active link is visible or more than one link could be the citation, fix the occurrence and check again. Do not check a substring taken from a comment, code example or protected quotation. If Python is unavailable, compare the resolved href literally with the registered URL.

Treat exit 0 from a comparison as an address match only. Lookup without a comparison operand also returns 0 and prints the registered URL alone. Separately inspect the visible title and edition, the cited provision, whether it supports the claim, and whether the destination was accessible. If any of those checks fails or remains open, do not report the citation as verified.

| Visible citation and resolved address | Address comparison | Citation decision |
| --- | --- | --- |
| GB/T 15834-2011, at the registered address | Match | Still inspect the provision and its support for the claim. |
| GB/T 15835-2011, at that same address | Match | The label names a different standard. Confirm the intended source and repair the citation. |
| GB/T 15834-2011, at an unrelated address | Mismatch | Resolve the correct document before citing it. |

The optional inline shortcut accepts one complete active inline link as the whole argument, with no CR or LF. Keep the label closing bracket and the destination opening parenthesis adjacent. Only spaces or tabs may surround the destination and title inside the outer parentheses; a title must be separated from the destination by at least one space or tab.

| Part | Shortcut requirements |
| --- | --- |
| Label | Include a letter or number other than an invisible Hangul filler after the checker applies Python's `html.unescape` to the label. This can decode a semicolonless entity such as `&copy` that Markdown renders literally; resolve the actual href if the shortcut rejects the label. The raw Markdown label cannot contain literal square brackets, angle brackets, backslashes or backticks. |
| Destination | Pass a nonempty literal URL, bare or wrapped in angle brackets. In either form, the raw URL token cannot contain whitespace matched by Python regex `\s`, angle brackets, parentheses, backslashes or an ampersand. |
| Title | Use single quotes, double quotes or parentheses. Do not include a backslash or the matching quote inside a quoted title, or a backslash or any parentheses inside a parenthesized title. |

Use the resolved-href method for any valid form outside this subset, including reference links, multiline links, escaped or nested labels, escaped titles and destinations written with Markdown entities or backslash escapes. If the renderer changes the destination spelling, compare the actual href with `--destination`. A percent-encoded URL is compared literally: do not percent-decode it for comparison. A shortcut diagnostic asking for `--destination` means the shortcut did not compare a URL; resolve the actual href before deciding whether the citation matches. The checker compares the URL, not the rendered structure, the claim's support or the link's availability.

Do not reconstruct the URL, add a fragment or substitute a search result, cached URL or mirror. Cached text can inform a judgment but does not establish that its indexed URL still opens. Keep the section number in plain text. This check applies only to explicit assistant-authored links to the registered standard text; leave supplied links, quotes, other authorities and protected literals untouched. If you cannot bind the destination and provision, give the supported judgment and state the evidence limit without that link.

## Worked decisions

| Situation | Decision |
| --- | --- |
| Chinese office note: `我想知道何时开门？` | Repair to `我想知道何时开门。` The sentence states a wish to know. Keep the question mark in `何时开门？` |
| Chinese title list: `书架上有《春潮》《归途》。` | No separator is normally needed here. Retain the separator in `书架上有《春潮》（修订版）、《归途》。` The parenthesis intervenes. |
| Chinese note: `请带齐：文件：申请表、回执。` | Use `请带齐下列文件：申请表、回执。` if wording edits are authorized. A change of colon glyph alone would not fix the introduction. |
| English update: `The log loaded, it contained 1.5 MB of data.` | A semicolon can repair the clause join without adding a causal claim. Keep the decimal point. |
| English eligibility notice: `Members, who renewed this year may vote.` | Flag the unmatched comma after `Members`. Ask whether all members renewed and may vote or only renewing members may vote. Closing the pair and removing the first comma convey different rules. |
| English sentence-final supplement: `We thanked Ava, who led the tour.` | If Ava is already identified, retain the comma after `Ava`; the period ends the supplement and the sentence. |
| English quoted phrase in body copy | Australian Government style: `The chair called it ‘a trial’.` Chicago-style placement: `The chair called it “a trial.”` The period is the host sentence's stop; do not turn it into part of an exact token. |
| Mixed text: 入口在 Setup 页面,请选择 `mode=a,b`。 | Change the host comma after 页面 to `，`. Keep the token comma and Markdown backticks. |
| English prose: `The driver’s key—still in its case—was on the desk．` | In ordinary English body text, replace the terminal U+FF0E with U+002E. Keep the apostrophe and dashes. A narrower Chinese comma at a PDF line end alone establishes no text error. |
| Chinese quote: `收到回执后,方可归档。登记簿写道：“未收到回执,不归档。”` | In a punctuation-only edit with an exact quotation, change the first comma to `，`; retain the quoted comma and stop. Keep both conditions and the negation. |

In a designated final copy, the last example would instead be a located discrepancy or proposal unless the user authorizes correction. In a short reply, apply the same distinctions without a visible checklist.
