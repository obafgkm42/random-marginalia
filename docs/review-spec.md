# Agent review process

Specification for the review that every article passes before a pull request is opened.

- **Status:** active
- **Version:** 1.0
- **Applies to:** every new article and every substantive rewrite of a published article
- **Companion documents:** [style-rules.md](style-rules.md) (the citable rules), [review-agents.md](review-agents.md) (role prompts), [../COMPLIANCE.md](../COMPLIANCE.md) (rights, privacy and sourcing policy)

## 1. Purpose

Articles here are drafted by AI. The risk is therefore not plagiarism of a competitor's blog post but a quieter failure: prose that is fluent, confidently sourced-looking and wrong, written in the flattened register that reinforcement-tuned models fall into. This process exists to catch both before publication, at a cost proportionate to a small repository.

It has three properties:

- **Adversarial.** Reviewers look for defects and are not asked to praise anything.
- **Neutral.** A finding is only admissible if it cites a numbered rule and quotes the text it applies to. Taste alone is not a finding.
- **Terminating.** An arbiter holds a hard round budget, so review cannot postpone publication indefinitely.

## 2. Non-goals

- **Not AI detection.** Every article is AI-drafted and says so. The question is whether the writing is accurate and readable, not whether a classifier can guess its origin.
- **Not a house voice.** Register follows the subject. A note on Yunnan's flora and a note on build systems should not sound alike. Only the rules in `style-rules.md` are enforced across topics.
- **Not a replacement for the human owner.** The arbiter can ship an article; it cannot decide a rights, privacy or contested-fact question. Those escalate.
- **Not a copy-editing service.** Reviewers report defects. They do not rewrite paragraphs; see §4.

## 3. Roles

| Role | Who | Responsibility |
| --- | --- | --- |
| Author | The agent that drafted the article | Drafts, keeps the source log, revises in response to admitted findings, answers each finding in the review log |
| Style reviewer | A separate agent instance | Finds violations of the `VOICE`, `TELL` and `FORM` rules |
| Substance reviewer | A separate agent instance | Finds incoherence, unsupported claims, sourcing defects and `COMPLIANCE.md` failures |
| Arbiter | A separate agent instance | Triages findings, resolves reviewer conflicts, controls the round budget, issues the terminal verdict |
| Owner | The human maintainer | Merges pull requests; decides anything escalated |

One agent may not hold two roles in the same round. The author agent may not review its own draft.

## 4. Neutrality requirements

1. A reviewer receives the article, `style-rules.md` and `COMPLIANCE.md`. It does not receive the author's drafting notes, its rationale, or the other reviewer's findings.
2. The two reviewers run independently. They are not shown each other's output before the arbiter triages.
3. Every finding cites a rule ID and quotes the span it applies to. A finding that cites no rule is inadmissible and the arbiter drops it.
4. **Reviewers describe defects; they do not supply replacement prose.** A reviewer that rewrites a paragraph imports its own register into the article, which is the failure mode this process exists to prevent. A reviewer may name the smallest change that would clear the finding — "cite the population for this figure", "delete the closing sentence" — but the author writes the text.
5. Findings are about the article, never about the author agent.

## 5. Finding schema

Each finding is one entry in the review log:

```text
ID        R<round>-<S|B><n>   e.g. R1-S04 (style), R1-B02 (substance)
Rule      A rule ID from style-rules.md (VOICE/TELL/EVID/FORM), or COMPLIANCE §n
Severity  must-fix | should-fix | optional
Locator   section heading plus a quoted span of at most 25 words
Problem   one sentence stating the defect
Basis     why the cited rule is violated, or what evidence is missing
```

Severity is assigned by the reviewer and may be adjusted by the arbiter under §7.

| Severity | Meaning | Effect |
| --- | --- | --- |
| `must-fix` | A factual error; a citation that is unverifiable, mismatched or fabricated; an incoherence that changes what the article claims; a `COMPLIANCE.md` checklist failure; or a style rule broken repeatedly enough to be a pattern, per `style-rules.md` §1 | Blocks the pull request |
| `should-fix` | A single local defect: one style tell, one loose transition, one thin but not wrong source | Author must fix it or record a one-line reason for declining |
| `optional` | Preference, alternative framing, further reading | Author may ignore it silently |

Only `must-fix` blocks. This is what keeps the process from converging on the reviewers' taste.

## 6. Round protocol

