---
# === CORE IDENTIFICATION ===
concept: Hamilton Cycles in Random Graphs
slug: hamilton-cycle-random-graph

# === CLASSIFICATION ===
category: random-graphs
subcategory: hamiltonicity
tier: advanced

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Graphs"
chapter_number: 7
pdf_page: 244
section: "VII.4 Hamilton Cycles—The Use of Graph Theoretic Tools"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Posa's theorem on Hamilton cycles

# === TYPED RELATIONSHIPS ===
prerequisites:
  - connectivity-threshold
  - threshold-function
extends: []
related:
  - property-hitting-time
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When does a random graph become Hamiltonian?"
---

# Quick Definition

For $p = c\log n / n$ with $c > 3$, almost every $G_{n,p}$ has a Hamilton path; for $c > 9$, almost every $G_{n,p}$ is Hamiltonian connected. The optimal threshold is $p = (\log n + \log\log n + \omega(n))/n$.

# Core Definition

**Theorem 13** (Posa, Bollobas, p. 245): Let $p = (c\log n)/n$. If $c > 3$ then almost every $G_{n,p}$ contains a Hamilton path from any given $x$ to $y$. If $c > 9$ then almost every $G_{n,p}$ is Hamiltonian connected. **Theorem 14** (Komlos-Szemeredi): The optimal threshold is $p = (\log n + \log\log n \pm \omega(n))/n$. **Theorem 15** (Bollobas, 1983): $\tau(\text{Ham}) = \tau(\delta \ge 2)$ a.s.

# Prerequisites

- **Connectivity threshold** -- Hamiltonicity requires connectivity
- **Threshold function** -- Framework for the result

# Key Properties

1. The proof combines graph-theoretic tools (Posa's rotation-extension) with probabilistic arguments
2. Below the threshold, having a vertex of degree $\le 1$ is the obstruction
3. The hitting time result is the sharpest form: the edge removing the last degree-1 vertex creates a Hamilton cycle
4. A sharper form gives $\lim_{n\to\infty} \mathbb{P}_p(G_{n,p} \text{ is Hamiltonian}) = e^{-e^{-c}}$ for $p = (\log n + \log\log n + c)/n$

# Construction / Recognition

## Proof Strategy (Theorem 13)
1. Show that with high probability, there are no pairs of disjoint sets $(X, Y)$ with $|X| = t$, $|Y| = n - 3t$, and no $X$-$Y$ edge (Lemma 12)
2. Use Posa's rotation-extension technique: if the longest path has $\ell$ endvertices of transforms, the lack of large disjoint sets forces $\ell \ge \gamma n$
3. Independence between path endpoints and vertex $x$ gives $\mathbb{P}(D \cap \overline{E}(W,x)) < n^{-c\gamma}$

# Context & Application

Posa's 1976 breakthrough showed that $O(\log n / n)$ suffices for Hamiltonicity. This combines non-trivial graph theory (rotation-extension) with probability. The optimal threshold $(\log n + \log\log n)/n$ matches the minimum degree 2 threshold.

# Examples

**Example** (p. 245): For $p = (\log n + \log\log n + c)/n$ with fixed $c$, $\mathbb{P}(\text{Hamiltonian}) \to e^{-e^{-c}}$, a double-exponential distribution.

# Relationships

## Builds Upon
- **Connectivity threshold** -- Must be connected first
- **Threshold function** -- Framework

## Enables
- Further study of Hamiltonian properties in random graphs

## Related
- **Property hitting time** -- $\tau(\text{Ham}) = \tau(\delta \ge 2)$ a.s.

## Contrasts With
- None

# Common Errors

- **Error**: Thinking Hamiltonicity threshold equals connectivity threshold
  **Correction**: The thresholds have the same first term ($\log n/n$) but differ in the second: connectivity needs $\log n/n$ while Hamiltonicity needs $(\log n + \log\log n)/n$

# Common Confusions

- **Confusion**: Thinking a probabilistic argument suffices without graph-theoretic tools
  **Clarification**: The proof essentially requires Posa's rotation-extension technique; pure probability does not suffice

# Source Reference

Chapter VII: Random Graphs, Section VII.4, Theorems 13--15, pages 244--246.

# Verification Notes

- Definition source: Theorems 13, 14, 15
- Confidence rationale: Explicit theorems with proofs/statements
- Uncertainties: None
- Cross-reference status: Verified
