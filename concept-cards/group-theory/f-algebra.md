---
# === CORE IDENTIFICATION ===
concept: F-algebra
slug: f-algebra

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
pdf_page: 100
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "algebra over a field"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
extends: []
related:
  - group-algebra
  - matrix-algebra
  - structure-constants
  - opposite-algebra
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an F-algebra?"
  - "What concepts are prerequisite to representation theory?"
---

# Quick Definition

An F-algebra is a ring A containing a field F in its centre that is finite-dimensional as an F-vector space. It need not be commutative.

# Core Definition

A ring A is an **F-algebra** if it contains F in its centre and is finite-dimensional as an F-vector space. For example, the matrix algebra M_n(F) is an F-algebra. (Milne, Chapter 7, p. 100)

# Prerequisites

- **Field** — F-algebras are built over a base field F
- **Ring** — an F-algebra is a ring with extra structure
- **Vector space** — must be finite-dimensional over F

# Key Properties

1. Contains F in its centre, so scalar multiplication by F is well-defined
2. Finite-dimensional as an F-vector space
3. Need not be commutative
4. Once a basis {e_1, ..., e_n} is chosen, the algebra is determined by its structure constants

# Construction / Recognition

1. Start with a ring A containing a field F in its centre
2. Verify A is finite-dimensional as an F-vector space
3. Choose a basis and compute the structure constants a_{ij}^k where e_i e_j = sum_k a_{ij}^k e_k

# Context & Application

F-algebras provide the algebraic framework for studying linear representations of finite groups. The group algebra F[G] is the central example. The theory of semisimple and simple F-algebras (Wedderburn theory) classifies the possible structures that arise.

# Examples

**Example 1** (p. 100): The matrix algebra M_n(F) is an F-algebra of dimension n^2 over F.

**Example 2** (p. 100): The group algebra F[G] of a finite group G is an F-algebra with dimension |G|.

# Relationships

## Builds Upon
- Rings, fields, vector spaces

## Enables
- **group-algebra** — F[G] is the primary F-algebra in representation theory
- **simple-f-algebra** — a key structural class of F-algebras
- **semisimple-f-algebra** — F-algebras whose modules are all semisimple

## Related
- **structure-constants** — determine the algebra relative to a chosen basis
- **opposite-algebra** — reversing multiplication gives another F-algebra

## Contrasts With
- Commutative algebras — F-algebras need not be commutative

# Common Errors

- **Error**: Assuming an F-algebra must be commutative
  **Correction**: F-algebras are generally noncommutative; M_n(F) for n >= 2 is noncommutative

# Common Confusions

- **Confusion**: Confusing "F in the centre" with "F-algebra is commutative"
  **Clarification**: F lies in the centre of A, but A may have elements outside the centre that do not commute with each other

# Source Reference

Chapter 7: Representations of Finite Groups, opening paragraph, p. 100.

# Verification Notes

- Definition source: Direct from Chapter 7 opening, p. 100
- Confidence rationale: HIGH — explicit definition given
- Uncertainties: None
- Cross-reference status: All referenced slugs correspond to planned cards
