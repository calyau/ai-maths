---
concept: Jordan Decomposition in Algebraic Groups
slug: jordan-decomposition
category: group-structure
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 131
section: "10b Application to Jordan decompositions"
extraction_confidence: high
aliases:
  - multiplicative Jordan decomposition
  - semisimple-unipotent decomposition
prerequisites:
  - reconstruction-theorem
  - semisimple-endomorphism
  - unipotent-endomorphism
extends: []
related:
  - unipotent-group
  - group-of-multiplicative-type
contrasts_with: []
answers_questions:
  - "How do I determine the Jordan decomposition of an element?"
  - "What is the Jordan decomposition in an algebraic group?"
---

# Quick Definition

For an algebraic group G over a perfect field k, every element g in G(k) has a unique Jordan decomposition g = g_s g_u = g_u g_s where g_s is semisimple and g_u is unipotent, meaning r(g_s) is semisimple and r(g_u) is unipotent for every representation r.

# Core Definition

*Theorem 10.18*: Let G be an algebraic group over a perfect field k. For any g in G(k), there exist unique elements g_s, g_u in G(k) such that r_V(g_s) = r_V(g)_s and r_V(g_u) = r_V(g)_u for all representations (V, r_V) of G. Furthermore, g = g_s g_u = g_u g_s. The elements g_s and g_u are called the *semisimple* and *unipotent parts* of g, and g = g_s g_u is the *(multiplicative) Jordan decomposition* of g (Milne, pp. 134-135).

# Prerequisites

- **Reconstruction theorem** -- The families (r_V(g)_s) and (r_V(g)_u) define elements of G(k) via the reconstruction theorem
- **Semisimple endomorphism** -- g_s is semisimple in all representations
- **Unipotent endomorphism** -- g_u is unipotent in all representations

# Key Properties

1. Existence and uniqueness over any perfect field (Theorem 10.18)
2. g_s and g_u commute: g = g_s g_u = g_u g_s
3. The decomposition is functorial: homomorphisms preserve Jordan decompositions (10.20)
4. To check a decomposition g = g_s g_u, it suffices to verify in a single faithful representation (10.19)
5. Each of alpha_s and alpha_u is a polynomial in alpha (for endomorphisms of finite-dimensional spaces)
6. The decomposition fails over non-perfect fields (Example 10.16)

# Construction / Recognition

## To Construct (for g in G(k)):
1. Choose a faithful representation r: G -> GL_V
2. Compute the Jordan decomposition r(g) = A_s A_u in GL(V)
3. By the reconstruction theorem, A_s = r(g_s) and A_u = r(g_u) for unique g_s, g_u in G(k)

## To Recognize:
1. g is semisimple iff g = g_s (equivalently, r(g) is semisimple for all/one faithful representation r)
2. g is unipotent iff g = g_u (equivalently, r(g) is unipotent for all/one faithful representation r)

# Context & Application

The Jordan decomposition is the multiplicative (group-theoretic) analogue of the additive Jordan decomposition in Lie algebras. It separates the "diagonalizable" and "nilpotent" aspects of group elements, which is fundamental to the structure theory of algebraic groups.

# Examples

**Example 1** (p. 133): For GL_n, the Jordan decomposition of a matrix A is A = A_s A_u where A_s is the semisimple part (diagonalizable after base change) and A_u is unipotent (eigenvalues all 1). The semisimple part A_s can be found using the Chinese Remainder Theorem on the characteristic polynomial.

**Example 2** (p. 134): Over a non-perfect field k of characteristic 2, the matrix ((0,1),(a,0)) with a not a square in k has no Jordan decomposition in M_2(k), illustrating the necessity of the perfect field hypothesis.

# Relationships

## Builds Upon
- **Reconstruction theorem** -- Provides existence and uniqueness
- **Semisimple endomorphism** -- Defines the semisimple part
- **Unipotent endomorphism** -- Defines the unipotent part

## Enables
- **Unipotent group** -- Groups consisting entirely of unipotent elements
- **Group of multiplicative type** -- Groups whose elements are all semisimple

# Common Errors

- **Error**: Attempting Jordan decomposition over a non-perfect field
  **Correction**: The decomposition requires k to be perfect; it can fail otherwise (Example 10.16)

# Common Confusions

- **Confusion**: Confusing the multiplicative Jordan decomposition (in groups) with the additive one (in Lie algebras)
  **Clarification**: In groups, g = g_s g_u (multiplicative); in Lie algebras, x = x_s + x_n (additive). The Lie algebra version appears in Chapter II.

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 10b, pages 131-136. Theorems 10.12, 10.17, 10.18.

# Verification Notes

- Definition source: Direct from Theorem 10.18
- Confidence rationale: Major theorem with complete proof
- Uncertainties: None
- Cross-reference status: Verified
