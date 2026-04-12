---
# === CORE IDENTIFICATION ===
concept: Unit Circle Group
slug: unit-circle-group

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
  - circle group
  - "C (unit circle)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
  - multiplicative-group
extends:
  - multiplicative-group
related:
  - order-of-an-element
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a group?"
---

# Quick Definition

The unit circle group, denoted C, is the set of complex numbers with modulus 1, forming a group under complex multiplication. It is an infinite abelian group containing elements of both finite and infinite order.

# Core Definition

"We use C to denote the unit circle in the complex plane, that is to say, the set of those complex numbers which have modulus one" (Armstrong, Ch. 3, p. 19). Armstrong verifies: if z, w are in C, then |zw| = |z||w| = 1, so zw is in C. The number 1 lies in C and is the identity. If z is in C, then |1/z| = 1/|z| = 1, so 1/z is in C. Complex multiplication makes C into a group.

# Prerequisites

- **Group** — C is verified to be a group
- **Multiplicative Group** — C is a multiplicative group of complex numbers

# Key Properties

1. Elements are complex numbers z with |z| = 1
2. The group operation is complex multiplication
3. The identity is 1
4. The inverse of z is 1/z (= conjugate of z)
5. The group is abelian and infinite
6. Elements can be written as e^{i*theta}
7. Contains elements of both finite and infinite order: e^{i*theta} has finite order precisely when theta is a rational multiple of 2pi

# Construction / Recognition

## To Verify:
1. |zw| = |z||w| = 1 (closure)
2. Complex multiplication is associative
3. |1| = 1 (identity in C)
4. |1/z| = 1/|z| = 1 (inverse in C)

# Context & Application

The unit circle group is notable because it is an infinite group containing elements of both finite and infinite order. This makes it a rich source of examples for order theory in Chapter 4.

# Examples

**Example 1** (p. 19): Closure proof: if z, w have |z| = |w| = 1, then |zw| = |z||w| = 1.

**Example 2** (Ch. 4, p. 25): A typical element e^{i*theta} has finite order precisely when theta = 2m*pi/n for integers m, n. For example, e^{i*pi/3} has order 6.

**Example 3** (Ch. 5, p. 28): {+1, -1} < C and C < C - {0} (chain of subgroups).

# Relationships

## Builds Upon
- **Multiplicative Group** — C is a multiplicative group of complex numbers

## Enables
- **Order of an Element** — C provides examples of both finite and infinite order

## Related
- **Cyclic Group Zn** — The nth roots of unity form a cyclic subgroup of C

# Common Errors

- **Error**: Assuming all elements of C have finite order
  **Correction**: e^{i*theta} has infinite order when theta is an irrational multiple of 2pi

# Common Confusions

- **Confusion**: Confusing the unit circle group C with the full multiplicative group C - {0}
  **Clarification**: C contains only elements of modulus 1; C - {0} contains all non-zero complex numbers

# Source Reference

Chapter 3: Numbers, page 12 (pdf p. 19). Also Chapter 4, page 18 (pdf p. 25) for order examples.

# Verification Notes

- Definition source: Direct quote and verification from p. 19
- Confidence rationale: High — explicitly constructed and verified
- Uncertainties: None
- Cross-reference status: Verified
