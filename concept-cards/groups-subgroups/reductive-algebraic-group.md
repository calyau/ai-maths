---
concept: Reductive Algebraic Group
slug: reductive-algebraic-group
category: group-structure
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 194
section: "17b Definition of semisimple and reductive groups"
extraction_confidence: high
aliases:
  - "reductive group"
prerequisites:
  - unipotent-radical
  - connected-algebraic-group
extends: []
related:
  - semisimple-algebraic-group
  - pseudoreductive-algebraic-group
  - derived-group
contrasts_with:
  - semisimple-algebraic-group
  - pseudoreductive-algebraic-group
answers_questions:
  - "What is a reductive algebraic group?"
  - "What distinguishes a reductive group from a semisimple group?"
---

# Quick Definition

A reductive algebraic group is a smooth connected algebraic group whose geometric unipotent radical is trivial. Equivalently (in characteristic zero), it is a group whose finite-dimensional representations are all semisimple.

# Core Definition

An algebraic group G over a field k is **reductive** if it is smooth and connected and its geometric unipotent radical R_u(G_{k^{al}}) is trivial (Milne, Definition 17.5b). Over a perfect field, this is equivalent to R_uG = 1 (Proposition 17.6b).

# Prerequisites

- **Unipotent radical** -- Reductivity means the unipotent radical vanishes
- **Connected algebraic group** -- Reductive groups must be connected

# Key Properties

1. semisimple => reductive => pseudoreductive
2. G is reductive iff every smooth connected normal commutative subgroup is a torus (over perfect fields, Proposition 17.7b)
3. For reductive G: DG is semisimple, Z(G)^0 is a torus, and G = Z(G)^0 . DG (Theorem 17.20)
4. Z(G) cap DG is the finite centre of DG
5. In characteristic zero, G is reductive iff Rep(G) is semisimple (Theorem 6.14, Ch II)
6. GL_n is the prototypical reductive group

# Construction / Recognition

## To Construct:
1. Take a semisimple group G' and a torus T, with a homomorphism phi: Z(G') -> T
2. Form G = (T x G') / Z(G') where Z(G') embeds via z -> (phi(z)^{-1}, z) (Remark 17.21)

## To Recognize:
1. Check G is smooth and connected
2. Verify R_uG = 1 (over perfect fields)
3. Alternatively, check all smooth connected normal commutative subgroups are tori

# Context & Application

Reductive groups occupy the middle ground between semisimple groups and general algebraic groups. They arise naturally as quotients G/R_uG. The structure theorem G = Z(G)^0 . DG shows every reductive group is a "central extension" of a semisimple group by a torus. In characteristic zero, the category of representations of a reductive group is semisimple.

# Examples

**Example 1** (p. 194): GL_n is reductive but not semisimple. Its centre G_m is a torus, and its derived group SL_n is semisimple.

**Example 2** (p. 196): For G the group of invertible block upper triangular matrices, G/R_uG is isomorphic to GL_m x GL_n, which is reductive.

# Relationships

## Builds Upon
- **Unipotent radical** -- G is reductive iff R_uG_{k^{al}} = 1

## Enables
- **Semisimple algebraic group** -- DG is semisimple for reductive G
- **Tannakian category** -- Rep(G) is semisimple iff G^0 is reductive (Ch II, 6.17)

## Contrasts With
- **Semisimple algebraic group** -- Semisimple means RG = 1; reductive allows a central torus

# Common Errors

- **Error**: Assuming reductive implies semisimple
  **Correction**: Reductive allows a central torus; GL_n is reductive but not semisimple

# Common Confusions

- **Confusion**: In nonzero characteristic, Rep(G) semisimple does NOT characterize reductive groups
  **Clarification**: The equivalence Rep(G) semisimple iff G reductive holds only in characteristic zero

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 17b and 17e, pages 194-200.

# Verification Notes

- Definition source: Direct from Definition 17.5b and Theorem 17.20
- Confidence rationale: Explicit definition with detailed structure theorem
- Uncertainties: None
- Cross-reference status: Verified
