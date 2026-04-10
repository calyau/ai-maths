---
# === CORE IDENTIFICATION ===
concept: Alpha p
slug: alpha-p

# === CLASSIFICATION ===
category: classical-groups
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 30
section: "Examples"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "\\alpha_p"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - affine-algebraic-group
  - additive-group
extends: []
related:
  - group-of-nth-roots-of-unity
contrasts_with:
  - group-of-nth-roots-of-unity

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine algebraic group?"
  - "What distinguishes an algebraic group from a group scheme?"
---

# Quick Definition

In characteristic p != 0, alpha_p is the algebraic group with alpha_p(R) = {r in R | r^p = 0} (additive group). Its coordinate ring is k[T]/(T^p), which has nilpotent elements -- a key example of a non-smooth algebraic group.

# Core Definition

Over a field k of characteristic p != 0, alpha_p is defined by the functor R -> alpha_p(R) = {r in R | r^p = 0}, which is an additive group (using the binomial theorem: (a+b)^p = a^p + b^p in characteristic p). It is an affine algebraic group with O(alpha_p) = k[T]/(T^p) (3.5, p. 30).

Note that alpha_p(K) = {0} for any field K containing k, but alpha_p is not the trivial group since O(alpha_p) = k[T]/(T^p) != k. This demonstrates that non-reduced algebraic groups can have trivial points over all fields (6.17, p. 61).

# Prerequisites

- **Affine algebraic group** — alpha_p is an algebraic group
- **Additive group** — alpha_p is a subgroup of G_a

# Key Properties

1. O(alpha_p) = k[T]/(T^p), which has nilpotent elements (T is nilpotent)
2. alpha_p is not smooth (not reduced)
3. alpha_p(K) = {0} for every field K, yet alpha_p is nontrivial
4. alpha_p is the kernel of the Frobenius map x -> x^p: G_a -> G_a (7.19, p. 77)
5. alpha_p is self-dual under Cartier duality: alpha_p^{vee} = alpha_p (Exercise 5-4)

# Examples

**Example 1** (p. 30): alpha_p(R) = {r in R | r^p = 0} for any k-algebra R in characteristic p.

**Example 2** (p. 77): alpha_p = Ker(x -> x^p: G_a -> G_a), showing that the pth power map on G_a is not injective.

# Relationships

## Builds Upon
- **Additive group** — alpha_p is a subgroup of G_a

## Contrasts With
- **Group of nth roots of unity** — mu_p is the multiplicative analogue; alpha_p is the additive analogue

# Common Confusions

- **Confusion**: Since alpha_p(K) = {0} for all fields K, one might think it is trivial
  **Clarification**: The functor is nontrivial because O(alpha_p) != k; alpha_p(R) can be nontrivial for non-reduced rings R

# Source Reference

Chapter I, 3.5 (p. 30), 6.17 (p. 61), 7.19 (p. 77).

# Verification Notes

- Definition source: Direct from 3.5
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
