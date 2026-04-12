---
concept: Unit
slug: unit-element
category: ring-theory
subcategory: basic-structures
tier: intermediate
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Rings"
chapter_number: 11
pdf_page: 339
section: "Definition of a Ring"
extraction_confidence: high
aliases:
  - "unit of a ring"
  - "invertible element"
prerequisites:
  - ring
extends: []
related:
  - field
  - zero-divisor
  - integral-domain
contrasts_with:
  - zero-divisor
  - irreducible-element
answers_questions:
  - "What is a unit in a ring?"
  - "What distinguishes a ring from a field?"
---

# Quick Definition

A unit of a ring is an element that has a multiplicative inverse. Fields are precisely the nonzero rings in which every nonzero element is a unit.

# Core Definition

A unit of a ring is an element that has a multiplicative inverse (Artin, p. 340). The identity element 1 is always a unit. Fields are rings in which 0 != 1 and in which every nonzero element is a unit.

# Prerequisites

- **Ring** -- Units are defined within the context of a ring

# Key Properties

1. The set of units forms a group under multiplication
2. The identity 1 is always a unit
3. A ring is a field if and only if 0 != 1 and every nonzero element is a unit

# Construction / Recognition

## To Recognize:
1. Check whether the element a has an element b such that ab = 1

# Context & Application

Units play a key role in factorization theory: two elements are associates if they differ by a unit factor, and irreducible factorizations are unique only up to unit factors.

# Examples

**Example 1** (p. 340): The units in Z are 1 and -1.

**Example 2** (p. 340): The units in Z[i] are +/-1 and +/-i.

**Example 3** (p. 340): The units in R[x] are the nonzero constant polynomials.

# Relationships

## Builds Upon
- **Ring** -- Units are elements of a ring with special properties

## Enables
- **Associates** -- Elements related by unit multiples
- **Field** -- A ring where all nonzero elements are units

## Contrasts With
- **Zero divisor** -- A nonzero non-unit element whose product with another nonzero element is zero

# Common Confusions

- **Confusion**: The term "unit" vs "unit element" (identity)
  **Clarification**: Artin notes the ambiguity: "unit" means an invertible element, while "the unit element" refers to the identity 1. The terminology is poorly chosen but standard.

# Source Reference

Chapter 11: Rings, Section 11.1, page 340.

# Verification Notes

- Definition source: Direct from text
- Confidence rationale: Explicit definition with examples
- Uncertainties: None
- Cross-reference status: Verified
