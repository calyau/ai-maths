---
concept: Lower and Upper Shadow
slug: lower-shadow-upper-shadow
category: matchings
subcategory: order-theory
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.3 Matching"
extraction_confidence: high
aliases:
  - "lower shadow"
  - "upper shadow"
  - "S⁻"
  - "S⁺"
prerequisites:
  - partial-order
  - antichain
extends: []
related:
  - dilworths-theorem
contrasts_with: []
answers_questions:
  - "What are lower and upper shadows in the proof of Dilworth's theorem?"
---

# Quick Definition
The lower shadow $S^-$ of an antichain $A$ consists of all elements $x$ with $x \le a_i$ for some $a_i \in A$. The upper shadow $S^+$ consists of all $x$ with $x \ge a_i$ for some $a_i$.

# Core Definition
In the proof of Dilworth's theorem, given an antichain $A = \{a_1, \ldots, a_m\}$, the lower shadow is $S^- = \{x \in P : x \le a_i \text{ for some } i\}$ and the upper shadow $S^+$ is defined analogously. Then $P = S^- \cup S^+$ (Bollobás, pp. 89-90).

# Prerequisites
- **Partial order** — Shadows are defined in posets
- **Antichain** — Shadows are relative to an antichain

# Key Properties
1. $P = S^- \cup S^+$ (otherwise $A$ could be extended)
2. Neither shadow is all of $P$
3. By induction, each shadow decomposes into $m$ chains
4. Chains through antichain elements can be concatenated

# Context & Application
Lower and upper shadows are the key construction in the proof of Dilworth's theorem.

# Examples
**Example** (p. 90): A maximal chain $C$ intersects both $P \setminus S^-$ and $P \setminus S^+$, so neither shadow contains $P$.

# Relationships
## Enables
- **dilworths-theorem** — Used in the proof

# Source Reference
Chapter III, Section III.3, pages 89-90.

# Verification Notes
- Definition source: Direct from pp. 89-90
- Confidence rationale: Explicitly defined in proof
- Uncertainties: None
- Cross-reference status: Verified
