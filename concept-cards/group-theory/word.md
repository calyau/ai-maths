---
# === CORE IDENTIFICATION ===
concept: Word
slug: word

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
pdf_page: 30
section: "Free monoids"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - word in generators

# === TYPED RELATIONSHIPS ===
prerequisites:
  - free-monoid
extends: []
related:
  - reduced-word
  - free-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a word in group theory?"
  - "How are words related to free groups?"
---

# Quick Definition

A word on a set $X$ is a finite sequence of symbols from $X$ (repetition allowed). In the context of free groups, words use symbols from $X' = \{a, a^{-1}, b, b^{-1}, \ldots\}$.

# Core Definition

"A **word** is a finite sequence of symbols from $X$ in which repetition is allowed." (Milne, p. 31)

For free groups, words are formed from $X' = \{a, a^{-1}, b, b^{-1}, \ldots\}$, and two words are equivalent if they have the same reduced form.

# Prerequisites

- **Free monoid** — words are the elements of the free monoid

# Key Properties

1. Words can be multiplied by juxtaposition (concatenation)
2. The empty word serves as the identity element
3. Two words are equivalent ($w \sim w'$) if they have the same reduced form (Proposition 2.1)
4. Products of equivalent words are equivalent (Proposition 2.2)

# Context & Application

Words are the raw material from which free groups and group presentations are built. Relations in a presentation are words that are declared equivalent to the empty word.

# Examples

**Example 1** (p. 31): On $X = \{a, b, c\}$, the words $aaaa$ and $aabac$ are distinct.

**Example 2** (p. 31): On $X' = \{a, a^{-1}, b, b^{-1}, c, c^{-1}\}$, the word $abb^{-1}ca$ contains cancellable pairs.

# Relationships

## Builds Upon
- **free-monoid** — words are elements of $S_X$

## Enables
- **reduced-word** — a word with no cancellable pairs
- **free-group** — equivalence classes of words

# Source Reference

Chapter 2, pages 31-32.

# Verification Notes

- Definition source: Direct from p. 31
- Confidence: HIGH
- Uncertainties: None
