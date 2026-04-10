---
concept: "Turán Graph"
slug: turan-graph
category: extremal-graph-theory
subcategory: extremal-structures
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
  - "T_r(n)"
  - "Turán graph"
  - "complete r-partite graph with equal classes"
prerequisites:
  - extremal-function
extends: []
related:
  - turans-theorem
  - turan-number
contrasts_with: []
answers_questions:
  - "What is the Turán graph?"
---

# Quick Definition
The Turán graph $T_r(n)$ is the complete $r$-partite graph on $n$ vertices with vertex classes as equal as possible.

# Core Definition
The Turán graph $T_r(n)$ is the complete $r$-partite graph with $n$ vertices and as equal classes as possible, so that if the classes have sizes $n_1 \le n_2 \le \cdots \le n_r$, then $n_r \le n_1 + 1$. The graph $T_r(n)$ is unique; $n_i = \lfloor(n+i-1)/r\rfloor$ (Bollobás, p. 116).

# Prerequisites
- **Extremal function** — $T_r(n)$ achieves $ex(n; K_{r+1})$

# Key Properties
1. Unique up to isomorphism
2. $\delta(T_r(n)) = n - \lceil n/r \rceil$ and $\Delta(T_r(n)) = n - \lfloor n/r \rfloor$
3. Removing a minimum-degree vertex gives $T_r(n-1)$
4. $e(T_r(n)) = t_r(n) \ge (1 - 1/r)\binom{n}{2}$
5. Contains no $K_{r+1}$
6. Maximum edges among all $r$-partite graphs of order $n$

# Construction / Recognition
1. Divide $n$ vertices into $r$ classes of sizes $\lfloor n/r \rfloor$ or $\lceil n/r \rceil$
2. Connect every pair of vertices in different classes
3. The result is $T_r(n)$

# Context & Application
The Turán graph is the unique extremal graph for Turán's theorem. It is the densest graph avoiding $K_{r+1}$.

# Examples
**Example** (p. 116, Fig. IV.3): $T_3(7)$ is shown — a complete 3-partite graph with classes of sizes 2, 2, 3.

**Example** (p. 116): $t_2(n) = \lfloor n^2/4 \rfloor$, achieved by the complete bipartite graph $K_{\lfloor n/2 \rfloor, \lceil n/2 \rceil}$.

# Relationships
## Enables
- **turans-theorem** — $T_r(n)$ is the unique extremal graph

## Related
- **turan-number** — $t_r(n) = e(T_r(n))$

# Common Errors
- **Error**: Constructing an $r$-partite graph with unbalanced classes
  **Correction**: $T_r(n)$ requires classes differing by at most 1 in size

# Common Confusions
- **Confusion**: Thinking any complete $r$-partite graph maximizes edges
  **Clarification**: Only the balanced one ($T_r(n)$) maximizes edges

# Source Reference
Chapter IV, Section IV.2, pages 116-117. Fig. IV.3.

# Verification Notes
- Definition source: Direct from p. 116
- Confidence rationale: Explicitly defined with uniqueness proof
- Uncertainties: None
- Cross-reference status: Verified
