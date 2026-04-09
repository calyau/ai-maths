---
# === CORE IDENTIFICATION ===
concept: Powers of an Element
slug: powers-of-an-element

# === CLASSIFICATION ===
category: group-fundamentals
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Basic Definitions and Results"
chapter_number: 1
pdf_page: 8
section: "Definitions and examples"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "integer multiples (additive notation)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
  - neutral-element
  - inverse-element
extends: []
related:
  - order-of-an-element
  - cyclic-subgroup
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How are integer powers of a group element defined?"
  - "What are the laws of exponents in a group?"
---

# Quick Definition

For an element a of a group G, the power a^n is defined for all integers n: a^n is the product of n copies of a when n > 0, equals e when n = 0, and is the product of |n| copies of a^{-1} when n < 0.

# Core Definition

For an element a of a group G, define:

- a^n = aa...a (n copies of a) when n > 0
- a^0 = e
- a^n = a^{-1}a^{-1}...a^{-1} (|n| copies of a^{-1}) when n < 0

The usual rules hold: a^m * a^n = a^{m+n} and (a^m)^n = a^{mn} for all m, n in Z (Equation 4, p. 8).

In additive notation, a^n is written na and the rules become ma + na = (m+n)a and m(na) = (mn)a.

# Prerequisites

- **Group** — powers are defined for elements of a group
- **Neutral element** — a^0 = e
- **Inverse element** — negative powers use inverses

# Key Properties

1. a^m * a^n = a^{m+n} for all m, n in Z
2. (a^m)^n = a^{mn} for all m, n in Z
3. a^0 = e (the neutral element)
4. a^{-1} is the inverse of a
5. The set {n in Z | a^n = e} is an ideal in Z

# Construction / Recognition

## To Construct:
1. For n > 0: multiply a by itself n times
2. For n = 0: the result is e
3. For n < 0: multiply a^{-1} by itself |n| times

# Context & Application

Powers of an element formalize repeated application of the group operation. They are central to defining the order of an element and cyclic subgroups. In a commutative group written additively, the notation becomes integer multiples: na = a + a + ... + a.

# Examples

**Example 1** (p. 8): In Z (written additively), na is just ordinary integer multiplication.

**Example 2** (p. 13, 1.17): In D_n, r^n = e, so r has order n. The elements of D_n include r^0 = e, r, r^2, ..., r^{n-1}.

# Relationships

## Builds Upon
- **neutral-element** — defines a^0
- **inverse-element** — defines negative powers

## Enables
- **order-of-an-element** — defined as the smallest positive n with a^n = e
- **cyclic-subgroup** — <a> = {a^n | n in Z}

# Common Errors

- **Error**: Assuming (ab)^n = a^n b^n in a non-abelian group
  **Correction**: This identity holds only when a and b commute

# Common Confusions

- **Confusion**: Thinking the exponent laws a^m a^n = a^{m+n} require commutativity
  **Clarification**: These laws hold for powers of a *single* element in any group; commutativity is only needed for products of powers of *different* elements

# Source Reference

Chapter 1: Basic Definitions and Results, page 8, Equation (4).

# Verification Notes

- Definition source: Direct from text, p. 8
- Confidence rationale: HIGH — explicitly defined with exponent laws stated
- Uncertainties: None
- Cross-reference status: Verified against planned cards
