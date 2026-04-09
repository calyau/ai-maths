---
# === CORE IDENTIFICATION ===
concept: Matrix Algebra M_n(F)
slug: matrix-algebra

# === CLASSIFICATION ===
category: module-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Representations of Finite Groups"
chapter_number: 7
pdf_page: 108
section: "Simple F-algebras and their modules"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "M_n(D)"
  - "M_n(F)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - f-algebra
  - division-algebra
extends:
  - simple-f-algebra
related:
  - wedderburn-theorem
  - decomposition-of-f-g
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why are matrix algebras important in representation theory?"
  - "What is the structure of M_n(D)?"
---

# Quick Definition

M_n(D) is the F-algebra of n x n matrices with entries in a division algebra D. It is the prototypical simple F-algebra.

# Core Definition

For a division algebra D over F, the **matrix algebra** M_n(D) consists of all n x n matrices with entries in D, with the usual matrix addition and multiplication. It is an F-algebra of dimension n^2 dim_F(D). M_n(D) is simple (7.19a), and every simple F-algebra is isomorphic to some M_n(D) (Wedderburn, 7.25). (Milne, Example 7.19, p. 108)

# Prerequisites

- **F-algebra** — M_n(D) is an F-algebra
- **Division algebra** — entries come from a division algebra

# Key Properties

1. M_n(D) is simple (7.19a): the only two-sided ideals are 0 and M_n(D)
2. M_n(D) = L(1) + ... + L(n) as a direct sum of minimal left ideals (7.19b)
3. Each L(i) consists of matrices whose only nonzero column is the ith
4. The centre of M_n(F) is the set of scalar matrices F * I_n (7.21b)
5. dim_F M_n(F) = n^2
6. When D = F, M_n(F) is the algebra of n x n matrices over F

# Construction / Recognition

1. Take all n x n matrices with entries in D
2. Addition and multiplication are the usual matrix operations
3. To verify simplicity: if a two-sided ideal contains a nonzero matrix, it contains all matrix units e_{ij}, hence equals M_n(D)

# Context & Application

Matrix algebras are the building blocks of semisimple algebras. By the Wedderburn-Artin theorem, every semisimple F-algebra is a product of matrix algebras M_{n_i}(D_i). For the group algebra F[G] over an algebraically closed field of characteristic zero, F[G] = M_{f_1}(F) x ... x M_{f_t}(F).

# Examples

**Example 1** (p. 108, 7.19): M_n(D) has minimal left ideals L(i), each isomorphic to D^n as a D-module.

**Example 2** (p. 108, 7.21b): The centre of M_n(F) is F * I_n (scalar matrices).

# Relationships

## Builds Upon
- **division-algebra** — entries from a division algebra
- **simple-f-algebra** — M_n(D) is simple

## Enables
- **wedderburn-theorem** — every simple algebra is M_n(D)
- **decomposition-of-f-g** — F[G] is a product of matrix algebras

## Related
- **centralizer-of-a-module** — centralizers in M_n(F) are computed explicitly

## Contrasts With
- Division algebras (M_1(D) = D; matrix algebras with n > 1 have zero divisors)

# Common Errors

- **Error**: Thinking M_n(D) has proper two-sided ideals
  **Correction**: M_n(D) is simple; its only two-sided ideals are 0 and itself

# Source Reference

Chapter 7: Representations of Finite Groups, Example 7.19, pp. 108-109.

# Verification Notes

- Definition source: Direct from Example 7.19
- Confidence rationale: HIGH — explicit construction
- Uncertainties: None
