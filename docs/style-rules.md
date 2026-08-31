# Style, coherence and evidence rules

- **Status:** active
- **Version:** 1.2

The numbered rules that reviewers cite. A finding without a rule ID here, or a section reference in [../COMPLIANCE.md](../COMPLIANCE.md), is inadmissible under [review-spec.md](review-spec.md) §4.

Five families:

- **VOICE** — register and stance
- **TELL** — the recognisable residue of an assistant-tuned model
- **COH** — continuity, structure and warranted scope
- **EVID** — claims, figures and sources
- **FORM** — layout and typography

## 1. How to apply these rules

Articles here are written by a language model. Some of these patterns will appear in any draft; their presence is not misconduct and not evidence of anything. Judge them the way Wikipedia's AI Cleanup project judges its own list: no single sign proves anything, and a rule is worth citing only where it damages the text in front of you.

The severity threshold follows from that:

- One instance of a `TELL` or `FORM` pattern is `should-fix`.
- Three or more instances of the same pattern, or a pattern that shapes the whole article's structure, is a **pattern** and therefore `must-fix`.
- A `VOICE`, `COH` or `EVID` violation is graded on the damage it does, not on how many times it occurs. One fabricated citation is `must-fix` on its own; one loose handoff between otherwise coherent sections is normally `should-fix`, while a missing organising logic that fragments the whole article is `must-fix`.

Quote the span. "The tone is off" is not a finding.

## 2. VOICE — register and stance

**VOICE-01 · Register follows the subject.** A note on alpine plants may be unhurried and descriptive; a note on build tooling may be terse. There is no house voice to conform to. A finding may not be raised because the article does not sound like a previous article.

**VOICE-02 · Constants hold across every register.** Whatever the subject: claims are traceable to a source, findings are distinguished from interpretation, uncertainty is stated rather than smoothed over, and no sentence tries to be memorable at the cost of being exact.

**VOICE-03 · No persuasion machinery.** No building suspense before a "reveal", no rhetorical question used as a section transition, no thesis withheld to keep the reader scrolling. State the thing, then support it.

**VOICE-04 · Do not address or coach the reader.** No "you might be wondering", no "let us look at", no instructions about how to feel about a finding. The article reports; the reader concludes.

**VOICE-05 · No unearned significance.** Do not call a finding surprising, important, striking or a milestone unless the article shows why, against what baseline. Adjectives are not evidence.

**VOICE-06 · No meta-narration.** Do not describe the article's own structure ("this article will examine three aspects", "having established X, we now turn to Y"), and do not point at the page's own components ("the two numbers above"), beyond what the introduction genuinely needs.

**VOICE-07 · Hedge once.** State uncertainty precisely and once — a sample size, a date range, a competing interpretation. Stacked hedges ("it may possibly suggest that, to some extent") say less than one honest caveat.

## 3. TELL — assistant-model residue

### 3.1 Chinese

**TELL-C01 · Conclusion-first framing formulas.** 「先說結論」「直接說結論」「一句話總結」「結論先行」. State the conclusion if it belongs there; do not announce that you are about to.

**TELL-C02 · Aesthetic-satisfaction register.** 「更漂亮的一點是」「更妙的是」「這樣就很舒服」「很爽」「絲滑」「優雅」 used about a design, a result or a method. This is chat register, not writing.

**TELL-C03 · Empty emphasis markers.** 「值得注意的是」「需要指出的是」「不難發現」「事實上」「說白了」 where the sentence carries the same information without them.

**TELL-C04 · Reflexive negative parallelism.** 「不僅僅是 X，而是 Y」「與其說是 X，不如說是 Y」「這不是…，這是…」 as a rhetorical reflex rather than a real distinction the article goes on to use.

**TELL-C05 · Era openers.** 「在當今…的時代」「隨著…的快速發展」「近年來，隨著…」. Start with the question, not with the century.

**TELL-C06 · Consultant and product jargon.** 「賦能」「抓手」「閉環」「顆粒度」「打法」「對齊」「心智」「深入探討」「底層邏輯」「範式」 outside a direct quotation.

**TELL-C07 · Restating section closers.** 「總的來說」「綜上所述」「總結一下」「展望未來」 followed by a sentence that adds nothing to the section it closes.

**TELL-C08 · Leftover chat scaffolding.** 「讓我們一起…」「希望這對你有幫助」「以上就是…」「本文將…」「話不多說」.

**TELL-C09 · Framing sentences that assert nothing.** 「這其實是一個…的問題」「這背後反映的是…」 where no specific claim follows.

### 3.2 English

**TELL-E01 · Vocabulary tells.** *delve, testament to, tapestry, landscape (figurative), underscore, leverage (verb), seamless, robust, pivotal, crucial, game-changer, unlock, harness*, outside a quotation or a genuine term of art.

**TELL-E02 · Negative parallelism.** "It's not just X — it's Y", "This isn't about X. It's about Y", used as a reflex.

**TELL-E03 · Vague attribution.** "Studies show", "experts say", "research suggests", "it is widely believed" with no named source. See EVID-02.

**TELL-E04 · Editorialising asides.** "It's important to note that", "interestingly", "notably", "it's worth mentioning".

**TELL-E05 · Restating summaries.** "In summary", "overall", "in conclusion" introducing a sentence that repeats what precedes it.

**TELL-E06 · False ranges.** "Ranging from X to Y" where X and Y are not endpoints of anything measurable.

**TELL-E07 · Superficial analysis verbs.** "Highlighting", "illustrating", "showcasing", "reflecting" used to assert relevance the article never demonstrates.

