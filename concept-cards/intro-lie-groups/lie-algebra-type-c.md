---
# === CORE IDENTIFICATION ===
concept: Lie Algebra sp(n,C) (Type C_n)
slug: lie-algebra-type-c

# === CLASSIFICATION ===
category: classification
subcategory: type-c
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Appendix C - Root Systems and Simple Lie Algebras"
chapter_number: null
pdf_page: 126
section: "C.3 C_n = sp(n,C)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "sp(n)"
  - "symplectic Lie algebra"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - root-system-type-c
  - cartan-subalgebra-type-c
contrasts_with:
  - lie-algebra-type-b

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Lie algebra of type C_n?"
  - "What is sp(n,C)?"
---

# Quick Definition
The Lie algebra of type $C_n$ is $\mathfrak{sp}(n, \mathbb{C})$, the Lie algebra preserving a skew-symmetric (symplectic) bilinear form on $\mathbb{C}^{2n}$. It has rank $n$ and dimension $n(2n+1)$.

# Core Definition
(Kirillov, p. 126): $\mathfrak{g} = \mathfrak{sp}(n, \mathbb{C}) = \{a \in \mathfrak{gl}(2n, \mathbb{C}) \mid a + Ja^tJ^{-1} = 0\}$ where $J = \begin{pmatrix} 0 & I_n \\ -I_n & 0 \end{pmatrix}$.

# Prerequisites
This is a foundational concept.

# Key Properties
1. $\dim \mathfrak{g} = n(2n+1)$ (same dimension as $B_n$)
2. $\mathrm{rank} = n$
3. Preserves a symplectic (skew-symmetric) form
4. Not simply laced: has long roots $\pm 2e_i$ and short roots $\pm e_i \pm e_j$
5. Dual to $B_n$: $C_n^\vee = B_n$

# Examples
**Example** (p. 126): $C_1 = \mathfrak{sp}(1, \mathbb{C}) \cong \mathfrak{sl}(2, \mathbb{C})$. $C_2 \cong B_2$ (the only coincidence).

# Relationships
## Contrasts With
- **Lie algebra type B** -- $B_n$ preserves a symmetric form; $C_n$ preserves a skew-symmetric form

# Source Reference
Appendix C, Section C.3, p. 126.

# Verification Notes
- Definition source: Direct from p. 126
- Confidence rationale: Explicit
- Uncertainties: None
- Cross-reference status: Verified
