---
# === CORE IDENTIFICATION ===
concept: Nilpotent Group
slug: nilpotent-group

# === CLASSIFICATION ===
category: nilpotent-groups
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Subnormal Series; Solvable and Nilpotent Groups"
chapter_number: 6
pdf_page: 92
section: "Nilpotent groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
  - upper-central-series
  - commutator
extends: []
related:
  - solvable-group
  - nilpotency-class
  - nilpotent-iff-direct-product-of-sylow
  - p-group
contrasts_with:
  - solvable-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a nilpotent group?"
  - "What is the difference between solvable and nilpotent groups?"
  - "How does the upper central series relate to nilpotency?"
---

# Quick Definition

A group G is nilpotent if its upper central series reaches G in finitely many steps: Z^m(G) = G for some m. Equivalently, nilpotent groups are those obtained from abelian groups by successive central extensions. Every finite nilpotent group is a direct product of its Sylow subgroups.

# Core Definition

Let G be a group. Define the ascending central series:

{1} subset Z(G) subset Z^2(G) subset ...,

where g in Z^i(G) iff [g, x] in Z^{i-1}(G) for all x in G.

If Z^m(G) = G for some m, then G is said to be *nilpotent*, and the smallest such m is called the *(nilpotency) class* of G.

(Milne, p. 92)

# Prerequisites

- **upper-central-series** -- the ascending series whose termination defines nilpotency
- **commutator** -- the central series is defined via commutators

# Key Properties

1. Only {1} has class 0; abelian groups have class 1
2. Class 2 groups are called metabelian: G/Z(G) is abelian
3. Every nilpotent group is solvable (but not conversely)
4. All finite p-groups are nilpotent (Corollary 6.17)
5. A finite group is nilpotent iff it is a direct product of its Sylow subgroups (Theorem 6.18)
6. A finite group is nilpotent iff every maximal proper subgroup is normal (Theorem 6.23)
7. Subgroups and quotients of nilpotent groups are nilpotent (Proposition 6.13)
8. Extensions of nilpotent groups need NOT be nilpotent (unlike solvable groups)

# Construction / Recognition

## Characterizations of Finite Nilpotent Groups:
1. Upper central series reaches G
2. Direct product of p-groups (its Sylow subgroups)
3. Every maximal proper subgroup is normal
4. Every proper subgroup is strictly contained in its normalizer
5. All Sylow subgroups are normal

## To Test Nilpotency:
For a finite group, check whether all Sylow subgroups are normal, or compute the upper central series.

# Context & Application

Nilpotent groups sit between abelian and solvable groups: every abelian group is nilpotent, and every nilpotent group is solvable. The key distinction from solvable groups is that nilpotent groups are built by *central* extensions. In the finite case, nilpotent = direct product of p-groups, which is a very strong structural result.

The terminology comes from linear algebra: a matrix is nilpotent if some power is zero; analogously, iterated commutators in a nilpotent group eventually vanish.

# Examples

**Example 1** (p. 92, 6.12a): The Borel subgroup B of GL_2(F) is solvable but NOT nilpotent: Z(B) = {aI : a != 0} and Z(B/Z(B)) is trivial.

**Example 2** (p. 92, 6.12b): The group of 3x3 upper unitriangular matrices is nilpotent of class 2 (metabelian).

**Example 3** (p. 93, 6.12c): Any nonabelian group of order p^3 is metabelian (nilpotent of class 2). The dihedral group D_{2^n} is nilpotent of class n.

**Example 4** (p. 93, 6.12c): D_n is nilpotent iff n is a power of 2.

# Relationships

## Builds Upon
- **upper-central-series** -- termination defines nilpotency

## Enables
- **nilpotency-class** -- the smallest m with Z^m(G) = G
- **nilpotent-iff-direct-product-of-sylow** -- structural characterization

## Related
- **p-group** -- all finite p-groups are nilpotent

## Contrasts With
- **solvable-group** -- solvable groups use arbitrary (not just central) extensions; B is solvable but not nilpotent

# Common Errors

- **Error**: Assuming extensions of nilpotent groups are nilpotent
  **Correction**: This is FALSE. U abelian and B/U abelian does not imply B nilpotent (Example 6.12a). This is a key difference from solvable groups.

# Common Confusions

- **Confusion**: Confusing nilpotent with solvable
  **Clarification**: Nilpotent implies solvable, but not conversely. Nilpotent = central extensions only; solvable = arbitrary abelian extensions.

# Source Reference

Chapter 6, pp. 92-95. Definition p. 92, characterizations in Theorems 6.18 and 6.23.

# Verification Notes

- Definition source: Direct from p. 92
- Confidence rationale: HIGH -- explicit definition with multiple characterizations
- Uncertainties: None
