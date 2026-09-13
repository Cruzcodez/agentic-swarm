# Eval log

What the seeds caught, in the order it happened. Kept because the misses are more instructive than the passes, and because "we tested it" means nothing without saying what the tests found.

## 2026-09-13, first full run

**Result: 34 of 34 seeds passing, after fixes.** Seven agents. Roughly forty individual seed runs to get there.

### Runner bugs (three)

- `must_not_mention: BLOCK` on every clean seed matched the section header `### Blocking`. Every clean seed would have failed forever. Fix: the check skips markdown headers.
- Agents were reviewing the `.claude/agents/` files the runner installs into the scratch directory, and reporting on the charters' own example text. Fix: the default prompt tells the agent to ignore `.claude/`.
- `must_not_mention` scanned the Noted section, so an agent correctly explaining why a rule *didn't* apply got penalized for naming the rule. Fix: only Blocking and Should fix are scanned.

### Charters that were too soft (two)

- **security-reviewer** recognized `AKIAIOSFODNN7EXAMPLE` as AWS's documented example key and downgraded to WARN. Technically right about the value, wrong about the pattern. The charter's "obviously fake" exception was too broad. Now: code that uses a credential-shaped value as a credential is BLOCK regardless of whether the value is a known placeholder. Placeholders in docs and example files are fine.
- **security-reviewer** filed `aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}` under Should fix, apparently because no key value was visible. Now the charter says a secret referenced by name in a static-credential slot is a static credential, and that's Blocking.

### Charters that were too strict or ambiguous (two)

- **infra-reviewer** was told a missing `permissions:` block is always BLOCK. The agent gave WARN on a job that only runs `npm test`, and it was right: no credentials, small blast radius. Now: BLOCK if the job deploys, publishes, has secrets, or assumes a role. Should fix otherwise.
- **test-reviewer** said BLOCK on an untested `raise KeyError` where the seed expected WARN. The charter had "new branch with no test" under BLOCK and "happy path only" under WARN, and those overlap. The agent drew the right line in its own reasoning: an explicitly coded error path is behavior; an implicit one (an exception that would just propagate) is not. That line is now in the charter.

### Seeds that were wrong (seven)

- **security/hardcoded-aws-key** demanded the literal string `AKIA` in the report. The agent deliberately didn't echo the key. Better hygiene than the test asked for. Check changed to substance.
- **docs/clean** got rejected four times, each time for a real gap: README referenced a `requirements.txt` and `infra/` that didn't exist; a stub function the README described as working; a teardown line made stale by a fix thirty seconds earlier; no setup section for the Terraform; no Python version stated for code using a 3.9+ method. Every rejection was legitimate. A genuinely clean project is harder to write than a broken one.
- **infra/clean** got rejected for having no remote Terraform backend, meaning state would live on the ephemeral CI runner and `terraform destroy` would remove nothing. Also referenced a `prod.tfvars` that didn't exist. Both real.
- **infra/no-permissions-block** used `must_not_mention: SHA` to test lane discipline. The agent mentioned SHA pinning in Noted to explain why it *didn't* apply. Correct behavior, bad check.
- **engagement-guide/does-not-invent** used `must_not_mention: budget:` to catch invented budgets. The correct output was `Budget: unknown`. Check inverted to assert the right text positively.
- **engagement-guide/marks-unknown** demanded "Do nothing" and the agent wrote "doing nothing." Loosened to "nothing".
- **engagement-guide/does-not-invent** flagged "weeks" as an invented timeline. The template's own guidance text says "Six weeks from now." Check removed.

### Pattern worth remembering

Of the fourteen fixes, three were in the runner, four were in charters, and seven were in the seeds themselves. The agents were right more often than the tests were. The seeds still earned their keep: every runner bug and every charter fix came from a seed failing, and none of them would have been found by reading.

`must_mention` and `must_not_mention` should test substance, never phrasing. Three separate seeds failed because the agent said the right thing in different words.
