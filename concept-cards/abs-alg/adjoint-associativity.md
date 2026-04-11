---
concept: Adjoint Associativity
slug: adjoint-associativity
category: module-theory
subcategory: exact-sequences
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Module Theory"
chapter_number: 10
pdf_page: 416
section: "10.5 Exact Sequences"
extraction_confidence: high
aliases:
  - "Hom-tensor adjunction"
  - "tensor-hom adjunction"
prerequisites:
  - tensor-product
  - module-homomorphism
extends: []
related:
  - flat-module
  - projective-module
contrasts_with: []
answers_questions:
  - "What is the adjoint associativity theorem?"
---

# Quick Definition
Adjoint Associativity is the natural isomorphism $\text{Hom}_S(A \otimes_R B, C) \cong \text{Hom}_R(A, \text{Hom}_S(B, C))$, relating tensor products and Hom.

# Core Definition
(Theorem 43) Let R and S be rings, A a right R-module, B an (R,S)-bimodule, and C a right S-module. Then $\text{Hom}_S(A \otimes_R B, C) \cong \text{Hom}_R(A, \text{Hom}_S(B, C))$ as abelian groups. If $R = S$ is commutative, this is an R-module isomorphism (Dummit & Foote, Theorem 43, p. 416).

# Prerequisites
- **tensor-product** — One side involves tensor product
- **module-homomorphism** — The other side involves Hom

# Key Properties
1. Shows tensor product and Hom are adjoint functors
2. Can be used to give alternate proofs of right exactness of tensor
3. Implies the tensor product of projective modules is projective

# Context & Application
This is a fundamental result connecting the tensor product and Hom functors, and is the basis for many results in homological algebra.

# Relationships
## Builds Upon
- **tensor-product**, **module-homomorphism**

## Enables
- Alternate proof that tensor is right exact
- Tensor product of projective modules is projective (Corollary 44)

# Source Reference
Chapter 10, Section 10.5, Theorem 43, pp. 416-417.

# Verification Notes
- Confidence: HIGH — explicit theorem with proof
