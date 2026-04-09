---
# === CORE IDENTIFICATION ===
concept: Standard Notation for Root System Data
slug: appendix-c-notation

# === CLASSIFICATION ===
category: lie-algebras
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Appendix C - Root Systems and Simple Lie Algebras"
chapter_number: null
pdf_page: 122
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - root-system
  - weyl-group
  - weight-lattice
extends: []
related:
  - highest-root
  - coxeter-number
  - rho-half-sum
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What notation is used when describing root system data?"
---

# Quick Definition
Appendix C establishes a uniform notation for describing root system data: $\mathfrak{g}$ (simple Lie algebra), $\mathfrak{h}$ (Cartan subalgebra), $R$ (root system), $E$ (real span of roots), $(,)$ (bilinear form normalized so long roots have $(\alpha, \alpha) = 2$), $R_+$ (positive roots), $\Pi$ (simple roots), $W$ (Weyl group), $P$ (weight lattice), $Q$ (root lattice), $\theta$ (highest root), $\rho$ (half-sum of positive roots), and $h$, $h^\vee$ (Coxeter and dual Coxeter numbers).

# Core Definition
(Kirillov, p. 122): The standard notation for Appendix C:
- $\mathfrak{g}$: complex simple Lie algebra with fixed Cartan subalgebra $\mathfrak{h} \subset \mathfrak{g}$
- $R \subset \mathfrak{h}^*$: root system
- $E = \mathfrak{h}_\mathbb{R}^*$: real vector space spanned by roots
- $(,)$: symmetric invariant bilinear form on $\mathfrak{h}^*$ normalized so $(\alpha, \alpha) = 2$ for long roots
- $R_+$: positive roots
- $\Pi = \{\alpha_1, \ldots, \alpha_r\}$, $r = \mathrm{rank}(R)$: simple roots
- $W$: Weyl group
- $P, Q \subset E$: weight and root lattices
- $\theta$: highest root
- $\rho = \frac{1}{2}\sum_{R_+} \alpha$
- $h = \mathrm{ht}(\theta) + 1$, $h^\vee = \mathrm{ht}(\theta^\vee) + 1$

# Prerequisites
- **Root system** -- the object being described
- **Weyl group** -- part of the data
- **Weight lattice** -- part of the data

# Key Properties
1. The bilinear form is normalized so long roots have $(\alpha, \alpha) = 2$
2. This normalization is standard in the literature
3. The data for each classical type ($A_n, B_n, C_n, D_n$) is given in subsequent sections

# Source Reference
Appendix C, introductory notation, p. 122.

# Verification Notes
- Definition source: Direct from p. 122
- Confidence rationale: Explicit notation list
- Uncertainties: None
- Cross-reference status: Verified
