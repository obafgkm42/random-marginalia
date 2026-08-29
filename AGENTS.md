# Repository instructions

## Read before changing the repository

- Read this file before making repository changes.
- Treat approval to merge or push one task as limited to that task. It is not standing permission for future direct pushes.
- Preserve unrelated user changes and existing repository conventions.

## Change workflow

- Use a pull request for every repository change by default, including small documentation and metadata edits.
- Commit or push directly to `main` only when the user explicitly authorizes a direct commit or direct push for the current task.
- Do not infer direct-push permission from the size or risk of a change, from earlier tasks, or from a general request to proceed autonomously.
- If the user has not specified a workflow, create a branch and open a pull request.
- Keep one task cohesive. When practical, make one complete commit instead of one commit per file or per API call.
- Do not rewrite published history merely to clean up commit messages unless the user explicitly requests it.

## Commit messages

Use lowercase Conventional Commits:

```text
<type>: <lowercase imperative subject>
```

Examples:

```text
docs: add repository workflow rules
feat: publish yunnan plants investigation
fix: correct article image attribution
style: support simplified chinese typography
```

- Use a lowercase type and begin the subject in lowercase.
- Prefer `feat`, `fix`, `docs`, `style`, `refactor`, `test`, or `chore`.
- Keep the first line concise, imperative, and without a trailing period.
- Do not add a personal email, user identity, or `Co-authored-by` trailer without explicit permission.

## Pull requests

- Use a short lowercase branch name such as `docs/workflow-rules` or `feat/yunnan-plants`.
- Summarize what changed, why it changed, and how it was checked.
- Keep unrelated changes out of the pull request.
- Do not merge the pull request unless the user asks for the merge or has explicitly included merging in the current task.
