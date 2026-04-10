---
concept: Degree Bounds of the Tutte Polynomial
slug: tutte-polynomial-degree-bounds
category: tutte-polynomial
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 345
section: "X.2 The Universal Form of the Tutte Polynomial"
extraction_confidence: high
aliases: []
prerequisites:
  - tutte-polynomial
  - rank-of-multigraph
  - nullity-of-multigraph
extends: []
related:
  - spanning-tree-expansion
contrasts_with: []
answers_questions:
  - "What is the Tutte polynomial?"
---

# Quick Definition
The maximum degree of $x$ in $T_G(x,y)$ is $r(G)$ (the rank) and the maximum degree of $y$ is $n(G)$ (the nullity).

# Core Definition
From the definition $T_G(x,y) = \sum_{F \subset E}(x-1)^{r(E)-r(F)}(y-1)^{n(F)}$: $\deg_x T_G = \max\{r(G) - r(F) : F \subset E\} = r(G)$ and $\deg_y T_G = \max\{n(F) : F \subset E\} = n(G)$ (Bollobás, p. 345).

# Prerequisites
- **Tutte polynomial**, **rank-of-multigraph**, **nullity-of-multigraph**

# Key Properties
1. $\deg_x T_G = r(G)$ (achieved by $F = \emptyset$)
2. $\deg_y T_G = n(G)$ (achieved by $F = E$)
3. These bounds are needed to prove $U(G)$ is a polynomial (Theorem 2)

# Relationships
## Builds Upon
- **tutte-polynomial**, **rank-of-multigraph**, **nullity-of-multigraph**

## Related
- **spanning-tree-expansion** — Also immediate from the activity expansion

# Source Reference
Chapter X, Section X.2, page 345.

# Verification Notes
- Definition source: Direct from p. 345
- Confidence rationale: Explicit computation
- Uncertainties: None
- Cross-reference status: Verified
