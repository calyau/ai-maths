---
concept: Pigeonhole Principle in Hamiltonicity
slug: pigeonhole-in-hamiltonicity
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
aliases: []
prerequisites:
  - diracs-theorem
extends: []
related:
  - chvatals-theorem
  - longest-path-argument
contrasts_with: []
answers_questions:
  - "How is the pigeonhole principle used in Hamiltonicity proofs?"
---

# Quick Definition
In the proof of Dirac's theorem, the pigeonhole principle guarantees that among the k < n vertices x0, ..., x_{k-1}, at least one xi satisfies both x0*x_{i+1} in E and xi*xk in E, enabling the closure of a path into a cycle.

# Core Definition
In the proof of Theorem 10.1.1 (Dirac), at least n/2 vertices among x0, ..., x_{k-1} are such that xi*xk is an edge, and at least n/2 are such that x0*x_{i+1} is an edge. Since k < n, the pigeonhole principle gives an i with both properties (Diestel, p. 286).

# Prerequisites
- **Dirac's theorem** — the main application

# Key Properties
1. Applied to the vertices of a longest path P
2. Two sets of indices each have size >= n/2
3. Both lie in {0, ..., k-1} with k < n
4. Their intersection is non-empty by pigeonhole
5. The resulting index i gives the cycle closure

# Context & Application
The pigeonhole principle is the simple but crucial step that turns degree conditions into cycle existence. It is used in the proofs of both Dirac's and Chvatal's theorems.

# Examples
**Example** (p. 286): In Dirac's proof, I = {i : x0*x_{i+1} in E} and J = {j : xj*xk in E} both have size >= n/2 and lie in {0,...,k-1}. Since k < n: |I| + |J| >= n > k, so I intersect J is non-empty.

# Relationships
## Related
- **Dirac's theorem** — uses pigeonhole
- **Chvatal's theorem** — similar argument
- **Longest path argument** — the context for pigeonhole application

# Source Reference
Chapter 10, Section 10.1, p. 286 (pdf p. 286).

# Verification Notes
- From proof of Theorem 10.1.1
- Confidence: HIGH — explicitly used
