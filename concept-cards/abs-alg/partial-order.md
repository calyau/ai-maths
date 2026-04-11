---
concept: Partial Order
slug: partial-order
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
  - "partially ordered set"
  - "poset"
prerequisites: []
extends: []
related:
  - chain
  - zorns-lemma
  - total-order
contrasts_with:
  - total-order
answers_questions:
  - "What is a partial order?"
---

# Quick Definition
A partial order on a set A is a relation ≤ that is reflexive, antisymmetric, and transitive. A set with a partial order is a partially ordered set (poset).

# Core Definition
A **partial order** on a nonempty set A is a relation ≤ satisfying: (1) x ≤ x (reflexive), (2) x ≤ y and y ≤ x implies x = y (antisymmetric), (3) x ≤ y and y ≤ z implies x ≤ z (transitive) (Definition, p. 907).

# Prerequisites
This is a foundational concept with no prerequisites within this source.

# Key Properties
1. Not all elements need be comparable (unlike total orders)
2. Subsets with all elements comparable are chains

# Examples
**Example** (p. 907): The power set of X ordered by ⊆ is a poset.

# Relationships
## Enables
- **zorns-lemma** — Statement involves partially ordered sets

## Contrasts With
- **total-order** — Total orders require all elements to be comparable

# Source Reference
Appendix I, Section 2, Definition, page 907.

# Verification Notes
- Confidence: HIGH — standard definition
