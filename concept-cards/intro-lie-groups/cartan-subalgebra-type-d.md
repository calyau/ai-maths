---
# === CORE IDENTIFICATION ===
concept: Cartan Subalgebra of Type D_n
slug: cartan-subalgebra-type-d

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cartan-subalgebra
extends:
  - cartan-subalgebra
related:
  - root-system-type-d
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Cartan subalgebra of so(2n,C)?"
---

# Quick Definition
The Cartan subalgebra of $\mathfrak{so}(2n, \mathbb{C})$ (in the alternative description) is $\mathfrak{h} = \{\mathrm{diag}(x_1, \ldots, x_n, -x_1, \ldots, -x_n)\}$, with dimension $n$.

# Core Definition
(Kirillov, p. 127-128): $\mathfrak{h} = \mathfrak{g} \cap \{\text{diagonal matrices}\} = \{\mathrm{diag}(x_1, \ldots, x_n, -x_1, \ldots, -x_n)\}$. The functionals $e_i$ extract $x_i$ and form a basis with $(e_i, e_j) = \delta_{ij}$.

# Prerequisites
- **Cartan subalgebra** -- general concept

# Key Properties
1. $\dim \mathfrak{h} = n$
2. Same form as $B_n$ Cartan subalgebra but without the extra zero entry (since $\mathfrak{so}(2n)$ acts on $\mathbb{C}^{2n}$, not $\mathbb{C}^{2n+1}$)

# Source Reference
Appendix C, Section C.4, pp. 127-128.

# Verification Notes
- Definition source: Direct from pp. 127-128
- Confidence rationale: Explicit
- Uncertainties: None
- Cross-reference status: Verified
