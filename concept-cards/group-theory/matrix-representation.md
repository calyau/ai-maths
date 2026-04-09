---
# === CORE IDENTIFICATION ===
concept: Matrix Representation
slug: matrix-representation

# === CLASSIFICATION ===
category: representation-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Representations of Finite Groups"
chapter_number: 7
pdf_page: 100
section: "Matrix representations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "matrix representation of degree n"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
extends: []
related:
  - linear-representation
  - faithful-representation
  - degree-of-representation
contrasts_with:
  - linear-representation

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a matrix representation of a finite group?"
  - "What is a linear representation of a finite group?"
---

# Quick Definition

A matrix representation of degree n of a group G over a field F is a group homomorphism G -> GL_n(F).

# Core Definition

A **matrix representation of degree n** of G over F is a homomorphism G -> GL_n(F). The representation is said to be *faithful* if the homomorphism is injective. A faithful representation identifies G with a group of n x n matrices. (Milne, Chapter 7, p. 100)

# Prerequisites

- **Group** — the group being represented
- **General linear group** — GL_n(F) is the target of the homomorphism

# Key Properties

1. Degree n refers to the size of the matrices
2. Every finite group has a faithful matrix representation (via Cayley's theorem and permutation matrices, Example 7.1b)
3. A matrix representation of degree n is the same as a linear representation on F^n (after choosing a basis)

# Construction / Recognition

1. Define a group homomorphism rho: G -> GL_n(F)
2. Verify rho(g_1 g_2) = rho(g_1) rho(g_2) for all g_1, g_2 in G
3. The degree is n (the size of the matrices)

# Context & Application

Matrix representations make abstract groups concrete by realizing them as matrix groups. They are the coordinate-dependent version of linear representations; choosing a basis for V converts a linear representation G -> GL(V) into a matrix representation.

# Examples

**Example 1** (p. 100, 7.1a): The quaternion group Q has a degree-2 representation over C sending a to the matrix with entries (0, sqrt(-1); sqrt(-1), 0) and b to (0, 1; -1, 0).

**Example 2** (p. 100, 7.1b): For G = S_n, the map sigma -> I(sigma) (permutation matrix) gives a faithful matrix representation of degree n.

**Example 3** (p. 100, 7.1c): For G = C_n = <sigma> with zeta a primitive nth root of 1 in F, the map sigma^i -> zeta^i gives a degree-1 representation. It is faithful iff zeta has order exactly n.

# Relationships

## Builds Upon
- **group** — the object being represented

## Enables
- **linear-representation** — basis-free generalization
- **character-of-a-representation** — trace of the matrix representation

## Related
- **faithful-representation** — injective matrix representations
- **degree-of-representation** — the integer n

## Contrasts With
- **linear-representation** — a linear representation is basis-independent; a matrix representation depends on a choice of basis

# Common Errors

- **Error**: Thinking a representation must be faithful
  **Correction**: A representation is any homomorphism G -> GL_n(F); it may have nontrivial kernel

# Common Confusions

- **Confusion**: Confusing the degree of a representation with the order of the group
  **Clarification**: The degree is the dimension of the vector space (matrix size); it can be much smaller than |G|

# Source Reference

Chapter 7: Representations of Finite Groups, "Matrix representations" section, pp. 100-101.

# Verification Notes

- Definition source: Direct from p. 100
- Confidence rationale: HIGH — explicit definition
- Uncertainties: None
