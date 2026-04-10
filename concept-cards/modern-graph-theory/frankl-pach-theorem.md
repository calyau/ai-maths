---
concept: Frankl-Pach Theorem
slug: frankl-pach-theorem
category: regularity-method
subcategory: applications
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Extremal Problems"
chapter_number: 4
pdf_page: 110
section: "IV.6 Simple Applications of Szemerédi's Lemma"
extraction_confidence: high
aliases:
  - "Theorem 35"
prerequisites:
  - szemeredis-regularity-lemma
  - turans-theorem
  - zarankiewicz-problem
extends: []
related:
  - regularity-removal-lemma
contrasts_with: []
answers_questions:
  - "What is the extremal number when both K_r and K_{s,t} are forbidden?"
---

# Quick Definition
If $G$ of order $n$ contains neither $K_r$ nor $K_{s,t}$ with $t = \lceil cn \rceil$, then $e(G) \le c^{1/s}((r-2)/(r-1))^{1-1/s}n^2/2 + \gamma n^2$.

# Core Definition
**Theorem 35** (Frankl-Pach, 1988): Let $r \ge 3$ and $s \ge 2$ be fixed integers, and $c, \gamma > 0$. For $n$ large enough, if $G$ of order $n$ contains neither $K_r$ nor $K_{s,t}$ where $t = \lceil cn \rceil$, then $e(G) \le c^{1/s}((r-2)/(r-1))^{1-1/s}n^2/2 + \gamma n^2$ (Bollobás, pp. 151-153).

# Prerequisites
- **Szemerédi's regularity lemma** — Provides the partition
- **Turán's theorem** — Bounds skeleton edges
- **Zarankiewicz problem** — Bounds edges in multipartite graphs

# Key Properties
1. Combines forbidden clique and forbidden bipartite conditions
2. Uses the skeleton from regularity to apply Turán's theorem
3. Then applies bipartite Zarankiewicz bound (Theorem 34) to the regularity piece
4. The upper bound is essentially best possible

# Construction / Recognition
1. Apply regularity to get partition; skeleton is $K_r$-free
2. By Turán: $e(S) \le (r-2)k^2/(2(r-1))$
3. Apply Theorem 34 to bound edges within the regularity piece

# Context & Application
"In fact, the upper bound in Theorem 35 is essentially best possible" (p. 153). The limiting value of $ex(n; K_r, K_{s,t})/\binom{n}{2}$ is $c^{1/s}((r-2)/(r-1))^{1-1/s}$.

# Examples
**Example** (p. 152): The proof combines Szemerédi's lemma, Turán for the skeleton, and a bipartite claw-counting argument for the regularity piece.

# Relationships
## Builds Upon
- **szemeredis-regularity-lemma** — The partition
- **turans-theorem** — For the skeleton
- **zarankiewicz-problem** — For the bipartite parts

# Source Reference
Chapter IV, Section IV.6, pages 151-153. Theorems 34-35.

# Verification Notes
- Definition source: Direct from pp. 151-153
- Confidence rationale: Explicitly stated with proof
- Uncertainties: None
- Cross-reference status: Verified
