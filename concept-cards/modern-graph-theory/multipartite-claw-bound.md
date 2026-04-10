---
concept: Multipartite Claw Bound
slug: multipartite-claw-bound
category: regularity-method
subcategory: technical-results
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
  - "Theorem 34"
prerequisites:
  - zarankiewicz-problem
  - turans-theorem
extends:
  - kovari-sos-turan-bound
related:
  - frankl-pach-theorem
contrasts_with: []
answers_questions:
  - "How do you bound edges in a multipartite graph avoiding K_{s,t}?"
---

# Quick Definition
In a $k$-partite graph with $\ell$ vertices per class, $q$ edge-pairs, and no $K_{s,t}$ within any class, the edges are bounded by $(2q)^{1-1/s}\ell^{2-1/s}(t-1)^{1/s}k^{1/s} + 2q\ell s$.

# Core Definition
**Theorem 34**: Let $H$ be a $k$-partite graph with equal classes of size $\ell$ and $q$ pairs with edges. If $H$ has no $K_{s,t}$ with all $s$ vertices in one class, then $2e(H) \le (2q)^{1-1/s}\ell^{2-1/s}(t-1)^{1/s}k^{1/s} + 2q\ell s$ (Bollobás, pp. 151-152).

# Prerequisites
- **Zarankiewicz problem** — Same counting technique
- **Turán's theorem** — Used to bound $q$ via the skeleton

# Key Properties
1. Generalizes Zarankiewicz to multipartite setting
2. Uses "claw" (star $K_{1,s}$) counting instead of general $t$-set counting
3. The constraint is $K_{s,t}$ with $s$ vertices in the same class

# Context & Application
Key technical tool for the Frankl-Pach theorem (Theorem 35).

# Examples
**Example** (p. 152): Define a claw as a $K_{1,s}$ with base in one class. Count claws: at most $(t-1)k\binom{\ell}{s}$ total, then apply convexity.

# Relationships
## Builds Upon
- **kovari-sos-turan-bound** — Same technique, multipartite setting

## Enables
- **frankl-pach-theorem** — Theorem 35

# Source Reference
Chapter IV, Section IV.6, pages 151-152. Theorem 34.

# Verification Notes
- Definition source: Direct from pp. 151-152
- Confidence rationale: Explicitly stated with proof
- Uncertainties: None
- Cross-reference status: Verified
