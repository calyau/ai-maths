---
# === CORE IDENTIFICATION ===
concept: "Weight Space V[lambda] for sl(2,C)"
slug: weight-space-for-sl2

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
  - "V[lambda]"
  - "eigenspace of h"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - weight-for-sl2
extends: []
related:
  - weight-decomposition-for-sl2
  - weight-space
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a weight space in a representation of sl(2,C)?"
---

# Quick Definition

The weight space $V[\lambda]$ is the subspace of all vectors of weight $\lambda$ in a representation $V$ of $\mathfrak{sl}(2,\mathbb{C})$, i.e., the $\lambda$-eigenspace of $h$.

# Core Definition

**Definition 5.1** (Kirillov, p. 58): $V[\lambda] = \{v \in V \mid hv = \lambda v\} \subset V$ is the subspace of vectors of weight $\lambda$.

# Prerequisites

- **Weight for sl(2,C)** — The weight space collects all vectors of a given weight

# Key Properties

1. $eV[\lambda] \subset V[\lambda + 2]$: the raising operator shifts weight spaces (Lemma 5.2)
2. $fV[\lambda] \subset V[\lambda - 2]$: the lowering operator shifts weight spaces (Lemma 5.2)
3. Weight spaces for different eigenvalues are linearly independent
4. For irreducible $V_n$: $\dim V_n[\lambda] = 1$ for $\lambda = n, n-2, \ldots, -n$ and $0$ otherwise
5. $\dim V[\lambda] = \dim V[-\lambda]$ for finite-dimensional $V$ (Theorem 5.7)

# Context & Application

Weight spaces are the basic building blocks of the weight decomposition. Understanding how $e$ and $f$ map between weight spaces is the key to classifying representations.

# Examples

**Example** (Theorem 5.6): For $V_n$ with basis $v^0, \ldots, v^n$: $V_n[n-2k] = \mathbb{C} v^k$ for $0 \leq k \leq n$.

# Relationships

## Builds Upon
- **Weight for sl(2,C)** — Weight spaces collect vectors of given weight

## Enables
- **Weight decomposition for sl(2,C)** — $V = \bigoplus V[\lambda]$

# Source Reference

Chapter 5, Section 5.1, Definition 5.1, p. 58.

# Verification Notes

- Definition source: Direct from Definition 5.1
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
