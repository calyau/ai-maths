---
# === CORE IDENTIFICATION ===
concept: Standard Representation of Type A_n
slug: standard-representation-type-a

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
aliases:
  - "defining representation"
  - "natural representation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - root-system-type-a
extends: []
related:
  - fundamental-weights-type-a
  - exterior-power-representation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the standard representation of sl(n+1,C)?"
---

# Quick Definition
The standard representation of $\mathfrak{sl}(n+1, \mathbb{C})$ is its action on $\mathbb{C}^{n+1}$ by matrix multiplication. It is irreducible with highest weight $\omega_1 = e_1$ and dimension $n+1$.

# Core Definition
(Kirillov, p. 123): The standard representation is the natural action of $\mathfrak{sl}(n+1, \mathbb{C})$ on $V = \mathbb{C}^{n+1}$. Its weights are $e_1, e_2, \ldots, e_{n+1}$, each with multiplicity 1.

# Prerequisites
- **Root system type A** -- provides the weight structure

# Key Properties
1. Dimension $n+1$
2. Weights: $e_1, e_2, \ldots, e_{n+1}$ (each of multiplicity 1)
3. Highest weight: $\omega_1 = e_1 = (1, 0, \ldots, 0)$
4. The first fundamental representation
5. All other fundamental representations are exterior powers: $\Lambda^k \mathbb{C}^{n+1}$

# Examples
**Example** (p. 123): For $A_1 = \mathfrak{sl}(2, \mathbb{C})$: the standard representation is $\mathbb{C}^2$ with weights $e_1, e_2$ (i.e., $+1, -1$ for the standard $h$).

# Relationships
## Enables
- **Exterior power representation** -- $\Lambda^k$ of the standard representation gives fundamental representations
- **All irreducible representations** -- can be constructed from the standard representation

# Source Reference
Appendix C, Section C.1, p. 123.

# Verification Notes
- Definition source: Inferred from root system description
- Confidence rationale: High -- standard concept consistent with source
- Uncertainties: None
- Cross-reference status: Verified
