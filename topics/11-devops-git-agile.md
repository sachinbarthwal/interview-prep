# DevOps, Git & Agile

> Usually a short, low-drama section of the interview — but a vague or generic
> answer here stands out as much as a sharp one does, precisely because most
> candidates coast through it.

## Table of Contents

| No. | Question |
|-----|----------|
| 1 | [What are the key components of a CI/CD pipeline?](#1-what-are-the-key-components-of-a-cicd-pipeline) |
| 2 | [How do you resolve a merge conflict in Git?](#2-how-do-you-resolve-a-merge-conflict-in-git) |
| 3 | [Describe your experience with Agile/Scrum](#3-describe-your-experience-with-agilescrum) |
| 4 | [Waterfall vs Agile](#4-waterfall-vs-agile) |
| 5 | [Describe a challenging Agile project and how you handled it](#5-describe-a-challenging-agile-project-and-how-you-handled-it) |

## 1. What are the key components of a CI/CD pipeline?

- **Continuous Integration:** every push/PR triggers an automated build and test
  run, catching integration problems immediately rather than at release time.
- **Continuous Delivery/Deployment:** a validated build automatically flows
  through environments (Dev → QA → Staging → Prod), with approval gates where
  needed for delivery, or fully automated for deployment.
- **Artifact management:** the exact build that passed CI is the *same* artifact
  promoted through every environment — never rebuilt per environment, which
  eliminates "it worked in staging but not prod because it was a different
  build" class of bugs.
- **Automated tests** integrated into the pipeline as a gate, not an afterthought.
- **Rollback strategy** for when a deployment goes wrong in production.

**[⬆ Back to Top](#table-of-contents)**

## 2. How do you resolve a merge conflict in Git?

```bash
git status                     # see which files conflict
# open each conflicting file, look for <<<<<<<, =======, >>>>>>> markers
# manually edit to keep the correct combined result, remove the markers
git add <resolved-file>
git commit                     # completes the merge
```

For a conflict during a `rebase` instead of a `merge`, the flow is the same
(edit, `git add`), but you continue with `git rebase --continue` instead of
`git commit`. **Talk through your actual judgment process too:** understanding
*why* both sides changed the same lines (checking `git log` / `git blame` on the
conflicting hunk) before blindly picking one side, and running the test suite
after resolving — a conflict resolving cleanly doesn't guarantee it's
*semantically* correct.

**[⬆ Back to Top](#table-of-contents)**

## 3. Describe your experience with Agile/Scrum

Structure this around the actual ceremonies and your role in them: daily
stand-ups (status/blockers, kept short), sprint planning (estimating and
committing to a sprint's scope), sprint reviews/demos (showing working software
to stakeholders), and retrospectives (what to keep/stop/start doing next sprint).
Mention concrete tools (Jira, Azure Boards) and something specific you
personally contributed to process improvement — a generic "we did stand-ups"
answer is forgettable; "I pushed for splitting a recurring blocker into its own
tracked spike after three retros flagged it" is not.

**[⬆ Back to Top](#table-of-contents)**

## 4. Waterfall vs Agile

**Waterfall** is sequential — requirements, design, implementation, testing,
deployment, each phase completed before the next begins, with a full plan
upfront. Works reasonably when requirements are genuinely stable and well
understood in advance. **Agile** is iterative — small increments (sprints)
delivering working software repeatedly, with room to adapt scope/priorities
based on feedback between iterations. It fits better when requirements are
expected to evolve, which is the common case for most product development. The
practical, honest answer in an interview: most real teams run something
Agile-ish but pragmatic, not a textbook-pure implementation of either.

**[⬆ Back to Top](#table-of-contents)**

## 5. Describe a challenging Agile project and how you handled it

Use a real example structured as: the situation (tight sprint, shifting
requirements, or a cross-team dependency), what specifically made it hard, the
concrete action you took (renegotiating scope with the product owner, breaking
a large story down, pairing with another engineer on a blocking piece), and the
outcome. Avoid a purely process-narrative answer with no personal decision in
it — the interviewer wants to see *your* judgment call, not just "we followed
Scrum and it worked out."

**[⬆ Back to Top](#table-of-contents)**
