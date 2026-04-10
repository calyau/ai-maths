---
concept: Bondy-Chvátal Theorem
slug: bondy-chvatal-theorem
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
  - "Theorem 15"
prerequisites:
  - k-closure
  - hamiltonian-graph
extends:
  - diracs-theorem
related:
  - chvatals-theorem
contrasts_with: []
answers_questions:
  - "What is the Bondy-Chvátal closure theorem?"
---

# Quick Definition
If no pair of nonadjacent vertices $x_i, x_j$ satisfies certain degree conditions (involving $d(x_i) + d(x_j) \le n - 1 - \varepsilon$ and positional constraints), then $G$ has a Hamilton cycle ($\varepsilon = 0$) or Hamilton path ($\varepsilon = 1$).

# Core Definition
**Theorem 15** (Bondy-Chvátal): Let $G$ have order $n \ge 3$ with $\varepsilon = 0$ or $1$. If no indices $i, j$ with $i < j$ satisfy $x_ix_j \notin E(G)$, $j \ge n - i + \varepsilon$, $d(x_i) \le i - \varepsilon$, $d(x_j) \le j - 1 - \varepsilon$, and $d(x_i) + d(x_j) \le n - 1 - \varepsilon$, then $G$ has a Hamilton cycle ($\varepsilon = 0$) or Hamilton path ($\varepsilon = 1$) (Bollobás, p. 130).

# Prerequisites
- **k-closure** — The theorem follows from closure analysis
- **Hamiltonian graph** — The property being established

# Key Properties
1. Gives precise conditions rather than just degree sum
2. Implies Chvátal's degree-sequence theorem (Corollary 16)
3. Based on Lemmas 13 and 14

# Context & Application
Provides the most detailed sufficient conditions for Hamiltonicity via the closure method.

# Examples
**Example** (p. 130): Lemma 14 identifies the critical nonadjacent pair in the $k$-closure; Theorem 15 ensures no such pair exists.

# Relationships
## Builds Upon
- **k-closure** — Foundation of the proof

## Enables
- **chvatals-theorem** — Immediate corollary

# Source Reference
Chapter IV, Section IV.3, page 130. Theorem 15.

# Verification Notes
- Definition source: Direct from p. 130
- Confidence rationale: Explicitly stated
- Uncertainties: None
- Cross-reference status: Verified
