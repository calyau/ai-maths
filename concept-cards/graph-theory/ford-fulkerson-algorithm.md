---
concept: Ford-Fulkerson Algorithm
slug: ford-fulkerson-algorithm
category: network-flows
subcategory: network-flows
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Flows"
chapter_number: 6
pdf_page: 153
section: "6.2 Flows in networks"
extraction_confidence: high
aliases:
  - "augmenting path algorithm"
prerequisites:
  - flow-in-network
  - augmenting-path
  - max-flow-min-cut-theorem
related:
  - integral-flow-theorem
answers_questions:
  - "How does the Ford-Fulkerson algorithm find a maximum flow?"
---

# Quick Definition
The Ford-Fulkerson algorithm finds a maximum flow by repeatedly identifying augmenting paths from source to sink and pushing flow along them until no more augmenting paths exist.

# Core Definition
The algorithm from the proof of Theorem 6.2.2:
1. Initialize f_0 := 0 (zero flow on all edges)
2. Compute S_n = set of vertices reachable from s via edges with residual capacity
3. If t in S_n: find s-t walk W, compute epsilon = min residual capacity, augment flow along W
4. If t not in S_n: stop; (S_n, S_n-bar) is a minimum cut and f_n is a maximum flow

Each augmentation increases |f| by at least 1 (for integral capacities), so the algorithm terminates after at most c(S, S-bar) steps. (Diestel, pp. 143-144)

# Prerequisites
- **Flow in network** — The algorithm operates on network flows
- **Augmenting path** — The mechanism for increasing flow
- **Max-flow min-cut theorem** — The algorithm proves this theorem

# Key Properties
1. Always terminates for integral capacities
2. Produces an integral maximum flow
3. Running time depends on path selection strategy
4. If augmenting paths are chosen as short as possible, the number is bounded by network size

# Construction / Recognition
## Algorithm Steps
1. Start with zero flow
2. Find augmenting s-t path with positive residual capacity
3. Push flow along path (amount = minimum residual capacity)
4. Repeat until no augmenting path exists
5. The set of reachable vertices from s gives the minimum cut

# Source Reference
Chapter 6, Section 6.2, proof of Theorem 6.2.2, pages 143-144 (pdf pages 153-154).

# Verification Notes
- Confidence: HIGH — algorithm extracted from the constructive proof
