---
concept: Semisimple Algebraic Group
slug: semisimple-algebraic-group
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
  - "semisimple group"
prerequisites:
  - radical-of-algebraic-group
  - connected-algebraic-group
extends: []
related:
  - reductive-algebraic-group
  - almost-simple-algebraic-group
  - semisimple-lie-algebra
contrasts_with:
  - reductive-algebraic-group
  - solvable-algebraic-group
answers_questions:
  - "What is a semisimple algebraic group?"
  - "What distinguishes a reductive group from a semisimple group?"
---

# Quick Definition

A semisimple algebraic group is a smooth connected algebraic group whose geometric radical is trivial — equivalently (over perfect fields), one with no nontrivial smooth connected normal solvable subgroup.

# Core Definition

An algebraic group G over a field k is **semisimple** if it is smooth and connected and its geometric radical R(G_{k^{al}}) is trivial (Milne, Definition 17.5a). Over a perfect field, this is equivalent to RG = 1 (Proposition 17.6).

# Prerequisites

- **Radical of algebraic group** -- Semisimplicity means the radical vanishes
- **Connected algebraic group** -- Semisimple groups must be connected

# Key Properties

1. Semisimple implies reductive implies pseudoreductive (Definition 17.5)
2. SL_n, SO_n, and Sp_n are semisimple; GL_n is reductive but not semisimple (p. 194)
3. G is semisimple iff every smooth connected normal commutative subgroup is trivial (over perfect fields, Proposition 17.7a)
4. A semisimple group is an almost-direct product of almost-simple groups (Theorem 17.16)
5. If G is semisimple, then DG = G (no commutative quotients, Corollary 17.18)
6. G/RG is always semisimple (Proposition 17.9)
7. In characteristic zero, G is semisimple iff Lie(G) is semisimple (Theorem 5.23, Ch II)

# Construction / Recognition

## To Recognize:
1. Check G is smooth and connected
2. Verify RG = 1 (over a perfect field), or R(G_{k^{al}}) = 1 in general
3. Alternatively, check that every smooth connected normal commutative subgroup is trivial

# Context & Application

Semisimple groups form the core building blocks of the structure theory. Every smooth connected algebraic group G over a perfect field fits into a canonical filtration with a semisimple quotient G/RG. The classification of semisimple groups reduces to classifying almost-simple groups, which in turn reduces to classifying root systems (Dynkin diagrams).

# Examples

**Example 1** (p. 194): SL_n is semisimple for n >= 2. Its centre mu_n is finite (not smooth connected), so the semisimplicity condition is satisfied.

**Example 2** (p. 194): GL_n is reductive but NOT semisimple because its centre G_m is a nontrivial smooth connected normal commutative subgroup.

# Relationships

## Builds Upon
- **Radical of algebraic group** -- G is semisimple iff RG = 1

## Enables
- **Almost-simple algebraic group** -- Semisimple groups decompose into almost-simple factors
- **Semisimple Lie algebra** -- In char 0, Lie(G) is semisimple iff G is semisimple

## Contrasts With
- **Reductive algebraic group** -- Reductive allows a central torus; semisimple does not

# Common Errors

- **Error**: Dropping one of the conditions (smooth, connected, normal, commutative) when checking semisimplicity
  **Correction**: All four conditions matter; see Remark 17.8 for counterexamples

# Common Confusions

- **Confusion**: Believing GL_n is semisimple
  **Clarification**: GL_n is reductive but not semisimple; its centre G_m is a nontrivial connected normal commutative subgroup

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 17b, pages 194-196.

# Verification Notes

- Definition source: Direct from Definition 17.5a
- Confidence rationale: Explicit definition with examples
- Uncertainties: None
- Cross-reference status: Verified
