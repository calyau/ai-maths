---
# === CORE IDENTIFICATION ===
concept: Cartan Subalgebra of Type C_n
slug: cartan-subalgebra-type-c

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cartan-subalgebra
extends:
  - cartan-subalgebra
related:
  - root-system-type-c
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Cartan subalgebra of sp(n,C)?"
---

# Quick Definition
The Cartan subalgebra of $\mathfrak{sp}(n, \mathbb{C})$ is $\mathfrak{h} = \{\mathrm{diag}(x_1, \ldots, x_n, -x_1, \ldots, -x_n)\}$, with dimension $n$.

# Core Definition
(Kirillov, p. 126): $\mathfrak{h} = \mathfrak{g} \cap \{\text{diagonal matrices}\} = \{\mathrm{diag}(x_1, \ldots, x_n, -x_1, \ldots, -x_n)\}$. The functionals $e_i$ extract $x_i$ and form a basis with $(e_i, e_j) = \frac{1}{2}\delta_{ij}$.

# Prerequisites
- **Cartan subalgebra** -- general concept

# Key Properties
1. $\dim \mathfrak{h} = n$
2. The bilinear form has $(e_i, e_j) = \frac{1}{2}\delta_{ij}$ (different normalization from $B_n$)

# Source Reference
Appendix C, Section C.3, p. 126.

# Verification Notes
- Definition source: Direct from p. 126
- Confidence rationale: Explicit
- Uncertainties: None
- Cross-reference status: Verified
