---
concept: Equivalence of Categories
slug: equivalence-of-categories
category: category-theory
subcategory: basic-concepts
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Appendix II: Category Theory"
chapter_number: null
pdf_page: 920
section: "2. Natural Transformations and Universals"
extraction_confidence: high
aliases: []
prerequisites:
  - functor
  - natural-transformation
extends: []
related:
  - category
contrasts_with: []
answers_questions:
  - "What does it mean for two categories to be equivalent?"
---

# Quick Definition
Categories C and D are equivalent if there are functors F: C → D and G: D → C such that GF is naturally isomorphic to the identity on C and FG is naturally isomorphic to the identity on D.

# Core Definition
Categories C and D are **equivalent** if there are functors F from C to D and G from D to C such that GF ≅ I_C and FG ≅ I_D as natural isomorphisms (Definition, p. 920). This is weaker than isomorphism of categories (where GF = I_C and FG = I_D exactly). For example, Z-Mod and Ab are isomorphic categories. The categories of affine algebraic sets and affine k-algebras are equivalent (p. 920).

# Prerequisites
- **functor** — F and G are functors
- **natural-transformation** — The comparison uses natural isomorphisms

# Key Properties
1. Weaker than isomorphism of categories
2. Reflexive, symmetric, and transitive
3. Affine algebraic sets ≡ affine k-algebras (over algebraically closed k)
4. R-Mod ≡ M_{n×n}(R)-Mod for commutative R

# Source Reference
Appendix II, Section 2, Definition and examples, page 920.

# Verification Notes
- Confidence: HIGH — explicit definition with examples
