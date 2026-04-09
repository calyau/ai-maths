---
# === CORE IDENTIFICATION ===
concept: Centralizer of a Subalgebra
slug: centralizer-of-a-module

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
  - "centralizer"
  - "C_B(A)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - f-algebra
extends: []
related:
  - double-centralizer-theorem
  - schur-lemma
  - matrix-algebra
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the centralizer of a subalgebra?"
  - "How does the centralizer relate to the double centralizer theorem?"
---

# Quick Definition

The centralizer of an F-subalgebra A in an F-algebra B is C_B(A) = {b in B : ba = ab for all a in A}. It is again an F-subalgebra of B.

# Core Definition

Let A be an F-subalgebra of an F-algebra B. The **centralizer** of A in B is C_B(A) = {b in B : ba = ab for all a in A}. It is again an F-subalgebra of B. (Milne, Chapter 7, p. 108)

# Prerequisites

- **F-algebra** — centralizers are defined between subalgebras

# Key Properties

1. C_B(A) is an F-subalgebra of B
2. C_B(C_B(A)) contains A (double centralizer always contains the original)
3. For A = F * I_n in M_n(F): C(A) = M_n(F) (7.21a)
4. For A = M_n(F) in M_n(F): C(A) = F * I_n (the centre) (7.21b)
5. For A = diagonal matrices in M_n(F): C(A) = A (7.21c)
6. In all three examples above, C(C(A)) = A

# Construction / Recognition

1. Given A as a subalgebra of B
2. Find all elements of B that commute with every element of A
3. The result is C_B(A)

# Context & Application

Centralizers are the key tool in the Wedderburn structure theory. The double centralizer theorem (7.22) states that for a faithful semisimple A-module V, C(C(A)) = A (centralizers in End_F(V)). This is used to prove the Wedderburn structure theorem for simple algebras.

# Examples

**Example 1** (p. 108, 7.21a): C(F * I_n) = M_n(F) in M_n(F).

**Example 2** (p. 108, 7.21b): C(M_n(F)) = F * I_n in M_n(F) (the centre).

**Example 3** (p. 109, 7.21c): The centralizer of diagonal matrices in M_n(F) is the diagonal matrices themselves.

# Relationships

## Builds Upon
- **f-algebra** — defined for F-algebras

## Enables
- **double-centralizer-theorem** — C(C(A)) = A for faithful semisimple modules
- **wedderburn-theorem** — proved via the double centralizer theorem

## Related
- **schur-lemma** — C(A) in End_F(S) is a division algebra when S is simple and A acts faithfully

## Contrasts With
- Centre of an algebra (centralizer of the whole algebra in itself)

# Common Errors

- **Error**: Confusing the centralizer with the centre
  **Correction**: The centre is C_A(A) (the centralizer of A in itself); the centralizer C_B(A) is relative to a larger algebra B

# Source Reference

Chapter 7: Representations of Finite Groups, pp. 108-109 (7.21).

# Verification Notes

- Definition source: Direct from p. 108
- Confidence rationale: HIGH — explicit definition
- Uncertainties: None
