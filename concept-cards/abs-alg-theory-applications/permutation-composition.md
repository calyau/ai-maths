---
# === CORE IDENTIFICATION ===
concept: Permutation Composition
slug: permutation-composition

# === CLASSIFICATION ===
category: permutation-groups
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Permutation Groups"
chapter_number: 5
pdf_page: 73
section: "5.1 Definitions and Notation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - permutation multiplication

# === TYPED RELATIONSHIPS ===
prerequisites:
  - permutation
extends: []
related:
  - symmetric-group
  - cycle
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do you multiply permutations?"
  - "What convention is used for composing permutations?"
---

# Quick Definition

Permutation composition is the group operation in permutation groups: given permutations $\sigma$ and $\tau$, the product $\sigma\tau$ means apply $\tau$ first, then $\sigma$ (right-to-left convention).

# Core Definition

"By $\sigma\tau(x)$ we mean $\sigma(\tau(x))$" (Judson, Remark 5.3, p. 73). The convention adopted is to multiply permutations right to left: to compute $\sigma\tau$, first apply $\tau$, then apply $\sigma$. This follows the standard convention for function composition.

# Prerequisites

- **Permutation** — Composition is defined on permutations

# Key Properties

1. Permutation composition is associative
2. Permutation composition is generally not commutative ($\sigma\tau \neq \tau\sigma$ in general)
3. The convention is right-to-left: $\sigma\tau(x) = \sigma(\tau(x))$
4. The identity permutation acts as the identity element

# Construction / Recognition

## To Compute $\sigma\tau$:
1. For each element $x$ in the set, first compute $\tau(x)$
2. Then compute $\sigma(\tau(x))$
3. The resulting function is the product $\sigma\tau$

# Context & Application

Understanding the composition convention is essential for correctly computing products in permutation groups. The right-to-left convention matches function composition but is opposite to the usual left-to-right reading order.

# Examples

**Example 1** (p. 73): Let $\sigma = \begin{pmatrix} 1 & 2 & 3 & 4 \\ 4 & 1 & 2 & 3 \end{pmatrix}$ and $\tau = \begin{pmatrix} 1 & 2 & 3 & 4 \\ 2 & 1 & 4 & 3 \end{pmatrix}$. Then $\sigma\tau = \begin{pmatrix} 1 & 2 & 3 & 4 \\ 1 & 4 & 3 & 2 \end{pmatrix}$ but $\tau\sigma = \begin{pmatrix} 1 & 2 & 3 & 4 \\ 3 & 2 & 1 & 4 \end{pmatrix}$, showing that $\sigma\tau \neq \tau\sigma$.

# Relationships

## Builds Upon
- **Permutation** — Composition is defined on permutations

## Enables
- **Cycle Notation** — Products can be computed more easily in cycle notation
- **Symmetric Group** — Composition is the binary operation of $S_n$

# Common Errors

- **Error**: Applying $\sigma$ first and then $\tau$ when computing $\sigma\tau$
  **Correction**: Apply $\tau$ first, then $\sigma$ (right-to-left)

# Common Confusions

- **Confusion**: Assuming permutation multiplication is commutative
  **Clarification**: Permutation multiplication is generally noncommutative for $n \geq 3$

# Source Reference

Chapter 5: Permutation Groups, Section 5.1, Remark 5.3 and Example 5.4, pages 73-74.

# Verification Notes

- Definition source: Direct from Remark 5.3, p. 73
- Confidence rationale: Explicit convention stated with examples
- Uncertainties: None
- Cross-reference status: Verified
