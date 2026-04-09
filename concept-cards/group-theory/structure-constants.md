---
# === CORE IDENTIFICATION ===
concept: Structure Constants
slug: structure-constants

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - f-algebra
extends: []
related:
  - matrix-algebra
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How is an F-algebra determined by numerical data?"
  - "What are structure constants of an algebra?"
---

# Quick Definition

The structure constants of an F-algebra A relative to a chosen basis {e_1, ..., e_n} are the scalars a_{ij}^k in F satisfying e_i e_j = sum_k a_{ij}^k e_k.

# Core Definition

Let A be an F-algebra with basis {e_1, ..., e_n} as an F-vector space. The **structure constants** are the elements a_{ij}^k in F defined by e_i e_j = sum_k a_{ij}^k e_k. Once a basis has been chosen, the algebra A is uniquely determined by its structure constants. (Milne, Chapter 7, p. 100)

# Prerequisites

- **F-algebra** — structure constants describe the multiplication in an F-algebra

# Key Properties

1. Depend on the choice of basis
2. Uniquely determine the algebra (given the basis)
3. Encode all the information about the multiplication table
4. There are n^3 structure constants for an n-dimensional algebra

# Construction / Recognition

1. Choose a basis {e_1, ..., e_n} for the F-algebra A
2. Compute each product e_i e_j
3. Express each product as a linear combination of basis elements
4. The coefficients are the structure constants

# Context & Application

Structure constants provide a concrete numerical description of an abstract algebra. They are useful for explicit computation and for determining whether two algebras are isomorphic.

# Examples

**Example 1** (p. 100): For M_2(F) with the standard basis {e_{11}, e_{12}, e_{21}, e_{22}}, the structure constants encode the multiplication rules e_{ij} e_{kl} = delta_{jk} e_{il}.

# Relationships

## Builds Upon
- **f-algebra** — structure constants describe an F-algebra

## Enables
- Explicit computation with algebras

## Related
- **matrix-algebra** — a key example where structure constants can be computed

## Contrasts With
- Basis-free descriptions of algebras

# Common Errors

- **Error**: Thinking structure constants are intrinsic to the algebra
  **Correction**: They depend on the choice of basis; a different basis gives different structure constants

# Common Confusions

- **Confusion**: Confusing structure constants with the algebra itself
  **Clarification**: The algebra is an abstract object; structure constants are its coordinates relative to a basis

# Source Reference

Chapter 7: Representations of Finite Groups, opening paragraph, p. 100.

# Verification Notes

- Definition source: Direct from p. 100
- Confidence rationale: HIGH — explicit definition
- Uncertainties: None
