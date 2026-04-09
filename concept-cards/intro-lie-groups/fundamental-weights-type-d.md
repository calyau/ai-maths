---
# === CORE IDENTIFICATION ===
concept: Fundamental Weights of Type D_n
slug: fundamental-weights-type-d

# === CLASSIFICATION ===
category: classification
subcategory: type-d
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Appendix C - Root Systems and Simple Lie Algebras"
chapter_number: null
pdf_page: 128
section: "C.4 D_n = so(2n,C)"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - simple-roots-type-d
  - fundamental-weight
extends: []
related:
  - weight-lattice-type-d
contrasts_with:
  - fundamental-weights-type-b

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the fundamental weights of type D_n?"
---

# Quick Definition
The fundamental weights of $D_n$ are: $\omega_k = e_1 + \cdots + e_k$ for $k = 1, \ldots, n-2$, $\omega_{n-1} = \frac{1}{2}(e_1 + \cdots + e_{n-1} - e_n)$, and $\omega_n = \frac{1}{2}(e_1 + \cdots + e_{n-1} + e_n)$. The last two are half-integer weights corresponding to the two half-spin representations.

# Core Definition
(Kirillov, p. 128): From the weight lattice and the duality condition $\langle \omega_k, \alpha_i^\vee \rangle = \delta_{ki}$:
- $\omega_k = e_1 + \cdots + e_k$ for $k = 1, \ldots, n-2$
- $\omega_{n-1} = \frac{1}{2}(e_1 + \cdots + e_{n-1} - e_n)$
- $\omega_n = \frac{1}{2}(e_1 + \cdots + e_{n-1} + e_n)$

# Prerequisites
- **Simple roots type D** -- dual basis relationship
- **Fundamental weight** -- general concept

# Key Properties
1. $\omega_1, \ldots, \omega_{n-2}$ are integer weights
2. $\omega_{n-1}$ and $\omega_n$ are half-integer weights (half-spin representations)
3. The two half-spin representations have dimensions $2^{n-1}$ each
4. The fork in the Dynkin diagram produces two half-spin fundamental weights (vs. one for $B_n$)
5. $\omega_{n-1}$ and $\omega_n$ are swapped by the outer automorphism of $D_n$

# Context & Application
The existence of two half-spin representations (rather than one as in type $B_n$) reflects the non-connectivity of $\mathrm{SO}(2n)$'s spin cover. For $D_4$, the triality automorphism permutes $\omega_1$, $\omega_3$, and $\omega_4$.

# Relationships
## Contrasts With
- **Fundamental weights type B** -- $B_n$ has only one half-integer fundamental weight (one spinor)

# Source Reference
Appendix C, Section C.4, p. 128.

# Verification Notes
- Definition source: Inferred from weight lattice and standard theory
- Confidence rationale: Medium -- follows from lattice description
- Uncertainties: None
- Cross-reference status: Verified
