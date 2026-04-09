---
concept: Partially Ordered Set
slug: partially-ordered-set

category: set-theory-foundations
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Infinite Sets"
chapter_number: null
pdf_page: 367
section: null

extraction_confidence: high

aliases:
  - "poset"
  - "partial ordering"
  - "minimal element"
  - "maximal element"
  - "upper bound"

prerequisites: []
extends: []
related:
  - chain
  - well-ordered-set
  - zorns-lemma
  - antichain
contrasts_with: []

answers_questions:
  - "What is a partially ordered set?"
  - "What is a minimal/maximal element?"
  - "What is an upper bound?"
---

# Quick Definition
A partially ordered set (poset) is a set with a reflexive, antisymmetric, transitive relation. An element is minimal if nothing is below it, maximal if nothing is above it.

# Core Definition
An element x of a partially ordered set X is minimal in X if there is no y in X with y < x, and maximal if there is no z in X with x < z. A partially ordered set may have one or many elements that are maximal or minimal, or none at all. An upper bound in X of a subset Y is any x in X such that y <= x for all y in Y (Diestel, p. 358).

# Prerequisites
This is a foundational concept.

# Key Properties
1. May have zero, one, or many minimal/maximal elements
2. An upper bound of Y need not be in Y
3. A greatest element is both maximal and an upper bound for all
4. Some pairs of elements may be incomparable

# Construction / Recognition
## To Define a Poset
1. Specify a set X and a relation <=
2. Verify reflexivity (x <= x), antisymmetry (x <= y and y <= x implies x = y), and transitivity (x <= y and y <= z implies x <= z)

# Context & Application
Partially ordered sets provide the framework for Zorn's lemma and are used in the definition of well-orderings and tree-orders. They appear in Chapter 8 (Infinite Graphs) and Chapter 12 (Well-Quasi-Ordering).

# Relationships
## Enables
- **chain** — a totally ordered subset
- **well-ordered-set** — a chain where every non-empty subset has a minimum
- **zorns-lemma** — guarantees maximal elements under certain conditions
- **antichain** — pairwise incomparable elements

# Source Reference
Appendix A: Infinite Sets, page 358 (pdf p. 368).

# Verification Notes
- Direct from p. 358
- Confidence: HIGH
