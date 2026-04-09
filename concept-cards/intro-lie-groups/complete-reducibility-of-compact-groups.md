---
# === CORE IDENTIFICATION ===
concept: Complete Reducibility for Compact Groups
slug: complete-reducibility-of-compact-groups

# === CLASSIFICATION ===
category: representations
subcategory: irreducibility
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of Lie Groups and Lie Algebras"
chapter_number: 4
pdf_page: 47
section: "4.6 Haar measure on compact Lie groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Weyl's theorem on complete reducibility"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - unitary-representation
  - haar-measure
extends:
  - unitary-representation
related:
  - completely-reducible-representation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why is every representation of a compact Lie group completely reducible?"
---

# Quick Definition

Every finite-dimensional representation of a compact Lie group is unitary (admits an invariant inner product) and therefore completely reducible as a direct sum of irreducibles.

# Core Definition

**Theorem 4.38** (Kirillov, p. 47): Any finite-dimensional representation of a compact Lie group is unitary and thus completely reducible.

**Proof**: Let $B(v,w)$ be any positive definite inner product. Average it: $\tilde{B}(v,w) = \int_G B(gv, gw)\, dg$. Then $\tilde{B}$ is positive definite and $G$-invariant. Complete reducibility follows from Theorem 4.29.

# Prerequisites

- **Unitary representation** — The key intermediate result: unitary implies completely reducible
- **Haar measure** — Needed for the averaging argument

# Key Properties

1. Applies to all compact Lie groups (including finite groups as a special case)
2. The proof is constructive: given any inner product, averaging produces an invariant one
3. This extends to representations of semisimple Lie algebras (by different methods)

# Examples

**Theorem 4.31** (p. 45): Every representation of a finite group is completely reducible (special case, using summing instead of integrating).

# Relationships

## Builds Upon
- **Unitary representation** — Complete reducibility via orthogonal complements
- **Haar measure** — The averaging tool

## Enables
- **Character theory** — Works most naturally for compact groups
- **Peter-Weyl theorem** — Builds on complete reducibility

# Source Reference

Chapter 4, Section 4.6, Theorem 4.38, p. 47.

# Verification Notes

- Definition source: Direct from Theorem 4.38, p. 47
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
