---
concept: Tait's Conjecture on Crossing Numbers
slug: tait-conjecture-crossing-number
category: knot-theory
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 377
section: "X.6 Polynomials of Knots and Links"
extraction_confidence: high
aliases:
  - "Tait's crossing number conjecture"
prerequisites:
  - tutte-polynomial-and-jones-polynomial
  - alternating-link-diagram
extends: []
related:
  - jones-polynomial
  - spanning-tree-expansion
contrasts_with: []
answers_questions:
  - "How do knot polynomials relate to the Tutte polynomial?"
---

# Quick Definition
Tait conjectured (c. 1876) and Murasugi/Thistlethwaite proved (1987) that the number of crossings of a connected alternating link diagram without nugatory crossings is an ambient isotopy invariant (i.e., minimal).

# Core Definition
Theorem 22 (p. 377): "The number of crossings of a connected alternating link diagram without nugatory crossings is an ambient isotopy invariant." The proof shows the crossing number equals the breadth of $V_L(t)$, using Theorem 14 on non-vanishing coefficients $t_{i0}$ and $t_{0j}$.

# Prerequisites
- **Tutte polynomial and Jones polynomial connection** — Theorem 21 expresses $V_L$ via $T_G$
- **Alternating link diagram** — The class of diagrams

# Key Properties
1. For alternating diagrams without nugatory crossings: crossing number = breadth of Jones polynomial
2. Breadth = $\max\deg V_L - \min\deg V_L = (a-1) - (-(m-a+1)) = m$
3. If $m'$ crossings are nugatory: $m - m'$ is the breadth (still an invariant)
4. Every alternating link has an alternating diagram with minimal crossings

# Context & Application
"This result was conjectured by Tait, and proved by Murasugi and Thistlethwaite independently about one hundred years later" (p. 377). The proof elegantly uses the spanning tree expansion (Theorem 14) via the Tutte-Jones connection.

# Relationships
## Builds Upon
- **tutte-polynomial-and-jones-polynomial**, **alternating-link-diagram**

## Related
- **jones-polynomial** — Breadth determines crossing number
- **spanning-tree-expansion** — Theorem 14 on non-vanishing coefficients

# Source Reference
Chapter X, Section X.6, Theorem 22, pages 377-378.

# Verification Notes
- Definition source: Direct from Theorem 22
- Confidence rationale: Named theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
