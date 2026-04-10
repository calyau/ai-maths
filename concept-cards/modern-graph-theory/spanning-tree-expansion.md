---
concept: Spanning Tree Expansion of the Tutte Polynomial
slug: spanning-tree-expansion
category: tutte-polynomial
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 356
section: "X.5 A Spanning Tree Expansion of the Tutte Polynomial"
extraction_confidence: high
aliases:
  - "Tutte's original definition"
  - "activity expansion"
prerequisites:
  - tutte-polynomial
  - internal-activity
  - external-activity
extends:
  - tutte-polynomial
related:
  - chromatic-invariant
contrasts_with: []
answers_questions:
  - "How does the Tutte polynomial relate to spanning trees?"
---

# Quick Definition
The Tutte polynomial equals $T_G(x,y) = \sum_{i,j} t_{ij} x^i y^j$ where $t_{ij}$ is the number of spanning forests with internal activity $i$ and external activity $j$, with respect to any ordering of the edges.

# Core Definition
Theorem 10 (p. 357): "Let $G$ be a graph with an ordering of its edges. Write $t_{ij}$ for the number of spanning forests with internal activity $i$ and external activity $j$. Then $\sum_{i,j} t_{ij} x^i y^j$ is precisely the Tutte polynomial $T_G(x,y)$ of $G$. In particular, $t_{ij} = t_{ij}(G)$ is independent of the ordering of the edges."

# Prerequisites
- **Tutte polynomial** — The polynomial being expanded
- **Internal activity** — Counts internally active edges in spanning forests
- **External activity** — Counts externally active edges

# Key Properties
1. $T_G(x,y) = \sum_{i,j} t_{ij} x^i y^j$ with $t_{ij} \geq 0$
2. $t_{ij}$ is independent of the edge ordering (remarkable!)
3. Fewer terms than the subset expansion (sum over spanning forests vs. all subsets)
4. Coefficients $t_{ij}$ are explicitly defined (non-negative integers)
5. $t_{00} = 0$ if $G$ has at least one edge
6. $t_{10} = t_{01}$ if $G$ has at least two edges (Theorem 11)

# Context & Application
"This was Tutte's original definition" (p. 360). The spanning tree expansion has advantages: fewer terms, non-negative coefficients, and explicit combinatorial meaning. "A judicious choice of the order on the edges is frequently advantageous in proving results about the coefficients."

# Examples
**Example** (Fig. X.2, p. 357): A spanning tree with internally active edges $e_1, e_7, e_9$ and externally active edges $e_2, e_3$.

# Relationships
## Builds Upon
- **tutte-polynomial**, **internal-activity**, **external-activity**

## Enables
- **chromatic-invariant** — $\theta(G) = t_{10}(G)$
- **tait-conjecture-crossing-number** — Proved using spanning tree expansion

# Source Reference
Chapter X, Section X.5, Theorem 10, pages 356-361.

# Verification Notes
- Definition source: Direct from Theorem 10
- Confidence rationale: Central theorem with two proofs
- Uncertainties: None
- Cross-reference status: Verified
