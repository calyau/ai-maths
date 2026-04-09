---
# === CORE IDENTIFICATION ===
concept: "Symmetric Powers as Irreducible Representations of sl(2,C)"
slug: symmetric-power-as-irreducible

# === CLASSIFICATION ===
category: representations
subcategory: highest-weight-theory
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of sl(2,C) and Spherical Laplace Operator"
chapter_number: 5
pdf_page: 61
section: "5.1 Representations of sl(2,C)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "S^k C^2"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - classification-of-sl2-representations
  - tensor-product-of-representations
extends:
  - classification-of-sl2-representations
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How can irreducible representations of sl(2,C) be realized concretely?"
---

# Quick Definition

The irreducible representation $V_k$ of $\mathfrak{sl}(2,\mathbb{C})$ with highest weight $k$ is isomorphic to $S^k\mathbb{C}^2$, the $k$-th symmetric power of the standard 2-dimensional representation.

# Core Definition

(Kirillov, p. 61): Irreducible representations $V_n$ can be described as symmetric powers of the usual two-dimensional representation: $V_n \cong S^n\mathbb{C}^2$ (Exercise 5.2).

**Exercise 4.2** (p. 55): The action of $e, f, h$ on $S^k V$ in the basis $e_1^i e_2^{k-i}$ can be written explicitly. In particular, $S^2 V$ is isomorphic to the adjoint representation.

# Prerequisites

- **Classification of sl(2,C) representations** — Identifies $V_n$ as the irreducible with highest weight $n$
- **Tensor product of representations** — Symmetric powers are subrepresentations of tensor products

# Key Properties

1. $\dim S^k\mathbb{C}^2 = k + 1 = \dim V_k$
2. The basis $e_1^{k-i} e_2^i$ corresponds to the weight vectors $v^i$
3. $S^0\mathbb{C}^2 = \mathbb{C}$ (trivial), $S^1\mathbb{C}^2 = \mathbb{C}^2$ (standard), $S^2\mathbb{C}^2 \cong \mathfrak{sl}(2,\mathbb{C})$ (adjoint)

# Examples

**Exercise 4.2** (p. 55): $S^2\mathbb{C}^2$ with basis $e_1^2, e_1 e_2, e_2^2$ is isomorphic to the adjoint representation of $\mathfrak{sl}(2,\mathbb{C})$.

# Relationships

## Builds Upon
- **Classification** — Identifies which symmetric power gives which $V_n$

# Source Reference

Chapter 5, Section 5.1, p. 61; Exercise 5.2, p. 64; Exercise 4.2, p. 55.

# Verification Notes

- Definition source: From remark on p. 61 and Exercise 5.2
- Confidence rationale: Explicit statement, proof left as exercise
- Uncertainties: None
- Cross-reference status: Verified
