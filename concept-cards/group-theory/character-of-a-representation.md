---
# === CORE IDENTIFICATION ===
concept: Character of a Representation
slug: character-of-a-representation

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
  - "character"
  - "chi_V"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - linear-representation
extends: []
related:
  - irreducible-character
  - class-function
  - character-inner-product
  - character-table
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the character of a representation?"
  - "How do characters relate to irreducible representations?"
---

# Quick Definition

The character of a representation rho: G -> GL(V) is the function chi_V: G -> F defined by chi_V(g) = Tr(rho(g)). It depends only on the isomorphism class of V and is a class function.

# Core Definition

From each representation g -> g_V: G -> GL(V), we obtain a function chi_V on G defined by chi_V(g) = Tr_V(g_V), called the **character** of rho. The character depends only on the isomorphism class of the F[G]-module V, and chi_V is a class function. (Milne, Chapter 7, p. 114)

# Prerequisites

- **Linear representation** — characters are derived from representations

# Key Properties

1. chi_V(g) = Tr(g_V), the trace of g acting on V
2. Depends only on the isomorphism class of V
3. Is a class function: chi_V(gag^{-1}) = chi_V(a)
4. chi_{V+W} = chi_V + chi_W (Lemma 7.42)
5. chi_V(e) = dim_F(V) (trace of the identity)
6. Two F[G]-modules are isomorphic iff they have the same character (7.44, over algebraically closed fields of char 0)

# Construction / Recognition

1. Given a representation rho: G -> GL(V)
2. Choose any basis for V
3. For each g, compute the matrix of rho(g) and take its trace
4. The resulting function chi_V: G -> F is the character

# Context & Application

Characters encode representations as numerical functions on G. The key insight is that characters determine representations (Proposition 7.44): two modules with the same character are isomorphic. This reduces representation theory to studying the functions chi_V.

# Examples

**Example 1** (p. 114): The regular character satisfies chi_reg(e) = |G| and chi_reg(g) = 0 for g != e.

**Example 2** (p. 114): For a 1-dimensional representation, chi_V(g) = rho(g) (a homomorphism G -> F^x).

# Relationships

## Builds Upon
- **linear-representation** — characters are the trace functions of representations

## Enables
- **character-inner-product** — inner product of characters
- **orthogonality-relations** — characters satisfy orthogonality
- **character-table** — tabulation of irreducible characters

## Related
- **class-function** — characters are class functions
- **irreducible-character** — character of an irreducible representation

## Contrasts With
- Virtual characters (Z-linear combinations, not just N-linear combinations)

# Common Errors

- **Error**: Thinking the character depends on the choice of basis
  **Correction**: The trace is basis-independent (conjugate matrices have the same trace)

# Common Confusions

- **Confusion**: Confusing "character" with "representation"
  **Clarification**: A character is a function G -> F (the trace); a representation is a homomorphism G -> GL(V). Different representations can have the same character only if they are isomorphic (over algebraically closed fields of char 0).

# Source Reference

Chapter 7: Representations of Finite Groups, "The characters of G" section, pp. 114-115.

# Verification Notes

- Definition source: Direct from p. 114
- Confidence rationale: HIGH — explicit definition
- Uncertainties: None
