---
concept: Probability of Connectedness from the Tutte Polynomial
slug: probability-of-connectedness
category: tutte-polynomial
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 357
section: "X.4 Special Values of the Tutte Polynomial"
extraction_confidence: high
aliases:
  - "reliability polynomial"
prerequisites:
  - tutte-polynomial
  - universal-polynomial-of-graphs
extends: []
related:
  - random-cluster-model
  - special-values-tutte-polynomial
contrasts_with: []
answers_questions:
  - "What information does the Tutte polynomial encode?"
---

# Quick Definition
If each edge of a connected graph $G$ is retained with probability $p$ independently, the probability that the resulting random subgraph is connected equals $p^{r(G)} q^{n(G)} T_G(1, 1/q)$ where $q = 1 - p$.

# Core Definition
Theorem 9 (p. 358): "Let $G = (V, E)$, $0 < p < 1$, $q = 1-p$ and $E_p$ be as above. Then $\mathbb{P}(r(E_p) = r(G)) = p^{r(G)} q^{n(G)} T_G(1, 1/q)$."

# Prerequisites
- **Tutte polynomial** — Evaluated at $(1, 1/q)$
- **Universal polynomial of graphs** — Used in the proof

# Key Properties
1. For connected $G$: $r(E_p) = r(G)$ iff $E_p$ is connected
2. $\mathbb{P}(\text{connected}) = p^{r(G)} q^{n(G)} T_G(1, 1/q)$
3. Verified by checking the deletion-contraction recursion

# Relationships
## Builds Upon
- **tutte-polynomial**, **universal-polynomial-of-graphs**

## Related
- **random-cluster-model** — Related probabilistic model
- **special-values-tutte-polynomial** — Another evaluation context

# Source Reference
Chapter X, Section X.4, Theorem 9, page 358.

# Verification Notes
- Definition source: Direct from Theorem 9
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
