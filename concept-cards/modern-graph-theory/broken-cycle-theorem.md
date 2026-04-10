---
concept: Broken Cycle Theorem
slug: broken-cycle-theorem
category: vertex-coloring
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Colouring"
chapter_number: 5
pdf_page: 157
section: "V.1 Vertex Colouring"
extraction_confidence: high
aliases:
  - "Theorem V.5"
  - "Whitney's broken cycle theorem"
prerequisites:
  - chromatic-polynomial
extends:
  - chromatic-polynomial
related:
  - deletion-contraction
contrasts_with: []
answers_questions:
  - "How can the coefficients of the chromatic polynomial be computed combinatorially?"
---

# Quick Definition
The coefficient aᵢ in the chromatic polynomial p_H(x) = Σ(−1)ⁱ aᵢ xⁿ⁻ⁱ equals the number of i-subsets of E(H) containing no broken cycle, where a broken cycle is obtained from a cycle's edge set by removing the edge of highest index.

# Core Definition
**Theorem 5** (Bollobás, p. 157): Let H have n vertices and edges E(H) = {e₁, ..., eₘ}. A **broken cycle** is a subset of E(H) obtained from the edge set of a cycle by deleting the edge of highest index. Then p_H(x) = Σᵢ₌₀ⁿ⁻¹ (−1)ⁱ aᵢ xⁿ⁻ⁱ, where aᵢ is the number of i-subsets of E(H) containing no broken cycle.

# Prerequisites
- **Chromatic polynomial** — the broken cycle theorem gives a combinatorial interpretation of its coefficients

# Key Properties
1. The count of broken-cycle-free i-subsets is independent of the edge ordering
2. a₀ = 1 and a₁ = m (number of edges) always
3. If H has girth g, then aᵢ = C(m,i) for i ≤ g − 2 (Corollary 6)
4. If g is finite and H has c_g cycles of length g, then a_{g−1} = C(m, g−1) − c_g

# Construction / Recognition
## To Compute Coefficients via Broken Cycles
1. Order edges e₁, e₂, ..., eₘ
2. For each cycle, remove its highest-indexed edge to get a broken cycle
3. For each i, count i-subsets of E(H) that avoid all broken cycles
4. This count gives aᵢ

# Context & Application
The broken cycle theorem provides a combinatorial interpretation of chromatic polynomial coefficients that avoids the exponential recursion of deletion-contraction. For graphs with large girth, it immediately gives the first several coefficients.

# Examples
**Example** (Corollary 6, p. 158): For a graph with girth g > 2, the first g − 1 coefficients are simply binomial coefficients C(m, i), since no broken cycle has fewer than g − 1 edges.

# Relationships
## Builds Upon
- **Chromatic polynomial** — interprets its coefficients

## Related
- **Deletion-contraction** — alternative computation method

# Common Errors
- **Error**: Thinking the broken cycles depend on the edge ordering
  **Correction**: While the individual broken cycles depend on the ordering, the count of broken-cycle-free sets does not

# Common Confusions
- **Confusion**: Confusing broken cycles with cycles
  **Clarification**: A broken cycle has one fewer edge than its parent cycle (the highest-indexed edge is removed)

# Source Reference
Chapter V: Colouring, Section V.1, Theorem 5 and Corollary 6, pages 157–158.

# Verification Notes
- Definition source: Direct theorem statement from p. 157
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
