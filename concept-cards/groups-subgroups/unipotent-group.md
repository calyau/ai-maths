---
concept: Unipotent Affine Group
slug: unipotent-group
category: unipotent-groups
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 176
section: "15 Unipotent affine groups"
extraction_confidence: high
aliases:
  - unipotent algebraic group
prerequisites:
  - linear-representation
  - unipotent-endomorphism
  - coconnected-hopf-algebra
extends: []
related:
  - trigonalizable-group
  - split-unipotent-group
contrasts_with:
  - group-of-multiplicative-type
  - diagonalizable-group
answers_questions:
  - "What is a unipotent group?"
  - "What distinguishes a unipotent group from a solvable group?"
---

# Quick Definition

An affine group G is unipotent if every nonzero representation has a nonzero fixed vector. Equivalently, G is isomorphic to a subgroup of U_n (upper unitriangular matrices) for some n. Equivalently, O(G) is coconnected as a Hopf algebra.

# Core Definition

An affine group G is *unipotent* if every nonzero representation of G has a nonzero fixed vector, i.e., a nonzero v in V with rho(v) = v tensor 1 (Definition 15.3). The equivalent characterizations for algebraic groups are (Theorem 15.6): (a) G is unipotent; (b) G is isomorphic to a subgroup of U_n for some n; (c) O(G) is coconnected (admits a filtration C_0 = k subset C_1 subset ... with union = A and Delta(C_r) subset sum C_i tensor C_{r-i}). The group G_a and its subgroups are unipotent. An algebraic group is unipotent iff it admits a subnormal series whose quotients are subgroups of G_a (Corollary 15.14, Milne, pp. 176-180).

# Prerequisites

- **Linear representation** -- Unipotence is defined via representations
- **Unipotent endomorphism** -- The linear algebra concept underlying unipotent groups
- **Coconnected Hopf algebra** -- The algebraic characterization

# Key Properties

1. Subgroups, quotients, and extensions of unipotent groups are unipotent (Corollary 15.7)
2. Every homomorphism from a unipotent group to a group of multiplicative type is trivial (Corollary 15.15)
3. The intersection of a unipotent subgroup with a multiplicative type subgroup is trivial (Corollary 15.16)
4. Unipotence is preserved by base field extension (Corollary 15.10)
5. If G is smooth, then G is unipotent iff all elements of G(k^al) are unipotent (Corollary 15.12)
6. In characteristic zero, unipotent groups are classified by nilpotent Lie algebras (Aside 15.23)
7. Not all unipotent groups are smooth: alpha_p is unipotent but not smooth

# Construction / Recognition

## To Construct:
1. Take a subgroup of U_n for some n
2. Or build extensions: if N and G/N are unipotent, so is G

## To Recognize:
1. Check that every nontrivial representation has a fixed vector
2. Or embed G in GL_n and check that G subset U_n (after suitable basis change)
3. Or verify that O(G) is coconnected

# Context & Application

Unipotent groups form one of the basic building blocks of algebraic groups. In the structure of solvable groups, the unipotent radical G_u is the "nilpotent" part. In characteristic zero, unipotent groups are equivalent to nilpotent Lie algebras via the exponential map.

# Examples

**Example 1** (p. 176): U_n, the group of upper unitriangular n x n matrices, is unipotent. It has the subnormal series U_n > G_1 > G_2 > ... > 1 with quotients G_a^{n-r-1}.

**Example 2** (p. 176): G_a is unipotent: its only representations in characteristic zero are of the form exp(rho_1 t).

**Example 3** (p. 179): alpha_p (in char p) is unipotent but not smooth.

# Relationships

## Builds Upon
- **Unipotent endomorphism** -- Elements of unipotent groups act unipotently

## Enables
- **Solvable algebraic group** -- Contains unipotent radical G_u
- **Trigonalizable group** -- Extensions of diagonalizable by unipotent

## Contrasts With
- **Group of multiplicative type** -- Hom(unipotent, mult. type) = 0
- **Diagonalizable group** -- Intersection with unipotent = trivial

# Common Errors

- **Error**: Assuming unipotent groups are always smooth
  **Correction**: alpha_p is unipotent but not smooth. Smoothness is extra.

# Common Confusions

- **Confusion**: Thinking "all elements unipotent" implies "G is unipotent"
  **Clarification**: Over non-smooth groups this can fail: mu_p in char p has mu_p(k^al) = 1 (all elements trivially unipotent) but mu_p is NOT unipotent (it is of multiplicative type)

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 15, pages 176-182. Definition 15.3, Theorem 15.6, Corollaries 15.7-15.18.

# Verification Notes

- Definition source: Direct from Definition 15.3
- Confidence rationale: Explicit definition with three equivalent characterizations
- Uncertainties: None
- Cross-reference status: Verified
