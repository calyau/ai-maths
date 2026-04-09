---
# === CORE IDENTIFICATION ===
concept: Vandermonde Matrix
slug: vandermonde-matrix

# === CLASSIFICATION ===
category: field-theory
subcategory: finite-fields
tier: advanced

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Finite Fields"
chapter_number: 22
pdf_page: 292
section: "22.2 Polynomial Codes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Vandermonde determinant"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - field
extends: []
related:
  - bch-code
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Vandermonde matrix?"
  - "When is a Vandermonde determinant nonzero?"
---

# Quick Definition

A Vandermonde matrix is an $n \times n$ matrix whose $(i,j)$-entry is $\alpha_j^{i-1}$. Its determinant equals $\prod_{1 \leq j < i \leq n}(\alpha_i - \alpha_j)$, which is nonzero if and only if all $\alpha_i$ are distinct.

# Core Definition

If $\alpha_1, \ldots, \alpha_n$ are elements in a field $F$, then the $n \times n$ matrix with entries $\alpha_j^{i-1}$ is called the **Vandermonde matrix**. Its determinant, the **Vandermonde determinant**, satisfies

$$\det \begin{pmatrix} 1 & 1 & \cdots & 1 \\ \alpha_1 & \alpha_2 & \cdots & \alpha_n \\ \vdots & \vdots & \ddots & \vdots \\ \alpha_1^{n-1} & \alpha_2^{n-1} & \cdots & \alpha_n^{n-1} \end{pmatrix} = \prod_{1 \leq j < i \leq n}(\alpha_i - \alpha_j)$$

(Judson, Lemma 22.20, p. 300).

# Prerequisites

- **Field** — The elements come from a field

# Key Properties

1. The determinant is nonzero if and only if the $\alpha_i$ are all distinct
2. The formula is proved by induction on $n$ (Lemma 22.20)
3. Used to prove the minimum distance bound for cyclic codes (Theorem 22.21)

# Context & Application

The Vandermonde determinant is used in the proof that BCH codes achieve their designed minimum distance. It guarantees that certain systems of equations have only the trivial solution.

# Examples

**Example 1**: For $n = 2$: $\det \begin{pmatrix} 1 & 1 \\ \alpha_1 & \alpha_2 \end{pmatrix} = \alpha_2 - \alpha_1$.

# Relationships

## Enables
- **BCH code** — The Vandermonde determinant is used to prove minimum distance bounds

# Source Reference

Chapter 22: Finite Fields, Section 22.2, pages 299–300. Lemma 22.20.

# Verification Notes

- Definition source: Direct from Lemma 22.20, p. 300
- Confidence: HIGH — explicit lemma with formula
- Cross-reference status: Verified
- Uncertainties: None
