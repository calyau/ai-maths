---
concept: "Turán's Theorem"
slug: turans-theorem
category: extremal-graph-theory
subcategory: fundamental-theorems
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Extremal Problems"
chapter_number: 4
pdf_page: 110
section: "IV.2 Complete Subgraphs"
extraction_confidence: high
aliases:
  - "Theorem 8"
  - "Turán 1941"
prerequisites:
  - turan-graph
  - turan-number
  - extremal-function
extends: []
related:
  - erdos-stone-theorem
  - clique-number
contrasts_with: []
answers_questions:
  - "How many edges guarantee a complete subgraph?"
---

# Quick Definition
Every graph of order $n$ with more than $t_r(n)$ edges contains a $K_{r+1}$, and $T_r(n)$ is the unique $K_{r+1}$-free graph of order $n$ with $t_r(n)$ edges.

# Core Definition
**Theorem 8** (Turán, 1941): For $r, n \ge 2$, $ex(n; K_{r+1}) = t_r(n)$ and $EX(n; K_{r+1}) = \{T_r(n)\}$. Every graph of order $n$ with more than $t_r(n)$ edges contains a $K_{r+1}$. Also, $T_r(n)$ is the unique graph of order $n$ and size $t_r(n)$ that does not contain $K_{r+1}$ (Bollobás, p. 119).

# Prerequisites
- **Turán graph** — The unique extremal graph
- **Turán number** — The extremal edge count
- **Extremal function** — The problem being solved

# Key Properties
1. Four proofs are given in the text (Theorems 6, 7, 8)
2. The greedy algorithm (Theorem 6) finds $K_{r+1}$ by picking max-degree vertices
3. Theorem 7 (Erdős): degree sequence of $K_{r+1}$-free graph is dominated by an $r$-partite graph
4. The extremal graph is unique: $T_r(n)$
5. Extends Mantel's theorem ($r = 2$)

# Construction / Recognition
1. Count edges: if $e(G) > t_r(n)$, then $G$ contains $K_{r+1}$
2. The greedy algorithm: repeatedly pick max-degree vertices and restrict to their common neighborhood

# Context & Application
"Extremal graph theory really started in 1941, when Turán... determined both $ex(n; K_r)$ and $EX(n; K_r)$" (p. 111). This is the foundational result of extremal graph theory.

# Examples
**Example** (pp. 117-120): Four proofs are given: (1) greedy clique-finding, (2) degree domination, (3) induction removing min-degree vertex, (4) induction removing a $K_r$.

# Relationships
## Builds Upon
- **turan-graph** — The extremal graph
- **turan-number** — The extremal edge count

## Enables
- **erdos-stone-theorem** — Major generalization
- **clique-number** — Turán gives lower bounds on clique number

# Common Errors
- **Error**: Applying Turán's theorem with the wrong value of $r$
  **Correction**: To avoid $K_{r+1}$, the Turán graph is $T_r(n)$ (not $T_{r+1}(n)$)

# Common Confusions
- **Confusion**: Thinking Turán's theorem gives the chromatic number
  **Clarification**: Turán's theorem concerns clique number, not chromatic number (though they are related via $\chi(G) \ge \omega(G)$)

# Source Reference
Chapter IV, Section IV.2, pages 116-121. Theorem 8 with four proofs.

# Verification Notes
- Definition source: Direct theorem statement from p. 119
- Confidence rationale: Major theorem with multiple proofs
- Uncertainties: None
- Cross-reference status: Verified
