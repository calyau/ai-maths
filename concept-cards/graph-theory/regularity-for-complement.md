---
concept: Regularity for Complement Graphs
slug: regularity-for-complement
category: extremal-graph-theory
subcategory: regularity
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Extremal Graph Theory"
chapter_number: 7
pdf_page: 201
section: "Exercises"
extraction_confidence: high
aliases:
  - "Exercise 38"
prerequisites:
  - epsilon-regular-pair
related:
  - regularity-lemma
  - ramsey-number-bounded-degree
answers_questions:
  - "Is an epsilon-regular pair also regular for the complement?"
---

# Quick Definition
Every epsilon-regular pair in G is also epsilon-regular in the complement G-bar (Exercise 38). This is crucial for Ramsey applications where both G and G-bar must be handled.

# Core Definition
**Exercise 38**: Show that any epsilon-regular pair in G is also epsilon-regular in G-bar. This follows because d_{G-bar}(X,Y) = 1 - d_G(X,Y) for disjoint X, Y, so |d_{G-bar}(X,Y) - d_{G-bar}(A,B)| = |d_G(X,Y) - d_G(A,B)| <= epsilon. (Diestel, p. 193)

This property is used in the proof of Theorem 9.2.2: R'' (the complement regularity graph) is also a valid regularity graph of G-bar.

# Prerequisites
- **Epsilon-regular pair** — The property transfers to complements

# Key Properties
1. Regularity is preserved under complementation
2. If (A, B) has density d in G, it has density 1-d in G-bar, and the same regularity
3. Essential for Ramsey applications using the regularity lemma

# Relationships
## Related
- **Ramsey number (bounded degree)** — Uses this in the proof of Theorem 9.2.2

# Source Reference
Chapter 7, Exercise 38, page 193 (pdf page 201). Used in Theorem 9.2.2 proof.

# Verification Notes
- Confidence: HIGH — stated as exercise with clear proof idea
