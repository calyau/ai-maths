---
concept: Tutte Polynomial Duality for Plane Graphs
slug: tutte-polynomial-duality
category: tutte-polynomial
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 378
section: "X.7 Exercises"
extraction_confidence: high
aliases: []
prerequisites:
  - tutte-polynomial
extends: []
related:
  - flow-polynomial-chromatic-duality
  - tutte-polynomial-of-cycle
  - tutte-polynomial-of-thick-edge
contrasts_with: []
answers_questions:
  - "How does the Tutte polynomial generalize the chromatic and flow polynomials?"
---

# Quick Definition
For a connected plane graph $G$ with dual $G^*$: $T_{G^*}(x,y) = T_G(y,x)$. Duality swaps the roles of $x$ and $y$.

# Core Definition
Exercise 15 (p. 378): "Let $G$ be a connected plane graph with dual $G^*$. Prove that $T_{G^*}(x,y) = T_G(y,x)$." This elegant duality swaps rank and nullity, bridges and loops, internal and external activity.

# Prerequisites
- **Tutte polynomial** — The polynomial satisfying the duality

# Key Properties
1. $T_{G^*}(x,y) = T_G(y,x)$
2. Bridges of $G$ correspond to loops of $G^*$ and vice versa
3. $r(G^*) = n(G)$, $n(G^*) = r(G)$
4. Implies $p_G(x) = q_{G^*}(x) x^{k(G)}$ (flow-chromatic duality)

# Relationships
## Builds Upon
- **tutte-polynomial**

## Related
- **flow-polynomial-chromatic-duality** — Consequence of $T$ duality
- **tutte-polynomial-of-cycle**, **tutte-polynomial-of-thick-edge** — Example of duality

# Source Reference
Chapter X, Exercise 15, page 378.

# Verification Notes
- Definition source: From Exercise 15
- Confidence rationale: Stated as exercise
- Uncertainties: None
- Cross-reference status: Verified
