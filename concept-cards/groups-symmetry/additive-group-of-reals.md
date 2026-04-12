---
# === CORE IDENTIFICATION ===
concept: Additive Group of Reals
slug: additive-group-of-reals

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
  - "(R, +)"
  - reals under addition

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
extends:
  - group
related:
  - additive-group-of-rationals
  - additive-group-of-integers
  - additive-group-of-complex-numbers
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a group?"
---

# Quick Definition

The additive group of reals, denoted R, is the set of all real numbers with addition as the group operation. The identity is 0 and the inverse of x is -x.

# Core Definition

"Addition of numbers (real or complex) makes each of the following sets into a group: ... R, the set of real numbers" (Armstrong, Ch. 3, p. 18). Armstrong notes that "we agree to use the same symbol R for the set of real numbers, and for the group of real numbers under addition" (p. 19).

# Prerequisites

- **Group** — R is verified to satisfy the group axioms under addition

# Key Properties

1. The group operation is addition
2. The identity element is 0
3. The inverse of x is -x
4. The group is abelian
5. R has infinite order
6. Every non-zero element has infinite order (repeatedly adding a non-zero real never gives 0)
7. Z < Q < R (chain of subgroups)

# Construction / Recognition

## To Verify:
1. The sum of two reals is real (closure)
2. Addition is associative
3. 0 is the identity
4. -x is the inverse of x

# Context & Application

Armstrong uses R as an example where "every element (except 0) has infinite order because repeatedly adding a real number to itself never gives zero, unless of course the number was zero to start with" (Ch. 4, p. 25).

# Examples

**Example 1** (p. 18): R forms a group under addition.

**Example 2** (Ch. 4, p. 25): R has infinite order, and every non-zero element has infinite order.

# Relationships

## Builds Upon
- **Group** — This is a group under addition

## Related
- **Additive Group of Integers** — Z < R
- **Additive Group of Rationals** — Q < R

# Common Errors

- **Error**: Confusing (R, +) with (R - {0}, *)
  **Correction**: These are different groups with different operations and different identity elements

# Common Confusions

- **Confusion**: Thinking some non-zero real number has finite order under addition
  **Clarification**: No non-zero real has finite order; nx = 0 implies x = 0

# Source Reference

Chapter 3: Numbers, page 11 (pdf p. 18). Also Chapter 4, page 18 (pdf p. 25) for order discussion.

# Verification Notes

- Definition source: Direct from p. 18
- Confidence rationale: High — explicitly listed
- Uncertainties: None
- Cross-reference status: Verified
