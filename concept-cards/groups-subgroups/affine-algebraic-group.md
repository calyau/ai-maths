---
# === CORE IDENTIFICATION ===
concept: Affine Algebraic Group
slug: affine-algebraic-group

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
pdf_page: 18
section: "Definitions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - algebraic group
  - linear algebraic group

# === TYPED RELATIONSHIPS ===
prerequisites:
  - representable-functor
  - coordinate-ring
extends:
  - affine-group
related:
  - hopf-algebra
  - affine-group-scheme
  - general-linear-group
contrasts_with:
  - abelian-variety
  - affine-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine algebraic group?"
  - "What distinguishes an algebraic group from a group scheme?"
  - "How does a Hopf algebra relate to an affine algebraic group?"
---

# Quick Definition

An affine algebraic group is an affine group whose coordinate ring is finitely presented as a k-algebra. Equivalently, it is a functor from k-algebras to groups that is representable by a finitely generated k-algebra.

# Core Definition

An affine group G = (A, Delta) is called an **affine algebraic group** when the coordinate ring O(G) = A is finitely presented (Definition 2.9, p. 22). Since any finitely presented k-algebra is isomorphic to k[X_1,...,X_n]/a for some finitely generated ideal a, the functor G is "defined by polynomials" in a precise sense (2.13, p. 23).

Starting from Section 2g (p. 29), Milne abbreviates "affine algebraic group" to simply "algebraic group". These groups are also called **linear algebraic groups** because they are exactly the algebraic groups that can be realized as a closed subgroup of GL_n for some n (p. 15).

Note: Unlike some older treatments, Milne allows nilpotent elements in coordinate rings. The coordinate ring need not be reduced.

# Prerequisites

- **Representable functor** — An algebraic group is defined as a representable functor from k-algebras to groups
- **Coordinate ring** — The finitely presented k-algebra O(G) that represents the group functor
- **Commutative k-algebra** — The ground category from which the functor takes values

# Key Properties

1. O(G) is a finitely presented k-algebra (equivalently, finitely generated when k is noetherian, by the Hilbert basis theorem)
2. The group law, identity, and inverse are all described by polynomials
3. Can always be embedded as a closed subgroup of GL_n for some n
4. The category of affine algebraic groups is equivalent to the opposite of the category of finitely generated Hopf algebras over k (Summary 6.11, p. 59)
5. Every algebraic group over a field of characteristic zero is smooth (Cartier's theorem, 6.31)

# Construction / Recognition

## To Construct:
1. Start with a finitely generated k-algebra A = k[X_1,...,X_n]/(f_1,...,f_m)
2. Define a comultiplication Delta: A -> A tensor A (encoding the group multiplication)
3. Verify that h^A(R) acquires a group structure for all k-algebras R
4. Equivalently, provide epsilon: A -> k (coidentity) and S: A -> A (coinverse) making A a Hopf algebra

## To Recognize:
1. Check that the functor is from k-algebras to groups (not just sets)
2. Verify representability by a finitely generated k-algebra
3. Alternatively, check that the coordinate ring is a finitely generated commutative Hopf algebra

# Context & Application

Affine algebraic groups are the central objects of study in the theory of algebraic groups. They encompass finite groups (realized as constant algebraic groups), classical matrix groups (GL_n, SL_n, Sp_n, O_n), tori, and unipotent groups. The functor-of-points approach adopted by Milne (following Demazure-Gabriel and Waterhouse) allows working over arbitrary base rings, not just algebraically closed fields.

The theory of affine algebraic groups subsumes both the theory of finite groups and the theory of Lie groups (via algebraic groups over R or C).

# Examples

**Example 1** (p. 14): SL_n is an affine algebraic group with coordinate ring k[X_11,...,X_nn]/(det(X_ij) - 1). The group law is matrix multiplication, which is polynomial in the entries.

**Example 2** (p. 22): The additive group G_a has coordinate ring k[X] with Delta(X) = X tensor 1 + 1 tensor X. Then G_a(R) = (R, +).

**Example 3** (p. 29): The multiplicative group G_m has coordinate ring k[X, X^{-1}] with Delta(X) = X tensor X. Then G_m(R) = R^x.

# Relationships

## Builds Upon
- **Affine group** — An affine algebraic group is an affine group with finitely presented coordinate ring
- **Representable functor** — The underlying functor to sets must be representable

## Enables
- **Hopf algebra** — The coordinate ring of an algebraic group is a Hopf algebra
- **Affine group scheme** — Algebraic groups give group objects in the category of affine schemes
- **Affine subgroup** — Subgroups defined by Hopf ideals

## Related
- **General linear group** — The prototypical example; every algebraic group embeds in GL_n
- **Special linear group** — Key example with coordinate ring k[X_ij]/(det - 1)

## Contrasts With
- **Abelian variety** — Connected algebraic groups that are projective (not affine) as varieties
- **Affine group** — More general: coordinate ring need not be finitely generated

# Common Errors

- **Error**: Assuming the coordinate ring must be reduced (no nilpotents)
  **Correction**: Milne explicitly allows nilpotent elements; mu_p in characteristic p has O(mu_p) = k[X]/(X^p - 1) which may have nilpotents

- **Error**: Confusing an algebraic group with its group of k-rational points G(k)
  **Correction**: The algebraic group is the entire functor R -> G(R), not just the value at k

# Common Confusions

- **Confusion**: Thinking "algebraic group" and "group variety" are the same
  **Clarification**: An algebraic group is a group scheme (possibly with nilpotents); a group variety requires the coordinate ring to be geometrically reduced (an affine k-algebra)

- **Confusion**: Believing algebraic groups must be smooth
  **Clarification**: In characteristic zero they are always smooth (Cartier's theorem), but in characteristic p there exist non-smooth algebraic groups like alpha_p and mu_p

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 2 "Definitions", pages 18-29. Key definitions at 2.9 (p. 22) and 2.16 (p. 25). Terminology convention at 2g (p. 29).

# Verification Notes

- Definition source: Direct from Definition 2.9, p. 22
- Confidence rationale: Explicit definition with extensive discussion
- Uncertainties: None
- Cross-reference status: Verified against planned extractions
