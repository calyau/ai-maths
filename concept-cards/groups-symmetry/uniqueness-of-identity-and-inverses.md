---
# === CORE IDENTIFICATION ===
concept: Uniqueness of Identity and Inverses
slug: uniqueness-of-identity-and-inverses

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
  - identity-element
  - inverse-element
  - associativity
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a group?"
  - "What distinguishes a group from a set with an operation?"
---

# Quick Definition

In any group, the identity element is unique and the inverse of each element is unique. These are the first theoretical consequences deduced purely from the group axioms.

# Core Definition

Armstrong proves two results from the axioms alone. First, the identity is unique: if e and e' are both identities, then ee' = e' (since e is an identity) and ee' = e (since e' is an identity), so e = e'. Second, inverses are unique: if y and z are both inverses of x, then "y = ey = (zx)y = z(xy) = ze = z" (Armstrong, Ch. 2, p. 16).

# Prerequisites

- **Group** — These are properties of groups
- **Identity Element** — The identity's uniqueness is being proved
- **Inverse Element** — Inverse uniqueness is being proved
- **Associativity** — The inverse uniqueness proof uses associativity

# Key Properties

1. The identity is unique: if e and e' both satisfy the identity axiom, then e = e'
2. Each element has exactly one inverse: if y and z both satisfy the inverse axiom for x, then y = z
3. Both proofs use only the group axioms, so they hold for every group
4. The inverse uniqueness proof specifically requires associativity

# Construction / Recognition

## Proof of Identity Uniqueness:
1. Suppose e and e' are both identities
2. Then ee' = e' (because e is an identity)
3. And ee' = e (because e' is an identity)
4. Therefore e = e'

## Proof of Inverse Uniqueness:
1. Suppose y and z are both inverses of x
2. y = ey = (zx)y = z(xy) = ze = z
3. Therefore y = z

# Context & Application

Armstrong uses these proofs to illustrate the power of the axiomatic method: "Notice that both arguments use only those facts about a group which are supplied by the axioms. For this reason we can be confident that the conclusions hold for every group" (Ch. 2, p. 16). These are the first examples of abstract reasoning from axioms in the text.

# Examples

**Example 1** (p. 16): The proof that identity is unique: ee' = e' (e is identity) and ee' = e (e' is identity), hence e = e'.

**Example 2** (p. 16): The proof that inverse of x is unique: y = ey = (zx)y = z(xy) = ze = z.

# Relationships

## Builds Upon
- **Group** — These are consequences of the group axioms
- **Associativity** — Used in the inverse uniqueness proof

## Enables
- Confidence that notation e and x^{-1} is unambiguous

# Common Errors

- **Error**: Attempting to prove uniqueness of inverses without using associativity
  **Correction**: The step (zx)y = z(xy) requires associativity; it is essential to the proof

# Common Confusions

- **Confusion**: Thinking uniqueness is part of the axioms
  **Clarification**: The axioms only assert existence; uniqueness is a theorem that follows from the axioms

# Source Reference

Chapter 2: Axioms, page 9 (pdf p. 16).

# Verification Notes

- Definition source: Direct proofs quoted from p. 16
- Confidence rationale: High — explicit proofs given
- Uncertainties: None
- Cross-reference status: Verified
