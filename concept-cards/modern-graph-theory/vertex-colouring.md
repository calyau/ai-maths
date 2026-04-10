---
# === CORE IDENTIFICATION ===
concept: Vertex Colouring
slug: vertex-colouring

# === CLASSIFICATION ===
category: vertex-coloring
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Colouring"
chapter_number: 5
pdf_page: 152
section: "V.1 Vertex Colouring"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "proper colouring"
  - "vertex coloring"
  - "graph colouring"
  - "k-colouring"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - chromatic-number
  - colour-class
  - edge-colouring
contrasts_with:
  - edge-colouring
  - list-colouring

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a vertex colouring of a graph?"
  - "What distinguishes vertex coloring from edge coloring?"
---

# Quick Definition
A proper colouring (or simply colouring) of the vertices of a graph G is an assignment of colours to the vertices such that adjacent vertices receive distinct colours.

# Core Definition
A **k-colouring** of the vertices of G is a function c: V(G) → {1, 2, ..., k} such that each set c⁻¹(j) is independent. The sets c⁻¹(j) are the **colour classes** of the colouring. The motivating example is scheduling talks in a congress so that no participant misses a talk they want to attend (Bollobás, p. 152).

# Prerequisites
This is a foundational concept with no prerequisites within this source.

# Key Properties
1. Adjacent vertices must receive distinct colours
2. A k-colouring partitions V(G) into at most k independent sets
3. The colour classes c⁻¹(j) are independent sets in G
4. χ(Kₖ) = k, χ(K̄ₖ) = 1, χ(C₂ₖ) = 2, χ(C₂ₖ₊₁) = 3
5. A graph is 2-colourable if and only if it is bipartite

# Construction / Recognition
## To Colour a Graph
1. Order the vertices x₁, x₂, ..., xₙ
2. Assign colour 1 to x₁
3. For each subsequent vertex xᵢ, assign the smallest colour not used by any already-coloured neighbour
4. This greedy algorithm always produces a valid colouring (though not necessarily optimal)

## To Verify a Colouring
1. For each edge uv ∈ E(G), check that c(u) ≠ c(v)
2. If all edges pass, the colouring is proper

# Context & Application
Vertex colouring is one of the most fundamental concepts in graph theory, with applications to scheduling, register allocation, frequency assignment, and map colouring. The chapter introduction frames it as a scheduling problem: assigning time slots to talks so conflicting talks occur at different times.

# Examples
**Example** (p. 152): The congress scheduling problem — vertices are talks, edges join talks with common attendees. The chromatic number gives the minimum number of time slots needed.

**Example** (p. 152): Complete graph Kₖ requires exactly k colours. The empty graph K̄ₖ needs only 1 colour. Even cycles need 2 colours, odd cycles need 3.

# Relationships
## Builds Upon
- Independent set (colour classes are independent sets)

## Enables
- **Chromatic number** — defined as the minimum k for which a k-colouring exists
- **Chromatic polynomial** — counts the number of k-colourings
- **Brooks' theorem** — bounds χ(G) in terms of Δ(G)

## Related
- **Edge colouring** — analogous concept for edges
- **List colouring** — variant where each vertex has a prescribed list of available colours

## Contrasts With
- **Edge colouring** — colours edges rather than vertices; adjacent edges get distinct colours

# Common Errors
- **Error**: Assuming the greedy algorithm always gives an optimal colouring
  **Correction**: The greedy algorithm may use far more colours than necessary; Figure V.1 shows a bipartite graph where greedy uses 4 colours instead of 2

# Common Confusions
- **Confusion**: Conflating vertex colouring with edge colouring
  **Clarification**: Vertex colouring assigns colours to vertices (adjacent vertices differ); edge colouring assigns colours to edges (incident edges differ). They are related by χ'(G) = χ(L(G))

# Source Reference
Chapter V: Colouring, Section V.1, pages 152–155.

# Verification Notes
- Definition source: Direct from p. 152, paragraph 1
- Confidence rationale: Explicit definition with notation and examples
- Uncertainties: None
- Cross-reference status: Verified against chapter content
