---
# === CORE IDENTIFICATION ===
concept: Orthogonality Relations
slug: orthogonality-relations

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
section: "The characters of G"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "first orthogonality relations"
  - "row orthogonality"
  - "character orthogonality"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - character-inner-product
  - irreducible-character
  - schur-lemma
extends: []
related:
  - character-table
  - number-of-irreducible-representations
  - hom-dimension-formula
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the orthogonality relations for characters?"
  - "Are irreducible characters orthonormal?"
---

# Quick Definition

The irreducible characters of G are orthonormal with respect to the character inner product: (chi|chi') = 1 if chi = chi', and 0 otherwise.

# Core Definition

**Theorem 7.51.** For any F[G]-modules V and W, dim_F Hom_{F[G]}(V, W) = (chi_V|chi_W).

**Corollary 7.52.** If chi and chi' are simple characters, then (chi|chi') = 1 if chi = chi', and 0 otherwise. Therefore the simple characters form an orthonormal basis for the space of class functions on G. (Milne, Theorem 7.51 and Corollary 7.52, p. 117)

This generalizes the orthogonality relations for abelian groups (Theorem 1.62, p. 28) to all finite groups.

# Prerequisites

- **Character inner product** — the inner product (f_1|f_2) = (1/|G|) sum f_1(a) conjugate(f_2(a))
- **Irreducible character** — the orthonormal basis elements
- **Schur's lemma** — Hom(S_i, S_j) = 0 for i != j and End(S_i) = F (over alg. closed fields)

# Key Properties

1. (chi_i|chi_j) = delta_{ij} (Kronecker delta)
2. Equivalently: (1/|G|) sum_{a in G} chi_i(a) conjugate(chi_j(a)) = delta_{ij}
3. The irreducible characters form an orthonormal basis for the t-dimensional space of class functions
4. For any character chi = sum m_i chi_i: m_i = (chi|chi_i) and (chi|chi) = sum m_i^2
5. chi is irreducible iff (chi|chi) = 1
6. Column orthogonality: sum_{i} chi_i(a) conjugate(chi_i(b)) = |C_G(a)| if a, b conjugate, 0 otherwise

# Construction / Recognition

To verify the orthogonality relations:
1. Compute (chi_i|chi_j) = (1/|G|) sum_{a in G} chi_i(a) conjugate(chi_j(a))
2. This equals dim Hom_{F[G]}(S_i, S_j) by Theorem 7.51
3. By Schur's lemma, this is 1 if i = j and 0 if i != j

# Context & Application

The orthogonality relations are the most important computational tool in character theory. They allow:
- Testing irreducibility: chi is irreducible iff (chi|chi) = 1
- Decomposing representations: m_i = (chi|chi_i)
- Computing character tables by exploiting orthogonality constraints

# Examples

**Example 1** (p. 117): For S_3, one can verify (chi_0|chi_0) = 1, (chi_0|chi_1) = 0, (chi_2|chi_2) = 1 using the character table.

**Example 2** (p. 28, Theorem 1.62): For abelian G: sum_{a in G} chi(a) psi(a^{-1}) = |G| if chi = psi, 0 otherwise. This is a special case.

# Relationships

## Builds Upon
- **character-inner-product** — the inner product used
- **irreducible-character** — the orthonormal elements
- **schur-lemma** — provides the key computation

## Enables
- **character-table** — construction uses orthogonality
- Irreducibility testing
- Decomposition of representations

## Related
- **number-of-irreducible-representations** — t = number of conjugacy classes = dimension of the orthonormal basis
- **hom-dimension-formula** — the general result that implies orthogonality

# Common Errors

- **Error**: Forgetting the complex conjugation in the inner product
  **Correction**: The second argument is conjugated: (chi|chi') = (1/|G|) sum chi(a) conjugate(chi'(a))

# Common Confusions

- **Confusion**: Confusing "first" and "second" orthogonality relations
  **Clarification**: The first (row) orthogonality sums over group elements; the second (column) orthogonality sums over irreducible characters. Milne states the first explicitly (7.52); the second follows by viewing the character table as a unitary matrix.

# Source Reference

Chapter 7: Representations of Finite Groups, Theorem 7.51 and Corollary 7.52, p. 117. See also Theorem 1.62 (p. 28) for the abelian case.

# Verification Notes

- Definition source: Direct from Corollary 7.52
- Confidence rationale: HIGH — explicit theorem
- Uncertainties: None
