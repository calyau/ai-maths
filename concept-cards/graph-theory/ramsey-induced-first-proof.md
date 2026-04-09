---
concept: "First Proof of Induced Ramsey Theorem (Deuber)"
slug: ramsey-induced-first-proof
category: ramsey-theory
subcategory: induced-ramsey
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Ramsey Theory for Graphs"
chapter_number: 9
pdf_page: 269
section: "9.3 Induced Ramsey theorems"
extraction_confidence: high
aliases:
  - "Deuber's proof"
prerequisites:
  - induced-ramsey-theorem
  - vertex-replacement-operation
related:
  - clique-preserving-ramsey-graph
answers_questions:
  - "How does the first proof of the induced Ramsey theorem work?"
---

# Quick Definition
The first proof constructs Ramsey graphs G^0, ..., G^n by iterated vertex replacement G[U -> G_2], where G_1 = G(H_1, H'_2) and G_2 = G(H'_1, H_2) are inductively obtained Ramsey graphs.

# Core Definition
The proof establishes the formally stronger statement (*): for any H_1, H_2 there exists G = G(H_1, H_2) such that every 2-colouring yields either an induced H_1 in colour 1 or an induced H_2 in colour 2.

Construction: Start with G^0 = G_1. For each induced copy of H'_2 in G^0 (there are n such copies), construct G^i from G^{i-1} by replacing vertices with copies of G_2 = G(H'_1, H_2). Add extra vertices x(F) for each way to select induced copies of H'_1 in all the G_2 copies. The assertion (**) is proved by induction on i. (Diestel, pp. 259-263)

# Prerequisites
- **Induced Ramsey theorem** — This is one proof
- **Vertex replacement** — The G[U -> H] operation

# Key Properties
1. Inductive on |H_1| + |H_2|
2. Uses both deletion (H' = H - x) and neighbour restriction (H'')
3. The constructed graphs grow enormously at each step
4. "Each offers a glimpse of true Ramsey theory"

# Source Reference
Chapter 9, Section 9.3, first proof of Theorem 9.3.1, pages 259-263 (pdf pages 269-273).

# Verification Notes
- Confidence: HIGH — complete proof given
