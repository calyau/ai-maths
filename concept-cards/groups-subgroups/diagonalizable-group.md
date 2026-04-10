---
concept: Diagonalizable Group
slug: diagonalizable-group
category: multiplicative-groups
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 165
section: "14d Diagonalizable groups"
extraction_confidence: high
aliases:
  - split group of multiplicative type
prerequisites:
  - group-like-element
  - character-of-affine-group
extends: []
related:
  - group-of-multiplicative-type
  - split-torus
  - group-algebra-functor
contrasts_with:
  - unipotent-group
answers_questions:
  - "What is a diagonalizable algebraic group?"
---

# Quick Definition

An affine group G is diagonalizable if the group-like elements in O(G) span it as a k-vector space. Equivalently, G is isomorphic to D(M) for some abelian group M, where D(M)(R) = Hom(M, R^x). Every representation of a diagonalizable group decomposes into eigenspaces.

# Core Definition

An affine group G is *diagonalizable* if the group-like elements in O(G) span it as a k-vector space (Definition 14.9). Equivalently (Theorem 14.10), G is isomorphic to D(M) for some commutative group M. The functor M -> D(M) is a contravariant equivalence from commutative groups to diagonalizable affine groups, with quasi-inverse G -> X(G) (Theorem 14.12). Under this equivalence, exact sequences of groups correspond to exact sequences of diagonalizable groups (with arrows reversed). The equivalent characterizations of diagonalizability are: G is diagonalizable iff every representation is diagonalizable iff V = direct-sum V_chi for every representation V (Theorem 14.15, Milne, pp. 165-169).

# Prerequisites

- **Group-like element** -- G is diagonalizable iff group-like elements span O(G)
- **Character of affine group** -- X(G) classifies diagonalizable groups

# Key Properties

1. M -> D(M) is a contravariant equivalence (Theorem 14.12)
2. D(M) is algebraic iff M is finitely generated
3. D(M) is connected iff M has only p-torsion (p = char. exponent)
4. D(M) is smooth iff M has no p-torsion
5. Every representation decomposes as direct sum of eigenspaces (Theorem 14.15)
6. Subgroups and quotients of diagonalizable groups are diagonalizable
7. Rep(D(M)) is semisimple with simple objects indexed by elements of M

# Construction / Recognition

## To Construct D(M):
1. Form the group algebra k[M] with basis M
2. Set Delta(m) = m tensor m, epsilon(m) = 1, S(m) = m^{-1} for m in M
3. D(M)(R) = Hom_{groups}(M, R^x)

## To Recognize:
1. Check if O(G) is spanned by its group-like elements
2. Equivalently, check if every representation is a direct sum of 1-dimensional representations

# Context & Application

Diagonalizable groups are the algebraic groups whose representation theory is completely transparent: every representation decomposes into characters. They are the "split" forms of groups of multiplicative type.

# Examples

**Example 1** (p. 164): D(Z) = G_m: the group algebra k[Z] = k[X, X^{-1}] is the coordinate ring of G_m.

**Example 2** (p. 164): D(Z/nZ) = mu_n: k[Z/nZ] = k[x]/(x^n - 1).

**Example 3** (p. 167): D(Z^n) = G_m^n: the n-dimensional split torus.

# Relationships

## Builds Upon
- **Group-like element** -- Spanning condition defines diagonalizability
- **Character of affine group** -- X(G) = M is the classifying data

## Enables
- **Split torus** -- A connected diagonalizable algebraic group
- **Group of multiplicative type** -- Groups that become diagonalizable over k^sep

## Contrasts With
- **Unipotent group** -- Has no nontrivial characters

# Common Confusions

- **Confusion**: Thinking diagonalizable means "can be put in diagonal form over k"
  **Clarification**: Diagonalizable means O(G) is spanned by group-like elements; it is the split form. Groups of multiplicative type may only become diagonalizable over a field extension.

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 14d, pages 165-169. Definition 14.9, Theorems 14.10, 14.12, 14.15.

# Verification Notes

- Definition source: Direct from Definition 14.9
- Confidence rationale: Explicit definition with multiple equivalent characterizations
- Uncertainties: None
- Cross-reference status: Verified
