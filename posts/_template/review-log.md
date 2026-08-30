# Review log — <article title>

Copied from `posts/_template/review-log.md`. Process: [docs/review-spec.md](../../docs/review-spec.md). Fill this in as the review happens, not afterwards.

| Field | Value |
| --- | --- |
| Article | `posts/YYYY-MM-slug/index.html` |
| Rules version | review-spec.md 1.1 |
| Author agent | model or tool name |
| Reviewer agents | style and structure / substance / arbiter, model or tool names |
| Rounds completed | n of 3 |
| Terminal verdict | ship \| ship-with-notes \| hold-for-human \| withdraw |

## Round 0 — draft

- Source log complete per `COMPLIANCE.md` §1: yes / no
- Author self-check against `docs/style-rules.md`: what was changed before review
- Central question, claim or task:
- Organising logic actually used:
- Broad, representative or comprehensive scope claims: none / list them

### Section relations

Record what each top-level section contributes and why it follows the preceding section. This is an author self-check, not input to the reviewers.

| Section | Work done | Relation to preceding section |
| --- | --- | --- |
| Opening | | — |
| | | |

## Round 1

### Style and structure reviewer report

Paste the report verbatim.

```text
ID        R1-S01
Rule      TELL-C03
Severity  should-fix
Locator   <section> — "<quoted span>"
Problem   <one sentence>
Basis     <why the rule is violated>
```

### Substance reviewer report

Paste the report verbatim.

### Arbiter triage

```text
Round 1 verdict: revise
Admitted findings:   R1-S01, R1-B02 (raised to must-fix: figure has no denominator, EVID-03)
Dismissed findings:  R1-S04 (style-rules.md §6, sentence-length preference)
Decisions:           —
Remaining blockers:  R1-B02 — state the sample size and period in the sentence
```

### Author dispositions

| Finding | Disposition | Note |
| --- | --- | --- |
| R1-S01 | fixed | |
| R1-B02 | fixed | added sample size and date range |
| R1-B05 | declined | source is primary; the summary cited is the only public version |

## Round 2

*Scope freeze is in effect from here: no new must-fix findings except a factual error, a fabricated or unsupported citation, or a rights or privacy problem.*

Same four blocks as round 1.

## Round 3

Same four blocks. The arbiter must close with a terminal verdict.

## Outcome

- **Verdict:**
- **Known limitations** (for `ship-with-notes`, repeated in the pull request description):
- **Escalations to the owner** (for `hold-for-human`, with the issue link):
- **Spans closed by the arbiter** (§7.3), and why:
