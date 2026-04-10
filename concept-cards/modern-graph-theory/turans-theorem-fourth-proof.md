---
concept: "Turán's Theorem (Fourth Proof)"
slug: turans-theorem-fourth-proof
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
  - "induction on n+r proof"
prerequisites:
  - turans-theorem
  - turan-graph
extends: []
related: []
contrasts_with: []
answers_questions:
  - "How is Turán's theorem proved by removing a complete subgraph?"
---

# Quick Definition
Find a $K_r$ in $G$ (it exists since $t_r(n) > t_{r-1}(n)$). Remove its vertices; the remainder has $\ge t_r(n-r)$ edges, so by induction it is $T_r(n-r)$, and the join structure forces $G \cong T_r(n)$.

# Core Definition
Fourth proof: Induction on $n+r$. Since $t_r(n) > t_{r-1}(n)$, $G$ contains $K_r$ with vertex set $W$. Set $H = G[V \setminus W]$. Then $e(H) = e(G) - \binom{r}{2} - e(U,W) \ge t_r(n) - \binom{r}{2} - (n-r)(r-1) = t_r(n-r)$. By induction $H \cong T_r(n-r)$ and each vertex of $H$ joins to exactly $r-1$ vertices of $W$, forcing $G \cong T_r(n)$ (Bollobás, p. 121).

# Prerequisites
- **Turán's theorem** — The theorem being proved
- **Turán graph** — Properties used

# Key Properties
1. Uses induction on $n + r$
2. Key calculation: removing $K_r$ removes exactly $\binom{r}{2} + (n-r)(r-1)$ edges from $T_r(n)$
3. The remainder is $T_r(n-r)$

# Context & Application
A fourth distinct proof, using the structure of complete subgraphs.

# Examples
**Example** (p. 121): Removing a $K_r$ from $T_r(n)$ always leaves $T_r(n-r)$ with exactly $t_r(n-r)$ edges.

# Relationships
## Builds Upon
- **turans-theorem** — Alternative proof

# Source Reference
Chapter IV, Section IV.2, page 121.

# Verification Notes
- Definition source: Synthesized from proof
- Confidence rationale: Complete proof given
- Uncertainties: None
- Cross-reference status: Verified
