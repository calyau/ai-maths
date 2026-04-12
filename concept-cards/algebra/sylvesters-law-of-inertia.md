---
# === CORE IDENTIFICATION ===
concept: "Sylvester's Law of Inertia"
slug: sylvesters-law-of-inertia

# === CLASSIFICATION ===
category: bilinear-forms
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Bilinear Forms"
chapter_number: 8
pdf_page: 240
section: "8.4 Orthogonality"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS ===
aliases:
  - "Sylvester's law"
  - "law of inertia"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - signature
  - orthogonal-basis
extends: []
related:
  - positive-definite-form
  - indefinite-form
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why is the signature of a form well-defined?"
---

# Quick Definition

Sylvester's Law of Inertia states that the signature (p, m) of a symmetric form is independent of the choice of orthogonal basis used to compute it. Two symmetric forms are equivalent (related by a change of basis) if and only if they have the same signature.

# Core Definition

Sylvester's Law asserts that the signature of a nondegenerate symmetric form does not depend on the choice of the orthogonal basis (Artin, p. 254, Exercise 4.21). The proof uses the fact that if subspaces W_1 (positive definite) and W_2 (negative semidefinite) satisfy positivity and negativity conditions respectively, then they must be independent.

# Prerequisites

- **Signature** — The invariant whose well-definedness this law establishes
- **Orthogonal basis** — The signature is computed via an orthogonal basis

# Key Properties

1. The number of positive, negative, and zero entries in a diagonalized form is invariant
2. Two nondegenerate symmetric forms on the same space are equivalent iff they have the same signature
3. Extends to degenerate forms by including the count z of zero diagonal entries

# Construction / Recognition

## To Apply:
1. Diagonalize the form in two different ways
2. Sylvester's Law guarantees the same counts (p, m, z)

# Context & Application

This law provides the fundamental classification theorem for symmetric bilinear forms over the reals. Combined with the existence of orthogonal bases, it reduces the classification problem to a discrete invariant (the signature).

# Examples

**Example 1** (p. 254): Any two orthogonal bases of a positive definite form give the same number of positive diagonal entries (all of them).

# Relationships

## Builds Upon
- **Signature** — The invariant classified by this law
- **Orthogonal basis** — The signature is computed from diagonal forms

## Related
- **Positive definite form** — Characterized by signature (n, 0)
- **Indefinite form** — Characterized by mixed signature

# Common Errors

- **Error**: Claiming two forms with the same determinant are equivalent
  **Correction**: The determinant alone does not determine the signature; diag(1, -1) and diag(-1, 1) have the same determinant but the same signature (1,1)

# Common Confusions

- **Confusion**: Thinking Sylvester's Law applies over any field
  **Clarification**: The law is specific to symmetric forms over the reals (or Hermitian forms over C). Over other fields, the classification is more subtle.

# Source Reference

Chapter 8: Bilinear Forms, Section 8.4, page 254. Exercise 4.21.

# Verification Notes

- Definition source: Referenced at p. 254, proof left as exercise
- Confidence rationale: Medium — statement is clear but proof is delegated to an exercise
- Uncertainties: None in the statement
- Cross-reference status: Verified
