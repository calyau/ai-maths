---
# === CORE IDENTIFICATION ===
concept: Character Inner Product
slug: character-inner-product

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
pdf_page: 116
section: "The characters of G"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "inner product of characters"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - character-of-a-representation
  - class-function
extends: []
related:
  - orthogonality-relations
  - irreducible-character
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the inner product of two characters?"
  - "How is the character inner product defined?"
---

# Quick Definition

For class functions f_1, f_2 on G (with F a subfield of C), the character inner product is (f_1|f_2) = (1/|G|) sum_{a in G} f_1(a) conjugate(f_2(a)).

# Core Definition

For class functions f_1 and f_2 on G (where F is a subfield of C stable under complex conjugation), define (f_1|f_2) = (1/|G|) sum_{a in G} f_1(a) conjugate(f_2(a)). This is an inner product on the F-space of class functions (Lemma 7.48). (Milne, Chapter 7, p. 116)

# Prerequisites

- **Character of a representation** — the inner product is applied to characters
- **Class function** — the inner product is defined on class functions

# Key Properties

1. It is a positive definite Hermitian form on class functions (7.48)
2. (chi|chi') = dim Hom_{F[G]}(V, W) for F[G]-modules V, W with characters chi, chi' (7.51)
3. Irreducible characters are orthonormal: (chi_i|chi_j) = delta_{ij} (7.52)
4. For a character chi = sum m_i chi_i: (chi|chi_i) = m_i (the multiplicity)

# Construction / Recognition

1. Given two class functions f_1, f_2: G -> C
2. Compute sum_{a in G} f_1(a) conjugate(f_2(a))
3. Divide by |G|

# Context & Application

The character inner product is the fundamental computational tool of character theory. It allows extraction of multiplicities: if V has character chi = sum m_i chi_i, then m_i = (chi|chi_i). The orthonormality of irreducible characters (7.52) makes this computation straightforward.

# Examples

**Example 1** (p. 116): For the regular character chi_reg and any irreducible chi_i: (chi_reg|chi_i) = (1/|G|) |G| chi_i(e) = f_i = dim S_i.

# Relationships

## Builds Upon
- **class-function** — the inner product is defined on class functions
- **character-of-a-representation** — primary application

## Enables
- **orthogonality-relations** — characters are orthonormal w.r.t. this inner product
- Multiplicity extraction: m_i = (chi|chi_i)

## Related
- **irreducible-character** — orthonormal basis

# Common Errors

- **Error**: Forgetting the factor 1/|G|
  **Correction**: The inner product is (1/|G|) sum, not just the sum

- **Error**: Forgetting to take the complex conjugate of f_2
  **Correction**: The inner product involves conjugate(f_2(a)), making it Hermitian

# Source Reference

Chapter 7: Representations of Finite Groups, Lemma 7.48, p. 116.

# Verification Notes

- Definition source: Direct from p. 116
- Confidence rationale: HIGH — explicit formula
- Uncertainties: None
