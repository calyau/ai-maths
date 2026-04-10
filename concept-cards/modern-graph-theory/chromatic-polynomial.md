---
concept: Chromatic Polynomial
slug: chromatic-polynomial
category: vertex-coloring
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Colouring"
chapter_number: 5
pdf_page: 156
section: "V.1 Vertex Colouring"
extraction_confidence: high
aliases:
  - "p_H(x)"
  - "chromatic polynomial of H"
prerequisites:
  - vertex-colouring
  - chromatic-number
extends: []
related:
  - deletion-contraction
  - tutte-polynomial
  - broken-cycle-theorem
contrasts_with:
  - tutte-polynomial
answers_questions:
  - "What is the chromatic polynomial?"
  - "How do I compute the chromatic polynomial of a graph?"
  - "What distinguishes the chromatic polynomial from the Tutte polynomial?"
---

# Quick Definition
The chromatic polynomial p_H(x) counts the number of proper colourings of graph H using colours 1, 2, ..., x. It is a polynomial in x whose smallest positive root determines χ(H).

# Core Definition
For a natural number x and a graph H, p_H(x) denotes the number of proper colourings of H with colours 1, 2, ..., x. **Theorem 4** (Bollobás, p. 157) establishes that p_H(x) is indeed a polynomial: if H has n vertices, m edges, and k components, then

p_H(x) = Σᵢ₌₀ⁿ⁻ᵏ (−1)ⁱ aᵢ xⁿ⁻ⁱ

where a₀ = 1, a₁ = m, and aᵢ is a positive integer for every i.

# Prerequisites
- **Vertex colouring** — chromatic polynomial counts proper colourings
- **Chromatic number** — χ(G) is the least k with p_G(k) ≥ 1

# Key Properties
1. p_H(x) is a polynomial of degree n (number of vertices)
2. Leading coefficient is 1 (coefficient of xⁿ)
3. Coefficient of xⁿ⁻¹ is −m (negative of edge count)
4. All coefficients alternate in sign
5. χ(H) is the smallest positive integer k with p_H(k) > 0
6. p_H(x) can also be expressed as Σᵣ πᵣ(H)(x)ᵣ where πᵣ(H) counts partitions into r independent sets

# Construction / Recognition
## To Compute p_H(x) via Deletion-Contraction
1. If H has no edges, p_H(x) = xⁿ (n = number of vertices)
2. If H has an edge ab, pick it and compute:
   - p_{H−ab}(x): delete edge ab
   - p_{H/ab}(x): contract edge ab
3. Then p_H(x) = p_{H−ab}(x) − p_{H/ab}(x)
4. Recurse until all graphs are edgeless

## Via Broken Cycle Theorem
1. Order edges e₁, ..., eₘ
2. A broken cycle is a cycle's edge set minus its highest-indexed edge
3. aᵢ = number of i-subsets of E(H) containing no broken cycle

# Context & Application
The chromatic polynomial was introduced by Birkhoff in connection with the four colour problem. It encodes richer information than just the chromatic number and is a specialization of the Tutte polynomial.

# Examples
**Example** (p. 157): For a graph with no edges, p_H(x) = xⁿ (every function is a colouring).

**Example**: For Kₙ, p_{Kₙ}(x) = x(x−1)(x−2)···(x−n+1) = (x)ₙ.

**Example** (Corollary 6, p. 158): If H has girth g, then aᵢ = C(m,i) for i ≤ g − 2.

# Relationships
## Builds Upon
- **Vertex colouring** — counts proper colourings

## Enables
- **Broken cycle theorem** — gives coefficients combinatorial interpretation
- **Tutte polynomial** — chromatic polynomial is a specialization

## Related
- **Deletion-contraction** — computational method
- **Chromatic number** — derived from chromatic polynomial

## Contrasts With
- **Tutte polynomial** — a substantial generalization defined for multigraphs using analogous cut/fuse operations

# Common Errors
- **Error**: Forgetting to include the sign alternation when computing coefficients
  **Correction**: The coefficient of xⁿ⁻ⁱ has sign (−1)ⁱ

# Common Confusions
- **Confusion**: Thinking the chromatic polynomial determines the graph
  **Clarification**: Non-isomorphic graphs can have the same chromatic polynomial (chromatically equivalent graphs)

# Source Reference
Chapter V: Colouring, Section V.1, Theorems 4–5, Corollary 6, pages 156–158.

# Verification Notes
- Definition source: Direct from p. 157 (Theorem 4)
- Confidence rationale: Explicit definition and theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
