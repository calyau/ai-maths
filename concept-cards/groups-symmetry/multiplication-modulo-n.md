---
# === CORE IDENTIFICATION ===
concept: Multiplication Modulo n
slug: multiplication-modulo-n

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
  - modular multiplication
  - "multiplication mod n"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
  - congruence-modulo-n
extends: []
related:
  - addition-modulo-n
  - cyclic-group-zn
contrasts_with:
  - addition-modulo-n

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a group?"
  - "What distinguishes a group from a set with an operation?"
---

# Quick Definition

Multiplication modulo n is the operation x *_n y = xy (mod n) on the integers {1, 2, ..., n-1}. This yields a group if and only if n is a prime number.

# Core Definition

"The integers 0, 1, 2, ..., n-1 may also be multiplied modulo n via x *_n y = xy (mod n)" (Armstrong, Ch. 3, p. 20). After removing 0, the set {1, ..., n-1} forms a group under this operation precisely when n is prime (Exercise 3.10). When n is not prime, the product of two non-zero elements can be zero (e.g., 2 *_10 5 = 0), violating closure.

# Prerequisites

- **Group** — To determine whether multiplication mod n gives a group
- **Congruence Modulo n** — The underlying arithmetic

# Key Properties

1. The operation is x *_n y = xy (mod n)
2. The identity element is 1
3. Closure on {1, ..., n-1} fails when n is composite (products can be 0 mod n)
4. When n is prime, {1, ..., n-1} forms a group of order n-1
5. For composite n, certain subsets of {1, ..., n-1} may still form groups

# Construction / Recognition

## To Verify (for prime p):
1. Show that the product of two elements of {1, ..., p-1} is non-zero mod p
2. Verify that 1 is the identity
3. Show each element x has a multiplicative inverse z with xz = 1 (mod p) (Exercise 3.9)
4. Associativity follows from integer multiplication

# Context & Application

This illustrates that whether a set with an operation forms a group depends on both the set and the operation. Armstrong uses the failure for composite n to motivate careful checking of group axioms.

# Examples

**Example 1** (p. 20): 5 *_6 3 = 15 (mod 6) = 3.

**Example 2** (p. 20): For n = 10, 2 *_10 5 = 10 (mod 10) = 0, which is not in {1, ..., 9}, so {1, ..., 9} does not form a group under multiplication mod 10.

**Example 3** (p. 20): Deleting 0, 2, 4, 5, 6, 8 from {0, ..., 9} leaves {1, 3, 7, 9}, which does form a group under multiplication mod 10.

# Relationships

## Builds Upon
- **Congruence Modulo n** — The underlying arithmetic

## Related
- **Addition Modulo n** — A different modular operation that always yields a group

## Contrasts With
- **Addition Modulo n** — Addition mod n always gives a group; multiplication mod n does not (unless n is prime)

# Common Errors

- **Error**: Assuming multiplication mod n always gives a group on {1, ..., n-1}
  **Correction**: This works only for prime n; for composite n, products of non-zero elements can be zero

# Common Confusions

- **Confusion**: Thinking that removing 0 is sufficient to fix the problem
  **Clarification**: For composite n, even after removing 0, products of remaining elements may fall outside the set (equal to 0 mod n)

# Source Reference

Chapter 3: Numbers, pages 13-14 (pdf pp. 20-21). See Exercises 3.9 and 3.10.

# Verification Notes

- Definition source: Direct quote from p. 20
- Confidence rationale: High — explicitly defined with counterexamples
- Uncertainties: None
- Cross-reference status: Verified
