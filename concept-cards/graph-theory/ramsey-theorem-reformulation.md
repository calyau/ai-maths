---
concept: Ramsey Theorem as Edge Colouring
slug: ramsey-theorem-reformulation
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
  - "partition reformulation"
prerequisites:
  - ramsey-theorem-finite
  - c-colouring
  - monochromatic-subgraph
related:
  - ramsey-number
answers_questions:
  - "How can Ramsey's theorem be restated in terms of edge colourings?"
---

# Quick Definition
Ramsey's theorem can be restated: for every r there exists n such that given any n-set X, every 2-colouring of [X]^2 yields a monochromatic r-set Y. This extends to c-colourings of k-sets.

# Core Definition
Ramsey's theorem (Theorem 9.1.1) can be expressed as: for every r there exists an n such that, given any n-set X, every 2-colouring of [X]^2 yields a monochromatic r-set Y subset X. This assertion remains true for c-colourings of [X]^k with arbitrary c and k (Theorem 9.1.3)—with almost exactly the same proof. (Diestel, p. 253)

# Prerequisites
- **Ramsey's theorem (finite)** — The original graph version
- **c-colouring** — The language of partitions as colourings
- **Monochromatic subgraph** — The objects being found

# Key Properties
1. Thinking of "partitions as colourings" is the standard Ramsey-theory idiom
2. The generalization from 2-colourings of pairs to c-colourings of k-sets requires only minor modifications
3. The infinite version (Theorem 9.1.2) is easier to prove; the finite follows by compactness

# Source Reference
Chapter 9, Section 9.1, page 253 (pdf page 263).

# Verification Notes
- Confidence: HIGH — explicit reformulation in text
