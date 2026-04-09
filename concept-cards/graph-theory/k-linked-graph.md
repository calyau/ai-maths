---
concept: k-Linked Graph
slug: k-linked-graph
category: connectivity
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Connectivity"
chapter_number: 3
pdf_page: 80
section: "3.5 Linking pairs of vertices"
extraction_confidence: high
aliases:
  - "k-linked"
prerequisites:
  - k-connected-graph
  - path
extends:
  - k-connected-graph
related:
  - topological-minor
  - mengers-theorem
contrasts_with: []
answers_questions:
  - "What is a k-linked graph?"
---

# Quick Definition
A graph G is k-linked if |G| >= 2k and for any 2k distinct vertices s1, ..., sk, t1, ..., tk, there exist disjoint paths Pi = si...ti for i = 1, ..., k.

# Core Definition
If |G| >= 2k and every set of at most 2k vertices is linked in G (meaning specified pairs can be connected by disjoint paths), then G is **k-linked** (Diestel, p. 80).

# Prerequisites
- **k-connected graph** — k-linked implies k-connected; high connectivity forces k-linkedness
- **Path** — the linking is by disjoint paths

# Key Properties
1. k-linked graphs are k-connected (and in fact (2k-1)-connected, Exercise 22)
2. Much stronger than k-connectivity: we specify which pairs to connect
3. Unlike Menger's theorem, we don't just want disjoint A-B paths; we want specific pairings
4. Every f(k)-connected graph is k-linked for some function f (Theorem 3.5.2)
5. f(k) can be chosen linearly: 2k-connected with epsilon(G) >= 8k suffices (Theorem 3.5.3)

# Construction / Recognition
## To Verify k-Linkedness
1. For every choice of 2k distinct vertices s1, ..., sk, t1, ..., tk
2. Find vertex-disjoint paths Pi from si to ti
3. If this succeeds for all choices, G is k-linked

# Context & Application
k-linkedness is a strong structural property that goes beyond mere connectivity. It asks not just for disjoint paths between two sets, but for paths with prescribed pairings. The main results of Section 3.5 show that high connectivity forces k-linkedness.

# Examples
**Example**: Complete graphs K_n are k-linked for k <= n/2. Every 10k-connected graph is k-linked (Theorem 3.5.2 with a specific function).

# Relationships
## Builds Upon
- **k-connected graph**

## Related
- **Topological minor** — k-linked graphs contain subdivisions of large complete graphs
- **Menger's theorem** — used in proofs about k-linked graphs

# Common Errors
- **Error**: Thinking k-connected implies k-linked
  **Correction**: k-linked is much stronger; high connectivity (roughly 10k or more) is needed

# Common Confusions
- **Confusion**: Confusing k-linked with k-connected
  **Clarification**: k-connected guarantees disjoint paths between any two vertices; k-linked guarantees simultaneous disjoint paths between k specified pairs

# Source Reference
Chapter 3, Section 3.5, pp. 80-87 (pdf pp. 80-87).

# Verification Notes
- Definition from p. 80
- Confidence: HIGH — explicitly defined
