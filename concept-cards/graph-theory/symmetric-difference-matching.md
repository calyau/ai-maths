---
concept: Symmetric Difference in Matching
slug: symmetric-difference-matching
category: matching-and-covering
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Matching, Covering and Packing"
chapter_number: 2
pdf_page: 44
section: "2.1 Matching in bipartite graphs"
extraction_confidence: high
aliases:
  - "augmentation by symmetric difference"
prerequisites:
  - matching
  - m-augmenting-path
extends: []
related:
  - maximum-matching
contrasts_with: []
answers_questions:
  - "How does symmetric difference relate to matching augmentation?"
---

# Quick Definition
The symmetric difference of a matching M with an augmenting path P produces a new matching M' = M triangle E(P) with |M'| = |M| + 1.

# Core Definition
Given a matching M and an M-augmenting path P, the **symmetric difference** M triangle E(P) = (M \ E(P)) union (E(P) \ M) is again a matching, and the set of matched vertices is increased by two (the ends of P) (Diestel, p. 44).

# Prerequisites
- **Matching** — the matching being augmented
- **M-augmenting path** — the path used for augmentation

# Key Properties
1. Edges of P in M are removed; edges of P not in M are added
2. The result is a valid matching (no vertex is doubly covered)
3. |M'| = |M| + 1
4. The two previously unmatched endpoints become matched
5. All other matched/unmatched statuses are preserved

# Context & Application
Symmetric difference is the fundamental operation in augmenting path algorithms. It transforms a suboptimal matching into a larger one in a single step.

# Examples
**Example** (p. 44, Fig. 2.1.1): An augmenting path P with alternating bold/thin edges. Taking the symmetric difference swaps matching and non-matching edges along P.

# Relationships
## Builds Upon
- **Matching**, **M-augmenting path**

## Enables
- **Maximum matching** — found by repeated augmentation

# Source Reference
Chapter 2, Section 2.1, p. 44 (pdf p. 44).

# Verification Notes
- From p. 44
- Confidence: HIGH — explicitly described
