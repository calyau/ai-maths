---
# === CORE IDENTIFICATION ===
concept: Inverse Element
slug: inverse-element

# === CLASSIFICATION ===
category: fundamentals
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Axioms"
chapter_number: 2
pdf_page: 13
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - inverse
  - group inverse

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
  - identity-element
extends:
  - inverse-symmetry
related:
  - inverse-of-a-product
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a group?"
  - "What distinguishes a group from a set with an operation?"
---

# Quick Definition

The inverse of an element x in a group G is the unique element x^{-1} in G satisfying x^{-1}x = e = xx^{-1}, where e is the identity element. Every element of a group has exactly one inverse.

# Core Definition

Group axiom (c): "Each element x of G has a (so-called) inverse x^{-1} which belongs to the set G and satisfies x^{-1}x = e = xx^{-1}" (Armstrong, Ch. 2, p. 13). Armstrong proves uniqueness: if y and z are both inverses of x, then y = ey = (zx)y = z(xy) = ze = z (Armstrong, Ch. 2, p. 16).

# Prerequisites

- **Group** — Inverses are part of the group definition
- **Identity Element** — Inverses are defined in terms of the identity

# Key Properties

1. x^{-1}x = e = xx^{-1}
2. The inverse of each element is unique (proved in Chapter 2)
3. The inverse of the identity is the identity: e^{-1} = e
4. The inverse of x^{-1} is x: (x^{-1})^{-1} = x
5. In additive groups, the inverse of x is -x
6. In multiplicative groups, the inverse of x is 1/x

# Construction / Recognition

## To Find:
1. Given element x, find an element y such that xy = e
2. Verify that yx = e also holds
3. This y is x^{-1} and is unique

# Context & Application

The existence and uniqueness of inverses is what distinguishes a group from a mere monoid (a set with an associative operation and identity). Armstrong emphasizes that the inverse must belong to the group itself, not merely exist in some larger structure. This is why the non-zero integers do not form a group under multiplication: 2 has no multiplicative inverse in the integers.

# Examples

**Example 1** (p. 13): In the additive group of real numbers, -x is the inverse of x because x + (-x) = 0.

**Example 2** (p. 14): In the Lorentz group, the inverse of the matrix with parameter u is the matrix with parameter -u.

**Example 3** (p. 16): Uniqueness proof: if y and z are both inverses of x, then y = ey = (zx)y = z(xy) = ze = z.

# Relationships

## Builds Upon
- **Group** — Inverses are axiom (c)
- **Identity Element** — Inverses are defined relative to e
- **Inverse Symmetry** — The abstract inverse generalizes the inverse symmetry

## Enables
- **Inverse of a Product** — (xy)^{-1} = y^{-1}x^{-1}
- **Subgroup Test Theorem** — Testing xy^{-1} membership

## Related
- **Inverse of a Product** — The inverse of a product reverses the order

# Common Errors

- **Error**: Assuming the inverse of x is always 1/x
  **Correction**: The form of the inverse depends on the group operation: -x for additive groups, 1/x for multiplicative groups, reverse rotation for symmetry groups

# Common Confusions

- **Confusion**: Thinking that having an inverse in a larger set suffices
  **Clarification**: The inverse must belong to the group G itself; e.g., 2 has an inverse (1/2) in the rationals, but not in the integers

# Source Reference

Chapter 2: Axioms, pages 6, 9 (pdf pp. 13, 16). Uniqueness proof on p. 16.

# Verification Notes

- Definition source: Direct quote from p. 13; uniqueness proof from p. 16
- Confidence rationale: High — formally defined as axiom (c) with uniqueness proof
- Uncertainties: None
- Cross-reference status: Verified
