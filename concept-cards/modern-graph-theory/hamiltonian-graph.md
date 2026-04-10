---
concept: Hamiltonian Graph
slug: hamiltonian-graph
category: extremal-graph-theory
subcategory: hamilton-theory
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Extremal Problems"
chapter_number: 4
pdf_page: 110
section: "IV.3 Hamilton Paths and Cycles"
extraction_confidence: high
aliases:
  - "Hamilton cycle"
  - "Hamiltonian"
prerequisites: []
extends: []
related:
  - hamilton-path
  - diracs-theorem
  - k-closure
contrasts_with: []
answers_questions:
  - "What is a Hamiltonian graph?"
---

# Quick Definition
A graph is Hamiltonian if it contains a cycle visiting every vertex exactly once (a Hamilton cycle).

# Core Definition
A graph is Hamiltonian if it contains a Hamilton cycle — a cycle of length $n = |G|$. The property of being Hamiltonian is $n$-stable: if $d(x) + d(y) \ge n$ for nonadjacent $x,y$, then $G$ is Hamiltonian iff $G + xy$ is (Bollobás, pp. 113, 127-128).

# Prerequisites
This is a foundational concept with no prerequisites within this source.

# Key Properties
1. Requires $n \ge 3$
2. Dirac's condition: $\delta(G) \ge n/2$ implies Hamiltonian
3. The $n$-closure $C_n(G)$ is Hamiltonian iff $G$ is (Lemma 13)
4. NP-complete to decide in general

# Construction / Recognition
1. Check degree conditions (Dirac, Chvátal, Ore)
2. Compute $k$-closure and check if it is $K_n$
3. If $C_n(G) = K_n$, then $G$ is Hamiltonian

# Context & Application
Hamiltonicity is one of the most studied graph properties. The $k$-closure method provides a systematic approach.

# Examples
**Example** (p. 115): $K_n$ ($n \ge 3$) is Hamiltonian. Graphs with $\delta \ge n/2$ are Hamiltonian.

# Relationships
## Enables
- **diracs-theorem** — $\delta \ge n/2$ suffices
- **k-closure** — Tool for proving Hamiltonicity

## Related
- **hamilton-path** — Path version

# Source Reference
Chapter IV, Sections IV.1 and IV.3, pages 113-128.

# Verification Notes
- Definition source: Direct from pp. 113, 127
- Confidence rationale: Standard definition
- Uncertainties: None
- Cross-reference status: Verified
