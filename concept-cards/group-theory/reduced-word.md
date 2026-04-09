---
# === CORE IDENTIFICATION ===
concept: Reduced Word
slug: reduced-word

# === CLASSIFICATION ===
category: free-groups-presentations
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Free Groups and Presentations; Coxeter Groups"
chapter_number: 2
pdf_page: 31
section: "Free groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - reduced form

# === TYPED RELATIONSHIPS ===
prerequisites:
  - word
extends: []
related:
  - free-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a reduced word?"
  - "How do you reduce a word in a free group?"
  - "Is the reduced form of a word unique?"
---

# Quick Definition

A word on $X'$ is reduced if it contains no adjacent pairs $aa^{-1}$ or $a^{-1}a$. Every word has a unique reduced form, obtained by repeatedly cancelling such pairs.

# Core Definition

"A word is said to be *reduced* if it contains no pairs of the form $aa^{-1}$ or $a^{-1}a$." (Milne, p. 32)

"There is only one reduced form of a word." (Proposition 2.1, p. 32)

# Prerequisites

- **Word** — reduced words are special words

# Key Properties

1. Every word can be reduced to a unique reduced form by cancelling adjacent inverse pairs (Proposition 2.1)
2. The order of cancellations does not matter (uniqueness)
3. Two words are equivalent iff they have the same reduced form
4. Each element of the free group is represented by a unique reduced word
5. Multiplication in the free group: juxtapose and reduce

# Construction / Recognition

## To Reduce a Word:
1. Scan for adjacent pairs $aa^{-1}$ or $a^{-1}a$
2. Cancel one such pair
3. Repeat until no cancellable pairs remain
4. The result is the unique reduced form (regardless of cancellation order)

# Context & Application

Reduced words provide canonical representatives for elements of free groups. The uniqueness of the reduced form (Proposition 2.1) is essential for the well-definedness of the free group construction.

# Examples

**Example 1** (p. 32): The word $cab \cdot a^{-1}a \cdot a^{-1}ca$ can be reduced by different cancellation sequences, but both yield the same reduced word $caba^{-1}ca$ (after working through the cancellations).

# Relationships

## Builds Upon
- **word**

## Enables
- **free-group** — elements are equivalence classes, represented by unique reduced words

# Common Errors

- **Error**: Worrying that different cancellation orders might yield different results
  **Correction**: Proposition 2.1 guarantees the reduced form is unique

# Source Reference

Chapter 2, Proposition 2.1, pages 31-32.

# Verification Notes

- Definition source: Direct from p. 32
- Confidence: HIGH — explicit definition with uniqueness proof
- Uncertainties: None
