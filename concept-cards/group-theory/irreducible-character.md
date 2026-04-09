---
# === CORE IDENTIFICATION ===
concept: Irreducible Character
slug: irreducible-character

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
pdf_page: 114
section: "The characters of G"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "simple character"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - character-of-a-representation
  - irreducible-representation
extends:
  - character-of-a-representation
related:
  - orthogonality-relations
  - character-table
  - number-of-irreducible-representations
contrasts_with:
  - virtual-character

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an irreducible character?"
  - "How do characters relate to irreducible representations?"
---

# Quick Definition

An irreducible (or simple) character is the character chi_V of an irreducible (simple) F[G]-module V.

# Core Definition

The character chi is said to be **simple** (or **irreducible**) if it is defined by a simple F[G]-module. The simple characters chi_1, ..., chi_t are linearly independent over F (Proposition 7.43) and form an orthonormal basis for the space of class functions (Corollary 7.52). (Milne, Chapter 7, pp. 114-116)

# Prerequisites

- **Character of a representation** — irreducible characters are a special case
- **Irreducible representation** — the underlying representation is irreducible

# Key Properties

1. Linearly independent over F (7.43)
2. Form an F-basis for the space of class functions (7.47)
3. Form an orthonormal basis with respect to the character inner product (7.52)
4. Number of irreducible characters = number of conjugacy classes (7.41a)
5. chi_i(e) = f_i = dim S_i (the degree)
6. Any character is a non-negative integer linear combination of irreducible characters

# Construction / Recognition

1. Find all simple F[G]-modules S_1, ..., S_t
2. Compute chi_i(g) = Tr(g_{S_i}) for each g in G
3. These are the irreducible characters

# Context & Application

Irreducible characters are the fundamental objects of character theory. They form a complete set of invariants for the representation theory: every character is a sum of irreducible characters, and the decomposition is unique. The orthonormality relations make computation feasible.

# Examples

**Example 1** (p. 114): The principal character chi_1 (trivial representation) satisfies chi_1(g) = 1 for all g.

**Example 2** (p. 115, equation 34): chi_i(e_j) = f_j if i = j, and 0 otherwise, where e_j is the central idempotent.

# Relationships

## Builds Upon
- **character-of-a-representation** — special case
- **irreducible-representation** — the underlying representation

## Enables
- **orthogonality-relations** — the key computational tool
- **character-table** — rows are irreducible characters

## Related
- **number-of-irreducible-representations** — equals number of conjugacy classes

## Contrasts With
- **virtual-character** — Z-linear combinations (may have negative coefficients)

# Common Errors

- **Error**: Thinking there can be infinitely many irreducible characters
  **Correction**: The number equals the number of conjugacy classes, which is finite

# Source Reference

Chapter 7: Representations of Finite Groups, pp. 114-116 (7.43-7.47, 7.52).

# Verification Notes

- Definition source: Direct from p. 114
- Confidence rationale: HIGH — explicit definition
- Uncertainties: None
