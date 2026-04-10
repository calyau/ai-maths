---
concept: Planar Edge Bound
slug: planar-edge-bound
category: planar-graphs
subcategory: planarity
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Fundamentals"
chapter_number: 1
pdf_page: 9
section: "I.4 Planar Graphs"
extraction_confidence: high
aliases:
  - "$m \\le 3n - 6$"
prerequisites:
  - planar-graph
  - eulers-formula
  - girth
extends:
  - eulers-formula
related:
  - kuratowskis-theorem
contrasts_with: []
answers_questions:
  - "How many edges can a planar graph have?"
---

# Quick Definition

A planar graph of order $n \ge 3$ has at most $3n - 6$ edges. More generally, a planar graph of girth $g$ has at most $\frac{g}{g-2}(n-2)$ edges (Theorem 16).

# Core Definition

"**Theorem 16.** A planar graph of order $n \ge 3$ has at most $3n - 6$ edges. Furthermore, a planar graph of order $n$ and girth at least $g$, $3 \le g < \infty$, has size at most $\max\{\frac{g}{g-2}(n-2), n-1\}$" (Bollobás, pp. 30-31). The proof combines Euler's formula with the fact that each face has at least $g$ boundary edges.

# Prerequisites

- **Planar graph** — The bound applies to planar graphs
- **Euler's formula** — The proof uses $n - m + f = 2$
- **Girth** — The refined bound uses the girth

# Key Properties

1. $m \le 3n - 6$ for planar graphs of order $n \ge 3$ (case $g = 3$)
2. $m \le 2n - 4$ for triangle-free planar graphs ($g \ge 4$)
3. $m \le \frac{5}{3}(n - 2)$ for planar graphs of girth $\ge 5$
4. $K_5$ is nonplanar: $e(K_5) = 10 > 9 = 3(5) - 6$
5. $K_{3,3}$ is nonplanar: girth 4 and $e(K_{3,3}) = 9 > 8 = 2(6) - 4$

# Construction / Recognition

The bound provides a necessary condition for planarity. If $e(G) > 3n - 6$ (or the girth-refined bound), the graph is definitely nonplanar.

# Context & Application

This is the primary tool for proving specific graphs are nonplanar, before resorting to Kuratowski's or Wagner's theorem.

# Examples

**Example** (p. 31): $K_5$: $e = 10 > 3(5) - 6 = 9$, so $K_5$ is nonplanar.

**Example** (p. 31): $K_{3,3}$: girth 4, $e = 9 > \frac{4}{2}(6-2) = 8$, so $K_{3,3}$ is nonplanar.

# Relationships

## Builds Upon
- **Planar graph**, **Euler's formula**, **Girth**

## Enables
- Quick nonplanarity proofs for $K_5$ and $K_{3,3}$
- **Kuratowski's theorem** — These are the key nonplanar graphs

# Common Errors

- **Error**: Using $3n - 6$ as a sufficient condition for planarity
  **Correction**: $e \le 3n - 6$ is necessary but not sufficient for planarity

# Common Confusions

- **Confusion**: Forgetting the girth refinement
  **Clarification**: The bound $3n - 6$ is for general planar graphs; triangle-free planar graphs have the tighter bound $2n - 4$

# Source Reference

Chapter I: Fundamentals, Section I.4, Theorem 16, pages 30-31.

# Verification Notes

- Definition source: Direct theorem statement from pp. 30-31
- Confidence rationale: Explicitly stated with proof
- Uncertainties: None
- Cross-reference status: Verified
