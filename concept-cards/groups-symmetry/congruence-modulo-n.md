---
# === CORE IDENTIFICATION ===
concept: Congruence Modulo n
slug: congruence-modulo-n

# === CLASSIFICATION ===
category: number-groups
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Numbers"
chapter_number: 3
pdf_page: 18
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - modular arithmetic
  - "mod n"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - addition-modulo-n
  - multiplication-modulo-n
  - cyclic-group-zn
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a cyclic group?"
---

# Quick Definition

Two integers are congruent modulo n if they differ by a multiple of n. Each integer is congruent modulo n to exactly one of 0, 1, ..., n-1, namely its remainder upon division by n.

# Core Definition

"Two integers are congruent modulo n if they differ by a multiple of n. Of course each integer x is congruent modulo n to exactly one of the integers 0, 1, 2, ..., n-1, namely, to the remainder obtained on dividing x by n. We shall refer to this remainder as 'x read mod n', or simply x (mod n)" (Armstrong, Ch. 3, p. 20).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. x is congruent to y mod n if and only if n divides (x - y)
2. Each integer has a unique representative in {0, 1, ..., n-1}
3. x (mod n) is the remainder when x is divided by n
4. Congruence mod n is an equivalence relation (reflexive, symmetric, transitive)
5. x +_n y = (x + y) (mod n) and x *_n y = (xy) (mod n)

# Construction / Recognition

## To Compute x (mod n):
1. Divide x by n using the division algorithm: x = qn + r where 0 <= r < n
2. The remainder r is x (mod n)

# Context & Application

Congruence modulo n is the foundation for modular arithmetic, which gives rise to both the cyclic group Z_n (under addition mod n) and, when n is prime, the multiplicative group {1, ..., n-1} under multiplication mod n.

# Examples

**Example 1** (p. 20): x +_n y is x + y read mod n. For instance, 5 +_6 3 = 8 (mod 6) = 2.

**Example 2** (p. 20): 5 *_6 3 = 15 (mod 6) = 3, since dividing 15 by 6 leaves remainder 3.

# Relationships

## Enables
- **Addition Modulo n** — Defined using congruence
- **Multiplication Modulo n** — Defined using congruence
- **Cyclic Group Zn** — Built from modular arithmetic

# Common Errors

- **Error**: Computing negative remainders
  **Correction**: The representative must be in {0, 1, ..., n-1}; add n if needed

# Common Confusions

- **Confusion**: Thinking congruence means equality
  **Clarification**: Congruent integers may be different (e.g., 8 and 2 are congruent mod 6 but are not equal)

# Source Reference

Chapter 3: Numbers, page 13 (pdf p. 20).

# Verification Notes

- Definition source: Direct quote from p. 20
- Confidence rationale: High — explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
