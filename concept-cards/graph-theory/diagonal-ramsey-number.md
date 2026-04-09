---
concept: Diagonal Ramsey Number
slug: diagonal-ramsey-number
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
  - "R(r,r)"
prerequisites:
  - ramsey-number
related:
  - erdos-szekeres-bound
answers_questions:
  - "What is the diagonal Ramsey number?"
---

# Quick Definition
The diagonal Ramsey number R(r) (or R(r,r)) is the least n such that every 2-colouring of the edges of K^n yields a monochromatic K^r. It satisfies 2^{r/2} <= R(r) <= 2^{2r-3}.

# Core Definition
The **diagonal Ramsey number** R(r) is the special case of R(H) where H = K^r. Equivalently, R(r) is the least n such that every graph of order n contains K^r or K-bar^r as an induced subgraph. Known values: R(1) = 1, R(2) = 2, R(3) = 6, R(4) = 18. (Diestel, p. 253)

# Prerequisites
- **Ramsey number** — R(r) is the most studied special case

# Key Properties
1. 2^{r/2} <= R(r) <= 2^{2r-3}
2. Exact values known only for r <= 4
3. R(5) is unknown despite decades of work
4. The gap between upper and lower bounds is one of the most famous open problems

# Source Reference
Chapter 9, Section 9.1, page 253 (pdf page 263).

# Verification Notes
- Confidence: HIGH — explicitly discussed
