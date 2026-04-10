---
concept: Brylawski Identity
slug: brylawski-identity
category: tutte-polynomial
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 362
section: "X.5 A Spanning Tree Expansion of the Tutte Polynomial"
extraction_confidence: high
aliases:
  - "Brylawski's identity for t_ij"
prerequisites:
  - spanning-tree-expansion
extends: []
related:
  - chromatic-invariant
  - nonvanishing-coefficients-tutte
contrasts_with: []
answers_questions:
  - "What information does the Tutte polynomial encode?"
---

# Quick Definition
Brylawski proved that if $e(G) > h$ then $\sum_{i=0}^h \sum_{j=0}^{h-i}(-1)^j \binom{h-i}{j} t_{ij} = 0$, giving an infinite family of identities among the coefficients $t_{ij}$ of the spanning tree expansion.

# Core Definition
"Brylawski proved that if $e(G) > h$ then $\sum_{i=0}^h \sum_{j=0}^{h-i}(-1)^j\binom{h-i}{j}t_{ij} = 0$" (Bollobás, p. 362). Special cases: $h = 0$: $t_{00} = 0$; $h = 1$: $t_{10} = t_{01}$; $h = 2$: $t_{20} - t_{11} + t_{02} = t_{10}$.

# Prerequisites
- **Spanning tree expansion** — The coefficients $t_{ij}$

# Key Properties
1. Infinite family of identities
2. $h = 0$: $t_{00} = 0$
3. $h = 1$: $t_{10} = t_{01}$ (Theorem 11)
4. $h = 2$: $t_{20} - t_{11} + t_{02} = t_{10}$

# Relationships
## Builds Upon
- **spanning-tree-expansion**

## Related
- **chromatic-invariant** — $\theta(G) = t_{10} = t_{01}$

# Source Reference
Chapter X, Section X.5, page 362.

# Verification Notes
- Definition source: Direct from p. 362
- Confidence rationale: Explicit formula
- Uncertainties: None
- Cross-reference status: Verified
