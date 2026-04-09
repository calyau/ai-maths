---
# === CORE IDENTIFICATION ===
concept: "Weight for sl(2,C)"
slug: weight-for-sl2

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
  - "eigenvalue of h"
  - "weight of v"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - representation-of-lie-algebra
extends: []
related:
  - weight-space-for-sl2
  - weight-decomposition-for-sl2
  - weight-of-representation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a weight in a representation of sl(2,C)?"
  - "How does sl(2,C) serve as a building block for semisimple Lie algebras?"
---

# Quick Definition

In a representation of $\mathfrak{sl}(2,\mathbb{C})$, a weight $\lambda \in \mathbb{C}$ is an eigenvalue of the operator $h$. A vector $v$ is a weight vector of weight $\lambda$ if $hv = \lambda v$.

# Core Definition

**Definition 5.1** (Kirillov, p. 58): Let $V$ be a representation of $\mathfrak{sl}(2,\mathbb{C})$. A vector $v \in V$ is called a vector of weight $\lambda$, $\lambda \in \mathbb{C}$, if it is an eigenvector for $h$ with eigenvalue $\lambda$: $hv = \lambda v$.

The subspace $V[\lambda] \subset V$ of vectors of weight $\lambda$ is the weight space.

# Prerequisites

- **Representation of a Lie algebra** — Weights are defined within a representation of $\mathfrak{sl}(2,\mathbb{C})$

# Key Properties

1. The operator $e$ raises weight by 2: $eV[\lambda] \subset V[\lambda + 2]$ (Lemma 5.2)
2. The operator $f$ lowers weight by 2: $fV[\lambda] \subset V[\lambda - 2]$ (Lemma 5.2)
3. In finite-dimensional representations, all weights are integers (Theorem 5.7)
4. Weights come in symmetric pairs: $\dim V[n] = \dim V[-n]$ (Theorem 5.7)
5. Eigenvectors with different eigenvalues are linearly independent

# Construction / Recognition

## To Find Weights:
1. Diagonalize the operator $\rho(h): V \to V$
2. The eigenvalues are the weights
3. The eigenspaces are the weight spaces

# Context & Application

Diagonalizing $h$ is "the main idea of the study of representations of $\mathfrak{sl}(2,\mathbb{C})$" (p. 58). This simple strategy generalizes to all semisimple Lie algebras, where one diagonalizes a Cartan subalgebra. The $\mathfrak{sl}(2,\mathbb{C})$ case is the prototype for all of highest-weight theory.

# Examples

**Example** (Theorem 5.6, p. 60): In the irreducible representation $V_n$ with basis $v^0, \ldots, v^n$, the weights are $n, n-2, n-4, \ldots, -n+2, -n$, each with multiplicity 1.

**Example**: For the adjoint representation ($V_2$, dimension 3), the weights are $2, 0, -2$ corresponding to $e, h, f$.

# Relationships

## Builds Upon
- **Representation of a Lie algebra** — Context in which weights are defined

## Enables
- **Weight decomposition for sl(2,C)** — $V = \bigoplus V[\lambda]$
- **Highest weight** — The maximal weight in a representation
- **Classification of sl(2,C) representations** — Based on highest weights

## Related
- **Weight of a representation** — General semisimple version (Chapter 9)

# Common Confusions

- **Confusion**: Expecting weights to always be positive.
  **Clarification**: Weights can be any integer (or complex number for infinite-dimensional representations). They come in symmetric pairs $\pm n$.

# Source Reference

Chapter 5, Section 5.1, Definition 5.1, Lemma 5.2, pp. 58-59.

# Verification Notes

- Definition source: Direct from Definition 5.1, p. 58
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
