---
concept: Star-Triangle Transformation
slug: star-triangle-transformation
category: electrical-networks
subcategory: network-simplification
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Electrical Networks"
chapter_number: 2
pdf_page: 46
section: "II.1 Graphs and Electrical Networks"
extraction_confidence: high
aliases:
  - star-delta transformation
  - Y-Delta transformation
prerequisites:
  - electrical-network
  - resistance-and-conductance
  - series-and-parallel-connection
extends: []
related:
  - principle-of-superposition
contrasts_with: []
answers_questions:
  - "What is the star-triangle transformation?"
---

# Quick Definition

The star-triangle transformation replaces a degree-3 vertex (star) connected to vertices $a, b, c$ by resistances $A, B, C$ with a triangle of resistances $A' = (AB + BC + CA)/C$, $B' = (AB + BC + CA)/A$, $C' = (AB + BC + CA)/B$.

# Core Definition

"If a vertex $v$ is joined to just three vertices, say $a, b$, and $c$, by edges of resistances $A, B$, and $C$, then we call $v$ the centre of a star" (Bollobás, p. 51). The star can be replaced by a triangle with resistances $A' = S/C$, $B' = S/A$, $C' = S/B$ where $S = AB + BC + CA$, preserving external currents. The inverse transformation uses $A = B'C'/T$, $B = C'A'/T$, $C = A'B'/T$ where $T = A' + B' + C'$.

# Prerequisites

- **Electrical network** — The transformation applies to networks
- **Resistance and conductance** — Uses resistance values
- **Series and parallel connection** — Simpler reduction operations

# Key Properties

1. Removes a degree-3 vertex by replacing star with triangle
2. Preserves all currents outside the transformed region
3. Inverse transformation: triangle to star
4. Formulas become symmetric using conductances: $\alpha = \beta'\gamma'/(\alpha' + \beta' + \gamma')$ etc.
5. Can be combined with series/parallel reductions for complex networks

# Construction / Recognition

## Star to Triangle
Given star with centre $v$, edges $va, vb, vc$ of resistances $A, B, C$:
1. Compute $S = AB + BC + CA$
2. Replace with triangle $ab, bc, ca$ of resistances $S/C, S/A, S/B$

# Context & Application

The star-triangle transformation is a standard technique in electrical engineering. Bollobás uses it to compute the resistance of a tetrahedron (Fig. II.5, p. 51).

# Examples

**Example** (p. 51): Fig. II.4 shows the star-triangle transformation. Fig. II.5 shows its application to computing the resistance of a tetrahedron.

# Relationships

## Builds Upon
- **Electrical network**, **Resistance and conductance**

## Enables
- Solving networks that cannot be reduced by series/parallel alone

## Related
- **Series and parallel connection** — Simpler special cases

# Common Errors

- **Error**: Forgetting to remove the centre vertex after the transformation
  **Correction**: The star-triangle transformation eliminates the centre vertex entirely

# Common Confusions

- **Confusion**: Thinking the transformation changes the network behaviour
  **Clarification**: External currents and potentials are preserved; only the internal structure changes

# Source Reference

Chapter II: Electrical Networks, Section II.1, pages 51-52.

# Verification Notes

- Definition source: Direct from p. 51
- Confidence rationale: Explicitly described with formulas
- Uncertainties: None
- Cross-reference status: Verified
