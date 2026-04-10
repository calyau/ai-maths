---
concept: Special Values of the Tutte Polynomial
slug: special-values-tutte-polynomial
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
extends: []
related:
  - chromatic-polynomial-from-tutte
  - flow-polynomial
  - acyclic-orientation-count
contrasts_with: []
answers_questions:
  - "What is the Tutte polynomial?"
  - "How does the Tutte polynomial generalize the chromatic and flow polynomials?"
---

# Quick Definition
At small integer values, the Tutte polynomial counts fundamental graph structures: $T_G(1,1)$ = spanning trees, $T_G(2,1)$ = forests, $T_G(1,2)$ = connected spanning subgraphs, $T_G(2,2) = 2^{|E|}$.

# Core Definition
Theorem 5 (p. 352): For a connected graph $G$:
- $T_G(1,1)$ = number of spanning trees
- $T_G(2,1)$ = number of forests
- $T_G(1,2)$ = number of connected spanning subgraphs
- $T_G(2,2) = 2^{|E(G)|}$ = number of spanning subgraphs

Additional: $T_G(2,0) = a(G)$ = number of acyclic orientations; $T_G(1,0) = a_u(G)$ = acyclic orientations with unique source $u$ (Theorem 8).

# Prerequisites
- **Tutte polynomial** — The polynomial being evaluated

# Key Properties
1. $T_G(1,1)$: spanning trees (rank = $r(G)$, nullity = 0)
2. $T_G(2,1)$: forests (nullity = 0)
3. $T_G(1,2)$: connected spanning subgraphs (rank = $r(G)$)
4. $T_G(2,2) = 2^{|E|}$: all subsets
5. $T_G(2,0)$: acyclic orientations
6. $T_G(1,0)$: acyclic orientations with unique source $u$ (independent of $u$)
7. $T_G(0,2)$: totally cyclic orientations

# Context & Application
These evaluations demonstrate the richness of information encoded in $T_G$. They connect the Tutte polynomial to enumeration problems in graph theory.

# Examples
**Example** (Theorem 5 proof): $T_G(1,1) = \sum_F 0^{r(G)-r(F)} 0^{n(F)} = |\{F : r(F) = r(G), n(F) = 0\}|$ = number of spanning trees.

# Relationships
## Builds Upon
- **tutte-polynomial**

## Related
- **chromatic-polynomial-from-tutte** — At $y = 0$
- **flow-polynomial** — At $x = 0$
- **acyclic-orientation-count** — At $(2,0)$ and $(1,0)$

# Source Reference
Chapter X, Section X.4, Theorems 5, 8, 9, pages 352-358.

# Verification Notes
- Definition source: Direct from Theorem 5
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
