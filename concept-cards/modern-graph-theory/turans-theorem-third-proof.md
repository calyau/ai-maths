---
concept: "Turán's Theorem (Third Proof)"
slug: turans-theorem-third-proof
category: extremal-graph-theory
subcategory: proof-techniques
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
  - "induction on n proof"
prerequisites:
  - turans-theorem
  - turan-graph
extends: []
related: []
contrasts_with: []
answers_questions:
  - "How is Turán's theorem proved by removing a minimum-degree vertex?"
---

# Quick Definition
Remove a minimum-degree vertex from $G$; by induction the remainder is $T_r(n-1)$. The removed vertex must be joined to all vertices outside a smallest class, forcing $G = T_r(n)$.

# Core Definition
Third proof of Turán's theorem: Fix $r \ge 2$, induct on $n$. If $G$ has $n$ vertices and $t_r(n)$ edges without $K_{r+1}$, remove a minimum-degree vertex $x$. Then $e(G-x) \ge t_r(n-1)$, so $G-x \cong T_r(n-1)$ by induction. Since $d(x) = \delta(G) \le \delta(T_r(n))$, vertex $x$ must join to all vertices outside a smallest class. Hence $G \cong T_r(n)$ (Bollobás, pp. 120-121).

# Prerequisites
- **Turán's theorem** — The theorem being proved
- **Turán graph** — Properties used in the proof

# Key Properties
1. Uses induction on $n$ (not $r$)
2. Key insight: minimum degree of $G$ matches that of $T_r(n)$
3. After removing $x$, the graph is uniquely determined

# Context & Application
One of four proofs, demonstrating the versatility of the Turán graph's properties.

# Examples
**Example** (p. 120): $e(G-x) = e(G) - d(x) \ge t_r(n) - \delta(T_r(n)) = t_r(n-1)$.

# Relationships
## Builds Upon
- **turans-theorem** — Alternative proof

# Source Reference
Chapter IV, Section IV.2, pages 120-121.

# Verification Notes
- Definition source: Synthesized from proof
- Confidence rationale: Complete proof given
- Uncertainties: None
- Cross-reference status: Verified
