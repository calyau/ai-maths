---
concept: Extremal Bound for Maximum Cycle Length
slug: extremal-bound-for-cycles
category: extremal-graph-theory
subcategory: forbidden-subgraphs
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
  - "Theorem 4"
prerequisites:
  - extremal-function
extends: []
related:
  - extremal-bound-for-paths
contrasts_with: []
answers_questions:
  - "How many edges can a graph have if all cycles have bounded length?"
---

# Quick Definition
A graph of order $n$ in which every cycle has length at most $k$ has at most $k(n-1)/2$ edges, with equality iff it is connected with all blocks being $K_k$.

# Core Definition
**Theorem 4**: Let $k \ge 2$ and let $G$ be a graph of order $n$ in which every cycle has length at most $k$. Then $e(G) \le \frac{k}{2}(n-1)$. Equality holds iff $G$ is connected and all its blocks are complete graphs of order $k$ (Bollobás, p. 116).

# Prerequisites
- **Extremal function** — This bounds the size for bounded circumference

# Key Properties
1. The bound is $k(n-1)/2$, slightly different from the path bound
2. Extremal graphs are connected with all blocks being $K_k$
3. The proof uses simple transforms (Section IV.3)

# Construction / Recognition
1. Check all cycles have length $\le k$
2. Count edges; at most $k(n-1)/2$

# Context & Application
Complements Theorem 3 by addressing cycle length bounds instead of path length bounds.

# Examples
**Example**: For $k = 2$ (no cycles of length $> 2$, i.e., forests), $e(G) \le n - 1$, which is the tree bound.

# Relationships
## Related
- **extremal-bound-for-paths** — Theorem 3

# Source Reference
Chapter IV, Section IV.1, page 116. Theorem 4.

# Verification Notes
- Definition source: Direct from p. 116
- Confidence rationale: Explicitly stated
- Uncertainties: None
- Cross-reference status: Verified
