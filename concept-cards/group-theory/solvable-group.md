---
# === CORE IDENTIFICATION ===
concept: Solvable Group
slug: solvable-group

# === CLASSIFICATION ===
category: series-solvability
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Subnormal Series; Solvable and Nilpotent Groups"
chapter_number: 6
pdf_page: 89
section: "Solvable groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - soluble group

# === TYPED RELATIONSHIPS ===
prerequisites:
  - subnormal-series
  - commutator-subgroup
extends: []
related:
  - solvable-series
  - derived-series
  - solvable-length
  - feit-thompson-theorem
  - composition-factors
contrasts_with:
  - nilpotent-group
  - simple-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a solvable group?"
  - "How do I determine whether a group is solvable?"
  - "What must I understand before studying solvable groups?"
  - "What is the difference between solvable and nilpotent groups?"
---

# Quick Definition

A group is solvable if it has a subnormal series whose successive quotients are all abelian. Equivalently, G is solvable if and only if its derived series terminates at {1}, or equivalently if all its composition factors are cyclic of prime order.

# Core Definition

A subnormal series whose quotient groups are all commutative is called a *solvable series*. A group is *solvable* (or *soluble*) if it has a solvable series. Equivalently, a group is solvable if it can be obtained by forming successive extensions of commutative groups.

Since a commutative group is simple if and only if it is cyclic of prime order, G is solvable if and only if for one (hence every) composition series the quotients are all cyclic groups of prime order.

(Milne, p. 89)

# Prerequisites

- **subnormal-series** -- a solvable series is a subnormal series with abelian quotients
- **commutator-subgroup** -- the derived series provides the canonical solvable series

# Key Properties

1. Every commutative group is solvable
2. Every dihedral group is solvable
3. Every group of order < 60 is solvable
4. A noncommutative simple group (e.g., A_n for n >= 5) is not solvable
5. G is solvable iff G^(k) = 1 for some k (Proposition 6.10)
6. Subgroups and quotients of solvable groups are solvable (Proposition 6.6a)
7. Extensions of solvable groups are solvable (Proposition 6.6b)

# Construction / Recognition

## To Determine Solvability:
1. Compute the derived series: G, G', G'', ...
2. G is solvable iff this series reaches {1} in finitely many steps
3. Alternatively, find any subnormal series with abelian quotients

## Characterizations:
- G is solvable iff G^(k) = 1 for some k
- G is solvable iff every composition factor is cyclic of prime order
- G is solvable iff G has a solvable series

# Context & Application

Solvability is one of the most important properties of finite groups. The name comes from Galois theory: a polynomial equation is solvable by radicals if and only if its Galois group is solvable. The Feit-Thompson theorem shows every group of odd order is solvable, which was a key step in the classification of finite simple groups.

# Examples

**Example 1** (p. 89): Every commutative group is solvable (the series G > {1} has abelian quotient G).

**Example 2** (p. 89, 6.5): The Borel subgroup B = {upper triangular matrices} in GL_2(F) is solvable: B > U > 1 where U = {unitriangular matrices}, and B/U is abelian, U is abelian.

**Example 3** (p. 89): A_n for n >= 5 is not solvable (it is simple and noncommutative).

# Relationships

## Builds Upon
- **subnormal-series** -- solvable series is a subnormal series with abelian quotients

## Enables
- **solvable-length** -- the length of the derived series
- **feit-thompson-theorem** -- odd order implies solvable

## Related
- **derived-series** -- the canonical solvable series
- **composition-factors** -- solvable iff all composition factors are C_p

## Contrasts With
- **nilpotent-group** -- nilpotent implies solvable, but not conversely
- **simple-group** -- a nonabelian simple group is never solvable

# Common Errors

- **Error**: Thinking solvable means the group has a normal series with abelian quotients
  **Correction**: A solvable *series* is subnormal (each term normal in the preceding one), not necessarily normal in G. However, the derived series is a normal series.

# Common Confusions

- **Confusion**: Confusing solvable with nilpotent
  **Clarification**: Nilpotent groups are obtained by successive *central* extensions; solvable groups by successive (not necessarily central) extensions. Every nilpotent group is solvable, but the Borel subgroup B of GL_2 is solvable but not nilpotent (Example 6.12a).

# Source Reference

Chapter 6, p. 89. Proposition 6.6 (closure properties), Proposition 6.10 (derived series characterization).

# Verification Notes

- Definition source: Direct from p. 89
- Confidence rationale: HIGH -- explicit definition with multiple characterizations
- Uncertainties: None
