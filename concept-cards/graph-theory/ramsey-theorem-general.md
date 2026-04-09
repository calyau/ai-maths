---
concept: "Ramsey's Theorem (General Finite)"
slug: ramsey-theorem-general
category: ramsey-theory
subcategory: classical-ramsey
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Ramsey Theory for Graphs"
chapter_number: 9
pdf_page: 264
section: "9.1 Ramsey's original theorems"
extraction_confidence: high
aliases:
  - "Theorem 9.1.3"
  - "finite Ramsey theorem for k-sets"
prerequisites:
  - ramsey-theorem-infinite
  - c-colouring
related:
  - ramsey-number
answers_questions:
  - "What is the general finite Ramsey theorem?"
---

# Quick Definition
For all k, c, r >= 1 there exists an n >= k such that every c-colouring of the k-subsets of any n-set yields a monochromatic r-subset.

# Core Definition
**Theorem 9.1.3**: For all k, c, r >= 1 there exists an n >= k such that every n-set X has a monochromatic r-subset with respect to any c-colouring of [X]^k.

The proof deduces this from the infinite version (Theorem 9.1.2) via Konig's infinity lemma: if the finite version fails, "bad colourings" of [n]^k for all n can be combined (by compactness) into a bad colouring of [N]^k, contradicting the infinite version. (Diestel, pp. 254-255)

The least n is the **Ramsey number** R(k, c, r).

# Prerequisites
- **Ramsey's theorem (infinite)** — The proof deduces the finite from the infinite version
- **c-colouring** — The theorem concerns colourings of k-subsets

# Key Properties
1. Generalizes the graph version (k = 2, c = 2) to arbitrary k and c
2. The proof by compactness avoids size-tracking calculations
3. The least n is the Ramsey number R(k, c, r)
4. For k = 2, c = 2: reduces to the graph Ramsey theorem

# Relationships
## Builds Upon
- **Ramsey's theorem (infinite)**

## Enables
- **Ramsey number** R(k, c, r) — quantifies this theorem

# Source Reference
Chapter 9, Section 9.1, Theorem 9.1.3, pages 254-255 (pdf pages 264-265).

# Verification Notes
- Confidence: HIGH — theorem with proof
