---
concept: A-Slice and B-Slice
slug: a-slice-b-slice
category: knot-theory
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 367
section: "X.6 Polynomials of Knots and Links"
extraction_confidence: high
aliases:
  - "A-region"
  - "B-region"
  - "A-channel"
  - "B-channel"
prerequisites:
  - link-diagram
extends: []
related:
  - state-of-link-diagram
  - kauffman-square-bracket
contrasts_with: []
answers_questions:
  - "How do knot polynomials relate to the Tutte polynomial?"
---

# Quick Definition
At each crossing in a link diagram, the two resolutions are called the A-slice (joining the A-regions) and the B-slice (joining the B-regions). The A-regions are found by rotating the overcrossing arc counterclockwise to the undercrossing arc.

# Core Definition
"Every unoriented crossing distinguishes two out of the four regions incident at its vertex. Rotate the overcrossing arc counterclockwise until the under-crossing arc is reached, and call the two regions swept out the A regions and the other two the B regions" (Bollobás, p. 367). An A-slice unites the two A-regions; a B-slice unites the two B-regions.

# Prerequisites
- **Link diagram** — Slicing resolves crossings in diagrams

# Key Properties
1. Each crossing has exactly two resolutions: A-slice and B-slice
2. A-slice: the two A-regions unite
3. B-slice: the two B-regions unite
4. A state of a diagram assigns A or B to each crossing
5. Analogous to deletion/contraction in graph theory

# Context & Application
The A-slice and B-slice are the link-diagram analogues of deletion and contraction: "There are also two ways of resolving a crossing in an (unoriented) link diagram" (p. 367), directly paralleling how the Tutte polynomial resolves edges.

# Examples
**Example** (Fig. X.8, p. 367): A diagram of knot $8_{19}$ with A and B regions marked.

**Example** (Fig. X.9, p. 367): A diagram $L$ with crossing at $v$, and the diagrams $L_v^A$ and $L_v^B$.

# Relationships
## Builds Upon
- **link-diagram**

## Enables
- **state-of-link-diagram** — A state is a choice of A or B at each crossing
- **kauffman-square-bracket** — Built from A and B slicings

# Source Reference
Chapter X, Section X.6, pages 367-368. Figures X.8, X.9.

# Verification Notes
- Definition source: Direct from p. 367
- Confidence rationale: Explicit definition with figures
- Uncertainties: None
- Cross-reference status: Verified
