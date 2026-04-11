---
concept: Category
slug: category
category: category-theory
subcategory: basic-concepts
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Appendix II: Category Theory"
chapter_number: null
pdf_page: 911
section: "1. Categories and Functors"
extraction_confidence: high
aliases: []
prerequisites: []
extends: []
related:
  - functor
  - natural-transformation
  - morphism
contrasts_with: []
answers_questions:
  - "What is a category?"
---

# Quick Definition
A category C consists of a class of objects and sets of morphisms between them, with composition of morphisms that is associative and has identities.

# Core Definition
A **category** C consists of a class of objects and sets of morphisms. For every pair A, B of objects there is a set Hom_C(A,B) of morphisms from A to B, with composition Hom(A,B) × Hom(B,C) → Hom(A,C) satisfying: (i) disjointness of Hom sets for distinct pairs, (ii) associativity of composition, (iii) existence of identity morphisms 1_A for each object A (Definition, p. 911).

# Prerequisites
This concept requires only basic mathematical maturity (set theory).

# Key Properties
1. Composition is associative
2. Identity morphisms are unique
3. Isomorphism: f: A → B with inverse g: B → A such that gf = 1_A, fg = 1_B
4. A subcategory has a subclass of objects with containment of Hom sets

# Examples
**Example** (p. 912): **Set** = category of sets with functions. **Grp** = groups with homomorphisms. **Ab** = abelian groups. **Ring** = rings with 1. **R-mod** = left R-modules. **Top** = topological spaces with continuous maps.

# Relationships
## Enables
- **functor** — Maps between categories
- **natural-transformation** — Maps between functors

# Source Reference
Appendix II, Section 1, Definition and Examples, pages 911-913.

# Verification Notes
- Confidence: HIGH — explicit definition with many examples
