# Repository instructions

## Workflow

- Use a pull request for every repository change unless the user explicitly authorizes a direct commit or direct push to `main` for the current task.
- Do not carry direct-push or merge authorization over from an earlier task.
- Do not merge a pull request unless the user explicitly asks for it in the current task.

## Review before a pull request

Every new article, and every substantive rewrite of a published one, passes agent review before its pull request is opened. The process is specified in [docs/review-spec.md](docs/review-spec.md).

- Complete at least one full round — two independent reviewers, arbitration, revision. The budget is three rounds and the arbiter closes the review at the end of round 3.
- Commit `review-log.md` in the article directory, in the same pull request as the article.
- Open the pull request only on a `ship` or `ship-with-notes` verdict, with no open `must-fix` finding.
- State the number of rounds, the verdict and any known limitations in the pull request description.

Changes that are not articles — styles, tooling, documentation — do not need a review round.

## Commit messages

Use lowercase Conventional Commits:

```text
<type>: <lowercase imperative subject>
```
