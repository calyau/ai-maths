---
concept: "Seymour's Conjecture"
slug: seymours-conjecture
category: hamiltonian-graph-theory
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Hamilton Cycles"
chapter_number: 10
pdf_page: 299
section: "10.3 Hamilton cycles in the square of a graph"
extraction_confidence: high
aliases:
  - "Seymour 1974"
prerequisites:
  - diracs-theorem
  - square-of-a-graph
  - hamiltonian-graph
extends:
  - diracs-theorem
related:
  - fleischners-theorem
contrasts_with: []
answers_questions:
  - "Does high minimum degree force a Hamilton cycle whose power lies in G?"
---

# Quick Definition
Seymour's conjecture states that if delta(G) >= kn/(k+1) for a positive integer k, then G has a Hamilton cycle H such that H^k is a subgraph of G.

# Core Definition
**Conjecture (Seymour 1974).** Let G be a graph of order n >= 3, and let k be a positive integer. If G has minimum degree delta(G) >= kn/(k+1), then G has a Hamilton cycle H such that H^k is a subgraph of G (Diestel, p. 299).

# Prerequisites
- **Dirac's theorem** — the k=1 case
- **Square of a graph** — H^k is the k-th power of the Hamilton cycle
- **Hamiltonian graph** — the conclusion

# Key Properties
1. For k=1, this is exactly Dirac's theorem (delta >= n/2)
2. Proved for large enough n (depending on k) by Komlos, Sarkozy, Szemeredi (1998)
3. The conjecture asks for H^k (the k-th power of a Hamilton cycle) to be a subgraph of G
4. A far-reaching generalization of Dirac's theorem

# Context & Application
Seymour's conjecture extends Dirac's theorem to higher-order Hamiltonian structure. Instead of just finding a Hamilton cycle, it asks for a Hamilton cycle whose k-th power lies in G, requiring more edges and higher minimum degree.

# Examples
**Example**: For k=2, the conjecture says delta >= 2n/3 implies G contains the square of a Hamilton cycle. For k=1, delta >= n/2 implies G contains a Hamilton cycle.

# Relationships
## Builds Upon
- **Dirac's theorem** — the k=1 case

## Related
- **Fleischner's theorem** — related to graph powers and Hamiltonicity

# Source Reference
Chapter 10, Section 10.3, p. 299 (pdf p. 299).

# Verification Notes
- Conjecture from p. 299
- Proved for large n by Komlos, Sarkozy, Szemeredi
- Confidence: HIGH — explicitly stated
