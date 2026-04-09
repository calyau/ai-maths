---
# === CORE IDENTIFICATION ===
concept: Exponential Map
slug: exponential-map

# === CLASSIFICATION ===
category: lie-algebras
subcategory: exponential-map
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups and Lie Algebras"
chapter_number: 3
pdf_page: 21
section: "3.1"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "$\\exp: \\mathfrak{g} \\to G$"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-group
  - one-parameter-subgroup
  - left-invariant-vector-field
extends:
  - matrix-exponential
related:
  - logarithmic-map
  - commutator-bracket
  - campbell-hausdorff-formula
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the exponential map?"
  - "How do I use the exponential map to go between Lie group and Lie algebra?"
  - "How does a Lie algebra relate to its Lie group?"
---

# Quick Definition

The exponential map $\exp: \mathfrak{g} \to G$ for a general Lie group is defined by $\exp(x) = \gamma_x(1)$, where $\gamma_x$ is the unique one-parameter subgroup with tangent vector $x$ at the identity.

# Core Definition

**Definition 3.2** (Kirillov): Let $G$ be a Lie group, $\mathfrak{g} = T_1G$. Then the exponential map $\exp: \mathfrak{g} \to G$ is defined by $\exp(x) = \gamma_x(1)$ where $\gamma_x(t)$ is the one-parameter subgroup with tangent vector at $1$ equal to $x$.

# Prerequisites

- **Lie group** — the target of the exponential map
- **One-parameter subgroup** — used in the definition
- **Left-invariant vector field** — one-parameter subgroups are integral curves of these

# Key Properties

1. $\exp(0) = 1$ and $\exp_*(0): \mathfrak{g} \to T_1G = \mathfrak{g}$ is the identity (Theorem 3.7 part 1).
2. $\exp$ is a local diffeomorphism near $0$ (Theorem 3.7 part 2); the local inverse is $\log$.
3. $\exp((t+s)x) = \exp(tx)\exp(sx)$ (Theorem 3.7 part 3).
4. For any morphism $\varphi: G_1 \to G_2$: $\exp(\varphi_*(x)) = \varphi(\exp(x))$ (Theorem 3.7 part 4).
5. $X\exp(y)X^{-1} = \exp(\mathrm{Ad}\, X . y)$ (Theorem 3.7 part 5).
6. Not necessarily surjective in general; surjective for compact groups (Remark 3.8).

# Construction / Recognition

## To Construct/Create:
1. For general Lie groups: find the flow of the left-invariant vector field corresponding to $x$, evaluated at time $1$.
2. For matrix groups: use the power series $\exp(x) = \sum x^k/k!$.

## To Identify/Recognize:
1. The unique smooth map $\mathfrak{g} \to G$ that restricts to one-parameter subgroups on lines through the origin.

# Context & Application

The exponential map is the fundamental bridge between the Lie algebra and the Lie group. It provides local coordinates on $G$ near the identity (logarithmic coordinates) and allows translation of group-level questions to algebra-level questions.

# Examples

**Example 3.3** (p. 21): For $G \subset \mathrm{GL}(n, \mathbb{R})$, the general definition agrees with the matrix exponential.

**Example 3.4** (p. 21): For $G = \mathbb{R}$, $\exp(a) = a$.

**Example 3.5** (p. 21): For $G = S^1 = \mathbb{R}/\mathbb{Z}$, $\exp(a) = a \mod \mathbb{Z}$ or $\exp(a) = e^{2\pi i a}$.

**Proposition 3.9** (p. 22): Any morphism $\varphi: G_1 \to G_2$ of connected groups is uniquely determined by $\varphi_*: \mathfrak{g}_1 \to \mathfrak{g}_2$, since exp determines $\varphi$ near the identity and the identity component generates $G_1$.

# Relationships

## Builds Upon
- **One-parameter subgroup** — $\exp(x) = \gamma_x(1)$
- **Matrix exponential** — the special case for matrix groups

## Enables
- **Commutator bracket** — appears in the Taylor expansion of the group law via exp
- **Campbell-Hausdorff formula** — expresses $\exp(x)\exp(y)$ using the bracket
- **Logarithmic coordinates** — local coordinates on $G$

## Related
- **Adjoint action on Lie algebra** — $\mathrm{Ad}(\exp x) = \exp(\mathrm{ad}\, x)$

# Common Errors

- **Error**: Assuming the exponential map is always surjective.
  **Correction**: Not true in general. Example: $\begin{pmatrix}-1 & 1\\0 & -1\end{pmatrix} \notin \exp(\mathfrak{sl}(2, \mathbb{R}))$ (Exercise 3.1).

- **Error**: Assuming $\exp(x)\exp(y) = \exp(x+y)$.
  **Correction**: This holds only when $[x, y] = 0$ (Theorem 3.33).

# Common Confusions

- **Confusion**: Whether the general exponential map requires matrix multiplication.
  **Clarification**: No. For general Lie groups, it is defined via one-parameter subgroups (flows of invariant vector fields), not power series. The power series is only valid for matrix groups.

# Source Reference

Chapter 3: Lie Groups and Lie Algebras, Section 3.1, Definition 3.2, Theorem 3.7, pages 20-22.

# Verification Notes

- Definition source: Direct from Definition 3.2
- Confidence rationale: Central definition with extensive treatment
- Uncertainties: None
- Cross-reference status: Verified with Theorem 3.7, Examples 3.3-3.5, Proposition 3.9
