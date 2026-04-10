---
concept: Signed Plane Graph
slug: signed-plane-graph
category: knot-theory
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 373
section: "X.6 Polynomials of Knots and Links"
extraction_confidence: high
aliases:
  - "edge-coloured plane graph"
prerequisites:
  - link-diagram
extends: []
related:
  - alternating-link-diagram
  - medial-graph
  - tutte-polynomial-and-jones-polynomial
contrasts_with: []
answers_questions:
  - "How do knot polynomials relate to the Tutte polynomial?"
---

# Quick Definition
A signed plane graph $G(D)$ is associated to a shaded link diagram $D$: vertices correspond to shaded faces, edges to crossings, and each edge is coloured $+$ or $-$ according to the crossing type. Two signed graphs are equivalent iff their link diagrams are equivalent.

# Core Definition
To each connected shaded plane diagram $D$, associate an edge-coloured multigraph $G(D)$: "For each shaded face $F$, take a vertex $v_F$ in $F$, and for each crossing at which $F_1$ and $F_2$ meet, take an edge $v_{F_1}v_{F_2}$. Furthermore, colour each edge $+$ or $-$ according to the type of the crossing" (Bollobás, p. 373).

# Prerequisites
- **Link diagram** — Signed plane graphs encode link diagrams

# Key Properties
1. Bijective correspondence between connected shaded diagrams and signed plane graphs
2. Conversely, $G(D)$ reconstructs $D$ via the medial graph
3. Reidemeister moves on diagrams correspond to "graph Reidemeister moves" on signed graphs
4. For alternating diagrams: all edges have the same sign

# Context & Application
Signed plane graphs reduce the study of link equivalence classes to the study of equivalence classes of signed plane graphs, enabling graph-theoretic techniques in knot theory.

# Examples
**Example** (Fig. X.12, p. 373): A shading of a link diagram, the two crossing types, and the resulting signed graph.

# Relationships
## Builds Upon
- **link-diagram**

## Enables
- **alternating-link-diagram** — All-$+$ or all-$-$ signed graphs
- **tutte-polynomial-and-jones-polynomial** — Via $G^+(L)$

## Related
- **medial-graph** — Used to reconstruct the diagram from the graph

# Source Reference
Chapter X, Section X.6, pages 373-374. Figures X.12-X.14.

# Verification Notes
- Definition source: Direct from p. 373
- Confidence rationale: Explicit construction
- Uncertainties: None
- Cross-reference status: Verified
