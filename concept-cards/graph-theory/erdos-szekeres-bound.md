---
concept: "Erd\u0151s-Szekeres Bound on Ramsey Numbers"
slug: erdos-szekeres-bound
category: ramsey-theory
subcategory: classical-ramsey
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Ramsey Theory for Graphs"
chapter_number: 9
pdf_page: 263
section: "9.1 Ramsey's original theorems"
extraction_confidence: high
aliases:
  - "exponential Ramsey bound"
prerequisites:
  - ramsey-number
  - ramsey-theorem-finite
related:
  - ramsey-number-bounded-degree
answers_questions:
  - "What are the best known bounds on Ramsey numbers?"
---

# Quick Definition
The proof of Ramsey's theorem gives R(r) <= 2^{2r-3}. A probabilistic lower bound gives R(r) >= 2^{r/2}. The gap between these exponential bounds remains one of the central open problems in combinatorics.

# Core Definition
The constructive proof of Theorem 9.1.1 yields **R(r) <= 2^{2r-3}**. Chapter 11 provides the probabilistic lower bound **R(r) >= 2^{r/2}** (Theorem 11.1.3). Closing the gap between these exponential bounds is a major open problem. (Diestel, p. 253)

# Prerequisites
- **Ramsey number** — The quantity being bounded
- **Ramsey's theorem (finite)** — Provides the upper bound

# Key Properties
1. Upper bound: R(r) <= 2^{2r-3} (from the proof, using halving at each step)
2. Lower bound: R(r) >= 2^{r/2} (probabilistic method, Chapter 11)
3. For bounded-degree graphs: R(H) <= c|H| is LINEAR (Theorem 9.2.2)
4. Exact values: R(3) = 6, R(4) = 18; R(5) is unknown

# Relationships
## Related
- **Ramsey number (bounded degree)** — Linear bounds for sparse graphs

# Source Reference
Chapter 9, Section 9.1, page 253 (pdf page 263). Lower bound from Chapter 11.

# Verification Notes
- Confidence: HIGH — bounds explicitly stated
