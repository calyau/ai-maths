---
# === CORE IDENTIFICATION ===
concept: Number of Irreducible Representations
slug: number-of-irreducible-representations

# === CLASSIFICATION ===
category: character-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Representations of Finite Groups"
chapter_number: 7
pdf_page: 113
section: "The representations of G"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - decomposition-of-f-g
  - conjugacy-classes-and-centre-of-f-g
extends: []
related:
  - irreducible-character
  - character-table
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How many irreducible representations does a finite group have?"
  - "What determines the number of irreducible characters?"
---

# Quick Definition

The number of isomorphism classes of irreducible (simple) representations of G over an algebraically closed field of characteristic zero equals the number of conjugacy classes of G.

# Core Definition

**Theorem 7.41(a).** The number of isomorphism classes of simple F[G]-modules is equal to the number of conjugacy classes in G. (Milne, Theorem 7.41a, p. 113)

The proof: F[G] = M_{f_1}(F) x ... x M_{f_t}(F), so the number of simple modules is t (7.37a). The centre of F[G] has dimension t (one copy of F per factor). By Proposition 7.38, dim(centre(F[G])) = number of conjugacy classes. Hence t = number of conjugacy classes.

# Prerequisites

- **Decomposition of F[G]** — F[G] = product of matrix algebras with t factors
- **Conjugacy classes and centre of F[G]** — dim(centre) = number of conjugacy classes

# Key Properties

1. Number of irreducible representations = t = number of conjugacy classes
2. For abelian groups: t = |G| (every conjugacy class has one element)
3. The degrees satisfy sum f_i^2 = |G|
4. This is a powerful constraint on the possible representation theories

# Construction / Recognition

1. Count the conjugacy classes of G
2. This is the number of irreducible representations
3. The degrees f_1, ..., f_t must satisfy sum f_i^2 = |G|

# Context & Application

This theorem is one of the most beautiful results in algebra: it connects two seemingly unrelated counts -- conjugacy classes (a combinatorial/group-theoretic notion) and irreducible representations (an algebraic/linear algebraic notion).

# Examples

**Example 1**: S_3 has 3 conjugacy classes {e}, {(12),(13),(23)}, {(123),(132)}, so it has 3 irreducible representations with degrees satisfying f_1^2 + f_2^2 + f_3^2 = 6, giving (1,1,2).

**Example 2**: D_4 and Q_8 each have 5 conjugacy classes, so 5 irreducible representations with 1^2 + 1^2 + 1^2 + 1^2 + 2^2 = 8.

# Relationships

## Builds Upon
- **decomposition-of-f-g** — the algebraic structure
- **conjugacy-classes-and-centre-of-f-g** — the combinatorial count

## Enables
- **character-table** — determines its size
- Representation-theoretic computations

## Related
- **irreducible-character** — one for each irreducible representation

# Source Reference

Chapter 7: Representations of Finite Groups, Theorem 7.41(a), pp. 113-114.

# Verification Notes

- Definition source: Direct from Theorem 7.41(a)
- Confidence rationale: HIGH — explicit theorem
- Uncertainties: None
