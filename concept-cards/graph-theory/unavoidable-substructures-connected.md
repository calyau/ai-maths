---
concept: Unavoidable Substructures in Connected Graphs
slug: unavoidable-substructures-connected
category: ramsey-theory
subcategory: ramsey-connectivity
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Ramsey Theory for Graphs"
chapter_number: 9
pdf_page: 278
section: "9.4 Ramsey properties and connectivity"
extraction_confidence: high
aliases:
  - "Proposition 9.4.1"
prerequisites:
  - ramsey-theorem-finite
  - graph
related:
  - unavoidable-substructures-2connected
  - kuratowski-set
answers_questions:
  - "What substructures must large connected graphs contain?"
---

# Quick Definition
For every r, every sufficiently large connected graph contains K^r, K_{1,r}, or P^r as an induced subgraph (Proposition 9.4.1).

# Core Definition
**Proposition 9.4.1**: For every r in N there is an n in N such that every connected graph of order at least n contains K^r, K_{1,r} or P^r as an induced subgraph.

Proof: If G has a vertex of degree >= d+1 (where d+1 is the Ramsey number of r), then by Theorem 9.1.1 either N(v) induces K^r or {v} union N(v) induces K_{1,r}. If Delta(G) <= d, then G has radius > r and contains a P^r. (Diestel, pp. 268-269)

# Prerequisites
- **Ramsey's theorem (finite)** — Used for the high-degree case
- **Graph** — Basic graph concepts

# Key Properties
1. The "unavoidable set" for connected graphs is {stars, complete graphs, paths}
2. This set is smallest possible and unique (Theorem 9.4.5(i))
3. For k-connected graphs with k >= 2, different containment relations and substructure sets apply

# Relationships
## Related
- **Unavoidable substructures (2-connected)** — Extends to higher connectivity
- **Kuratowski set** — The formal framework for unavoidable sets

# Source Reference
Chapter 9, Section 9.4, Proposition 9.4.1, pages 268-269 (pdf pages 278-279).

# Verification Notes
- Confidence: HIGH — proposition with proof
