---
# === CORE IDENTIFICATION ===
concept: Representable Functor
slug: representable-functor

# === CLASSIFICATION ===
category: algebraic-groups
subcategory: category-theory
tier: foundational

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 21
section: "Some category theory"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - yoneda-lemma
extends: []
related:
  - coordinate-ring
  - affine-group
  - affine-algebraic-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine algebraic group?"
  - "What must I know before understanding Hopf algebras?"
---

# Quick Definition

A functor F: A -> Set is representable if it is isomorphic to h^A = Hom(A, -) for some object A. A pair (A, a) with a in F(A) represents F if the corresponding natural transformation T_a: h^A -> F is an isomorphism.

# Core Definition

A functor F: A -> Set is said to be **representable** if it is isomorphic to h^A for some object A (2.3, p. 21). A pair (A, a), a in F(A), is said to **represent** F if T_a: h^A -> F is an isomorphism, where T_a is the natural transformation given by the Yoneda lemma. If F is representable, say F is isomorphic to h^A, then the choice of isomorphism T: h^A -> F determines an element a_T in F(A) such that (A, a_T) represents F.

In the context of algebraic groups, the key category is Alg_k (commutative k-algebras), and a representable functor Alg_k -> Set is one of the form R -> Hom_{k-alg}(A, R) for a k-algebra A.

# Prerequisites

- **Yoneda lemma** — Establishes the bijection between natural transformations h^A -> F and elements of F(A)

# Key Properties

1. If F is representable by A, the representing object A is unique up to unique isomorphism (by the Yoneda lemma, 2.2)
2. The functors Alg_k -> Set defined by sets of polynomials are exactly the representable functors (2.16, p. 25)
3. A representable functor to groups gives an affine group; representable by a finitely generated algebra gives an algebraic group

# Construction / Recognition

## To Construct:
1. Given a k-algebra A, the functor h^A: R -> Hom_{k-alg}(A, R) is representable by definition
2. For a set S of polynomials in k[X_1,...,X_n], the zero-set functor R -> S(R) is representable by k[X_1,...,X_n]/(S)

## To Recognize:
1. A functor F: Alg_k -> Set is representable if there exists a k-algebra A with F isomorphic to Hom_{k-alg}(A, -)
2. Use the representability criterion (Theorem 2.20): F is representable if it satisfies sheaf condition (*) and becomes representable after a faithfully flat base change

# Context & Application

Representability is the fundamental concept bridging algebra and geometry in the theory of algebraic groups. An affine algebraic group is precisely a functor Alg_k -> Grp whose underlying functor to Set is representable by a finitely generated k-algebra. This approach, originating with Demazure-Gabriel, allows a uniform treatment over arbitrary base rings.

# Examples

**Example 1** (p. 19): The functor R -> SL_n(R) is representable by k[X_11,...,X_nn]/(det(X_ij) - 1).

**Example 2** (p. 22): The functor R -> R (underlying additive group) is representable by k[X].

# Relationships

## Enables
- **Affine group** — A functor to groups representable as a functor to sets defines an affine group
- **Coordinate ring** — The representing algebra is the coordinate ring

## Related
- **Yoneda lemma** — The theoretical foundation for representability

# Common Confusions

- **Confusion**: Thinking representability of the functor to Grp is required
  **Clarification**: Only the underlying functor to Set needs to be representable; the group structure is additional data encoded in the comultiplication

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 2b "Some category theory", 2.3, p. 21.

# Verification Notes

- Definition source: Direct from 2.3, p. 21
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
