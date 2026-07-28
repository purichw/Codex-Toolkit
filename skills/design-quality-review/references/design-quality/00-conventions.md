# 00 · Conventions

Notation and process definitions used by every other file. Read once.

## Fact vs. recommendation

Design review fails when observations and opinions are mixed in the same sentence. Every
statement in this guide is tagged.

| Tag | Meaning | How it's settled |
| --- | --- | --- |
| `[FACT]` | Observable in a screenshot or the DOM with no product knowledge. "Row height is 28px." "Focus ring is browser-default blue." | Measure it. Not debatable. |
| `[CRAFT]` | A convention with broad agreement in the discipline; deviations are usually mistakes, occasionally intent. "Numbers in a column are right-aligned." | Follow unless the reference contradicts it. |
| `[PD]` | **Requires product decision.** Depends on users, risk, business model, legal, or roadmap. "Should deleting an invoice be undoable or confirmed?" | Escalate. Do not settle by taste. Record the answer in the ticket. |

**Reviewer rule:** if you cannot tag your comment, it isn't ready to post. `[FACT]` comments are
blocking. `[CRAFT]` comments are blocking if they violate a cited rule. `[PD]` comments are
questions, never change requests.

## Rule IDs

Rules are numbered per file with a stable prefix so they can be cited in review:

| Prefix | File |
| --- | --- |
| `VD` | 01 Visual diagnosis |
| `DT` | 02 Domain taste |
| `IA` | 03 Information architecture |
| `IX` | 04 Interaction design |
| `MB` | 05 Mobile-native feel |
| `DS` | 06 Design systems |
| `AD` | 07 Art direction & imagery |
| `TY` | 08 Typography |
| `MO` | 09 Motion |
| `AX` | 10 Accessibility |
| `RC` | 11 Reference critique |

Cite as `TY-7` in a comment. IDs are append-only: never renumber, retire with `~~TY-7~~
(retired 2026-03)`.

## Severity

Attach a severity to every defect. It decides whether the PR blocks.

| Severity | Definition | Examples | Action |
| --- | --- | --- | --- |
| **S1** | Changes meaning, hierarchy, or reachability. A user reads the screen wrong or can't complete the task. | Two elements tie for primary action; numbers misaligned in a ledger; focus ring absent; destructive action is the default focus target. | Blocks merge. |
| **S2** | Breaks system consistency or reference fidelity in a way that repeats. | Off-scale spacing used in a shared component; 5th distinct border-radius introduced; 2px error on a shared alignment edge; hover state missing on one of six buttons. | Blocks merge unless explicitly deferred with a ticket. |
| **S3** | Cosmetic, local, non-repeating, ≤2px. | One icon 1px low in a one-off illustration; letter-spacing off by 0.005em in a footnote. | Log, don't block. |

**The 2px rule** `[FACT]` — a difference of ≤2px from the reference is noise **unless** it (a)
repeats across instances, (b) sits on an alignment edge shared with other elements, or (c)
crosses a minimum (tap target, contrast, measure). Then it is S2.

## Screenshot review setup

Design QA happens on captures, not on your live dev server. Details in
[Appendix A](appendix-a-screenshot-qa-protocol.md); the minimum:

- Capture at the reference's viewport width, 100% zoom, device pixel ratio noted.
- Same content as the reference — not lorem, not your test row named "asdf".
- Hide dev overlays, extensions, and your own cursor.
- Capture the **states**, not just the default: empty, loading, error, long content, permission-denied.

## Four transforms that expose most defects

Apply to a screenshot before you look at it analytically. Each isolates one channel.

| Transform | Reveals | Pass condition |
| --- | --- | --- |
| **Grayscale** | Hierarchy carried by hue instead of value/size | Reading order unchanged from color version |
| **Blur 8px** (at 1440px width) | What actually reads first | Exactly one element dominates; the intended reading path survives |
| **Invert** | Shadow/border weight, muddy fills | No element becomes unreadable or newly dominant |
| **Edge/threshold** | Alignment | Left edges collapse onto ≤3 vertical lines per column |

## Vocabulary discipline

Banned in review comments because they carry no action: *clean, modern, polished, tighten,
breathe, feels off, more premium, make it pop, better spacing.* Replace with the diagnostic
terms in [01](01-visual-diagnosis.md) plus a measurement.

> ❌ "This feels cramped, tighten it up."
> ✅ "`[FACT]` S2 — card padding is 8px against 16px/1.5 body text; the same 8px separates the
> title group from the metadata group, so grouping is unreadable. Rule VD-4: inner gap must be
> ≤½ the group gap. Suggest 16px padding, 8px inside groups, 20px between."

## Design intent

**Design intent** = the reason a visual decision was made. It is not visible in the artifact,
which is why it dies during implementation.

Preserve it by recording it (Appendix B), not by memorizing it. If a reference has an unusual
value (a 13px label, a 3px gap, an off-grid offset), assume intent until proven otherwise and
ask before normalizing it. If you must normalize to ship, leave a code comment naming the
deviation so the next person doesn't re-litigate it silently.
