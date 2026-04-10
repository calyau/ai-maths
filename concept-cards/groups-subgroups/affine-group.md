---
# === CORE IDENTIFICATION ===
concept: Affine Group
slug: affine-group

# === CLASSIFICATION ===
category: algebraic-groups
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 22
section: "Definition of an affine (algebraic) group"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - affine group over k

# === TYPED RELATIONSHIPS ===
prerequisites:
  - coordinate-ring
  - comultiplication
extends: []
related:
  - affine-algebraic-group
  - hopf-algebra
  - representable-functor
contrasts_with:
  - affine-algebraic-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine algebraic group?"
  - "What distinguishes an algebraic group from a group scheme?"
---

# Quick Definition

An affine group over k is a k-algebra A together with a comultiplication Delta: A -> A tensor A such that h^A(R) = Hom_{k-alg}(A, R) is a group for all k-algebras R. When A is finitely presented, it is called an affine algebraic group.

# Core Definition

An **affine group** over k is a k-algebra A together with a homomorphism Delta: A -> A tensor A such that, for any k-algebra R, the binary operation on h^A(R) defined by f_1 * f_2 = (f_1, f_2) composed with Delta makes h^A(R) into a group (Definition 2.9, p. 22).

The ring A is called the **coordinate ring** (or coordinate algebra) of G and is denoted O(G). The map Delta is called the **comultiplication** of G. A homomorphism of affine groups (A, Delta) -> (A', Delta') is a k-algebra homomorphism alpha: A' -> A such that Delta composed with alpha = (alpha tensor alpha) composed with Delta'.

# Prerequisites

- **Coordinate ring** — The k-algebra A = O(G) that defines the affine group
- **Comultiplication** — The structure map Delta: A -> A tensor A encoding the group law
- **Tensor product of k-algebras** — Needed to define products and comultiplication

# Key Properties

1. An affine group is equivalently a functor Alg_k -> Grp whose underlying functor to Set is representable (Theorem 2.14, p. 24)
2. The coordinate ring O(G) carries a natural Hopf algebra structure (Theorem 5.18, p. 46)
3. Homomorphisms of affine groups correspond contravariantly to Hopf algebra homomorphisms
4. An element f of O(G) is a family of functions f_R: G(R) -> R, natural in R

# Construction / Recognition

## To Construct:
1. Choose a k-algebra A
2. Define Delta: A -> A tensor A (a k-algebra homomorphism)
3. Verify that h^A(R) is a group under the operation (f_1, f_2) -> (f_1, f_2) composed with Delta, for all k-algebras R
4. Alternatively, provide epsilon: A -> k and S: A -> A making (A, Delta, epsilon, S) a Hopf algebra

## To Recognize:
1. A pair (A, Delta) where A is a k-algebra and Delta is a k-algebra homomorphism A -> A tensor A
2. The associated functor R -> Hom(A, R) takes values in groups

# Context & Application

The notion of an affine group (without the finiteness condition on A) is more general than an affine algebraic group. This generality is needed for pro-algebraic groups (inverse limits of algebraic groups) and for working over base rings rather than fields.

# Examples

**Example 1** (p. 22): The additive group G_a = (k[X], Delta) with Delta(X) = X tensor 1 + 1 tensor X. Then h^A(R) is isomorphic to (R, +).

**Example 2** (p. 22-23): For a commutative group M, the group algebra kM with Delta(m) = m tensor m gives an affine group with h^A(R) = Hom_group(M, R^x).

# Relationships

## Builds Upon
- **Coordinate ring** — O(G) is the representing k-algebra

## Enables
- **Affine algebraic group** — The finitely presented case
- **Hopf algebra** — The coordinate ring of an affine group is a Hopf algebra

## Contrasts With
- **Affine algebraic group** — Requires O(G) to be finitely presented

# Common Errors

- **Error**: Forgetting that a homomorphism of affine groups reverses the direction of the algebra map
  **Correction**: A homomorphism G -> G' corresponds to alpha*: O(G') -> O(G), contravariantly

# Common Confusions

- **Confusion**: Thinking an affine group must have finitely generated coordinate ring
  **Clarification**: That additional condition defines an affine algebraic group; affine groups allow arbitrary k-algebras

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 2c "Definition of an affine (algebraic) group", Definition 2.9, p. 22.

# Verification Notes

- Definition source: Direct quote from Definition 2.9
- Confidence rationale: Explicit, clearly stated definition
- Uncertainties: None
- Cross-reference status: Verified
