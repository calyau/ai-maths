---
concept: Rank-Generating Polynomial
slug: rank-generating-polynomial
category: tutte-polynomial
subcategory: null
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 342
section: "X.1 Basic Properties of the Tutte Polynomial"
extraction_confidence: high
aliases:
  - "S(G; x, y)"
  - "Whitney rank polynomial"
prerequisites: []
extends: []
related:
  - tutte-polynomial
  - rank-of-graph
  - nullity-of-graph
contrasts_with:
  - tutte-polynomial
answers_questions:
  - "What is the Tutte polynomial?"
---

# Quick Definition
The rank-generating polynomial of a multigraph $G = (V, E)$ is $S(G; x, y) = \sum_{F \subset E} x^{r(E) - r(F)} y^{n(F)}$, summing over all spanning subgraphs.

# Core Definition
$S(G; x, y) = \sum_{F \subset E(G)} x^{r(E) - r(F)} y^{n(F)} = \sum_{F \subset E(G)} x^{k(F) - k(E)} y^{n(F)}$ (Bollobás, p. 342). The Tutte polynomial is $T_G(x,y) = S(G; x-1, y-1)$.

# Prerequisites
This is a foundational concept with no prerequisites beyond basic graph theory (rank, nullity, spanning subgraphs).

# Key Properties
1. $S(E_n) = 1$ for the empty $n$-graph
2. Recursion (Theorem 1): bridge gives $(x+1)S(G-e)$; loop gives $(y+1)S(G-e)$; otherwise $S(G-e) + S(G/e)$
3. Integer coefficients: $S(G; x, y) \in \mathbb{Z}[x, y]$
4. Multiplicative: $S(G_1 \cup G_2) = S(G_1) S(G_2)$ when sharing at most one vertex
5. $S(K_2) = x + 1$, $S(L) = y + 1$

# Construction / Recognition
Compute by summing $x^{r(E)-r(F)} y^{n(F)}$ over all $2^{|E|}$ subsets $F \subset E$.

# Context & Application
The rank-generating polynomial is the "most natural" form of the family; Bollobás chooses to "start with the rank-generating polynomial" (p. 342) and derive the Tutte polynomial from it.

# Examples
**Example**: For $K_2$: $S(K_2; x, y) = x + 1$ (one edge, either included or not).

# Relationships
## Builds Upon
- **rank-of-graph**, **nullity-of-graph** (implicit)

## Enables
- **tutte-polynomial** — $T_G(x,y) = S(G; x-1, y-1)$

# Source Reference
Chapter X, Section X.1, pages 342-343. Theorem 1.

# Verification Notes
- Definition source: Direct from p. 342
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
