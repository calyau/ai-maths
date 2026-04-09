---
concept: Unavoidable Substructures in 2-Connected Graphs
slug: unavoidable-substructures-2connected
category: ramsey-theory
subcategory: ramsey-connectivity
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Ramsey Theory for Graphs"
chapter_number: 9
pdf_page: 279
section: "9.4 Ramsey properties and connectivity"
extraction_confidence: high
aliases:
  - "Proposition 9.4.2"
prerequisites:
  - unavoidable-substructures-connected
related:
  - kuratowski-set
answers_questions:
  - "What substructures must large 2-connected graphs contain?"
---

# Quick Definition
For every r, every sufficiently large 2-connected graph contains C^r or K_{2,r} as a topological minor (Proposition 9.4.2).

# Core Definition
**Proposition 9.4.2**: For every r in N there is an n in N such that every 2-connected graph of order at least n contains C^r or K_{2,r} as a topological minor.

If Delta(G) <= d then diam G > r, so Menger's theorem gives two independent paths forming a long cycle. If G has a high-degree vertex v, the neighbours of v in a spanning tree of G-v can be linked to v by r independent paths to form TK_{2,r}. (Diestel, p. 269)

# Prerequisites
- **Unavoidable substructures (connected)** — The 1-connected case

# Key Properties
1. The unavoidable set for 2-connected graphs (w.r.t. topological minors) is {cycles, K_{2,r}s}
2. This is the unique 2-element Kuratowski set (Theorem 9.4.5(ii))
3. The containment relation relaxes from "induced subgraph" to "topological minor"

# Relationships
## Related
- **Kuratowski set** — The formal framework

# Source Reference
Chapter 9, Section 9.4, Proposition 9.4.2, page 269 (pdf page 279).

# Verification Notes
- Confidence: HIGH — proposition with proof
