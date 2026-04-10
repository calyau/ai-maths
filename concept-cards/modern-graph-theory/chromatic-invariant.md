---
concept: Chromatic Invariant
slug: chromatic-invariant
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
  - "theta(G)"
  - "t_10(G)"
prerequisites:
  - spanning-tree-expansion
extends: []
related:
  - chromatic-polynomial-from-tutte
contrasts_with: []
answers_questions:
  - "What information does the Tutte polynomial encode?"
---

# Quick Definition
The chromatic invariant $\theta(G) = t_{10}(G)$ is the coefficient of $x$ in $T_G(x,0)$. It satisfies $p'_G(1) = (-1)^{r(G)+1}\theta(G)$ and is invariant under homeomorphism for graphs with at least two edges.

# Core Definition
"$t_{10} = t_{10}(G)$ is a significant graph invariant in its own right: it is usually called the chromatic invariant of $G$ and is denoted by $\theta(G)$" (Bollobás, p. 362). Theorem 12: (i) $p'_G(1) = (-1)^{r(G)+1}\theta(G)$; (ii) if $G, H$ are homeomorphic with at least two edges, $\theta(G) = \theta(H)$.

# Prerequisites
- **Spanning tree expansion** — $\theta(G) = t_{10}(G)$ is a coefficient in this expansion

# Key Properties
1. $\theta(G) = t_{10}(G)$ = number of $(1,0)$-trees
2. $t_{10} = t_{01}$ (Theorem 11) when $G$ has at least two edges
3. $p'_G(1) = (-1)^{r(G)+1}\theta(G)$
4. Invariant under homeomorphism (subdivision of edges)

# Context & Application
The chromatic invariant connects the spanning tree expansion to the chromatic polynomial and is the simplest nontrivial coefficient in the Tutte polynomial's spanning tree expansion.

# Relationships
## Builds Upon
- **spanning-tree-expansion**

## Related
- **chromatic-polynomial-from-tutte** — $\theta$ is the derivative of $p_G$ at 1

# Source Reference
Chapter X, Section X.5, Theorems 11-12, pages 362-363.

# Verification Notes
- Definition source: Direct from p. 362
- Confidence rationale: Explicit definition and theorems
- Uncertainties: None
- Cross-reference status: Verified
