---
concept: Replacement Theorem for Perfect Graphs
slug: replacement-theorem-for-perfect-graphs
category: perfect-graphs
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Colouring"
chapter_number: 5
pdf_page: 177
section: "V.5 Perfect Graphs"
extraction_confidence: high
aliases:
  - "Theorem V.19"
  - "substitution theorem"
prerequisites:
  - perfect-graph
extends:
  - perfect-graph
related:
  - perfect-graph-theorem
contrasts_with: []
answers_questions:
  - "Can perfect graphs be built from smaller perfect graphs?"
---

# Quick Definition
A graph obtained from a perfect graph by replacing its vertices by perfect graphs is perfect. This enables construction of large families of perfect graphs.

# Core Definition
**Theorem 19** (Bollobás, p. 177): A graph obtained from a perfect graph by replacing its vertices by perfect graphs is perfect. Formally, if G has vertices [n] and G₁, ..., Gₙ are perfect, then G* = G[G₁, ..., Gₙ] (obtained by replacing vertex i with Gᵢ, joining all of Gᵢ to all of Gⱼ when ij ∈ E(G)) is perfect.

The proof uses Lemma 18 (characterization via independent sets meeting all maximum cliques) and proceeds by finding appropriate independent sets in G*.

# Prerequisites
- **Perfect graph** — the class being preserved

# Key Properties
1. Perfection is closed under vertex substitution
2. Used as a key lemma in the proof of the Perfect Graph Theorem
3. Can replace vertices one at a time

# Relationships
## Builds Upon
- **Perfect graph** definition

## Enables
- **Perfect graph theorem** — the replacement theorem is a key step

# Source Reference
Chapter V: Colouring, Section V.5, Theorem 19, pages 177–178.

# Verification Notes
- Definition source: Direct theorem statement from p. 177
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
