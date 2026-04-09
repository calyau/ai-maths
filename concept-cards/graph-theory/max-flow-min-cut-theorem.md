---
concept: Max-Flow Min-Cut Theorem
slug: max-flow-min-cut-theorem
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
  - "Ford-Fulkerson theorem"
  - "MFMC theorem"
prerequisites:
  - flow-in-network
  - cut-in-network
  - cut-capacity
  - total-flow-value
related:
  - integral-flow-theorem
  - augmenting-path
  - menger-theorem-flow-version
answers_questions:
  - "How does the max-flow relate to the min-cut?"
  - "What is the max-flow min-cut theorem?"
---

# Quick Definition
In every network, the maximum total value of a flow equals the minimum capacity of a cut.

# Core Definition
**Theorem 6.2.2** (Ford & Fulkerson 1956): In every network, the maximum total value of a flow equals the minimum capacity of a cut.

The proof constructs a sequence f_0, f_1, f_2, ... of integral flows of strictly increasing total value. Starting from the zero flow, at each step an augmenting s-t walk W is found with residual capacity epsilon > 0, and flow is pushed along W. When no augmenting walk exists, the set S_n of vertices reachable from s via edges with residual capacity forms a cut (S_n, S_n-bar) with capacity exactly |f_n|. (Diestel, p. 142-144)

# Prerequisites
- **Flow in network** — The theorem characterizes maximum flows
- **Cut in network** — The theorem characterizes minimum cuts
- **Cut capacity** — The minimum cut capacity equals the maximum flow
- **Total flow value** — The quantity being maximized

# Key Properties
1. max |f| = min c(S, S-bar) over all flows f and cuts (S, S-bar)
2. The proof is constructive: the Ford-Fulkerson algorithm finds both the maximum flow and minimum cut
3. The maximum flow is achieved by an integral flow when capacities are integral (Corollary 6.2.3)
4. Implies Menger's theorem without much difficulty (Exercise 3)

# Construction / Recognition
## Ford-Fulkerson Algorithm
1. Start with the zero flow f_0
2. Find the set S_n of vertices reachable from s via edges with residual capacity
3. If t is in S_n, find an s-t walk W through such edges
4. Compute epsilon = min residual capacity along W
5. Augment: push epsilon units of flow along W to get f_{n+1}
6. If t is not in S_n, stop: (S_n, S_n-bar) is a minimum cut and f_n is a maximum flow

# Context & Application
The max-flow min-cut theorem is one of the most important results in combinatorial optimization. It provides the theoretical foundation for network flow algorithms and implies fundamental results in connectivity (Menger's theorem) and matching theory. Diestel calls it a "classic result" and notes that it "indicates some of the natural power lying in this approach."

# Examples
**Example** (p. 143, Fig. 6.2.2): An augmenting path W with increment epsilon = 2, starting from constant flow f_n = 0 with capacities c = 3.

# Relationships
## Builds Upon
- **Flow in network**, **Cut in network**, **Total flow value**, **Cut capacity**

## Enables
- **Integral flow theorem** — A corollary: integral capacities yield integral maximum flows
- **Menger's theorem (flow version)** — Can be derived from max-flow min-cut

## Related
- **Augmenting path** — The constructive proof uses augmenting paths

# Common Errors
- **Error**: Assuming the algorithm always terminates for non-integer capacities
  **Correction**: The Ford-Fulkerson algorithm as stated requires integral capacities for guaranteed termination; with real capacities, convergence is not guaranteed without careful path selection

# Common Confusions
- **Confusion**: Thinking the maximum flow is unique
  **Clarification**: The maximum flow VALUE is unique, but there may be multiple distinct flows achieving it

# Source Reference
Chapter 6: Flows, Section 6.2, Theorem 6.2.2, pages 142-144 (pdf pages 152-154).

# Verification Notes
- Theorem statement: Directly quoted from p. 142-143
- Proof method: Summarized from the constructive proof on pp. 143-144
- Confidence: HIGH — the central theorem of the section, fully proved
