---
concept: Medial Graph
slug: medial-graph
category: knot-theory
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 374
section: "X.6 Polynomials of Knots and Links"
extraction_confidence: high
aliases:
  - "M(G)"
prerequisites:
  - signed-plane-graph
extends: []
related:
  - link-diagram
  - alternating-link-diagram
contrasts_with: []
answers_questions:
  - "How do knot polynomials relate to the Tutte polynomial?"
---

# Quick Definition
The medial graph $M(G)$ of a plane graph $G$ is a 4-regular plane graph obtained by placing a vertex on each edge of $G$ and joining two new vertices by an edge in each face of $G$ if they lie on adjacent edges of that face.

# Core Definition
"The medial graph $M(G)$ of $G$ is obtained by inserting a vertex on every edge of $G$, and joining two new vertices by an edge lying in a face of $G$ if the vertices are on adjacent edges of the face. Thus $M(G)$ is a 4-regular plane graph whose alternate faces contain vertices of $G$" (Bollobás, p. 374).

# Prerequisites
- **Signed plane graph** — The medial graph reconstructs the link diagram from it

# Key Properties
1. $M(G)$ is 4-regular
2. Its alternate faces contain vertices of $G$
3. Shading those faces and assigning crossings according to edge signs reconstructs the link diagram
4. Provides the bridge between signed plane graphs and link diagrams

# Examples
**Example** (Fig. X.13, p. 374): A multigraph and its medial graph.

# Relationships
## Builds Upon
- **signed-plane-graph**

## Enables
- **link-diagram** — Reconstructed from signed graph via medial graph

## Related
- **alternating-link-diagram** — All-same-sign case

# Source Reference
Chapter X, Section X.6, pages 374-375. Figure X.13.

# Verification Notes
- Definition source: Direct from p. 374
- Confidence rationale: Explicit definition with figure
- Uncertainties: None
- Cross-reference status: Verified
