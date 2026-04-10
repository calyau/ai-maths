---
concept: Euler's Formula for Planar Graphs
slug: euler-formula-for-planar-graphs
category: planar-graphs
subcategory: null
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Colouring"
chapter_number: 5
pdf_page: 161
section: "V.3 Graphs on Surfaces"
extraction_confidence: high
aliases:
  - "Euler's formula"
  - "n - e + f = 2"
prerequisites: []
extends: []
related:
  - euler-poincare-formula
  - five-colour-theorem
contrasts_with: []
answers_questions:
  - "How does Euler's formula constrain planar graphs?"
---

# Quick Definition
For a connected planar graph with n vertices, e edges, and f faces: n − e + f = 2. This implies e ≤ 3n − 6 and δ(G) ≤ 5.

# Core Definition
Euler's formula states that for a connected plane graph with n vertices, e edges, and f faces, n − e + f = 2. A key consequence (Theorem I.16, cited on p. 161) is that every plane graph of order n has at most 3n − 6 edges, and therefore has minimum degree at most 5. This is the essential ingredient for the five-colour theorem and the proof strategy of the four-colour theorem.

# Prerequisites
This is a foundational concept with no prerequisites within this source.

# Key Properties
1. n − e + f = 2 for connected planar graphs
2. e ≤ 3n − 6 for planar graphs with n ≥ 3
3. Every planar graph has a vertex of degree at most 5
4. χ(G) ≤ 6 for every planar graph G (immediate from degeneracy bound)

# Context & Application
Euler's formula is the starting point for all colouring results on planar graphs. The discharging method used in the four-colour theorem proof assigns charges based on Euler's formula to show unavoidability of configurations.

# Examples
**Example** (p. 161): Every plane graph of order n has at most 3n − 6 edges, so its minimal degree is at most 5. By Theorem 1 (degeneracy bound), χ(G) ≤ 6.

# Relationships
## Enables
- **Five colour theorem** — needs a degree-≤-5 vertex
- **Four colour theorem** — discharging method based on Euler's formula
- **Heawood bound** — generalization to surfaces

## Related
- **Euler-Poincaré formula** — generalization to arbitrary surfaces

# Source Reference
Chapter V: Colouring, Section V.3, page 161. (Theorem I.16 from Chapter I.)

# Verification Notes
- Definition source: Referenced from Chapter I, applied on p. 161
- Confidence rationale: Well-known formula, explicitly used
- Uncertainties: None
- Cross-reference status: Verified
