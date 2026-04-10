---
# === CORE IDENTIFICATION ===
concept: Chromatic Number
slug: chromatic-number

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
  - "χ(G)"
  - "vertex chromatic number"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - vertex-colouring
extends: []
related:
  - clique-number
  - independence-number
  - chromatic-polynomial
  - chromatic-index
contrasts_with:
  - chromatic-index
  - list-chromatic-number

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the chromatic number of a graph?"
  - "How does the chromatic number relate to the clique number?"
---

# Quick Definition
The chromatic number χ(G) of a graph G is the minimal number of colours needed in a proper vertex colouring of G.

# Core Definition
The chromatic number χ(G) is the minimal value of k for which V(G) can be partitioned into k classes V₁, V₂, ..., Vₖ such that no edge joins two vertices of the same class. Equivalently, χ(G) is the least natural number k for which the chromatic polynomial satisfies p_G(k) ≥ 1 (Bollobás, p. 152).

# Prerequisites
- **Vertex colouring** — χ(G) is defined as the minimum number of colours in a proper vertex colouring

# Key Properties
1. χ(G) ≥ ω(G), where ω(G) is the clique number
2. χ(G) ≥ |G|/α(G), where α(G) is the independence number
3. χ(G) ≥ max{ω(G), |G|/α(G)}
4. χ(G) ≤ Δ(G) + 1 (from the greedy algorithm)
5. χ(G) = 1 iff G has no edges; χ(G) = 2 iff G is bipartite with at least one edge
6. χ(G) ≥ 3 iff G contains an odd cycle

# Construction / Recognition
## To Determine or Bound χ(G)
1. Find the clique number ω(G) — this gives a lower bound
2. Compute |G|/α(G) — this gives another lower bound
3. Apply the greedy algorithm with a good vertex ordering — this gives an upper bound
4. Apply Brooks' theorem if G is connected, not complete, and not an odd cycle

## To Verify χ(G) = k
1. Exhibit a proper k-colouring (upper bound)
2. Show no (k−1)-colouring exists (lower bound), e.g., by finding a k-clique or using other arguments

# Context & Application
The chromatic number is one of the most studied graph invariants. It is NP-hard to compute in general, even to approximate within a constant factor. It arises naturally in scheduling, register allocation, and frequency assignment problems.

# Examples
**Example** (p. 152): χ(Kₖ) = k, χ(K̄ₖ) = 1, χ(C₂ₖ) = 2, χ(C₂ₖ₊₁) = 3.

**Example** (p. 153): There exist triangle-free graphs with arbitrarily large chromatic number (shown via random graphs in Chapter VII), demonstrating that ω(G) can be much smaller than χ(G).

# Relationships
## Builds Upon
- **Vertex colouring** — χ(G) minimizes the number of colours used

## Enables
- **Brooks' theorem** — gives tight upper bound χ(G) ≤ Δ(G)
- **Perfect graphs** — defined by χ(H) = ω(H) for all induced subgraphs H
- **Chromatic polynomial** — counts colourings, with χ(G) as the smallest k where p_G(k) > 0

## Related
- **Clique number** — lower bound ω(G) ≤ χ(G)
- **Independence number** — related via |G|/α(G) ≤ χ(G)

## Contrasts With
- **Chromatic index** — minimum colours for edge colouring
- **List-chromatic number** — minimum list size guaranteeing a list colouring

# Common Errors
- **Error**: Assuming χ(G) = ω(G) for all graphs
  **Correction**: This equality holds only for perfect graphs; in general χ(G) can be much larger than ω(G)

# Common Confusions
- **Confusion**: Thinking that triangle-free graphs must have small chromatic number
  **Clarification**: There exist triangle-free graphs (ω = 2) with arbitrarily large chromatic number

# Source Reference
Chapter V: Colouring, Section V.1, pages 152–154.

# Verification Notes
- Definition source: Direct from p. 152
- Confidence rationale: Explicit definition with standard notation χ(G)
- Uncertainties: None
- Cross-reference status: Verified
