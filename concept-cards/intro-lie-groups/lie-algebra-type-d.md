---
# === CORE IDENTIFICATION ===
concept: Lie Algebra so(2n,C) (Type D_n)
slug: lie-algebra-type-d

# === CLASSIFICATION ===
category: classification
subcategory: type-d
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Appendix C - Root Systems and Simple Lie Algebras"
chapter_number: null
pdf_page: 127
section: "C.4 D_n = so(2n,C)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "so(2n)"
  - "even orthogonal Lie algebra"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - root-system-type-d
  - cartan-subalgebra-type-d
contrasts_with:
  - lie-algebra-type-b

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Lie algebra of type D_n?"
  - "What is so(2n,C)?"
---

# Quick Definition
The Lie algebra of type $D_n$ is $\mathfrak{so}(2n, \mathbb{C})$, the Lie algebra of skew-symmetric matrices with respect to a symmetric bilinear form on $\mathbb{C}^{2n}$. It has rank $n$ and dimension $n(2n-1)$.

# Core Definition
(Kirillov, p. 127): $\mathfrak{g} = \mathfrak{so}(2n, \mathbb{C}) = \mathfrak{so}(B) = \{a \in \mathfrak{gl}(2n, \mathbb{C}) \mid a + Ba^tB^{-1} = 0\}$ where $B = \begin{pmatrix} 0 & I_n \\ I_n & 0 \end{pmatrix}$.

# Prerequisites
This is a foundational concept.

# Key Properties
1. $\dim \mathfrak{g} = n(2n-1)$, $\mathrm{rank} = n$
2. Simply laced (unlike $B_n$ and $C_n$)
3. Requires $n \geq 3$ for distinctness: $D_2 \cong A_1 \times A_1$, $D_3 \cong A_3$
4. Has a Dynkin diagram with a fork (unique among classical types)
5. For $n = 4$: triality symmetry ($S_3$ outer automorphism group)

# Examples
**Example** (p. 127): $D_3 = \mathfrak{so}(6, \mathbb{C}) \cong \mathfrak{sl}(4, \mathbb{C}) = A_3$.

# Relationships
## Contrasts With
- **Lie algebra type B** -- $B_n = \mathfrak{so}(2n+1, \mathbb{C})$ has odd dimension; $D_n$ has even dimension and is simply laced

# Source Reference
Appendix C, Section C.4, p. 127.

# Verification Notes
- Definition source: Direct from p. 127
- Confidence rationale: Explicit
- Uncertainties: None
- Cross-reference status: Verified
