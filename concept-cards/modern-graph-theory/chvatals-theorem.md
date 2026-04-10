---
concept: "Chvátal's Theorem"
slug: chvatals-theorem
category: extremal-graph-theory
subcategory: hamilton-theory
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Extremal Problems"
chapter_number: 4
pdf_page: 110
section: "IV.3 Hamilton Paths and Cycles"
extraction_confidence: high
aliases:
  - "Corollary 16"
  - "Chvátal's degree sequence condition"
prerequisites:
  - k-closure
  - hamiltonian-graph
extends:
  - diracs-theorem
related:
  - bondy-chvatal-theorem
contrasts_with: []
answers_questions:
  - "What degree sequence conditions guarantee a Hamilton cycle?"
---

# Quick Definition
If the degree sequence $d_1 \le \cdots \le d_n$ satisfies: whenever $d_k \le k < n/2$, then $d_{n-k} \ge n-k$, then the graph is Hamiltonian.

# Core Definition
**Corollary 16** (Chvátal): Let $G$ have degree sequence $d_1 \le d_2 \le \cdots \le d_n$, $n \ge 3$. Suppose $d_{n-k} \ge n-k$ whenever $d_k \le k < n/2$. Then $G$ has a Hamilton cycle. The analogous condition with $\varepsilon = 1$ gives a Hamilton path (Bollobás, pp. 130-131).

# Prerequisites
- **k-closure** — The theorem follows from closure analysis
- **Hamiltonian graph** — The property being established

# Key Properties
1. Subsumes Dirac's theorem (if $\delta \ge n/2$, the condition is trivially satisfied)
2. The condition is best possible in a strong sense (Exercise 32-33)
3. Works via the Bondy-Chvátal closure

# Construction / Recognition
1. Sort degree sequence
2. Check: for each $k$ with $d_k \le k < n/2$, verify $d_{n-k} \ge n-k$
3. If all checks pass, the graph is Hamiltonian

# Context & Application
Chvátal's theorem provides the most general degree-sequence condition for Hamiltonicity.

# Examples
**Example**: If $d_1 \ge n/2$, then the condition is vacuous (no $k$ satisfies $d_k \le k < n/2$), recovering Dirac's theorem.

# Relationships
## Builds Upon
- **k-closure** — Derived from closure theory

## Extends
- **diracs-theorem** — Generalized

# Source Reference
Chapter IV, Section IV.3, pages 130-131. Corollary 16.

# Verification Notes
- Definition source: Direct from p. 131
- Confidence rationale: Explicitly stated
- Uncertainties: None
- Cross-reference status: Verified
