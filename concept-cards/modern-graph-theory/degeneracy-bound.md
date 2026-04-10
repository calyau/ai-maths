---
concept: Degeneracy Bound on Chromatic Number
slug: degeneracy-bound
category: vertex-coloring
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Colouring"
chapter_number: 5
pdf_page: 155
section: "V.1 Vertex Colouring"
extraction_confidence: high
aliases:
  - "Theorem V.1"
  - "degeneracy colouring bound"
prerequisites:
  - chromatic-number
  - greedy-colouring-algorithm
extends:
  - greedy-colouring-algorithm
related:
  - brooks-theorem
contrasts_with: []
answers_questions:
  - "How can the minimum degree of subgraphs bound the chromatic number?"
---

# Quick Definition
If k = max_H δ(H) over all induced subgraphs H of G, then χ(G) ≤ k + 1. Equivalently, a minimal (k+1)-chromatic graph has minimum degree at least k.

# Core Definition
**Theorem 1** (Bollobás, p. 155): Let k = max_H δ(H), where the maximum is taken over all induced subgraphs of G. Then χ(G) ≤ k + 1.

The proof constructs a vertex ordering by repeatedly removing a vertex of minimum degree from the current subgraph, then applying greedy colouring in the reverse order.

# Prerequisites
- **Chromatic number** — the quantity being bounded
- **Greedy colouring algorithm** — the proof uses greedy with a specific ordering

# Key Properties
1. χ(G) ≤ max_H δ(H) + 1 where H ranges over induced subgraphs
2. This is at most Δ(G) + 1, but can be much tighter
3. A minimal (k+1)-chromatic graph has δ(G) ≥ k
4. If G is connected and not Δ-regular, then χ(G) ≤ Δ(G)

# Construction / Recognition
## To Apply the Degeneracy Ordering
1. Let xₙ be a vertex of minimum degree in G
2. Let xₙ₋₁ be a vertex of minimum degree in G − {xₙ}
3. Continue removing minimum-degree vertices to get ordering x₁, ..., xₙ
4. Apply greedy colouring in this order — each xⱼ has at most k previously-coloured neighbours

# Context & Application
The degeneracy bound is a refinement of the trivial Δ(G) + 1 bound. It captures the idea that sparse substructures allow better colourings and motivates Brooks' theorem, which handles the regular case.

# Examples
**Example** (p. 155): Every planar graph has an induced subgraph with minimum degree at most 5 (by Euler's formula), so χ(G) ≤ 6 for planar graphs.

# Relationships
## Builds Upon
- **Greedy colouring algorithm** — uses greedy with degeneracy ordering

## Enables
- **Brooks' theorem** — addresses the remaining case when G is Δ-regular

## Related
- The Δ(G) + 1 bound is a corollary

# Common Errors
- **Error**: Confusing max_H δ(H) with δ(G)
  **Correction**: The bound uses the maximum minimum degree over ALL induced subgraphs, not just G itself

# Common Confusions
- **Confusion**: Thinking this bound is always tight
  **Clarification**: The bound can be strict; Brooks' theorem often gives a better result

# Source Reference
Chapter V: Colouring, Section V.1, Theorem 1, page 155.

# Verification Notes
- Definition source: Direct theorem statement from p. 155
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
