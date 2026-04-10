---
concept: k-Closure
slug: k-closure
category: extremal-graph-theory
subcategory: hamilton-theory
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
  - "C_k(G)"
  - "Bondy-Chvátal closure"
prerequisites:
  - k-stable-property
extends: []
related:
  - hamiltonian-graph
  - chvatals-theorem
contrasts_with: []
answers_questions:
  - "How does the closure method help determine Hamiltonicity?"
---

# Quick Definition
The $k$-closure $C_k(G)$ is the unique minimal supergraph of $G$ where every pair of nonadjacent vertices has degree sum at most $k-1$.

# Core Definition
For every graph $G$ of order $n$ there is a unique minimal graph $G^* = C_k(G)$ containing $G$ such that $d_{G^*}(x) + d_{G^*}(y) \le k-1$ for $xy \notin E(G^*)$. By the stability principle: if $\mathcal{P}$ is $k$-stable, then $G$ has property $\mathcal{P}$ iff $C_k(G)$ does (Bollobás, p. 128).

# Prerequisites
- **k-stable property** — The closure leverages stability

# Key Properties
1. $C_k(G)$ is unique
2. Obtained by repeatedly adding edges between nonadjacent vertices with degree sum $\ge k$
3. $G$ is Hamiltonian iff $C_n(G)$ is (Lemma 13)
4. $G$ has a Hamilton path iff $C_{n-1}(G)$ does (Lemma 13)
5. If $C_n(G) = K_n$, then $G$ is Hamiltonian

# Construction / Recognition
1. Find nonadjacent $x,y$ with $d(x)+d(y) \ge k$
2. Add edge $xy$
3. Repeat until no such pair exists
4. The result is $C_k(G)$

# Context & Application
The $k$-closure provides a powerful framework for proving Hamiltonicity results. It unifies Dirac's theorem, Ore's theorem, and leads to Chvátal's theorem.

# Examples
**Example** (p. 128): If $d(x)+d(y) \ge n$ for all nonadjacent pairs, then $C_n(G) = K_n$, so $G$ is Hamiltonian (Dirac's theorem as a special case).

# Relationships
## Builds Upon
- **k-stable-property** — The theoretical foundation

## Enables
- **chvatals-theorem** — Corollary 16

# Source Reference
Chapter IV, Section IV.3, pages 128-129. Lemma 13.

# Verification Notes
- Definition source: Direct from p. 128
- Confidence rationale: Explicitly defined with uniqueness
- Uncertainties: None
- Cross-reference status: Verified
