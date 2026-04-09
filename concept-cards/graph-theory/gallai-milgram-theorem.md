---
concept: Gallai-Milgram Theorem
slug: gallai-milgram-theorem
category: matching-and-covering
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Matching, Covering and Packing"
chapter_number: 2
pdf_page: 60
section: "2.5 Path covers"
extraction_confidence: high
aliases:
  - "Gallai & Milgram 1960"
  - "path cover theorem"
prerequisites:
  - path-cover
  - independent-set
extends: []
related:
  - dilworths-theorem
  - konigs-theorem
contrasts_with: []
answers_questions:
  - "How many directed paths are needed to cover all vertices?"
---

# Quick Definition
Every directed graph G has a path cover P and an independent set of representatives {v_P : P in P} with v_P in P for every P.

# Core Definition
**Theorem 2.5.1 (Gallai & Milgram 1960).** Every directed graph G has a path cover P and an independent set {v_P | P in P} of vertices such that v_P is in P for every P in P (Diestel, p. 60).

# Prerequisites
- **Path cover** — the theorem produces a path cover
- **Independent set** — the cover has independent representatives

# Key Properties
1. The path cover P has an independent set of representatives (one per path)
2. This implies |P| <= alpha(G) (independence number)
3. Hence the minimum path cover size <= alpha(G)
4. The proof is by induction on |G|, using minimality of terminal vertices
5. Implies Dilworth's theorem for partial orders

# Construction / Recognition
## Proof Strategy
1. Start with a path cover P with minimum terminal vertex set ter(P)
2. If ter(P) is independent, we are done
3. Otherwise, use an edge between terminal vertices to modify P
4. Apply induction to a smaller graph G' = G - v1

# Context & Application
The Gallai-Milgram theorem connects directed graph structure to independent sets. Its main corollary is Dilworth's theorem for partial orders.

# Examples
**Example** (p. 60-61, Fig. 2.5.1): The path cover P = {P1, ..., Pm} is modified when two terminal vertices are connected. The induction removes one vertex and works with a smaller path cover.

# Relationships
## Builds Upon
- **Path cover**, **independent set**

## Enables
- **Dilworth's theorem** — minimum chain cover = maximum antichain

## Related
- **Konig's theorem** — special case for bipartite matchings

# Common Errors
- **Error**: Assuming the path cover must be of minimum size
  **Correction**: The theorem produces a path cover whose size is bounded by alpha(G), but it may not be minimum

# Common Confusions
- **Confusion**: Confusing this with the Gallai-Edmonds matching theorem
  **Clarification**: Gallai-Milgram is about directed path covers; Gallai-Edmonds is about matching structure

# Source Reference
Chapter 2, Section 2.5, Theorem 2.5.1, pp. 60-61 (pdf pp. 60-61).

# Verification Notes
- Theorem from p. 60
- Proof from pp. 60-61
- Confidence: HIGH — named theorem with full proof
