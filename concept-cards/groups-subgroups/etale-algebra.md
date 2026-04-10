---
concept: Etale Algebra
slug: etale-algebra
category: group-structure
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 144
section: "12b Etale affine groups"
extraction_confidence: high
aliases:
  - etale k-algebra
prerequisites:
  - affine-algebraic-group
extends: []
related:
  - etale-affine-group
  - connected-component-group
contrasts_with: []
answers_questions:
  - "What is an etale algebra?"
---

# Quick Definition

A k-algebra A is etale if it is finite and is a product of separable field extensions of k. Equivalently, A tensor k^al is a product of copies of k^al, or A tensor k^al is reduced.

# Core Definition

A finite k-algebra A is *etale* if it satisfies the equivalent conditions (Proposition 12.2): (a) A is a product of separable field extensions of k; (b) A tensor k^al is a product of copies of k^al; (c) A tensor k^al is reduced (Definition 12.3). Etale algebras are classified by finite sets with continuous Galois action: A -> F(A) = Hom_{k-alg}(A, k^sep) is a contravariant equivalence from etale k-algebras to finite Gamma-sets (Theorem 12.7, Milne, pp. 144-147).

# Prerequisites

- **Affine algebraic group** -- Etale algebras arise as coordinate rings of etale groups and as pi_0(O(G))

# Key Properties

1. Products, tensor products, and quotients of etale algebras are etale (Proposition 12.4)
2. The composite of etale subalgebras is etale (Corollary 12.5)
3. Etale algebras are preserved by base field extension (Proposition 12.6)
4. Classified by finite sets with continuous Galois action (Theorem 12.7)
5. A finite k-algebra is etale iff it has no non-zero k-derivations (Exercise 12-1)

# Context & Application

Etale algebras provide the algebraic framework for understanding the "discrete" aspects of algebraic groups. The largest etale subalgebra pi_0(O(G)) of O(G) corresponds to the group of connected components.

# Examples

**Example 1** (p. 146): k[X]/(f(X)) is etale iff f has distinct roots in k^al. The decomposition into orbits of Gamma on the roots gives the factorization into irreducible factors.

# Relationships

## Enables
- **Etale affine group** -- O(G) etale defines etale groups
- **Connected component group** -- pi_0(O(G)) is the largest etale subalgebra

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 12b, pages 144-148. Definition 12.3, Theorem 12.7.

# Verification Notes

- Definition source: Direct from Definition 12.3
- Confidence rationale: Explicit definition with classification theorem
- Uncertainties: None
- Cross-reference status: Verified
