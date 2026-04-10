---
# === CORE IDENTIFICATION ===
concept: Colour Class
slug: colour-class

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
  - "color class"
  - "independent colour set"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - vertex-colouring
extends: []
related:
  - chromatic-number
  - independence-number
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a colour class in a graph colouring?"
---

# Quick Definition
A colour class in a k-colouring c of a graph G is the set c⁻¹(j) of all vertices assigned colour j; each colour class is an independent set.

# Core Definition
Given a k-colouring c: V(G) → {1, 2, ..., k}, the sets c⁻¹(j) for j = 1, ..., k are the **colour classes** of the colouring. Each colour class is an independent set since no two adjacent vertices share a colour (Bollobás, p. 152).

# Prerequisites
- **Vertex colouring** — colour classes arise from a proper vertex colouring

# Key Properties
1. Each colour class is an independent set in G
2. The colour classes partition V(G) into at most k parts
3. The size of each colour class is at most α(G), the independence number
4. A k-colouring has exactly k non-empty colour classes (assuming all colours are used)

# Construction / Recognition
## To Identify Colour Classes
1. Given a colouring c, group vertices by their assigned colour
2. Each group is a colour class
3. Verify each group is independent (no internal edges)

# Context & Application
Colour classes provide the bridge between colouring and partition problems. The chromatic number χ(G) equals the minimum number of independent sets needed to partition V(G).

# Examples
**Example** (p. 152): In a 2-colouring of a bipartite graph G with parts A and B, the two colour classes are exactly A and B.

# Relationships
## Builds Upon
- **Vertex colouring** — colour classes are defined by a colouring

## Enables
- **Chromatic number** — χ(G) = min number of colour classes in a partition of V(G)

## Related
- **Independence number** — each colour class has size ≤ α(G), giving χ(G) ≥ |G|/α(G)

# Common Errors
- **Error**: Forgetting that colour classes must be independent sets
  **Correction**: By definition of proper colouring, each colour class contains no adjacent pair

# Common Confusions
- **Confusion**: Thinking colour classes must have equal size
  **Clarification**: Colour classes can have any sizes as long as they partition V(G)

# Source Reference
Chapter V: Colouring, Section V.1, page 152.

# Verification Notes
- Definition source: Direct from p. 152
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
