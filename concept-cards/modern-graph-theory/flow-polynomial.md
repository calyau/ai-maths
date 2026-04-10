---
concept: Flow Polynomial
slug: flow-polynomial
category: tutte-polynomial
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 354
section: "X.4 Special Values of the Tutte Polynomial"
extraction_confidence: high
aliases:
  - "q_G(x)"
  - "nowhere-zero flow polynomial"
prerequisites:
  - tutte-polynomial
  - nowhere-zero-flow
  - universal-polynomial-of-graphs
extends: []
related:
  - chromatic-polynomial-from-tutte
  - five-flow-conjecture
contrasts_with:
  - chromatic-polynomial-from-tutte
answers_questions:
  - "How does the Tutte polynomial generalize the chromatic and flow polynomials?"
---

# Quick Definition
The flow polynomial $q_G(x)$ counts the number of nowhere-zero $A$-flows on $G$, where $|A| = x$. It depends only on $|A|$ and equals $(-1)^{n(G)} T_G(0, 1-x)$.

# Core Definition
Theorem 7 (p. 355): "Let $A$ be a finite Abelian group and $G$ a multigraph. Then $q_G(A) = (-1)^{n(G)} T_G(0, 1-|A|)$." Since this depends only on $|A|$, we write $q_G(k)$ and extend to a polynomial $q_G(x) \in \mathbb{Z}[x]$.

# Prerequisites
- **Tutte polynomial** — The flow polynomial is a specialization at $x = 0$
- **Nowhere-zero flow** — The objects being counted
- **Universal polynomial of graphs** — Used in the proof

# Key Properties
1. $q_G(A) = (-1)^{n(G)} T_G(0, 1-|A|)$
2. Depends only on $|A|$, not on the group structure of $A$
3. If $G$ has a bridge: $q_G(x) = 0$
4. If $e$ is a loop: $q_G = (x-1) q_{G-e}$
5. The flow polynomial is "the dual of the chromatic polynomial" (p. 355)
6. For a connected plane graph with dual $G^*$: $p_G(x) = q_{G^*}(x) \cdot x^{k(G)}$

# Context & Application
The flow polynomial connects to the four colour theorem: "the four colour theorem is equivalent to the fact that every bridgeless planar graph has a nowhere-zero 4-flow" (p. 355). Tutte's 5-flow conjecture (1954) asserts every bridgeless graph has a nowhere-zero 5-flow. Seymour proved every bridgeless graph has a nowhere-zero 6-flow.

# Examples
**Example** (p. 354): $q_{E_n}(A) = 1$ for every $n$. $q_{C_n}(A) = |A| - 1$ for the $n$-cycle.

# Relationships
## Builds Upon
- **tutte-polynomial**, **nowhere-zero-flow**, **universal-polynomial-of-graphs**

## Enables
- **five-flow-conjecture** — States $q_G(5) > 0$ for bridgeless $G$

## Contrasts With
- **chromatic-polynomial-from-tutte** — Chromatic at $y = 0$; flow at $x = 0$

# Source Reference
Chapter X, Section X.4, Theorem 7, pages 354-355.

# Verification Notes
- Definition source: Direct from Theorem 7
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
