---
concept: "k-Flow and Z_k-Flow Equivalence"
slug: tutte-kflow-zkflow-equivalence
category: network-flows
subcategory: algebraic-flows
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Flows"
chapter_number: 6
pdf_page: 157
section: "6.3 Group-valued flows"
extraction_confidence: high
aliases:
  - "Theorem 6.3.3"
  - "Tutte's k-flow theorem"
prerequisites:
  - k-flow
  - h-flow
related:
  - tutte-flow-group-equivalence
  - flow-polynomial
answers_questions:
  - "How are k-flows related to Z_k-flows?"
---

# Quick Definition
A multigraph admits a k-flow if and only if it admits a Z_k-flow (Tutte 1950). This reduces general group-valued flow questions to integer-valued flows.

# Core Definition
**Theorem 6.3.3** (Tutte 1950): A multigraph admits a k-flow if and only if it admits a Z_k-flow. The proof: given a Z_k-flow g, find f in Z satisfying (F1) and |f| < k with sigma_k o f = g; then minimize K(f) = sum |f(x,V)| to force K(f) = 0 (Kirchhoff's law). The key insight: f(x,V) and f(x',V) are multiples of k (since g satisfies (F2) in Z_k), so sending k units back along a walk from x to x' reduces K. (Diestel, pp. 147-149)

# Prerequisites
- **k-flow** — One side of the equivalence
- **H-flow** — The Z_k-flow on the other side

# Key Properties
1. The central reduction theorem for algebraic flows
2. Z_k-flows are often easier to construct (by summing partial flows)
3. Combined with Corollary 6.3.2: H-flow existence for all groups reduces to k-flows
4. The proof uses a minimum-deviation argument

# Relationships
## Related
- **Tutte flow-group equivalence** — Corollary 6.3.2
- **Flow polynomial** — Theorem 6.3.1

# Source Reference
Chapter 6, Section 6.3, Theorem 6.3.3, pages 147-149 (pdf pages 157-159).

# Verification Notes
- Confidence: HIGH — major theorem with complete proof
