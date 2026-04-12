---
# === CORE IDENTIFICATION ===
concept: Associativity
slug: associativity

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
  - associative law
  - associative property

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
extends: []
related:
  - general-associative-law
  - composition-of-symmetries
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a group?"
  - "What distinguishes a group from a set with an operation?"
---

# Quick Definition

Associativity is the first group axiom: for any three elements x, y, z of a group, (xy)z = x(yz). It ensures that the product of three or more elements is well-defined regardless of how the terms are bracketed.

# Core Definition

Group axiom (a): "The multiplication is associative, that is to say (xy)z = x(yz) for any three (not necessarily distinct) elements from G" (Armstrong, Ch. 2, p. 13). This property is inherited from the concrete setting of symmetry composition, where Armstrong notes "(uv)w = u(vw) for any three (not necessarily distinct) symmetries of T" (Ch. 1, p. 11).

# Prerequisites

- **Group** — Associativity is one of the defining axioms of a group

# Key Properties

1. (xy)z = x(yz) for all x, y, z in the group
2. Extends to products of any finite number of elements (general associative law)
3. Does not need to be checked when verifying a subgroup (inherited from the ambient group)
4. Must be verified independently when checking that a new algebraic structure is a group

# Construction / Recognition

## To Verify:
1. For an arbitrary triple x, y, z from the candidate group, compute (xy)z
2. Compute x(yz) independently
3. Verify these are equal for all triples

# Context & Application

Associativity is often the easiest axiom to verify because it is frequently inherited from a known structure (e.g., matrix multiplication, function composition, or number arithmetic are all known to be associative). Armstrong proves the general associative law in Chapter 4, showing that associativity of triples implies well-definedness of arbitrary-length products.

# Examples

**Example 1** (p. 11): For symmetries of the tetrahedron, (uv)w = u(vw) holds because composition of functions is associative.

**Example 2** (p. 14): The Lorentz group inherits associativity from matrix multiplication.

**Example 3** (p. 13): Addition of real numbers is associative: (x + y) + z = x + (y + z).

# Relationships

## Builds Upon
- **Group** — Associativity is axiom (a) of a group

## Enables
- **General Associative Law** — Extends associativity to products of n elements

## Related
- **Composition of Symmetries** — Composition is associative

# Common Errors

- **Error**: Attempting to verify associativity for a subgroup
  **Correction**: Associativity is inherited from the ambient group; only closure, identity, and inverses need checking for subgroups

# Common Confusions

- **Confusion**: Confusing associativity with commutativity
  **Clarification**: Associativity says (xy)z = x(yz) (bracketing doesn't matter); commutativity says xy = yx (order doesn't matter). These are independent properties.

# Source Reference

Chapter 2: Axioms, page 6 (pdf p. 13). Also Chapter 1, page 5 (pdf p. 12) for the symmetry motivation.

# Verification Notes

- Definition source: Direct quote from p. 13
- Confidence rationale: High — explicitly stated as axiom (a)
- Uncertainties: None
- Cross-reference status: Verified
