---
# === CORE IDENTIFICATION ===
concept: Reduced Word
slug: reduced-word

# === CLASSIFICATION ===
category: combinatorial-group-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Free Groups and Presentations"
chapter_number: 27
pdf_page: 173
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - reduced form

# === TYPED RELATIONSHIPS ===
prerequisites:
  - word
extends:
  - word
related:
  - free-group
contrasts_with:
  - word

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a reduced word?"
  - "How do I reduce a word in a free group?"
---

# Quick Definition

A reduced word is a word x_1^{n_1} x_2^{n_2} ... x_k^{n_k} in which no two adjacent generators are equal (x_i is not x_{i+1}) and all exponents are non-zero. Every word simplifies to a unique reduced word.

# Core Definition

Armstrong says "the word is reduced if x_i is never equal to x_{i+1} and all the m_i are non-zero" (Ch. 27, p. 173). "Each word can be simplified to a reduced word by collecting up powers when adjacent elements are equal, and omitting zeroth powers" (Armstrong, p. 173). Theorem 27.1 proves that "each word can be simplified to only one reduced word" (Armstrong, p. 174).

# Prerequisites

- **Word** -- A reduced word is a word in canonical form

# Key Properties

1. No two adjacent generators are the same
2. All exponents are non-zero
3. Every word reduces to a unique reduced word (Theorem 27.1)
4. The empty word is the reduced form of any word that evaluates to the identity
5. The inverse of a reduced word x_1^{n_1} ... x_k^{n_k} is x_k^{-n_k} ... x_1^{-n_1}, which is also reduced
6. Multiplication in the free group: concatenate two reduced words, then reduce the result

# Construction / Recognition

## To Reduce a Word
1. Scan for adjacent occurrences of the same generator
2. Add their exponents: x^m x^n = x^{m+n}
3. If the combined exponent is zero, remove the factor entirely
4. Repeat until no adjacent generators are equal and no zero exponents remain

## To Recognize a Reduced Word
1. Check that no two consecutive factors use the same generator
2. Check that all exponents are non-zero
3. If both conditions hold, the word is reduced

# Context & Application

Reduced words are the canonical representatives of elements in a free group. The uniqueness of reduction (Theorem 27.1) is essential: it ensures the free group is well-defined. Armstrong proves uniqueness using a permutation argument reminiscent of Cayley's theorem.

# Examples

**Example 1** (p. 174): x^{-3}x^2y^5y^{-5}x^7z^2z^{-2}x^{-1}xzy^2x^{-1} reduces to x^6zy^2x^{-1}.

**Example 2** (p. 174): The word x_1^0 reduces to the empty word.

# Relationships

## Builds Upon
- **Word** -- A reduced word is a simplified word

## Enables
- **Free group** -- The free group is the group of reduced words under concatenation-and-reduce

## Contrasts With
- **Word** -- A general word may have adjacent equal generators or zero exponents

# Common Errors

- **Error**: Thinking reduction might yield different results depending on the order of simplification
  **Correction**: Theorem 27.1 guarantees uniqueness of the reduced form

# Common Confusions

- **Confusion**: Thinking reduced means "simplified in the quotient group"
  **Clarification**: Reduction is purely formal -- it only combines adjacent equal generators. In a non-free group, additional simplifications (from relations) apply

# Source Reference

Chapter 27: Free Groups and Presentations, pages 173-175 (pdf pp. 173-175). Definition on p. 173; Theorem 27.1 (uniqueness) on p. 174.

# Verification Notes

- Definition: Directly quoted from Armstrong p. 173
- Uniqueness theorem: Theorem 27.1, proved on p. 174
- Confidence: HIGH -- explicit definition and theorem
- Cross-references: Verified against planned extractions
- Uncertainties: None
