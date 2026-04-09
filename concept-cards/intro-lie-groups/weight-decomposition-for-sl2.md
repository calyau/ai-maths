---
# === CORE IDENTIFICATION ===
concept: "Weight Decomposition for sl(2,C)"
slug: weight-decomposition-for-sl2

# === CLASSIFICATION ===
category: representations
subcategory: highest-weight-theory
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of sl(2,C) and Spherical Laplace Operator"
chapter_number: 5
pdf_page: 58
section: "5.1 Representations of sl(2,C)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "weight space decomposition"
  - "eigenspace decomposition of h"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - weight-for-sl2
  - weight-space-for-sl2
  - completely-reducible-representation
extends: []
related:
  - weight-decomposition-theorem
  - classification-of-sl2-representations
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I decompose a representation of sl(2,C) into weight spaces?"
  - "What is the weight decomposition of a representation?"
---

# Quick Definition

Every finite-dimensional representation of $\mathfrak{sl}(2,\mathbb{C})$ decomposes as a direct sum of weight spaces: $V = \bigoplus_\lambda V[\lambda]$, where $V[\lambda]$ is the $\lambda$-eigenspace of $h$.

# Core Definition

**Theorem 5.3** (Kirillov, pp. 58-59): Every finite-dimensional representation $V$ of $\mathfrak{sl}(2,\mathbb{C})$ can be written in the form $V = \bigoplus_\lambda V[\lambda]$, where $V[\lambda]$ is defined in Definition 5.1. This decomposition is called the weight decomposition of $V$.

**Proof sketch**: By complete reducibility, reduce to the irreducible case. The subspace $V' = \bigoplus V[\lambda]$ spanned by eigenvectors of $h$ is a subrepresentation (by Lemma 5.2). Since $V$ is irreducible and $V' \neq 0$, we have $V' = V$.

# Prerequisites

- **Weight for sl(2,C)** — Weights label the summands
- **Weight space for sl(2,C)** — The summands themselves
- **Completely reducible representation** — Used to reduce to the irreducible case

# Key Properties

1. The decomposition holds for every finite-dimensional representation (not just irreducible ones)
2. For finite-dimensional $V$: all weights are integers (Theorem 5.7)
3. $\dim V[n] = \dim V[-n]$ (weight symmetry, Theorem 5.7)
4. The maps $e^n: V[-n] \to V[n]$ and $f^n: V[n] \to V[-n]$ are isomorphisms for $n \geq 0$ (Theorem 5.7)

# Context & Application

The weight decomposition is the starting point for analyzing any representation of $\mathfrak{sl}(2,\mathbb{C})$. It converts the problem of understanding a representation into the problem of understanding the dimensions of its weight spaces, which are combinatorial data.

# Examples

**Example** (Theorem 5.6): For the irreducible $V_n$: $V_n = V_n[n] \oplus V_n[n-2] \oplus \cdots \oplus V_n[-n]$, each weight space one-dimensional.

**Example**: For $V_2$ (adjoint representation): $V_2 = V_2[2] \oplus V_2[0] \oplus V_2[-2]$, with $\dim = 1 + 1 + 1 = 3$.

# Relationships

## Builds Upon
- **Weight for sl(2,C)** and **weight spaces** — Define the decomposition

## Enables
- **Classification of sl(2,C) representations** — Via highest weights
- **Integer weight theorem** — All weights are integers

## Related
- **Weight decomposition theorem** — General semisimple version (Chapter 9)

# Common Confusions

- **Confusion**: Thinking the weight decomposition depends on a choice of basis.
  **Clarification**: The decomposition depends only on the choice of $h$ in $\mathfrak{sl}(2,\mathbb{C})$ (the Cartan element). For a fixed standard basis $\{e, f, h\}$, it is canonical.

# Source Reference

Chapter 5, Section 5.1, Theorem 5.3, pp. 58-59.

# Verification Notes

- Definition source: Direct from Theorem 5.3
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
