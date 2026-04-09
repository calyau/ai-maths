---
concept: "Chvatal-Erdos Theorem"
slug: chvatal-erdos-theorem
category: hamiltonian-graph-theory
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Hamilton Cycles"
chapter_number: 10
pdf_page: 287
section: "10.1 Simple sufficient conditions"
extraction_confidence: high
aliases:
  - "Chvatal & Erdos 1972"
  - "alpha <= kappa implies Hamiltonian"
prerequisites:
  - hamiltonian-graph
  - independent-set
  - connectivity
extends: []
related:
  - diracs-theorem
  - mengers-theorem
contrasts_with: []
answers_questions:
  - "When does alpha(G) <= kappa(G) imply Hamiltonicity?"
---

# Quick Definition
Every graph G with |G| >= 3 and alpha(G) <= kappa(G) has a Hamilton cycle.

# Core Definition
**Proposition 10.1.2.** Every graph G with |G| >= 3 and alpha(G) <= kappa(G) has a Hamilton cycle (Diestel, p. 287).

# Prerequisites
- **Hamiltonian graph** — the conclusion
- **Independent set** — alpha(G) = independence number
- **Connectivity** — kappa(G) = vertex connectivity

# Key Properties
1. The condition alpha(G) <= kappa(G) forces Hamiltonicity
2. The proof uses Menger's theorem (fan version, Corollary 3.3.4)
3. Assumes the existence of a longest cycle C and shows it must be Hamiltonian
4. If C is not Hamiltonian, a vertex v outside C has a v-C fan of size >= k
5. The fan creates an independent set of size k+1, contradicting alpha <= k

# Construction / Recognition
## Proof Strategy
1. Let kappa(G) = k and C be a longest cycle
2. If C is not Hamiltonian, pick v in G-C
3. Find a v-C fan F of size >= min{k, |C|} by Menger's theorem
4. Show consecutive fan endpoints are not possible (would give a longer cycle)
5. Show the set {v_{i+1} : i in I} union {v} is independent of size >= k+1
6. Contradiction with alpha(G) <= k

# Context & Application
This theorem connects two fundamental graph parameters: independence number and connectivity. It shows that when the graph has few independent vertices relative to its connectivity, it must be Hamiltonian.

# Examples
**Example** (p. 287): The proof uses fan F = {Pi : i in I} where each Pi ends at vi on C. Since no two consecutive vertices of C are fan endpoints, the successors form an independent set.

# Relationships
## Builds Upon
- **Hamiltonian graph**, **independent set**, **connectivity**

## Related
- **Dirac's theorem** — a special case (delta >= n/2 implies alpha <= n/2 <= kappa)
- **Menger's theorem** — fan version used in proof

# Source Reference
Chapter 10, Section 10.1, Proposition 10.1.2, pp. 287-288 (pdf pp. 287-288).

# Verification Notes
- From p. 287
- Confidence: HIGH — explicit proposition with proof
