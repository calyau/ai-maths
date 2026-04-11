---
concept: Choice Function
slug: choice-function
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
aliases: []
prerequisites: []
extends: []
related:
  - cartesian-product
  - axiom-of-choice
contrasts_with: []
answers_questions:
  - "What is a choice function?"
---

# Quick Definition
A choice function for a collection {A_i | i ∈ I} of sets is a function f: I → ∪A_i with f(i) ∈ A_i for each i. Elements of the Cartesian product are choice functions.

# Core Definition
A **choice function** is any function f: I → ∪_{i∈I} A_i such that f(i) ∈ A_i for all i ∈ I (Definition (1), p. 905). Each choice function picks one element from each set A_i.

# Prerequisites
This is a foundational concept with no prerequisites within this source.

# Relationships
## Related
- **cartesian-product** — Elements are choice functions
- **axiom-of-choice** — Asserts existence of choice functions for nonempty sets

# Source Reference
Appendix I, Section 1, Definition (1), page 905.

# Verification Notes
- Confidence: HIGH — explicit definition
