---
concept: Spanning Tree Count from Tutte Polynomial
slug: spanning-tree-count
category: tutte-polynomial
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 352
section: "X.4 Special Values of the Tutte Polynomial"
extraction_confidence: high
aliases: []
prerequisites:
  - tutte-polynomial
  - special-values-tutte-polynomial
extends: []
related:
  - spanning-tree-expansion
contrasts_with: []
answers_questions:
  - "What information does the Tutte polynomial encode?"
---

# Quick Definition
The number of spanning trees of a connected graph $G$ is $T_G(1,1)$, the Tutte polynomial evaluated at $(1,1)$.

# Core Definition
From Theorem 5 (p. 352): $T_G(1,1) = \sum_{F \subset E} 0^{r(G)-r(F)} 0^{n(F)} = |\{F : r(F) = r(G), n(F) = 0\}|$, which counts exactly the spanning trees (subgraphs with maximal rank and no cycles).

# Prerequisites
- **Tutte polynomial** — Evaluated at $(1,1)$
- **Special values of the Tutte polynomial** — Context

# Key Properties
1. $T_G(1,1) = $ number of spanning trees (connected $G$)
2. Related to Kirchhoff's matrix tree theorem (Chapter II)
3. For $K_n$: $T_{K_n}(1,1) = n^{n-2}$ (Cayley's formula)

# Relationships
## Builds Upon
- **tutte-polynomial**, **special-values-tutte-polynomial**

## Related
- **spanning-tree-expansion** — Alternative expression via activities

# Source Reference
Chapter X, Section X.4, Theorem 5, page 352.

# Verification Notes
- Definition source: Direct from Theorem 5
- Confidence rationale: Explicit theorem
- Uncertainties: None
- Cross-reference status: Verified
