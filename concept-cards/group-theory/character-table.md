---
# === CORE IDENTIFICATION ===
concept: Character Table
slug: character-table

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
pdf_page: 117
section: "The character table of a group"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - irreducible-character
  - orthogonality-relations
extends: []
related:
  - number-of-irreducible-representations
  - class-function
  - decomposition-of-f-g
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the character table of a finite group?"
  - "How do I construct the character table of a finite group?"
  - "What information does the character table encode?"
---

# Quick Definition

The character table of G is an n x n matrix (over C) whose rows are the irreducible characters and whose columns are the conjugacy classes. Here n = number of conjugacy classes.

# Core Definition

Let G be a group with n conjugacy classes, and hence n irreducible characters. The **character table** of G is an n x n matrix whose entries are the values of the irreducible characters on the conjugacy classes. By convention, the rows are labelled by the irreducible characters and the columns by the conjugacy classes. (Milne, Chapter 7, p. 117)

# Prerequisites

- **Irreducible character** — the rows of the table
- **Orthogonality relations** — constrain the entries

# Key Properties

1. Square matrix: n rows (characters) x n columns (conjugacy classes)
2. Rows are orthonormal with respect to the character inner product (7.52)
3. First column entries are the degrees f_i = dim S_i (positive integers)
4. sum f_i^2 = |G|
5. Contains enough information to read off the normal subgroups of G (p. 119)
6. The commutator subgroup = intersection of kernels of linear characters (p. 119)
7. Does NOT uniquely determine the group: D_4 and Q_8 have the same character table (7.55-7.56)

# Construction / Recognition

1. List the conjugacy classes C_1, ..., C_n (C_1 = {e} by convention)
2. Determine the degrees f_1, ..., f_n from sum f_i^2 = |G|
3. Find the 1-dimensional characters (homomorphisms G -> C^x)
4. Use orthogonality relations to constrain remaining entries
5. Use specific representations to compute remaining characters

# Context & Application

The character table is the central computational object in the representation theory of finite groups. It encodes the complete representation theory of G over C. Although it does not determine G up to isomorphism, it determines many group-theoretic properties: normal subgroups, commutator subgroup, and more.

# Examples

**Example 1** (p. 117, 7.53): Character table of C_3 with zeta = e^{2pi i/3}:
Rows: chi_0 = (1,1,1), chi_1 = (1, zeta, zeta^2), chi_2 = (1, zeta^2, zeta).

**Example 2** (p. 117, 7.54): Character table of S_3:
chi_0 = (1,1,1), chi_1 = (1,-1,1), chi_2 = (2,0,-1).

**Example 3** (p. 118, 7.55): Character table of D_4 (and Q_8):
Five conjugacy classes, four degree-1 and one degree-2 representation.

# Relationships

## Builds Upon
- **irreducible-character** — the rows
- **orthogonality-relations** — constraining equations

## Enables
- Reading off normal subgroups
- Computing the commutator subgroup
- Decomposing arbitrary representations

## Related
- **number-of-irreducible-representations** — dimensions of the table
- **decomposition-of-f-g** — algebraic underpinning

## Contrasts With
- The group itself: the character table does not determine G (D_4 vs Q_8 example)

# Common Errors

- **Error**: Thinking the character table uniquely determines the group
  **Correction**: D_4 and Q_8 have the same character table but are not isomorphic (7.55-7.56)

# Common Confusions

- **Confusion**: Thinking character table entries are always integers
  **Clarification**: Entries can be complex numbers (roots of unity appear for non-real characters, as in the C_3 example)

# Source Reference

Chapter 7: Representations of Finite Groups, "The character table of a group", pp. 117-119 (7.53-7.56).

# Verification Notes

- Definition source: Direct from p. 117
- Confidence rationale: HIGH — explicit definition with examples
- Uncertainties: None
