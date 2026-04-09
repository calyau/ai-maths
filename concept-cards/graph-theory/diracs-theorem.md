---
concept: "Dirac's Theorem"
slug: diracs-theorem
category: hamiltonian-graph-theory
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Hamilton Cycles"
chapter_number: 10
pdf_page: 286
section: "10.1 Simple sufficient conditions"
extraction_confidence: high
aliases:
  - "Dirac 1952"
prerequisites:
  - hamiltonian-graph
  - minimum-degree
extends: []
related:
  - ores-theorem
  - chvatals-theorem
  - seymours-conjecture
contrasts_with: []
answers_questions:
  - "How does the degree sequence relate to Hamiltonicity?"
  - "What is Dirac's theorem?"
---

# Quick Definition
Every graph with n >= 3 vertices and minimum degree at least n/2 has a Hamilton cycle.

# Core Definition
**Theorem 10.1.1 (Dirac 1952).** Every graph with n >= 3 vertices and minimum degree at least n/2 has a Hamilton cycle (Diestel, p. 286).

# Prerequisites
- **Hamiltonian graph** — the conclusion
- **Minimum degree** — delta(G) >= n/2 is the condition

# Key Properties
1. The bound n/2 is best possible: for odd n, two copies of K^{ceil(n/2)} sharing one vertex have delta = floor(n/2) but kappa = 1
2. The high minimum degree ensures connectivity (G must be connected since delta >= n/2)
3. The proof uses a longest path argument with pigeonhole principle
4. Implies Hamiltonicity for delta >= n/2, which also ensures 2-connectedness
5. Subsumed by Ore's theorem and Chvatal's theorem

# Construction / Recognition
## Proof Strategy
1. Let P = x0...xk be a longest path in G
2. All neighbors of x0 and xk lie on P (by maximality)
3. At least n/2 vertices xi have x0*x_{i+1} in E, and n/2 have xi*xk in E
4. By pigeonhole, some xi satisfies both: x0*x_{i+1} and xi*xk are edges
5. Form cycle C = x0*x_{i+1}*P*xk*xi*P*x0
6. If C is not Hamiltonian, G-C has a neighbor on C (by connectedness), giving a longer path

# Context & Application
Dirac's theorem is the foundational sufficient condition for Hamiltonicity. It was the point of departure for a series of increasingly general results (Ore, Posa, Chvatal). The bound n/2 is tight but ensures enough connectivity to guarantee a Hamilton cycle.

Dirac's theorem is the k=1 special case of Seymour's conjecture (p. 299).

# Examples
**Example** (p. 286): For n odd, the graph formed by two copies of K^{ceil(n/2)} sharing one vertex has delta = floor(n/2) < n/2 and is not Hamiltonian (kappa = 1), showing the bound is tight.

**Example** (p. 286, Fig. 10.1.1): The proof construction showing the cycle C formed from the longest path P.

# Relationships
## Builds Upon
- **Hamiltonian graph**, **minimum degree**

## Enables
- **Ore's theorem** — generalizes Dirac
- **Chvatal's theorem** — further generalization
- **Seymour's conjecture** — conjectured generalization to higher powers

## Related
- **Proposition 10.1.2** — alpha(G) <= kappa(G) implies Hamiltonicity

# Common Errors
- **Error**: Applying Dirac's theorem with delta = floor(n/2) instead of n/2
  **Correction**: The condition is delta >= n/2, not delta >= floor(n/2); for odd n the bound n/2 is not an integer and floor(n/2) is insufficient

# Common Confusions
- **Confusion**: Thinking Dirac's theorem is the strongest degree condition for Hamiltonicity
  **Clarification**: Chvatal's theorem (Theorem 10.2.1) is strictly stronger, encompassing Dirac and Ore

# Source Reference
Chapter 10, Section 10.1, Theorem 10.1.1, p. 286 (pdf p. 286).

# Verification Notes
- Theorem and proof from p. 286
- Tightness example from p. 286
- Confidence: HIGH — major named theorem with proof
