---
# === CORE IDENTIFICATION ===
concept: Semisimple Quotient Theorem
slug: semisimple-quotient-theorem

# === CLASSIFICATION ===
category: structure-theory
subcategory: semisimple
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Structure Theory of Lie Algebras"
chapter_number: 6
pdf_page: 72
section: "6.4. The radical. Semisimple and reductive algebras"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - radical
  - semisimple-lie-algebra
extends:
  - radical
related:
  - levi-decomposition
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Is the quotient of a Lie algebra by its radical semisimple?"
---

# Quick Definition

For any Lie algebra $\mathfrak{g}$, the quotient $\mathfrak{g}/\operatorname{rad}(\mathfrak{g})$ is semisimple. Conversely, if $\mathfrak{b}$ is a solvable ideal with $\mathfrak{g}/\mathfrak{b}$ semisimple, then $\mathfrak{b} = \operatorname{rad}(\mathfrak{g})$.

# Core Definition

**Theorem 6.24** (Kirillov, p. 72): For any Lie algebra $\mathfrak{g}$, $\mathfrak{g}/\operatorname{rad}(\mathfrak{g})$ is semisimple. Conversely, if $\mathfrak{b}$ is a solvable ideal such that $\mathfrak{g}/\mathfrak{b}$ is semisimple, then $\mathfrak{b} = \operatorname{rad}(\mathfrak{g})$.

# Prerequisites

- **Radical** — The ideal being quotiented
- **Semisimple Lie algebra** — The quotient's property

# Key Properties

1. Any Lie algebra fits in an exact sequence $0 \to \operatorname{rad}(\mathfrak{g}) \to \mathfrak{g} \to \mathfrak{g}_{ss} \to 0$
2. The Levi decomposition shows this sequence splits
3. The radical is the unique maximal solvable ideal giving a semisimple quotient

# Relationships

## Builds Upon
- **Radical** — Characterizes the radical uniquely

## Enables
- **Levi decomposition** — Strengthens the exact sequence to a splitting

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.4, page 72. Theorem 6.24.

# Verification Notes

- Definition source: Direct from Theorem 6.24
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
