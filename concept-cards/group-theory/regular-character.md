---
# === CORE IDENTIFICATION ===
concept: Regular Character
slug: regular-character

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
  - "chi_reg"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - character-of-a-representation
  - regular-representation
extends:
  - character-of-a-representation
related:
  - decomposition-of-f-g
contrasts_with:
  - principal-character

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the regular character?"
  - "What are the values of the regular character?"
---

# Quick Definition

The regular character chi_reg is the character of the regular representation. It satisfies chi_reg(e) = |G| and chi_reg(g) = 0 for g != e.

# Core Definition

The **regular character** chi_reg is defined by the regular representation (G acting on F[G] by left multiplication). Using the elements of G as a basis for F[G], one sees that chi_reg(g) = |G| if g = e and chi_reg(g) = 0 otherwise. (Milne, Chapter 7, p. 114)

# Prerequisites

- **Character of a representation** — the regular character is a specific character
- **Regular representation** — the underlying representation

# Key Properties

1. chi_reg(e) = |G|
2. chi_reg(g) = 0 for g != e
3. chi_reg = sum f_i chi_i where f_i = dim S_i (from 7.41b)

# Construction / Recognition

1. Use the elements of G as a basis for F[G]
2. Left multiplication by g permutes the basis elements
3. chi_reg(g) = number of fixed basis elements = number of h in G with gh = h
4. Only g = e fixes any basis element, so chi_reg(e) = |G|, chi_reg(g) = 0 otherwise

# Context & Application

The regular character encodes how all irreducible representations combine. Its decomposition chi_reg = sum f_i chi_i shows that S_i appears with multiplicity f_i in the regular representation. Evaluating at e gives sum f_i^2 = |G|.

# Examples

**Example 1** (p. 114): For any G, chi_reg is the delta function scaled by |G|: it equals |G| at the identity and 0 elsewhere.

# Relationships

## Builds Upon
- **regular-representation** — the underlying representation
- **character-of-a-representation** — it is a character

## Enables
- The dimension formula sum f_i^2 = |G|

## Related
- **decomposition-of-f-g** — chi_reg = sum f_i chi_i

## Contrasts With
- **principal-character** — chi_1 is constant 1; chi_reg is supported only at e

# Source Reference

Chapter 7: Representations of Finite Groups, p. 114.

# Verification Notes

- Definition source: Direct from p. 114
- Confidence rationale: HIGH — explicit formula
- Uncertainties: None
