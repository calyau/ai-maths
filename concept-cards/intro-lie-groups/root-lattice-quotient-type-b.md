---
# === CORE IDENTIFICATION ===
concept: Root Lattice Quotient P/Q for Types B_n and C_n
slug: root-lattice-quotient-type-b

# === CLASSIFICATION ===
category: classification
subcategory: type-b
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Appendix C - Root Systems and Simple Lie Algebras"
chapter_number: null
pdf_page: 125
section: "C.2 B_n = so(2n+1,C)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - weight-lattice-type-b
  - weight-lattice-type-c
extends: []
related:
  - root-lattice-quotient-type-a
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is P/Q for types B_n and C_n?"
---

# Quick Definition
For both types $B_n$ and $C_n$, the quotient $P/Q \cong \mathbb{Z}_2$. For $B_n$, the non-trivial coset corresponds to spinor representations (half-integer weights); for $C_n$, it corresponds to representations with odd coordinate sum.

# Core Definition
(Kirillov, pp. 125, 127):
- $B_n$: $P/Q \cong \mathbb{Z}_2$, with $P = \{(\lambda_i) \mid \lambda_i \in \frac{1}{2}\mathbb{Z}, \lambda_i - \lambda_j \in \mathbb{Z}\}$ and $Q = \mathbb{Z}^n$
- $C_n$: $P/Q \cong \mathbb{Z}_2$, with $P = \mathbb{Z}^n$ and $Q = \{(\lambda_i) \mid \lambda_i \in \mathbb{Z}, \sum \lambda_i \in 2\mathbb{Z}\}$

# Prerequisites
- **Weight lattice type B** -- for $B_n$
- **Weight lattice type C** -- for $C_n$

# Key Properties
1. Both have $|P/Q| = 2$
2. For $B_n$: the non-trivial coset is the half-integer weights (spinor representations)
3. For $C_n$: the non-trivial coset has odd coordinate sum

# Source Reference
Appendix C, Sections C.2 and C.3, pp. 125, 127.

# Verification Notes
- Definition source: Direct from pp. 125, 127
- Confidence rationale: Explicit
- Uncertainties: None
- Cross-reference status: Verified
