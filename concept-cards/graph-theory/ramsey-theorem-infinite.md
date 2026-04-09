---
concept: "Ramsey's Theorem (Infinite)"
slug: ramsey-theorem-infinite
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
  - "Theorem 9.1.2"
  - "infinite Ramsey theorem"
prerequisites:
  - ramsey-theorem-finite
  - c-colouring
related:
  - ramsey-theorem-general
answers_questions:
  - "Does Ramsey's theorem hold for infinite sets?"
---

# Quick Definition
If the k-subsets of an infinite set X are coloured with c colours, then X has an infinite monochromatic subset.

# Core Definition
**Theorem 9.1.2**: Let k, c be positive integers, and X an infinite set. If [X]^k is coloured with c colours, then X has an infinite monochromatic subset.

The proof uses induction on k, with c fixed. For k = 1 it holds trivially. For k > 1, construct an infinite sequence of infinite subsets X_0, X_1, ... choosing x_i in X_i so that all k-sets {x_i} union Z with Z in [X_{i+1}]^{k-1} have the same colour. By finiteness of c, infinitely many x_i share a colour. (Diestel, pp. 253-254)

# Prerequisites
- **Ramsey's theorem (finite)** — The infinite version is the stronger companion
- **c-colouring** — The theorem concerns colourings

# Key Properties
1. Stronger than the finite version (which is deduced from it "by compactness")
2. Easier to prove (no need to track set sizes)
3. The finite version follows from the infinite via Konig's infinity lemma
4. Does NOT extend to uncountable sets (Exercise 4)

# Relationships
## Related
- **Ramsey theorem (general, finite)** — Deduced from the infinite version

# Source Reference
Chapter 9, Section 9.1, Theorem 9.1.2, pages 253-254 (pdf pages 263-264).

# Verification Notes
- Confidence: HIGH — theorem with proof
