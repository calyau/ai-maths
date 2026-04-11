---
concept: Vector Space
slug: vector-space
category: linear-algebra
subcategory: basic-definitions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Vector Spaces"
chapter_number: 11
pdf_page: 408
section: "11.1 Definitions and Basic Theory"
extraction_confidence: high
aliases:
  - "F-module"
  - "linear space"
prerequisites:
  - field
  - left-module
extends:
  - left-module
related:
  - basis
  - dimension
  - linear-transformation
  - subspace
contrasts_with:
  - left-module
answers_questions:
  - "What is a vector space?"
  - "How do modules generalize vector spaces?"
---

# Quick Definition
A vector space over a field F is an F-module, i.e., an abelian group V with scalar multiplication by elements of F satisfying the module axioms. Every vector space has a basis.

# Core Definition
When the ring R is a field F, the axioms for an R-module are precisely the axioms for a vector space over F. The terminology changes: module elements become vectors, ring elements become scalars, submodules become subspaces, module homomorphisms become linear transformations, finitely generated modules become finite dimensional vector spaces, rank becomes dimension, and free modules become vector spaces with bases (Dummit & Foote, p. 408).

# Prerequisites
- **field** — Scalars come from a field
- **left-module** — A vector space is a module over a field

# Key Properties
1. Every vector space has a basis (every F-module is free)
2. Any two bases of a vector space have the same cardinality
3. $V \cong F^n$ for any n-dimensional vector space V
4. dim V = dim W + dim V/W for any subspace W
5. A linear transformation between spaces of the same finite dimension is injective iff surjective iff an isomorphism

# Construction / Recognition
## To Construct:
1. Start with an abelian group V
2. Define scalar multiplication $F \times V \to V$
3. Verify the module axioms (automatically satisfied if V is an F-module)

# Context & Application
Vector spaces are the "nicest" modules. All the complications of general module theory (torsion, non-free modules) vanish over fields. The theory provides the foundation for linear algebra and serves as a prelude to field theory and Galois theory.

# Examples
**Example 1** (p. 409): F[x] is an infinite dimensional vector space over F with basis $1, x, x^2, \ldots$
**Example 2** (p. 409): The solution space of a linear ODE $y'' - 3y' + 2y = 0$ is a 2-dimensional space over $\mathbb{C}$ with basis $\{e^t, e^{2t}\}$.

# Relationships
## Builds Upon
- **field**, **left-module**

## Enables
- **basis**, **dimension**, **linear-transformation**, **dual-space**

## Contrasts With
- **left-module** — General modules may lack bases and have torsion

# Common Confusions
- **Confusion**: Thinking all module properties hold for vector spaces and vice versa. **Clarification**: Vector spaces are much "nicer": every subspace has a complement, every vector space is free/projective/injective/flat.

# Source Reference
Chapter 11, Section 11.1, pp. 408-414.

# Verification Notes
- Confidence: HIGH — foundational concept with explicit treatment
