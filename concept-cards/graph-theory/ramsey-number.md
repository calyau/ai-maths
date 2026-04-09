---
concept: Ramsey Number
slug: ramsey-number
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
  - "R(r)"
  - "R(k,c,r)"
  - "R(H)"
  - "R(H_1, H_2)"
prerequisites:
  - ramsey-theorem-finite
related:
  - ramsey-theorem-general
  - monochromatic-subgraph
  - erdos-szekeres-bound
answers_questions:
  - "How do Ramsey numbers relate to graph colouring?"
  - "What is a Ramsey number?"
---

# Quick Definition
The Ramsey number R(r) is the least n such that every graph of order at least n contains K^r or K-bar^r as an induced subgraph. More generally, R(k, c, r) is the least n such that every c-colouring of the k-subsets of an n-set yields a monochromatic r-subset.

# Core Definition
The least integer n associated with r as in Theorem 9.1.1 is the **Ramsey number** R(r); the proof shows R(r) <= 2^{2r-3}. A probabilistic lower bound gives R(r) >= 2^{r/2} (Theorem 11.1.3).

More generally, the **Ramsey number** R(k, c, r) (defined after Theorem 9.1.3) is the least n >= k such that every c-colouring of [X]^k yields a monochromatic r-subset, for any n-set X.

For graphs: **R(H)** is the least n such that every graph G of order n has H subset G or H subset G-bar. **R(H_1, H_2)** is the least n such that H_1 subset G or H_2 subset G-bar. (Diestel, pp. 253-255)

# Prerequisites
- **Ramsey's theorem (finite)** — Ramsey numbers quantify the theorem

# Key Properties
1. R(r) <= 2^{2r-3} (from the proof of Theorem 9.1.1)
2. R(r) >= 2^{r/2} (probabilistic lower bound, Chapter 11)
3. Exact values known for very few r: R(3) = 6, R(4) = 18
4. R(H) <= R(|H|) for any H, since H subset K^{|H|}
5. R(H) can be much smaller than R(|H|) for sparse H
6. R(T, K^s) = (s-1)(t-1) + 1 for trees T of order t (Proposition 9.2.1)

# Context & Application
Ramsey numbers are notoriously difficult to compute. Even for small r, exact values are unknown. Lower bounds from random graphs are often sharper than those from explicit constructions. The study of Ramsey numbers for various graph classes is a major area of combinatorics.

# Examples
**Example** (p. 253): R(r) <= 2^{2r-3}; e.g., R(3) <= 2^3 = 8 (the actual value is 6).

# Relationships
## Builds Upon
- **Ramsey's theorem** — Ramsey numbers quantify the theorem

## Related
- **Theorem 9.2.2** — R(H) <= c|H| for bounded-degree H (linear Ramsey numbers)

# Source Reference
Chapter 9, Sections 9.1-9.2, pages 253-255 (pdf pages 263-265).

# Verification Notes
- Confidence: HIGH — multiple definitions given explicitly
