---
# === CORE IDENTIFICATION ===
concept: Virtual Character
slug: virtual-character

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
pdf_page: 115
section: "The characters of G"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - character-of-a-representation
  - irreducible-character
extends: []
related:
  - class-function
contrasts_with:
  - irreducible-character

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a virtual character?"
  - "How do virtual characters relate to actual characters?"
---

# Quick Definition

A virtual character is any Z-linear combination of characters, i.e., a function G -> F of the form sum m_i chi_i with m_i in Z (possibly negative).

# Core Definition

Any function G -> F that can be expressed as a Z-linear combination of characters is called a **virtual character**. The simple characters form a Z-basis for the virtual characters (Proposition 7.46). (Milne, Chapter 7, p. 115)

# Prerequisites

- **Character of a representation** — virtual characters are Z-linear combinations of these
- **Irreducible character** — form a Z-basis for virtual characters

# Key Properties

1. Virtual characters form a Z-module (free abelian group) with basis the irreducible characters
2. Characters (actual, not virtual) are the virtual characters with all coefficients in N
3. A virtual character is a class function, but not every class function is a virtual character
4. The term "generalized character" is sometimes used but Milne avoids it (footnote, p. 115)

# Construction / Recognition

1. A virtual character is sum m_i chi_i with m_i in Z
2. It is an actual character iff all m_i >= 0
3. To test if a class function is a virtual character, compute (f | chi_i) and check they are integers

# Context & Application

Virtual characters arise naturally in induction and restriction formulas, and in the theory of Brauer characters. They form the natural Z-module in which character arithmetic takes place.

# Examples

**Example 1** (p. 115): chi_1 - chi_2 is a virtual character (but not an actual character if chi_1 != chi_2).

# Relationships

## Builds Upon
- **character-of-a-representation** — Z-linear combinations of characters
- **irreducible-character** — form a Z-basis

## Related
- **class-function** — virtual characters are class functions with integer inner products

## Contrasts With
- **irreducible-character** — actual characters have non-negative integer coefficients

# Source Reference

Chapter 7: Representations of Finite Groups, Proposition 7.46, p. 115.

# Verification Notes

- Definition source: Direct from p. 115
- Confidence rationale: HIGH — explicit definition
- Uncertainties: None
