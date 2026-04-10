---
concept: Nešetřil-Rödl Theorem
slug: nesetril-rodl-theorem
category: ramsey-theory
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Ramsey Theory"
chapter_number: 6
pdf_page: 204
section: "VI.3 Ramsey Theory For Graphs"
extraction_confidence: high
aliases:
  - "Theorem VI.19"
prerequisites:
  - graphical-ramsey-number
  - ramsey-theorem-finite
extends:
  - ramsey-theorem-finite
related: []
contrasts_with: []
answers_questions:
  - "Can Ramsey-type results hold for sparse graphs (not just complete graphs)?"
---

# Quick Definition
For every graph H and integer k ≥ 1, there is a graph G with ω(G) = ω(H) such that every k-colouring of E(G) contains a monochromatic induced copy of H. Ramsey properties hold even for graphs with small clique number.

# Core Definition
**Theorem 19** (Bollobás, p. 204): For every graph H and integer k ≥ 1, there is a graph G with ω(G) = ω(H) such that every k-colouring of the edges of G contains a monochromatic induced subgraph isomorphic to H. This shows that the Ramsey property does not require dense graphs — G can have the same clique number as H.

# Prerequisites
- **Graphical Ramsey number** — context for Ramsey on specific graphs
- **Ramsey theorem (finite)** — extended by this result

# Key Properties
1. G can have ω(G) = ω(H) — no denser than necessary
2. The monochromatic copy is an induced subgraph
3. Extends earlier results of Graham and Folkman

# Context & Application
This deep result shows that Ramsey phenomena are not an artifact of working with complete graphs. Even sparse host graphs can force monochromatic copies.

# Relationships
## Builds Upon
- **Ramsey theorem** — extends to sparse host graphs

# Source Reference
Chapter VI: Ramsey Theory, Section VI.3, Theorem 19, page 204.

# Verification Notes
- Definition source: Direct theorem statement from p. 204
- Confidence rationale: Explicitly stated (proof not given)
- Uncertainties: None
- Cross-reference status: Verified
