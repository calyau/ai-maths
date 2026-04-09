---
# === CORE IDENTIFICATION ===
concept: Nilpotent Operator Theorem
slug: nilpotent-operator-theorem

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
  - nilpotent-lie-algebra
extends: []
related:
  - engel-theorem
  - lie-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When can a Lie algebra of nilpotent operators be simultaneously strictly upper-triangularized?"
---

# Quick Definition

If a Lie subalgebra $\mathfrak{g} \subset \mathfrak{gl}(V)$ consists entirely of nilpotent operators, then there exists a basis of $V$ in which all elements of $\mathfrak{g}$ are strictly upper-triangular. This is the representation-theoretic foundation for Engel's theorem.

# Core Definition

**Theorem 6.17** (Kirillov, p. 70): Let $V$ be a finite-dimensional vector space (real or complex) and let $\mathfrak{g} \subset \mathfrak{gl}(V)$ be a Lie subalgebra which consists of nilpotent operators. Then there exists a basis in $V$ such that all operators $x \in \mathfrak{g}$ are strictly upper-triangular.

# Prerequisites

- **Nilpotent Lie algebra** — This theorem is the key tool for proving Engel's theorem

# Key Properties

1. Works over both $\mathbb{R}$ and $\mathbb{C}$ (unlike Lie's theorem)
2. The conclusion is strictly upper-triangular (not just upper-triangular as in Lie's theorem)
3. The hypothesis is that elements are nilpotent as operators on $V$, not just that $\operatorname{ad} x$ is nilpotent

# Context & Application

This theorem is the analog of Lie's theorem (Theorem 6.14) for nilpotent algebras. The key difference is that it applies to concrete matrix algebras consisting of nilpotent operators, while Engel's theorem translates this to an abstract criterion using the adjoint representation.

# Examples

**Example**: The strictly upper-triangular matrices $\mathfrak{n} \subset \mathfrak{gl}(n, \mathbb{K})$ are already in the standard form predicted by the theorem.

# Relationships

## Enables
- **Engel theorem** — Derived by applying this theorem to $\operatorname{ad} \mathfrak{g} \subset \mathfrak{gl}(\mathfrak{g})$

## Related
- **Lie theorem** — Analogous result for solvable algebras, but gives only upper-triangular form

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.3, page 70. Theorem 6.17.

# Verification Notes

- Definition source: Direct from Theorem 6.17
- Confidence rationale: Explicit theorem statement; proof referenced to other texts
- Uncertainties: Proof not given in source
- Cross-reference status: Verified
