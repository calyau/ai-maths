---
# === CORE IDENTIFICATION ===
concept: Cartan Subalgebra of Type A_n
slug: cartan-subalgebra-type-a

# === CLASSIFICATION ===
category: classification
subcategory: type-a
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Appendix C - Root Systems and Simple Lie Algebras"
chapter_number: null
pdf_page: 123
section: "C.1 A_n = sl(n+1,C)"

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
  - root-system-type-a
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Cartan subalgebra of sl(n+1,C)?"
---

# Quick Definition
The Cartan subalgebra of $\mathfrak{sl}(n+1, \mathbb{C})$ is the space of traceless diagonal matrices: $\mathfrak{h} = \{\mathrm{diag}(h_1, \ldots, h_{n+1}) \mid \sum h_i = 0\}$. It has dimension $n$ (the rank of $A_n$).

# Core Definition
(Kirillov, p. 123): $\mathfrak{h} = \{\text{diagonal matrices with trace } 0\}$. The functionals $e_i \in \mathfrak{h}^*$ are defined by $e_i: \mathrm{diag}(h_1, \ldots, h_{n+1}) \mapsto h_i$. Then $\mathfrak{h}^* = \bigoplus \mathbb{C}e_i / \mathbb{C}(e_1 + \cdots + e_{n+1})$.

# Prerequisites
- **Cartan subalgebra** -- general concept

# Key Properties
1. $\dim \mathfrak{h} = n$ (rank of $A_n$)
2. $\mathfrak{h}^* = \bigoplus \mathbb{R}e_i / \mathbb{R}(e_1 + \cdots + e_{n+1})$
3. Inner product on $\mathfrak{h}^*$: $(\lambda, \mu) = \sum \lambda_i \mu_i$ when representatives satisfy $\sum \lambda_i = \sum \mu_i = 0$

# Examples
**Example** (p. 123): For $A_1 = \mathfrak{sl}(2, \mathbb{C})$: $\mathfrak{h} = \mathbb{C} \cdot \mathrm{diag}(1, -1)$, one-dimensional.

# Relationships
## Builds Upon
- **Cartan subalgebra** -- this is the specific instance for type A

## Enables
- **Root system type A** -- roots are functionals on $\mathfrak{h}$

# Source Reference
Appendix C, Section C.1, p. 123.

# Verification Notes
- Definition source: Direct from p. 123
- Confidence rationale: Explicit description
- Uncertainties: None
- Cross-reference status: Verified
