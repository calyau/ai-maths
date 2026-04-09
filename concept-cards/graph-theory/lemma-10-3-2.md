---
concept: Path Rearrangement Lemma
slug: lemma-10-3-2
category: hamiltonian-graph-theory
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Hamilton Cycles"
chapter_number: 10
pdf_page: 291
section: "10.3 Hamilton cycles in the square of a graph"
extraction_confidence: high
aliases:
  - "Lemma 10.3.2"
prerequisites:
  - square-of-a-graph
  - path
extends: []
related:
  - fleischners-theorem
contrasts_with: []
answers_questions:
  - "How are paths rearranged in P^2 for Fleischner's theorem?"
---

# Quick Definition
Lemma 10.3.2 shows how to rearrange a path P in P^2 to create paths that bridge every internal vertex, enabling the construction of Hamilton cycles in G^2.

# Core Definition
**Lemma 10.3.2.** Let P = v0...vk be a path (k >= 1), and let G be obtained from P by adding vertices u, w with edges uv1 and wvk. Then: (i) P^2 contains a v0-v1 path Q visiting all of V(P) with bridging properties. (ii) G^2 contains disjoint paths Q and Q' from v0 to vk and from u to w, covering all of V(G) (Diestel, p. 291).

# Prerequisites
- **Square of a graph** — the lemma works in P^2 and G^2
- **Path** — the basic structure being rearranged

# Key Properties
1. Part (i): a Hamiltonian path of P in P^2 that bridges every internal vertex
2. Part (ii): two disjoint paths in G^2 covering all vertices
3. The construction depends on whether k is even or odd
4. Key technical lemma for the proof of Fleischner's theorem

# Construction / Recognition
## Part (i) Construction
- If k even: Q = v0 v2 ... v_{k-2} vk v_{k-1} v_{k-3} ... v3 v1
- If k odd: Q = v0 v2 ... v_{k-1} vk v_{k-2} ... v3 v1

# Context & Application
This lemma provides the path rearrangement technique needed in the proof of Fleischner's theorem to handle intervals of type 2 and type 3.

# Examples
**Example** (p. 291): For k=4 (even), Q = v0 v2 v4 v3 v1, which visits all vertices and bridges v1, v2, v3.

# Relationships
## Related
- **Fleischner's theorem** — uses this lemma for interval modifications

# Source Reference
Chapter 10, Section 10.3, Lemma 10.3.2, pp. 291-292 (pdf pp. 291-292).

# Verification Notes
- Lemma from p. 291
- Confidence: HIGH — explicitly stated with proof
