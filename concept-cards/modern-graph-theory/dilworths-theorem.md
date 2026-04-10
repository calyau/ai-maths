---
concept: "Dilworth's Theorem"
slug: dilworths-theorem
category: matchings
subcategory: order-theory
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.3 Matching"
extraction_confidence: high
aliases:
  - "Theorem 13"
  - "Dilworth decomposition"
prerequisites:
  - halls-theorem
extends: []
related:
  - partial-order
  - chain
  - antichain
contrasts_with: []
answers_questions:
  - "How does matching theory apply to partially ordered sets?"
---

# Quick Definition
If every antichain in a finite partially ordered set $P$ has at most $m$ elements, then $P$ is the union of $m$ chains.

# Core Definition
**Theorem 13** (Dilworth): If every antichain in a (finite) partially ordered set $P$ has at most $m$ elements, then $P$ is the union of $m$ chains. The minimum number of chains needed to cover $P$ equals the maximum size of an antichain (Bollobás, p. 89).

# Prerequisites
- **Hall's theorem** — The proof technique parallels Hall's inductive proof

# Key Properties
1. Another instance of "trivial necessary condition is sufficient"
2. The proof uses induction on $|P|$ with upper and lower shadows
3. Holds for all finite partially ordered sets
4. Extends to infinite partially ordered sets (Exercise 53)

# Construction / Recognition
1. Find a maximal antichain $A = \{a_1, \ldots, a_m\}$
2. Define lower shadow $S^- = \{x : x \le a_i \text{ for some } i\}$ and upper shadow $S^+$ similarly
3. By induction, decompose each shadow into $m$ chains
4. Concatenate matching chains through the antichain elements

# Context & Application
Dilworth's theorem connects matching theory to order theory. It is proved using the same inductive technique as Hall's theorem.

# Examples
**Example** (p. 89, Fig. III.5): A partially ordered set and a maximal antichain are shown, where edges indicate the order relation.

# Relationships
## Builds Upon
- **halls-theorem** — Proof technique

## Related
- **partial-order** — The underlying structure
- **chain** — The covering objects
- **antichain** — Determines the chain number

# Source Reference
Chapter III, Section III.3, pages 89-90. Theorem 13.

# Verification Notes
- Definition source: Direct theorem statement from p. 89
- Confidence rationale: Explicitly stated with proof
- Uncertainties: None
- Cross-reference status: Verified
