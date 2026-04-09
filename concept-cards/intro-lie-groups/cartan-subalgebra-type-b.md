---
# === CORE IDENTIFICATION ===
concept: Cartan Subalgebra of Type B_n
slug: cartan-subalgebra-type-b

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cartan-subalgebra
extends:
  - cartan-subalgebra
related:
  - root-system-type-b
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Cartan subalgebra of so(2n+1,C)?"
---

# Quick Definition
The Cartan subalgebra of $\mathfrak{so}(2n+1, \mathbb{C})$ (in the alternative description using bilinear form $B$) is $\mathfrak{h} = \{\mathrm{diag}(x_1, \ldots, x_n, -x_1, \ldots, -x_n, 0)\}$, with dimension $n$.

# Core Definition
(Kirillov, p. 124): In the alternative description, $\mathfrak{h} = \mathfrak{g} \cap \{\text{diagonal matrices}\} = \{\mathrm{diag}(x_1, \ldots, x_n, -x_1, \ldots, -x_n, 0)\}$. The functionals $e_i \in \mathfrak{h}^*$ are defined by $e_i: \mathrm{diag}(x_1, \ldots, x_n, -x_1, \ldots, -x_n, 0) \mapsto x_i$, forming a basis of $\mathfrak{h}^*$ with $(e_i, e_j) = \delta_{ij}$.

# Prerequisites
- **Cartan subalgebra** -- general concept

# Key Properties
1. $\dim \mathfrak{h} = n$ (rank of $B_n$)
2. Consists of block-diagonal matrices with $2 \times 2$ blocks $\begin{pmatrix} 0 & a_i \\ -a_i & 0 \end{pmatrix}$ and a final zero entry
3. In the alternative description: diagonal matrices of the given form

# Source Reference
Appendix C, Section C.2, p. 124.

# Verification Notes
- Definition source: Direct from p. 124
- Confidence rationale: Explicit
- Uncertainties: None
- Cross-reference status: Verified
