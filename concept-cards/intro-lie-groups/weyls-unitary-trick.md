---
# === CORE IDENTIFICATION ===
concept: "Weyl's Unitary Trick"
slug: weyls-unitary-trick

# === CLASSIFICATION ===
category: structure-theory
subcategory: complete-reducibility
tier: advanced

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Structure Theory of Lie Algebras"
chapter_number: 6
pdf_page: 78
section: "6.9. Complete reducibility of representations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - compact-real-form
  - semisimple-lie-algebra
extends: []
related:
  - complete-reducibility
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is Weyl's unitary trick?"
---

# Quick Definition

Weyl's unitary trick reduces complete reducibility of complex semisimple Lie algebra representations to the known complete reducibility of compact group representations, by passing through the compact real form.

# Core Definition

(Kirillov, p. 78): If $\mathfrak{g}$ is a semisimple complex Lie algebra, write $\mathfrak{g} = \mathfrak{k} \otimes \mathbb{C}$ where $\mathfrak{k} = \operatorname{Lie}(K)$ for compact $K$ (Theorem 6.52). Then complex representations of $\mathfrak{g}$, $\mathfrak{k}$, and $K$ are equivalent. Since every representation of compact $K$ is completely reducible (Theorem 4.38), the same holds for $\mathfrak{g}$.

# Prerequisites

- **Compact real form** — Provides the compact group $K$
- **Semisimple Lie algebra** — The setting

# Key Properties

1. Uses the bijection between complex representations of $\mathfrak{g}$ and those of $K$
2. Compact groups have complete reducibility by averaging (Theorem 4.38)
3. This was historically the first proof of complete reducibility

# Context & Application

The unitary trick is an elegant argument that uses analysis (compactness, integration) to prove an algebraic result. The algebraic proof via the Casimir element (Section 6.9) avoids topology but is more technical.

# Relationships

## Builds Upon
- **Compact real form** — Provides the bridge

## Enables
- **Complete reducibility** — Alternative proof

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.9, page 78.

# Verification Notes

- Definition source: Synthesized from discussion on p. 78
- Confidence rationale: Clearly described method; not formally numbered
- Uncertainties: None
- Cross-reference status: Verified
