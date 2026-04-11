---
concept: Morphism of Algebraic Sets
slug: morphism-of-algebraic-sets
category: algebraic-geometry
subcategory: affine-geometry
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Commutative Rings and Algebraic Geometry"
chapter_number: 15
pdf_page: 675
section: "15.1 Noetherian Rings and Affine Algebraic Sets"
extraction_confidence: high
aliases:
  - "polynomial map"
  - "regular map"
prerequisites:
  - affine-algebraic-set
  - coordinate-ring
extends: []
related:
  - isomorphism-of-algebraic-sets
contrasts_with: []
answers_questions:
  - "What is a morphism between affine algebraic sets?"
---

# Quick Definition
A morphism φ: V → W of affine algebraic sets is a map defined by polynomials. Morphisms correspond bijectively to k-algebra homomorphisms k[W] → k[V].

# Core Definition
A map φ: V → W is called a **morphism** (or polynomial map or regular map) of algebraic sets if there are polynomials φ_1,...,φ_m such that φ((a_1,...,a_n)) = (φ_1(a_1,...,a_n),...,φ_m(a_1,...,a_n)) for all points in V (Definition, p. 676). The map φ induces a k-algebra homomorphism φ̃: k[W] → k[V] defined by φ̃(f) = f ∘ φ. Theorem 6 establishes a bijective correspondence between morphisms V → W and k-algebra homomorphisms k[W] → k[V].

# Prerequisites
- **affine-algebraic-set** — Domain and codomain are algebraic sets
- **coordinate-ring** — Morphisms induce homomorphisms of coordinate rings

# Key Properties
1. Every morphism induces a k-algebra homomorphism of coordinate rings (contravariant)
2. Every k-algebra homomorphism k[W] → k[V] arises from a unique morphism V → W
3. φ is an isomorphism iff φ̃ is a k-algebra isomorphism
4. Composition of morphisms corresponds to reversed composition of k-algebra homomorphisms

# Context & Application
The contravariant correspondence between geometry (morphisms) and algebra (k-algebra homomorphisms) is fundamental. It means questions about maps between geometric objects can be answered purely algebraically.

# Examples
**Example** (p. 677): The map φ(a) = (a^2, a^3) from A^1 to Z(x^3-y^2) is a bijective morphism that is NOT an isomorphism, since the induced map on coordinate rings is not surjective.

# Relationships
## Builds Upon
- **coordinate-ring** — Morphisms are detected by coordinate ring homomorphisms

## Enables
- **isomorphism-of-algebraic-sets** — Isomorphisms are bijective morphisms with polynomial inverses

# Source Reference
Chapter 15, Section 15.1, Definition and Theorem 6, pages 675-677.

# Verification Notes
- Confidence: HIGH — Theorem 6 is stated and proved explicitly
