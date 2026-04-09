---
concept: Thomas-Wollan Theorem
slug: thomas-wollan-theorem
category: connectivity
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Connectivity"
chapter_number: 3
pdf_page: 81
section: "3.5 Linking pairs of vertices"
extraction_confidence: high
aliases:
  - "Thomas & Wollan 2005"
  - "linear linkedness theorem"
prerequisites:
  - k-linked-graph
  - mengers-theorem
extends:
  - linkedness-theorem
related: []
contrasts_with: []
answers_questions:
  - "What is the best connectivity bound for k-linkedness?"
---

# Quick Definition
If a graph G is 2k-connected and has average degree epsilon(G) >= 8k, then G is k-linked.

# Core Definition
**Theorem 3.5.3 (Thomas & Wollan 2005).** Let G be a graph and k in N. If G is 2k-connected and epsilon(G) >= 8k, then G is k-linked (Diestel, p. 81).

# Prerequisites
- **k-linked graph** — the conclusion
- **Menger's theorem** — used in the proof

# Key Properties
1. Linear bound: 2k-connectivity plus epsilon >= 8k suffices for k-linkedness
2. Since 2*epsilon(G) >= delta(G) >= kappa(G), the condition kappa(G) >= 16k implies k-linkedness
3. The proof is involved, using induction on |G| and ||V\X||^+
4. Uses the concept of "light" and "heavy" vertex sets
5. Constructs a k-linked subgraph via Lemma 3.5.4

# Construction / Recognition
## Proof Key Ideas
1. Show linked X-separations can be handled by induction
2. Use edge contraction to ensure large minimum degree (>= 8k)
3. Show degree is bounded above (<= 16k-1) by edge deletion arguments
4. Find a vertex v0 of minimum degree; its neighborhood has a k-linked subgraph

# Context & Application
The Thomas-Wollan theorem is the strongest known result on connectivity forcing k-linkedness. It improves the exponential bound of Theorem 3.5.2 to a linear one, showing that the fundamental barrier to k-linkedness is really just linear connectivity.

# Examples
**Example**: A 32-connected graph with epsilon >= 16 is 2-linked. A 160-connected graph with epsilon >= 80 is 10-linked.

# Relationships
## Builds Upon
- **k-linked graph**, **Menger's theorem**

## Enables
- Linear bound for topological minor existence (Theorem 7.2.1)

# Source Reference
Chapter 3, Section 3.5, Theorem 3.5.3, pp. 81-87 (pdf pp. 81-87).

# Verification Notes
- Theorem from p. 81
- Detailed proof spanning pp. 81-87
- Confidence: HIGH — major theorem with complete proof
