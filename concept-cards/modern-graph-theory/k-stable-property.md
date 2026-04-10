---
concept: k-Stable Property
slug: k-stable-property
category: extremal-graph-theory
subcategory: graph-properties
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Extremal Problems"
chapter_number: 4
pdf_page: 110
section: "IV.3 Hamilton Paths and Cycles"
extraction_confidence: high
aliases:
  - "k-stability"
prerequisites:
  - monotone-property
extends: []
related:
  - k-closure
  - hamiltonian-graph
contrasts_with: []
answers_questions:
  - "What is a k-stable property?"
---

# Quick Definition
A property $\mathcal{P}$ of graphs of order $n$ is $k$-stable if for any graph $G$ and nonadjacent vertices $x,y$ with $d(x)+d(y) \ge k$, $G$ has property $\mathcal{P}$ iff $G + xy$ does.

# Core Definition
Let $n$ and $k$ be natural numbers and $\mathcal{P}$ a class of graphs of order $n$. We say $\mathcal{P}$ is $k$-stable if whenever $G$ is a graph of order $n$ and $x,y$ are nonadjacent with $d(x)+d(y) \ge k$, then $G$ has property $\mathcal{P}$ iff $G^+ = G + xy$ has it also (Bollobás, p. 128).

# Prerequisites
- **Monotone property** — Stability refines monotonicity

# Key Properties
1. Being Hamiltonian is $n$-stable
2. Having a Hamilton path is $(n-1)$-stable
3. $k$-stability enables the $k$-closure approach

# Context & Application
The $k$-stability principle: $G$ has property $\mathcal{P}$ iff $C_k(G)$ does. This reduces checking $\mathcal{P}$ to checking it for the closure.

# Examples
**Example** (p. 128): Theorem 2 shows Hamiltonicity is $n$-stable: adding an edge between vertices with degree sum $\ge n$ preserves Hamiltonicity status.

# Relationships
## Builds Upon
- **monotone-property** — Stability applies to monotone properties

## Enables
- **k-closure** — The closure operation leveraging stability

# Source Reference
Chapter IV, Section IV.3, page 128.

# Verification Notes
- Definition source: Direct from p. 128
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
