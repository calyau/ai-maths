---
concept: Affine k-Algebra
slug: affine-k-algebra
category: algebraic-geometry
subcategory: affine-geometry
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Commutative Rings and Algebraic Geometry"
chapter_number: 15
pdf_page: 740
section: "15.5 The Prime Spectrum of a Ring"
extraction_confidence: high
aliases: []
prerequisites:
  - finitely-generated-k-algebra
  - affine-algebraic-set
extends: []
related:
  - coordinate-ring
contrasts_with: []
answers_questions:
  - "What is an affine k-algebra?"
---

# Quick Definition
An affine k-algebra is a finitely generated algebra over an algebraically closed field k with no nonzero nilpotent elements. These are exactly the coordinate rings of affine algebraic sets.

# Core Definition
A finitely generated algebra over an algebraically closed field k having no nonzero nilpotent elements is called an **affine k-algebra** (Definition, p. 740). These are precisely the rings k[V] for affine algebraic sets V. The category of affine algebraic sets with morphisms is equivalent to the category of affine k-algebras with k-algebra homomorphisms (p. 740).

# Prerequisites
- **finitely-generated-k-algebra** — Must be finitely generated over k
- **affine-algebraic-set** — Affine k-algebras are coordinate rings

# Key Properties
1. Affine k-algebras = coordinate rings of affine algebraic sets
2. No nonzero nilpotents ↔ corresponding ideal is radical
3. Categories of algebraic sets and affine k-algebras are equivalent

# Relationships
## Builds Upon
- **coordinate-ring** — Affine k-algebras are coordinate rings

# Source Reference
Chapter 15, Section 15.5, Definition and equivalence of categories, pages 740-741.

# Verification Notes
- Confidence: HIGH — explicit definition with categorical equivalence
