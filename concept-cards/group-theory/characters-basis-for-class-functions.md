---
# === CORE IDENTIFICATION ===
concept: Characters Form a Basis for Class Functions
slug: characters-basis-for-class-functions

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - irreducible-character
  - class-function
  - linear-independence-of-characters
  - number-of-irreducible-representations
extends: []
related:
  - orthogonality-relations
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Do the irreducible characters form a basis for the class functions?"
---

# Quick Definition

The simple characters of G form an F-basis for the F-vector space of class functions on G.

# Core Definition

**Proposition 7.47.** The simple characters of G form an F-basis for the class functions on G. The proof: class functions form a t-dimensional space (one dimension per conjugacy class), and the t irreducible characters are linearly independent (7.43), so they form a basis. (Milne, Proposition 7.47, p. 116)

# Prerequisites

- **Irreducible character** — the basis elements
- **Class function** — the vector space
- **Linear independence of characters** — guarantees they are a basis
- **Number of irreducible representations** — t = dimension of the space

# Key Properties

1. Every class function is an F-linear combination of irreducible characters
2. Over C with the character inner product, the irreducible characters form an orthonormal basis (7.52)
3. This gives a complete description of the space of class functions

# Relationships

## Builds Upon
- **irreducible-character**, **class-function**, **linear-independence-of-characters**

## Enables
- **orthogonality-relations** — strengthened to orthonormal basis
- Any class function can be expanded in the character basis

# Source Reference

Chapter 7: Representations of Finite Groups, Proposition 7.47, p. 116.

# Verification Notes

- Definition source: Direct from Proposition 7.47
- Confidence rationale: HIGH — explicit proposition
- Uncertainties: None
