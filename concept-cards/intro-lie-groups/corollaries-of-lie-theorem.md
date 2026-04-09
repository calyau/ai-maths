---
# === CORE IDENTIFICATION ===
concept: Corollaries of Lie Theorem
slug: corollaries-of-lie-theorem

# === CLASSIFICATION ===
category: structure-theory
subcategory: solvable-nilpotent
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Structure Theory of Lie Algebras"
chapter_number: 6
pdf_page: 70
section: "6.3. Lie and Engel theorems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-theorem
  - solvable-lie-algebra
extends:
  - lie-theorem
related:
  - nilpotent-lie-algebra
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the main consequences of Lie's theorem?"
  - "When is a Lie algebra solvable iff its commutant is nilpotent?"
---

# Quick Definition

Corollary 6.16 gives three key consequences of Lie's theorem: (1) irreducible representations of solvable algebras are 1-dimensional, (2) solvable complex algebras admit chains of codimension-1 ideals, and (3) a Lie algebra is solvable iff $[\mathfrak{g}, \mathfrak{g}]$ is nilpotent.

# Core Definition

**Corollary 6.16** (Kirillov, p. 70):
1. Any irreducible representation of a solvable Lie algebra is 1-dimensional.
2. If a complex Lie algebra $\mathfrak{g}$ is solvable, there exists $0 \subset I^1 \subset \cdots \subset I^n = \mathfrak{g}$ with each $I^k$ an ideal and $I^{k+1}/I^k$ one-dimensional.
3. $\mathfrak{g}$ is solvable if and only if $[\mathfrak{g}, \mathfrak{g}]$ is nilpotent.

# Prerequisites

- **Lie theorem** — These are direct consequences
- **Solvable Lie algebra** — The hypothesis

# Key Properties

1. Part (1) follows from Proposition 6.15 (common eigenvector)
2. Part (2) applies Lie's theorem to the adjoint representation
3. Part (3): if solvable, apply Lie's theorem to adjoint rep; then $\operatorname{ad}[\mathfrak{g},\mathfrak{g}]$ is strictly upper-triangular, hence nilpotent

# Context & Application

Part (3) is particularly useful: it provides a practical criterion for solvability by checking only the derived subalgebra $[\mathfrak{g}, \mathfrak{g}]$ for nilpotency.

# Relationships

## Builds Upon
- **Lie theorem** — Source of all three corollaries

## Related
- **Nilpotent Lie algebra** — Part (3) connects solvability to nilpotency of $[\mathfrak{g}, \mathfrak{g}]$

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.3, page 70. Corollary 6.16.

# Verification Notes

- Definition source: Direct from Corollary 6.16
- Confidence rationale: Explicit corollary with proofs
- Uncertainties: None
- Cross-reference status: Verified