**Round 0 — draft.** The author writes the article, completes the source log required by `COMPLIANCE.md` §1, and self-checks against `style-rules.md`. Round 0 is not a review and does not count toward the budget.

**Round n (n ≥ 1).**

1. Style reviewer and substance reviewer run independently against the current draft.
2. The arbiter triages: it drops inadmissible findings, merges duplicates, resolves conflicts between the two reviewers, applies the scope freeze (§7.2), and adjusts severity where §7 permits.
3. The arbiter issues a round verdict: `revise` or a terminal verdict from §8.
4. On `revise`, the author revises and records a disposition for every admitted finding — `fixed`, `declined` with a reason, or `deferred` to the known-limitations list.
5. Round n + 1 begins, unless a terminal verdict has been issued or the budget is exhausted.

**Minimum.** At least one full round — review, arbitration and revision — must complete before a pull request is opened.

**Anti-rubber-stamp.** A round-1 report containing no findings at any severity is not accepted. The arbiter returns it and that reviewer runs once more. If the second attempt is also empty, the arbiter records the fact explicitly in the log and it counts as the round.

## 7. Convergence and deadlock control

The arbiter is deliberately given more power than the reviewers. Review that never ends is a worse failure than an article with a documented rough edge.

### 7.1 Round budget

Three rounds, hard. The arbiter must issue a terminal verdict at the end of round 3 whatever the state of the draft; if `must-fix` findings survive, the verdict is `hold-for-human`, not a fourth round.

### 7.2 Scope freeze

From round 2 onward, **no new `must-fix` finding may be raised**, with three exemptions:

- a factual error;
- a citation that is fabricated, unverifiable or does not support the claim attached to it;
- a rights, privacy or confidentiality problem.

Anything else discovered late enters as `should-fix` at most. Without this rule, each revision invites a fresh objection and the article never converges.

### 7.3 Ping-pong detection

If a span is changed, changed back, and challenged a third time, the arbiter chooses one version, records the choice and its reason in the log, and marks that span closed. It may not be reopened in a later round.

### 7.4 Reviewer conflict

If the two reviewers contradict each other, the arbiter decides in one line and the decision is final for the article. It does not go back to the reviewers.

### 7.5 Stated exit condition

Every `revise` verdict must state what remains blocking and what would clear it. A reviewer cannot move the target after the arbiter has stated it; a new demand on an already-stated blocker is dropped as out of scope.

### 7.6 Escalation

The arbiter escalates to the owner only for a suspected fabricated source, a rights or privacy question, or a factual dispute it cannot settle from the sources at hand. Everything else it decides itself, including shipping an article whose remaining defects are documented.

## 8. Terminal verdicts

| Verdict | Meaning | Pull request |
| --- | --- | --- |
| `ship` | No `must-fix` findings remain | Allowed |
| `ship-with-notes` | No `must-fix` findings remain; some `should-fix` items were declined or deferred and are recorded as known limitations | Allowed; the notes are quoted in the pull request description |
| `hold-for-human` | An escalation under §7.6, or `must-fix` findings surviving round 3 | Blocked; open an issue describing the open question |
| `withdraw` | The article's premise does not survive review — the central claim is unsupported by the sources | No pull request; the draft is abandoned or restarted from round 0 |

## 9. Artifacts

Each article directory carries a review log beside the article:

```text
posts/YYYY-MM-slug/
├── index.html
└── review-log.md
```

The log is copied from [../posts/_template/review-log.md](../posts/_template/review-log.md) and committed together with the article, in the same pull request. It records every round, every admitted finding and its disposition, the arbiter's decisions with reasons, and the terminal verdict. It is the audit trail: a reader who doubts a claim can see whether anyone challenged it and what happened.

The log is a repository document, not part of the published page. It is not linked from `index.html`.

## 10. Acceptance criteria

A pull request that adds or substantively rewrites an article is ready when all of the following hold:

- [ ] At least one full review round completed, with two independent reviewers.
- [ ] `review-log.md` exists in the article directory and every admitted finding has a disposition.
- [ ] The terminal verdict is `ship` or `ship-with-notes`.
- [ ] No `must-fix` finding is open.
- [ ] The `COMPLIANCE.md` pre-publication checklist is complete.
- [ ] The pull request description states the number of rounds, the verdict, and any known limitations.

## 11. Changing this process

Rule text, severity definitions and the round budget are changed by pull request like anything else in the repository. An in-flight review keeps the version of the rules it started under; a rule added mid-review is not retroactive, for the same reason as §7.2.
