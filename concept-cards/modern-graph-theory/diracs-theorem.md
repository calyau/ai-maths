---
concept: "Dirac's Theorem"
slug: diracs-theorem
category: extremal-graph-theory
subcategory: hamilton-theory
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Extremal Problems"
chapter_number: 4
pdf_page: 110
section: "IV.1 Paths and Cycles"
extraction_confidence: high
aliases:
  - "Dirac 1952"
prerequisites:
  - degree-sum-path-cycle-theorem
extends: []
related:
  - hamilton-cycle
  - chvatals-theorem
contrasts_with: []
answers_questions:
  - "When is a graph Hamiltonian?"
---

# Quick Definition
Every graph of order $n \ge 3$ and minimum degree at least $n/2$ is Hamiltonian.

# Core Definition
Dirac's theorem (1952): every graph of order $n \ge 3$ and minimal degree at least $n/2$ is Hamiltonian. This is a special case of Theorem 2 with $k = n$ (Bollobás, p. 115).

# Prerequisites
- **Degree-sum path and cycle theorem** — Dirac's theorem is a corollary

# Key Properties
1. The minimum degree bound $n/2$ is best possible (consider two disjoint copies of $K_{n/2}$)
2. Contained in Theorem 2 as the case where $d(x) + d(y) \ge n$ for all nonadjacent pairs

# Construction / Recognition
1. Check $\delta(G) \ge n/2$
2. If so, $G$ is Hamiltonian

# Context & Application
Dirac's theorem is "a fundamental theorem" (p. 113) that initiated the study of degree conditions for Hamiltonicity.

# Examples
**Example**: $K_{n/2, n/2}$ has minimum degree $n/2$ and is Hamiltonian.

# Relationships
## Builds Upon
- **degree-sum-path-cycle-theorem** — Dirac's theorem is a corollary

## Related
- **chvatals-theorem** — A stronger degree-sequence condition

# Source Reference
Chapter IV, Section IV.1, page 115.

# Verification Notes
- Definition source: Direct from p. 115
- Confidence rationale: Explicitly stated as corollary
- Uncertainties: None
- Cross-reference status: Verified
