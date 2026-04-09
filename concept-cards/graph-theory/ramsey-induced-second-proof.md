---
concept: "Second Proof of Induced Ramsey Theorem (Nesetril-Rodl)"
slug: ramsey-induced-second-proof
category: ramsey-theory
subcategory: induced-ramsey
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Ramsey Theory for Graphs"
chapter_number: 9
pdf_page: 276
section: "9.3 Induced Ramsey theorems"
extraction_confidence: high
aliases:
  - "Nesetril-Rodl proof"
  - "partite construction"
prerequisites:
  - induced-ramsey-theorem
  - bipartite-ramsey-lemma
  - clique-preserving-ramsey-graph
related:
  - ramsey-induced-first-proof
answers_questions:
  - "How does the second proof preserve clique number?"
---

# Quick Definition
The second proof constructs an n-partite graph G by iterating the bipartite Ramsey lemma over all edge pairs of K^n, preserving omega(G) = omega(H).

# Core Definition
Start with G^0 having n = R(r) rows, each containing C(n,r) vertices arranged as copies of H. For each edge e_k of K^n, construct G^{k+1} from G^k by applying the bipartite Ramsey lemma to the bipartite subgraph between the two relevant rows. The final G = G^m satisfies: any 2-colouring has an induced G^0 in G that is monochromatic between each pair of rows; projecting to K^n gives a monochromatic K^r, inside which lies a monochromatic induced H. (Diestel, pp. 266-268)

# Prerequisites
- **Induced Ramsey theorem** — This is the second proof
- **Bipartite Ramsey lemma** — Applied iteratively to pairs of rows
- **Clique-preserving Ramsey graph** — The key feature of this construction

# Key Properties
1. Preserves omega(G) = omega(H)
2. Uses bipartite Ramsey iteration over C(n,2) pairs
3. The construction is explicit but enormous
4. Reduces general problem to bipartite case (Lemma 9.3.3)

# Source Reference
Chapter 9, Section 9.3, second proof of Theorem 9.3.1, pages 266-268 (pdf pages 276-278).

# Verification Notes
- Confidence: HIGH — complete proof given
