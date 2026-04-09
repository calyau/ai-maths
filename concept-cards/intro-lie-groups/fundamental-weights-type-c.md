---
# === CORE IDENTIFICATION ===
concept: Fundamental Weights of Type C_n
slug: fundamental-weights-type-c

# === CLASSIFICATION ===
category: classification
subcategory: type-c
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Appendix C - Root Systems and Simple Lie Algebras"
chapter_number: null
pdf_page: 127
section: "C.3 C_n = sp(n,C)"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - simple-roots-type-c
  - fundamental-weight
extends: []
related:
  - weight-lattice-type-c
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the fundamental weights of type C_n?"
---

# Quick Definition
The fundamental weights of $C_n$ are $\omega_k = e_1 + \cdots + e_k$ for $k = 1, \ldots, n$. All fundamental weights are integer weights, reflecting that $P = \mathbb{Z}^n$.

# Core Definition
(Kirillov, p. 127): From the weight lattice $P = \mathbb{Z}^n$ and the condition $\langle \omega_k, \alpha_i^\vee \rangle = \delta_{ki}$:
- $\omega_k = e_1 + \cdots + e_k$ for $k = 1, \ldots, n$

# Prerequisites
- **Simple roots type C** -- dual basis relationship
- **Fundamental weight** -- general concept

# Key Properties
1. All fundamental weights are integer vectors (since $P = \mathbb{Z}^n$)
2. $\omega_1 = e_1$ is the highest weight of the standard representation ($\mathbb{C}^{2n}$)
3. $\omega_n = e_1 + \cdots + e_n$ is the highest weight of $\mathfrak{sp}(n)$'s analogue of the determinant representation

# Source Reference
Appendix C, Section C.3, p. 127.

# Verification Notes
- Definition source: Inferred from weight lattice
- Confidence rationale: Medium -- consistent with lattice description
- Uncertainties: None
- Cross-reference status: Verified
