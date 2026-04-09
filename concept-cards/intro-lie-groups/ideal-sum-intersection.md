---
# === CORE IDENTIFICATION ===
concept: Ideal Operations
slug: ideal-sum-intersection

# === CLASSIFICATION ===
category: structure-theory
subcategory: solvable-nilpotent
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Structure Theory of Lie Algebras"
chapter_number: 6
pdf_page: 66
section: "6.1. Ideals and commutant"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-algebra-ideal
extends:
  - lie-algebra-ideal
related:
  - commutant
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What operations on ideals produce ideals?"
---

# Quick Definition

If $I_1, I_2$ are ideals in $\mathfrak{g}$, then $I_1 \cap I_2$, $I_1 + I_2$, and $[I_1, I_2]$ are all ideals. In Lie algebras, every ideal is both left and right (by skew-symmetry of the bracket).

# Core Definition

**Lemma 6.2** (Kirillov, p. 66): Let $I_1, I_2$ be ideals in $\mathfrak{g}$. Then $I_1 \cap I_2$, $I_1 + I_2 = \{x + y \mid x \in I_1, y \in I_2\}$, and $[I_1, I_2] = \operatorname{span}\{[x,y] \mid x \in I_1, y \in I_2\}$ are ideals in $\mathfrak{g}$.

Also: every ideal is two-sided (no distinction between left and right ideals) due to skew-symmetry of the bracket.

# Prerequisites

- **Lie algebra ideal** — The operations are on ideals

# Key Properties

1. No distinction between left and right ideals (skew-symmetry)
2. $[I_1, I_2] \subset I_1 \cap I_2$ when both are ideals
3. The isomorphism theorem holds: $\mathfrak{g}/\operatorname{Ker} f \cong \operatorname{Im} f$ (Lemma 6.1)

# Relationships

## Builds Upon
- **Lie algebra ideal** — Operations on ideals

## Enables
- **Commutant** — $[\mathfrak{g}, \mathfrak{g}]$ is a special case
- **Radical** — Sum of solvable ideals is solvable

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.1, page 66. Lemma 6.1, Lemma 6.2.

# Verification Notes

- Definition source: Direct from Lemma 6.2
- Confidence rationale: Explicit lemma
- Uncertainties: None
- Cross-reference status: Verified
