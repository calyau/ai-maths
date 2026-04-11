---
concept: Natural Transformation
slug: natural-transformation
category: category-theory
subcategory: basic-concepts
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Appendix II: Category Theory"
chapter_number: null
pdf_page: 917
section: "2. Natural Transformations and Universals"
extraction_confidence: high
aliases:
  - "morphism of functors"
  - "natural isomorphism"
prerequisites:
  - functor
extends: []
related:
  - equivalence-of-categories
contrasts_with: []
answers_questions:
  - "What is a natural transformation?"
  - "What makes a map 'natural'?"
---

# Quick Definition
A natural transformation η from functor F to functor G assigns to each object A a morphism η_A: FA → GA such that for every morphism f: A → B, the diagram G(f)η_A = η_B F(f) commutes. If each η_A is an isomorphism, η is a natural isomorphism.

# Core Definition
Let F, G be covariant functors from C to D. A **natural transformation** η from F to G assigns to each object A in C a morphism η_A ∈ Hom_D(FA,GA) such that for every f ∈ Hom_C(A,B), the diagram commutes: G(f)η_A = η_B F(f) (Definition, p. 917). If each η_A is an isomorphism, η is called a **natural isomorphism**.

# Prerequisites
- **functor** — Natural transformations are between functors

# Key Properties
1. Commutativity condition: G(f) ∘ η_A = η_B ∘ F(f) for all f
2. Natural isomorphism means each component is an isomorphism
3. Gives precise meaning to "natural" (coordinate-free) maps

# Examples
**Example** (p. 919): The canonical map V → V** (double dual) for finite-dimensional vector spaces is a natural isomorphism from the identity functor to the double dual functor.

**Example** (p. 919): The determinant det: GL_n(R) → R× is a natural transformation from the functor GL_n to the units functor.

# Relationships
## Builds Upon
- **functor** — Natural transformations are between functors

## Enables
- **equivalence-of-categories** — Defined using natural isomorphisms

# Source Reference
Appendix II, Section 2, Definition and Examples, pages 917-920.

# Verification Notes
- Confidence: HIGH — explicit definition with commutative diagram and examples
