---
concept: BEST Theorem
slug: best-theorem
category: paths-and-cycles
subcategory: hamilton-euler
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Fundamentals"
chapter_number: 1
pdf_page: 9
section: "I.3 Hamilton Cycles and Euler Circuits"
extraction_confidence: high
aliases:
  - de Bruijn-van Aardenne-Ehrenfest-Smith-Tutte theorem
prerequisites:
  - eulerian-graph
  - euler-circuit
  - directed-graph
  - spanning-tree
extends: []
related:
  - matrix-tree-theorem
contrasts_with: []
answers_questions:
  - "How many Euler circuits does a directed multigraph have?"
---

# Quick Definition

The BEST theorem expresses the number of Euler circuits in an Eulerian directed multigraph as $s(G) = t_i(G) \prod_{j=1}^{n} (d^+(v_j) - 1)!$, where $t_i(G)$ is the number of spanning trees oriented towards $v_i$.

# Core Definition

"**Theorem 13.** Let $G$ be a directed multigraph with vertex set $V(G) = \{v_1, \ldots, v_n\}$, such that $d^+(v_i) = d^-(v_i)$ for every $i$. Denote by $s(G)$ the number of Euler circuits of $G$, and by $t_i(G)$ the number of spanning trees oriented towards $i$. Then $s(G) = t_i(G) \prod_{j=1}^{n} (d^+(v_j) - 1)!$ for every $i$, $1 \le i \le n$. In particular, $t_1(G) = \cdots = t_n(G)$" (Bollobás, p. 28).

# Prerequisites

- **Eulerian graph** — The theorem applies to Eulerian directed multigraphs
- **Euler circuit** — The theorem counts Euler circuits
- **Directed graph** — Requires directed multigraphs
- **Spanning tree** — Uses oriented spanning trees

# Key Properties

1. The number of oriented spanning trees $t_i(G)$ is the same for all roots $i$
2. The formula combines oriented spanning tree counts with degree factorials
3. The proof constructs a bijection $\phi_i: \mathcal{E}_i \to T_i$ from Euler trails to oriented spanning trees
4. Each Euler trail maps to the tree formed by "last exit" edges at each vertex

# Construction / Recognition

The theorem is a counting result, not a construction method. It reduces counting Euler circuits to counting oriented spanning trees, which can be done via the matrix-tree theorem.

# Context & Application

The BEST theorem connects two seemingly different counting problems: Euler circuits and oriented spanning trees. It is named after de Bruijn, van Aardenne-Ehrenfest, Smith, and Tutte.

# Examples

**Example** (p. 27): The proof constructs, for each Euler trail $S$ starting at $v_1$, a spanning tree $T$ oriented towards $v_1$, by taking the "last exit" edge $e_j$ from each vertex $v_j$.

# Relationships

## Builds Upon
- **Eulerian graph**, **Euler circuit**, **Spanning tree**

## Related
- **Matrix-tree theorem** — Computes $t_i(G)$, which feeds into the BEST formula

# Common Errors

- **Error**: Applying the theorem to non-Eulerian directed graphs
  **Correction**: The theorem requires $d^+(v) = d^-(v)$ for all vertices

# Common Confusions

- **Confusion**: Thinking the BEST theorem applies to undirected Euler circuits
  **Clarification**: It applies to directed multigraphs; for undirected graphs, orient each edge and apply accordingly

# Source Reference

Chapter I: Fundamentals, Section I.3, Theorem 13, pages 27-28.

# Verification Notes

- Definition source: Direct theorem statement from p. 28
- Confidence rationale: Explicitly stated with proof
- Uncertainties: None
- Cross-reference status: Verified
