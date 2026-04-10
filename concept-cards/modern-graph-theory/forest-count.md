---
concept: Forest Count from Tutte Polynomial
slug: forest-count
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
  - spanning-tree-count
contrasts_with: []
answers_questions:
  - "What information does the Tutte polynomial encode?"
---

# Quick Definition
The number of forests in a graph $G$ is $T_G(2,1)$.

# Core Definition
From Theorem 5 (p. 352): $T_G(2,1) = \sum_{F \subset E} 1^{r(G)-r(F)} 0^{n(F)} = |\{F : n(F) = 0\}|$, counting all acyclic subgraphs.

# Prerequisites
- **Tutte polynomial** — Evaluated at $(2,1)$
- **Special values of the Tutte polynomial** — Context

# Key Properties
1. $T_G(2,1) = $ number of edge sets forming forests
2. Includes the empty forest and the spanning forest(s)
3. Also equals the number of score vectors of orientations (Exercise 11)

# Relationships
## Builds Upon
- **tutte-polynomial**, **special-values-tutte-polynomial**

## Related
- **spanning-tree-count** — $T_G(1,1)$ counts spanning trees only

# Source Reference
Chapter X, Section X.4, Theorem 5, page 352.

# Verification Notes
- Definition source: Direct from Theorem 5
- Confidence rationale: Explicit theorem
- Uncertainties: None
- Cross-reference status: Verified
