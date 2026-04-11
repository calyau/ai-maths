---
concept: Affine Variety
slug: affine-variety
category: algebraic-geometry
subcategory: affine-geometry
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Commutative Rings and Algebraic Geometry"
chapter_number: 15
pdf_page: 702
section: "15.2 Radicals and Affine Varieties"
extraction_confidence: high
aliases:
  - "irreducible algebraic set"
prerequisites:
  - affine-algebraic-set
  - prime-ideal
extends:
  - affine-algebraic-set
related:
  - coordinate-ring
  - field-of-rational-functions
contrasts_with: []
answers_questions:
  - "What is an affine variety?"
  - "When is an algebraic set irreducible?"
---

# Quick Definition
An affine variety is a nonempty affine algebraic set V that is irreducible — it cannot be written as the union of two proper algebraic subsets. Equivalently, I(V) is a prime ideal.

# Core Definition
A nonempty affine algebraic set V is called **irreducible** if it cannot be written as V = V_1 ∪ V_2 where V_1 and V_2 are proper algebraic subsets of V. An irreducible affine algebraic set is called an affine **variety** (Definition, p. 702). By Proposition 17: (1) V is irreducible iff I(V) is a prime ideal, equivalently iff k[V] is an integral domain. (2) Every nonempty algebraic set has a unique decomposition into irreducible components.

# Prerequisites
- **affine-algebraic-set** — Varieties are special algebraic sets
- **prime-ideal** — Irreducibility corresponds to primality of I(V)

# Key Properties
1. V is a variety iff I(V) is prime iff k[V] is an integral domain
2. Every algebraic set decomposes uniquely into varieties (Proposition 17)
3. For a variety V, the field of fractions of k[V] is the field of rational functions k(V)
4. The dimension of V is the transcendence degree of k(V) over k
5. Single points are varieties of dimension 0
6. Lines and linear subsets are varieties

# Context & Application
Varieties are the building blocks of algebraic geometry — every algebraic set decomposes uniquely into them. The correspondence V ↔ prime ideal in k[V] is part of the Nullstellensatz dictionary.

# Examples
**Example** (p. 703): The x-axis Z(y) in R^2 is a variety (coordinate ring R[x] is a domain). The union of axes Z(xy) is NOT a variety: Z(xy) = Z(x) ∪ Z(y).

**Example** (p. 704): The hyperbola Z(xy-1) is a variety since k[x,1/x] is a domain, even though it has two disjoint branches.

# Relationships
## Builds Upon
- **affine-algebraic-set** — Varieties are irreducible algebraic sets

## Enables
- **field-of-rational-functions** — Defined for varieties as Frac(k[V])

# Source Reference
Chapter 15, Section 15.2, Definition and Proposition 17, pages 702-704.

# Verification Notes
- Confidence: HIGH — explicit definition and unique decomposition theorem
