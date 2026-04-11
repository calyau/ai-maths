---
concept: Total Order
slug: total-order
category: foundations
subcategory: order-theory
tier: foundational
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Appendix I: Cartesian Products and Zorn's Lemma"
chapter_number: null
pdf_page: 907
section: "2. Partially Ordered Sets and Zorn's Lemma"
extraction_confidence: high
aliases:
  - "linear order"
  - "simple order"
prerequisites:
  - partial-order
extends:
  - partial-order
related:
  - well-ordering
  - chain
contrasts_with:
  - partial-order
answers_questions:
  - "What is a total order?"
---

# Quick Definition
A total order is a partial order in which every pair of elements is comparable: for all x,y, either x ≤ y or y ≤ x. Also called a linear or simple ordering.

# Core Definition
A subset B of a partially ordered set A is called a **chain** (or totally/linearly/simply ordered subset) if for all x,y ∈ B, either x ≤ y or y ≤ x (Definition, p. 908). A total order on A is a partial order where all of A is a chain.

# Prerequisites
- **partial-order** — A total order is a special partial order

# Source Reference
Appendix I, Section 2, Definition, page 908.

# Verification Notes
- Confidence: HIGH — standard definition
