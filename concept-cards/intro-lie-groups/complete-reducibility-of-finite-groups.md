---
# === CORE IDENTIFICATION ===
concept: Complete Reducibility for Finite Groups
slug: complete-reducibility-of-finite-groups

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
pdf_page: 44
section: "4.5 Complete reducibility of unitary representations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Maschke's theorem"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - unitary-representation
extends: []
related:
  - complete-reducibility-of-compact-groups
  - completely-reducible-representation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why is every representation of a finite group completely reducible?"
---

# Quick Definition

Every representation of a finite group is unitary (admits an invariant inner product) and therefore completely reducible. The invariant inner product is constructed by averaging any inner product over the group.

# Core Definition

**Theorem 4.30** (Kirillov, p. 44): Any representation of a finite group is unitary.

**Proof**: Let $B(v,w)$ be any positive definite inner product. Average: $\tilde{B}(v,w) = \frac{1}{|G|}\sum_{g \in G} B(gv, gw)$. Then $\tilde{B}$ is positive definite and $G$-invariant.

**Theorem 4.31** (p. 45): Every representation of a finite group is completely reducible.

# Prerequisites

- **Unitary representation** — Every finite group representation is unitary

# Key Properties

1. The averaging trick works because $|G| < \infty$ (no convergence issues)
2. This is the prototype for the compact group result (Theorem 4.38)
3. The theorem is constructive but does not give an explicit decomposition

# Relationships

## Related
- **Complete reducibility for compact groups** — Generalization using Haar measure

# Source Reference

Chapter 4, Section 4.5, Theorems 4.30-4.31, pp. 44-45.

# Verification Notes

- Definition source: Direct from Theorems 4.30-4.31
- Confidence rationale: Explicit theorems with proofs
- Uncertainties: None
- Cross-reference status: Verified