**TELL-E08 · Era openers and letter phrasing.** "In today's fast-paced world", "as technology continues to evolve", "I hope this helps".

### 3.3 Structural

**TELL-S01 · Rule of three.** Triplets of adjectives, examples or clauses recurring across the article regardless of whether the subject has three of anything.

**TELL-S02 · Symmetric sections.** Every section the same length with the same internal shape — context, then two examples, then a closing line. Real subjects are lumpy.

**TELL-S03 · Both-sides closing.** A final paragraph that balances advantages against disadvantages and declines to conclude, where the evidence in the article does support a conclusion.

**TELL-S04 · Padding by enumeration.** A list of items that could be one sentence, or list entries carrying one clause each.

**TELL-S05 · Caveats in a fixed slot.** Limitations that all arrive in the same position and the same shape — a closing clause on the pattern "this is the figure for X, not Y", paragraph after paragraph — or a paragraph-final verdict with no stated subject. Each may be accurate and the set still reads as a mannerism. This is the commonest way an article acquires a tic from its own review: one `EVID` finding is cleared by bolting a qualification onto the end of a paragraph, and the next is cleared the same way.

## 4. COH — continuity, structure and warranted scope

These rules judge whether an article sustains the structure it has chosen. They do not prescribe a house structure. Chronological, spatial, causal, comparative, procedural, question-led, reference-style and other forms are all admissible; a short note may need no visible sections at all.

**COH-01 · The organising logic is recoverable.** The article's central question, claim or task and the relation among its main parts can be recovered from the published text. It may combine or change organising logics when the change is necessary and made legible. Do not require a journey, anecdote, narrative arc or any other preferred form.

**COH-02 · Sections hand off substance, not stage directions.** An adjacent section advances, tests, contrasts, narrows, widens or deliberately changes the level of the preceding discussion. A heading or transition should make that relation legible where it is not already obvious. Meta-narration such as "next we examine" does not repair a missing relation.

**COH-03 · Examples accumulate.** Examples, cases and profiles attach to a section-level claim and alter what the article has established. A repeated sequence of self-contained entries that resets the context each time is a defect when the article presents an explanation or argument; it is not a defect in a catalogue or reference article whose declared purpose is retrieval.

**COH-04 · Supporting apparatus keeps its place.** Checklists, glossaries, safety notes, source notes, rights records and methodological cautions belong in the main sequence when they advance the article's central task. Otherwise they are set apart as a note or appendix rather than interrupting the article's line of development.

**COH-05 · Scope is supported or narrowed.** When an article claims to explain a broad domain, provide a representative survey or cover named dimensions, its selection of evidence must support that claim. A reviewer may identify an omission only by showing which published scope claim, comparison or conclusion the omission leaves unsupported. There is no required number of examples and no universal coverage checklist.

**COH-06 · Endings resolve the opening task.** The ending states what the assembled evidence establishes, preserves any material limitation and returns to the question, claim or task that opened the article. A summary table can support that work but does not replace it when the article has developed an explanation or argument.

## 5. EVID — claims and sources

**EVID-01 · Every material claim carries a source.** Recorded per `COMPLIANCE.md` §1, with the source's date and limitations.

**EVID-02 · Attribution is specific.** Name the study, organisation or dataset in the text. A hyperlink alone does not satisfy this where the claim is contested or quantitative.

**EVID-03 · Figures carry their frame.** A number is stated with its population, denominator, period and units. A percentage without a base is a `must-fix` defect.

**EVID-04 · The cited source supports the cited claim.** A source that is real but does not say what the sentence claims is treated as a citation failure, at the same severity as a fabricated one.

**EVID-05 · Finding and interpretation are visibly separate.** The reader can tell in every paragraph which sentences report a source and which are the article's own reasoning.

**EVID-06 · Prefer the primary source.** A press release or secondary summary is cited only when the primary is unavailable, and the substitution is stated.

**EVID-07 · Uncertainty is carried forward.** If a source is preliminary, small, self-reported or vendor-funded, that qualification travels with the claim rather than living only in the source list.

**EVID-08 · No smoothed-over gaps.** Where the evidence does not settle a question, say so. An inferred bridge between two sourced facts is the article's own interpretation and is labelled as such.

## 6. FORM — layout and typography

**FORM-01 · Emphasis is rationed.** Bold marks a term on first definition or a genuine warning. Bold used for pacing is a tell.

**FORM-02 · Em dashes are punctuation, not rhythm.** Where a comma, colon or parentheses fit better, use them.

**FORM-03 · Headings are informative.** A heading names what the section establishes, not a teaser.

**FORM-04 · Components match their purpose.** Use `.readouts`, `.note`, `.ladder` and `.check` as documented in the README. A callout that carries ordinary prose is decoration.

**FORM-05 · No emoji in headings or body text.**

**FORM-06 · Terminology is consistent.** One term per concept throughout, with the English original marked by `<span class="en">` on first use in Chinese prose.

## 7. What is not a rule

These are outside the process, and a finding that rests on them is dropped:

- sentence length, paragraph length or article length as such;
- preference between two accurate phrasings;
- the presence or absence of storytelling, scene-setting, a journey, an anecdote or a visible thesis statement as such;
- chronological, spatial, causal, comparative, procedural, question-led or reference-style organisation as a category;
- the number of sections, examples or covered categories as such;
- the order of sections, unless their current relations violate a `COH` rule;
- topic choice, and the article's conclusion where the sources support it.
