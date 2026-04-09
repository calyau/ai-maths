---
# === CORE IDENTIFICATION ===
concept: Fundamental Weights of Type B_n
slug: fundamental-weights-type-b

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
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - simple-roots-type-b
  - fundamental-weight
extends: []
related:
  - weight-lattice-type-b
contrasts_with:
  - fundamental-weights-type-d

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the fundamental weights of type B_n?"
---

# Quick Definition
The fundamental weights of $B_n$ are $\omega_k = e_1 + \cdots + e_k$ for $k = 1, \ldots, n-1$ and $\omega_n = \frac{1}{2}(e_1 + \cdots + e_n)$. The last fundamental weight $\omega_n$ is a half-integer weight, corresponding to the spin representation.

# Core Definition
(Kirillov, p. 125): Determined by the condition $\langle \omega_k, \alpha_i^\vee \rangle = \delta_{ki}$. From the weight lattice description:
- $\omega_k = e_1 + \cdots + e_k$ for $k = 1, \ldots, n-1$ (highest weight of $\Lambda^k \mathbb{C}^{2n+1}$)
- $\omega_n = \frac{1}{2}(e_1 + \cdots + e_n)$ (highest weight of the spin representation)

# Prerequisites
- **Simple roots type B** -- dual basis relationship
- **Fundamental weight** -- general concept

# Key Properties
1. $\omega_1, \ldots, \omega_{n-1}$ are integer weights (in $Q$)
2. $\omega_n$ is a half-integer weight (not in $Q$), generating the non-trivial coset of $P/Q \cong \mathbb{Z}_2$
3. The spin representation has highest weight $\omega_n = (\frac{1}{2}, \ldots, \frac{1}{2})$ and dimension $2^n$

# Relationships
## Contrasts With
- **Fundamental weights type D** -- $D_n$ has two half-integer fundamental weights (two spinors)

# Source Reference
Appendix C, Section C.2, p. 125.

# Verification Notes
- Definition source: Inferred from weight lattice and standard theory
- Confidence rationale: Medium -- fundamental weights not listed explicitly but follow from lattice
- Uncertainties: None
- Cross-reference status: Verified
