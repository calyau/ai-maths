---
# === CORE IDENTIFICATION ===
concept: "Highest Weight for sl(2,C)"
slug: highest-weight-for-sl2

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
pdf_page: 59
section: "5.1 Representations of sl(2,C)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - weight-for-sl2
  - weight-decomposition-for-sl2
extends: []
related:
  - highest-weight-vector-for-sl2
  - classification-of-sl2-representations
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the highest weight of an irreducible representation of sl(2,C)?"
---

# Quick Definition

The highest weight of a finite-dimensional representation of $\mathfrak{sl}(2,\mathbb{C})$ is the weight $\lambda$ with maximal real part. For irreducible representations, the highest weight is a non-negative integer $n$, and it completely determines the representation.

# Core Definition

(Kirillov, p. 59): Let $\lambda$ be a weight of $V$ which is maximal in the sense that $\mathrm{Re}\,\lambda \geq \mathrm{Re}\,\lambda'$ for every weight $\lambda'$ of $V$. Such a weight is called the "highest weight of $V$."

By Theorem 5.6, for irreducible representations, the highest weight is always a non-negative integer $n$, and it uniquely determines the irreducible representation $V_n$ of dimension $n+1$.

# Prerequisites

- **Weight for sl(2,C)** — Highest weight is the maximal weight
- **Weight decomposition for sl(2,C)** — Ensures weights exist

# Key Properties

1. Every finite-dimensional representation has at least one highest weight vector
2. $ev = 0$ for any highest weight vector $v$ (Lemma 5.4, since $V[\lambda + 2] = 0$)
3. The highest weight of the irreducible $V_n$ is $n$ (a non-negative integer)
4. $\dim V_n = n + 1$
5. The weights of $V_n$ are $n, n-2, \ldots, -n$

# Examples

**Theorem 5.6** (p. 60): The irreducible representations of $\mathfrak{sl}(2,\mathbb{C})$ are $V_0, V_1, V_2, \ldots$ with highest weights $0, 1, 2, \ldots$ and dimensions $1, 2, 3, \ldots$ respectively.

# Relationships

## Builds Upon
- **Weight decomposition for sl(2,C)** — Provides the weights to compare

## Enables
- **Classification of sl(2,C) representations** — Highest weight classifies irreducibles

# Source Reference

Chapter 5, Section 5.1, pp. 59-60.

# Verification Notes

- Definition source: Direct from text, p. 59
- Confidence rationale: Explicit definition with key theorem
- Uncertainties: None
- Cross-reference status: Verified
