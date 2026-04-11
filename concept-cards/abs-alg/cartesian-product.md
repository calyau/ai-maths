---
concept: Cartesian Product
slug: cartesian-product
category: foundations
subcategory: set-theory
tier: foundational
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Appendix I: Cartesian Products and Zorn's Lemma"
chapter_number: null
pdf_page: 905
section: "1. Cartesian Products"
extraction_confidence: high
aliases:
  - "direct product of sets"
prerequisites: []
extends:
  - set
related:
  - choice-function
  - axiom-of-choice
contrasts_with: []
answers_questions:
  - "What is the Cartesian product of an arbitrary collection of sets?"
---

# Quick Definition
The Cartesian product ∏_{i∈I} A_i is the set of all choice functions f: I → ∪A_i with f(i) ∈ A_i. For finite index sets, elements are n-tuples.

# Core Definition
Let {A_i | i ∈ I} be a collection of sets. The **Cartesian product** ∏_{i∈I} A_i is the set of all choice functions from I to ∪A_i (Definition, p. 905). When I = {1,...,n}, elements are ordered n-tuples (a_1,...,a_n). The j-th projection map sends ∏a_i ↦ a_j. The cardinality |∏A_i| = ∏|A_i| (Proposition 1).

# Prerequisites
This is a foundational concept with no prerequisites within this source.

# Key Properties
1. Elements are choice functions (or equivalently, tuples)
2. |∏A_i| = ∏|A_i| for countable index sets
3. Projection maps pick out coordinates
4. For I = Z^+, elements are infinite sequences

# Examples
**Example** (p. 906): A × B = {(a,b) | a ∈ A, b ∈ B}. R^n is the n-fold Cartesian product of R.

# Relationships
## Enables
- **axiom-of-choice** — States Cartesian products of nonempty sets are nonempty

# Source Reference
Appendix I, Section 1, Definition and Proposition 1, pages 905-907.

# Verification Notes
- Confidence: HIGH — explicit definition
