---
concept: Longest Path Argument
slug: longest-path-argument
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
  - "longest path technique"
prerequisites:
  - path
  - hamiltonian-graph
extends: []
related:
  - diracs-theorem
  - chvatals-theorem
contrasts_with: []
answers_questions:
  - "How is the longest path argument used to prove Hamiltonicity?"
---

# Quick Definition
The longest path argument is a proof technique: take a longest path P, observe that its endpoints' neighborhoods must lie on P (by maximality), then use degree conditions and pigeonhole to close P into a cycle.

# Core Definition
A common proof technique for Hamiltonicity results: let P = x0...xk be a longest path in G. By maximality, all neighbors of x0 and xk lie on P. The degree conditions then guarantee, via pigeonhole, an index i such that x0*x_{i+1} and xi*xk are both edges, allowing P to be closed into a cycle (Diestel, p. 286, proof of Theorem 10.1.1).

# Prerequisites
- **Path** — the longest path is the starting point
- **Hamiltonian graph** — the argument proves Hamiltonicity

# Key Properties
1. Start with a longest path P = x0...xk
2. By maximality: N(x0) and N(xk) are subsets of V(P)
3. Pigeonhole: at least delta vertices among x0,...,x_{k-1} are in both "shifts"
4. Find i with x0*x_{i+1} and xi*xk edges
5. Close into cycle C; if C is not Hamiltonian, use connectivity to find a longer path (contradiction)

# Context & Application
This technique is used in the proofs of Dirac's theorem and Chvatal's theorem. It is the standard approach to proving degree-based sufficient conditions for Hamiltonicity.

# Examples
**Example** (p. 286, Fig. 10.1.1): The proof of Dirac's theorem shows the cycle C = x0*x_{i+1}*P*xk*xi*P*x0 formed from the longest path.

# Relationships
## Related
- **Dirac's theorem** — proved by this technique
- **Chvatal's theorem** — uses a variation (edge-maximal non-Hamiltonian graph + longest path)

# Source Reference
Chapter 10, Section 10.1, Theorem 10.1.1, p. 286 (pdf p. 286).

# Verification Notes
- From proof of Theorem 10.1.1
- Confidence: HIGH — explicitly used proof technique
