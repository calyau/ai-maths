---
# === CORE IDENTIFICATION ===
concept: Lie Algebra so(2n+1,C) (Type B_n)
slug: lie-algebra-type-b

# === CLASSIFICATION ===
category: classification
subcategory: type-b
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Appendix C - Root Systems and Simple Lie Algebras"
chapter_number: null
pdf_page: 124
section: "C.2 B_n = so(2n+1,C)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "so(2n+1)"
  - "odd orthogonal Lie algebra"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - root-system-type-b
  - cartan-subalgebra-type-b
contrasts_with:
  - lie-algebra-type-d

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Lie algebra of type B_n?"
  - "What is so(2n+1,C)?"
---

# Quick Definition
The Lie algebra of type $B_n$ is $\mathfrak{so}(2n+1, \mathbb{C})$, the Lie algebra of skew-symmetric matrices with respect to a symmetric bilinear form on $\mathbb{C}^{2n+1}$. It has rank $n$ and dimension $n(2n+1)$.

# Core Definition
(Kirillov, p. 124): $\mathfrak{g} = \mathfrak{so}(2n+1, \mathbb{C})$. In the alternative description: $\mathfrak{g} = \mathfrak{so}(B) = \{a \in \mathfrak{gl}(2n+1, \mathbb{C}) \mid a + Ba^tB^{-1} = 0\}$ where $B = \begin{pmatrix} 0 & I_n & 0 \\ I_n & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}$.

# Prerequisites
This is a foundational concept.

# Key Properties
1. $\dim \mathfrak{g} = n(2n+1)$, $\mathrm{rank} = n$
2. Corresponds to the odd orthogonal group $\mathrm{SO}(2n+1)$
3. Not simply laced: has roots of two different lengths
4. $B_1 \cong A_1$, $B_2 \cong C_2$

# Examples
**Example** (p. 124): For $B_1 = \mathfrak{so}(3, \mathbb{C}) \cong \mathfrak{sl}(2, \mathbb{C})$.

# Relationships
## Contrasts With
- **Lie algebra type D** -- $\mathfrak{so}(2n, \mathbb{C})$ for even dimension

# Source Reference
Appendix C, Section C.2, p. 124.

# Verification Notes
- Definition source: Direct from p. 124
- Confidence rationale: Explicit
- Uncertainties: None
- Cross-reference status: Verified
