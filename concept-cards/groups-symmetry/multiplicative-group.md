---
# === CORE IDENTIFICATION ===
concept: Multiplicative Group
slug: multiplicative-group

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
  - multiplicative group of non-zero numbers

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
extends:
  - group
related:
  - unit-circle-group
  - additive-group-of-integers
contrasts_with:
  - additive-group-of-integers

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a group?"
  - "What distinguishes a group from a set with an operation?"
---

# Quick Definition

A multiplicative group is a group whose operation is multiplication of numbers. Zero must be excluded because it has no multiplicative inverse. Examples include Q - {0}, R - {0}, R^{pos}, Q^{pos}, {+1, -1}, C - {0}, and {+1, -1, +i, -i}.

# Core Definition

"Multiplication of numbers (real or complex) makes each of the following sets into a group: Q - {0}, R - {0}, Q^{pos}, R^{pos}, {+1, -1}, C - {0}, C, {+1, -1, +i, -i}. In each case the number 1 is the identity element, and 1/x is the inverse of the number x" (Armstrong, Ch. 3, p. 18).

# Prerequisites

- **Group** — Multiplicative groups satisfy the group axioms

# Key Properties

1. The group operation is multiplication
2. The identity element is 1
3. The inverse of x is 1/x
4. Zero must be excluded: there is no x with 0 * x = 1
5. All listed multiplicative groups are abelian
6. The non-zero integers do not form a multiplicative group (e.g., 2 has no integer multiplicative inverse)

# Construction / Recognition

## To Verify:
1. Check that the product of any two elements is in the set (closure)
2. Multiplication is associative
3. 1 is in the set and acts as identity
4. For each element x, 1/x is in the set

# Context & Application

Armstrong emphasizes what is missing from the list as much as what is present. The integers cannot form a multiplicative group because most integers lack multiplicative inverses within Z. This illustrates that the same set may form a group under one operation but not another.

# Examples

**Example 1** (p. 18-19): Q - {0} forms a group under multiplication: 1 is the identity, and 1/x is the inverse of any non-zero rational x.

**Example 2** (p. 19): The non-zero integers do not form a multiplicative group because 2 has no multiplicative inverse in Z (1/2 is not an integer).

**Example 3** (p. 18): {+1, -1} forms a group under multiplication with identity 1; each element is its own inverse.

# Relationships

## Builds Upon
- **Group** — Multiplicative groups are groups

## Related
- **Unit Circle Group** — C (modulus-1 complex numbers) is a multiplicative group

## Contrasts With
- **Additive Group of Integers** — Same underlying set (Z), but multiplication does not give a group on Z

# Common Errors

- **Error**: Including zero in a multiplicative group
  **Correction**: Zero has no multiplicative inverse and must always be excluded

- **Error**: Assuming all non-zero integers form a multiplicative group
  **Correction**: Most integers lack multiplicative inverses in Z; only {+1, -1} works

# Common Confusions

- **Confusion**: Thinking a set that forms a group under addition automatically forms a group under multiplication
  **Clarification**: The two operations have different structural requirements; Z forms a group under addition but not under multiplication

# Source Reference

Chapter 3: Numbers, pages 11-12 (pdf pp. 18-19).

# Verification Notes

- Definition source: Direct from p. 18
- Confidence rationale: High — explicitly listed with analysis of failures
- Uncertainties: None
- Cross-reference status: Verified
