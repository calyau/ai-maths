---
# === CORE IDENTIFICATION ===
concept: Special Orthogonal Group
slug: special-orthogonal-group

# === CLASSIFICATION ===
category: classical-groups
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 15
section: "Introductory overview"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - SO_n

# === TYPED RELATIONSHIPS ===
prerequisites:
  - orthogonal-group
extends:
  - orthogonal-group
related:
  - almost-simple-algebraic-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine algebraic group?"
---

# Quick Definition

The special orthogonal group SO_n is the identity component of O_n, consisting of orthogonal matrices with determinant 1. SO_{2n+1} is almost-simple of type B_n; SO_{2n} is almost-simple of type D_n.

# Core Definition

The **special orthogonal group** SO_n = Ker(det: O_n -> {+/-1}) is the connected component of the identity in O_n, a normal algebraic subgroup of index 2 (p. 16).

In the Killing-Cartan classification: SO_{2n+1} is almost-simple of type B_n (n >= 2), and SO_{2n} is almost-simple of type D_n (n >= 4) (p. 15).

# Prerequisites

- **Orthogonal group** — SO_n is the identity component of O_n

# Key Properties

1. SO_n = {A in O_n | det(A) = 1}
2. SO_n is connected
3. SO_n is almost-simple for n >= 3

# Relationships

## Extends
- **Orthogonal group** — SO_n is the identity component of O_n

## Related
- **Almost-simple algebraic group** — SO_n is almost-simple (types B_n and D_n)

# Source Reference

Chapter I, Section 1a (p. 15-16).

# Verification Notes

- Definition source: Direct from p. 16
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
