---
concept: Class 1 and Class 2 Graphs
slug: class-one-class-two
category: edge-coloring
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Colouring"
chapter_number: 5
pdf_page: 159
section: "V.2 Edge Colouring"
extraction_confidence: medium
aliases:
  - "Class 1 graph"
  - "Class 2 graph"
prerequisites:
  - chromatic-index
  - vizings-theorem
extends:
  - vizings-theorem
related: []
contrasts_with: []
answers_questions:
  - "What determines whether a graph is Class 1 or Class 2?"
---

# Quick Definition
A graph is Class 1 if χ'(G) = Δ(G) (edge-colourable with exactly Δ colours) and Class 2 if χ'(G) = Δ(G) + 1. By Vizing's theorem, every graph falls into one of these two classes.

# Core Definition
By Vizing's theorem, every graph G satisfies χ'(G) ∈ {Δ(G), Δ(G) + 1}. Graphs with χ'(G) = Δ(G) are called **Class 1** and those with χ'(G) = Δ(G) + 1 are called **Class 2**. Determining which class a graph belongs to is NP-complete in general (Bollobás, pp. 158–160).

# Prerequisites
- **Chromatic index** — the classification depends on whether χ' = Δ or Δ + 1
- **Vizing's theorem** — establishes that these are the only two possibilities

# Key Properties
1. Bipartite graphs are always Class 1
2. Complete graphs Kₙ with n odd are Class 2
3. Complete graphs Kₙ with n even are Class 1
4. The Petersen graph is Class 2
5. Determining the class of a graph is NP-complete

# Construction / Recognition
## Known Class 1 Families
1. All bipartite graphs (by König/Hall's theorem)
2. Complete graphs of even order
3. Planar graphs with Δ ≥ 7 (by Vizing's planar graph theorem)

## Known Class 2 Families
1. Odd complete graphs
2. The Petersen graph
3. Odd cycles (Δ = 2, χ' = 3)

# Context & Application
The Class 1/Class 2 dichotomy is one of the central questions in edge-colouring theory. Petersen's observation (1891) that the four-colour theorem is equivalent to every 2-connected cubic planar graph being Class 1 shows the depth of this classification.

# Examples
**Example** (p. 158): Bipartite graphs satisfy χ'(G) = Δ(G) (Class 1).

**Example** (p. 159): χ'(Kⁿ) = n − 1 = Δ when n is even (Class 1); χ'(Kⁿ) = n = Δ + 1 when n is odd (Class 2).

# Relationships
## Builds Upon
- **Vizing's theorem** — creates the dichotomy

## Related
- **Four colour theorem** — equivalent to every 2-connected cubic planar graph being Class 1

# Common Confusions
- **Confusion**: Thinking sparse graphs are always Class 1
  **Clarification**: Even sparse graphs like odd cycles are Class 2

# Source Reference
Chapter V: Colouring, Section V.2, pages 158–160.

# Verification Notes
- Definition source: Synthesized from Vizing's theorem discussion, pp. 158–160
- Confidence rationale: Medium — terminology implicit in discussion
- Uncertainties: The terms "Class 1" and "Class 2" are standard but not explicitly named in the source text
- Cross-reference status: Verified
