---
# === CORE IDENTIFICATION ===
concept: Weyl Integration Formula for U(n)
slug: weyl-integration-formula-example

# === CLASSIFICATION ===
category: representations
subcategory: characters
tier: advanced

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of Lie Groups and Lie Algebras"
chapter_number: 4
pdf_page: 46
section: "4.6 Haar measure on compact Lie groups"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - "Weyl integration formula"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - haar-measure
extends:
  - haar-measure
related:
  - character-of-representation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How can integrals of class functions over U(n) be computed?"
---

# Quick Definition

The Weyl integration formula reduces integration of conjugation-invariant functions on $U(n)$ to integration over the maximal torus of diagonal matrices, weighted by the Vandermonde determinant $\prod_{i<j}|t_i - t_j|^2$.

# Core Definition

**Example 4.37** (Kirillov, p. 46): For $G = U(n)$ and $f$ a smooth class function ($f(ghg^{-1}) = f(h)$):

$$\int_{U(n)} f(g)\, dg = \frac{1}{n!}\int_T f\begin{pmatrix} t_1 & & \\ & \ddots & \\ & & t_n\end{pmatrix} \prod_{i < j}|t_i - t_j|^2\, dt$$

where $T$ is the torus of diagonal unitary matrices with $t_k = e^{i\varphi_k}$ and $dt = (2\pi)^{-n}\, d\varphi_1 \cdots d\varphi_n$.

# Prerequisites

- **Haar measure** — The measure being computed on the torus

# Key Properties

1. Only works for conjugation-invariant (class) functions
2. The factor $\prod_{i<j}|t_i - t_j|^2$ is the Weyl denominator
3. The $1/n!$ accounts for permutations of eigenvalues (Weyl group)
4. Generalizes to all compact Lie groups (with appropriate root system data)

# Context & Application

This is the most practical way to compute character inner products for unitary groups. It reduces an $n^2$-dimensional integral to an $n$-dimensional one.

# Relationships

## Builds Upon
- **Haar measure** — The integration measure

## Related
- **Character of representation** — Characters are class functions, so this formula applies

# Source Reference

Chapter 4, Section 4.6, Example 4.37, pp. 46-47.

# Verification Notes

- Definition source: Direct from Example 4.37
- Confidence rationale: Medium — stated as an example of a general result; full proof not given
- Uncertainties: Full proof deferred to reference [3]
- Cross-reference status: Verified
