---
# === CORE IDENTIFICATION ===
concept: Addition Modulo n
slug: addition-modulo-n

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
  - modular addition
  - "addition mod n"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
  - congruence-modulo-n
extends: []
related:
  - cyclic-group-zn
  - multiplication-modulo-n
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a cyclic group?"
  - "How do I compute a multiplication table for a dihedral group?"
---

# Quick Definition

Addition modulo n is the operation on the set {0, 1, 2, ..., n-1} where x +_n y equals x + y if x + y < n, and x + y - n if x + y >= n. This operation makes the set into the cyclic group Z_n.

# Core Definition

Armstrong defines: "if x and y are members of this set, define x +_n y = x + y if 0 <= x + y < n, and x + y - n if x + y >= n, and use this as 'multiplication'" (Armstrong, Ch. 3, p. 19). Equivalently, x +_n y is "x + y read mod n."

# Prerequisites

- **Group** — Addition modulo n is verified to give a group
- **Congruence Modulo n** — The underlying equivalence relation

# Key Properties

1. The set is {0, 1, 2, ..., n-1}
2. The result x +_n y is always in {0, 1, ..., n-1}
3. The operation is associative (both (x +_n y) +_n z and x +_n (y +_n z) equal x + y + z reduced mod n)
4. Zero is the identity element
5. The inverse of x (for x != 0) is n - x
6. The operation is commutative: x +_n y = y +_n x

# Construction / Recognition

## To Compute x +_n y:
1. Add x and y as ordinary integers
2. If the sum is less than n, that is the answer
3. If the sum is >= n, subtract n from it
4. The result is the remainder when x + y is divided by n

# Context & Application

Addition modulo n is "a familiar idea; think of adding angles modulo 2pi" (Armstrong, p. 19). It produces the finite cyclic group Z_n, which is one of the fundamental building blocks in group theory.

# Examples

**Example 1** (p. 19): 5 +_6 3 = 8 - 6 = 2.

**Example 2** (p. 20): In Z_6, the element 4 generates the subgroup {0, 2, 4}: 4, 4 +_6 4 = 2, 4 +_6 4 +_6 4 = 0.

# Relationships

## Builds Upon
- **Group** — This operation yields a group
- **Congruence Modulo n** — The underlying arithmetic

## Enables
- **Cyclic Group Zn** — Z_n = ({0, ..., n-1}, +_n)

## Related
- **Multiplication Modulo n** — A different modular operation on the same set

# Common Errors

- **Error**: Forgetting to reduce the sum when x + y >= n
  **Correction**: Always check whether the ordinary sum exceeds n-1 and subtract n if so

# Common Confusions

- **Confusion**: Thinking addition modulo n is the same as multiplication modulo n
  **Clarification**: Addition modulo n always produces a group on {0, ..., n-1}; multiplication modulo n on {1, ..., n-1} gives a group only when n is prime

# Source Reference

Chapter 3: Numbers, pages 12-14 (pdf pp. 19-21).

# Verification Notes

- Definition source: Direct quote from p. 19
- Confidence rationale: High — formally defined with explicit formula
- Uncertainties: None
- Cross-reference status: Verified
