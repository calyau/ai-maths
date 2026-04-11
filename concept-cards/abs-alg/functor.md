---
concept: Functor
slug: functor
category: category-theory
subcategory: basic-concepts
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Appendix II: Category Theory"
chapter_number: null
pdf_page: 913
section: "1. Categories and Functors"
extraction_confidence: high
aliases:
  - "covariant functor"
  - "contravariant functor"
prerequisites:
  - category
extends: []
related:
  - natural-transformation
  - forgetful-functor
contrasts_with: []
answers_questions:
  - "What is a functor?"
  - "What is the difference between covariant and contravariant functors?"
---

# Quick Definition
A covariant functor F: C → D maps objects and morphisms between categories, preserving composition and identities. A contravariant functor reverses the direction of morphisms.

# Core Definition
A **covariant functor** F from C to D assigns: (a) to each object A in C an object FA in D, (b) to each f ∈ Hom_C(A,B) a morphism F(f) ∈ Hom_D(FA,FB), satisfying (i) F(gf) = F(g)F(f) and (ii) F(1_A) = 1_{FA} (Definition, p. 913). A **contravariant functor** reverses arrows: F(f) ∈ Hom_D(FB,FA) and F(gf) = F(f)F(g). A functor is **faithful** if injective on Hom sets, **full** if surjective.

# Prerequisites
- **category** — Functors map between categories

# Key Properties
1. Covariant: preserves direction of morphisms
2. Contravariant: reverses direction
3. Faithful: injective on Hom sets
4. Full: surjective on Hom sets

# Examples
**Example** (p. 914): The forgetful functor Grp → Set "forgets" the group structure. The abelianizing functor Grp → Ab sends G to G/G'. The Hom functor Hom(D,_) is covariant; Hom(_,D) is contravariant. The tensor product D ⊗_ is a covariant functor.

# Relationships
## Builds Upon
- **category** — Domain and codomain are categories

## Enables
- **natural-transformation** — Maps between functors

# Source Reference
Appendix II, Section 1, Definition and Examples, pages 913-916.

# Verification Notes
- Confidence: HIGH — explicit definition with many examples
