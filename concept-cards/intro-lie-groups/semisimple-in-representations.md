---
# === CORE IDENTIFICATION ===
concept: Semisimple Elements Act Semisimply in Representations
slug: semisimple-in-representations

# === CLASSIFICATION ===
category: root-systems
subcategory: abstract-root-systems
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Complex Semisimple Lie Algebras"
chapter_number: 7
pdf_page: 83
section: "7.1. Semisimple elements and toroidal subalgebras"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - semisimple-element
  - complete-reducibility
extends:
  - semisimple-element
related:
  - weight-decomposition-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Does a semisimple element act diagonalizably in every representation?"
---

# Quick Definition

If $x \in \mathfrak{g}$ is semisimple (in a semisimple Lie algebra) and $V$ is any finite-dimensional representation, then $\rho(x) \in \mathfrak{gl}(V)$ is a semisimple (diagonalizable) operator.

# Core Definition

**Theorem 7.5** (Kirillov, p. 83): Let $\mathfrak{g}$ be a semisimple Lie algebra and $x \in \mathfrak{g}$ semisimple. Let $V$ be a finite-dimensional complex representation. Then $\rho(x) \in \mathfrak{gl}(V)$ is semisimple.

# Prerequisites

- **Semisimple element** — The element must be semisimple in $\mathfrak{g}$
- **Complete reducibility** — The proof uses complete reducibility to reduce to irreducible case

# Key Properties

1. The proof reduces to irreducible $V$ by complete reducibility
2. For irreducible $V$: $V = \bigoplus V[\lambda]$ where $V[\lambda] = \{v \mid \rho(x).v = \lambda v\}$, using eigenspace decomposition of $\mathfrak{g}$ under $x$
3. This justifies using weight decompositions in arbitrary representations

# Context & Application

This theorem ensures that the weight decomposition, first seen for $\mathfrak{sl}(2)$ representations, extends to any semisimple algebra: a toroidal subalgebra acts diagonalizably in every representation, producing weight space decompositions.

# Relationships

## Builds Upon
- **Semisimple element** — The hypothesis
- **Complete reducibility** — Used in the proof

## Enables
- **Weight decomposition theorem** — Weight spaces in arbitrary representations

# Source Reference

Chapter 7: Complex Semisimple Lie Algebras, Section 7.1, page 83. Theorem 7.5.

# Verification Notes

- Definition source: Direct from Theorem 7.5
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
