---
# === CORE IDENTIFICATION ===
concept: Second Fundamental Theorem of Lie Theory
slug: second-fundamental-theorem-of-lie-theory

# === CLASSIFICATION ===
category: lie-algebras
subcategory: fundamental-theorems
tier: advanced

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups and Lie Algebras"
chapter_number: 3
pdf_page: 31
section: "3.8"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Theorem 3.43"
  - "subalgebra-subgroup correspondence"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-subalgebra
  - immersed-subgroup
  - frobenius-integrability-criterion
extends: []
related:
  - first-fundamental-theorem
  - lie-third-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does a Lie algebra relate to its Lie group?"
  - "What must I know before studying the structure theory of Lie algebras?"
---

# Quick Definition

There is a bijection between connected immersed subgroups $H \subset G$ and Lie subalgebras $\mathfrak{h} \subset \mathfrak{g}$, given by $H \mapsto \mathfrak{h} = T_1H$.

# Core Definition

**Theorem 3.43** (Kirillov): There is a bijection between connected immersed subgroups $H \subset G$ and subalgebras $\mathfrak{h} \subset \mathfrak{g}$. The correspondence is given by $H \to \mathfrak{h} = \mathrm{Lie}(H) = T_1H$.

# Prerequisites

- **Lie subalgebra** — the algebraic side of the correspondence
- **Immersed subgroup** — the geometric side
- **Frobenius integrability criterion** — used in the proof

# Key Properties

1. Every subalgebra corresponds to an immersed subgroup (existence).
2. The subgroup is given by $H = \{\exp(x_1)\cdots\exp(x_n) \mid x_i \in \mathfrak{h}\}$ (from the proof).
3. If $\mathfrak{h}$ is an ideal, the corresponding subgroup is normal (if connected, Theorem 3.19).
4. The subgroup $H$ is constructed as the maximal connected integral manifold of the distribution $\mathcal{D}^{\mathfrak{h}}_p = \mathfrak{h} \cdot p$.

# Construction / Recognition

## To Construct/Create:
1. Given a subalgebra $\mathfrak{h} \subset \mathfrak{g}$, form the distribution $\mathcal{D}^{\mathfrak{h}}_p = \mathfrak{h} \cdot p$.
2. By Frobenius theorem, this is completely integrable (since $\mathfrak{h}$ is closed under bracket).
3. Take the maximal connected integral manifold through $1$.
4. This is the immersed subgroup $H$.

## To Identify/Recognize:
1. A connected immersed subgroup and its tangent space at identity.

# Context & Application

This theorem, together with Theorem 3.38, constitutes the first two fundamental theorems of Lie theory. It establishes the complete dictionary between subalgebras and subgroups.

# Examples

**Example 3.37** (p. 30): For $G = T^2$ and $\mathfrak{h} = \{(t, \alpha t)\}$ with $\alpha$ irrational, the corresponding immersed subgroup is the irrational winding — dense but not closed.

**Example** (Lemma 3.47, p. 32): Locally, the integral manifold through $g$ is $H^0 \cdot g$ where $H^0 = \exp(\mathfrak{u})$ for a neighborhood $\mathfrak{u}$ of $0$ in $\mathfrak{h}$.

# Relationships

## Builds Upon
- **Lie subalgebra** — the algebraic input
- **Immersed subgroup** — the geometric output
- **Frobenius integrability criterion** — the analytic tool

## Enables
- **First fundamental theorem** — derived as a consequence (Proposition 3.44)

## Related
- **Lie's third theorem** — the third piece of the puzzle

# Common Errors

- **Error**: Expecting the subgroup to always be a Lie subgroup (closed).
  **Correction**: The subgroup is only guaranteed to be an immersed subgroup. It may not be closed (Example 3.37).

# Common Confusions

- **Confusion**: Whether the bijection requires $G$ to be simply connected.
  **Clarification**: No. The bijection between subalgebras and connected immersed subgroups holds for any Lie group $G$.

# Source Reference

Chapter 3: Lie Groups and Lie Algebras, Section 3.8, Theorem 3.43, Lemma 3.47, pages 31-32.

# Verification Notes

- Definition source: Direct from Theorem 3.43
- Confidence rationale: Explicit theorem with proof via Frobenius
- Uncertainties: None
- Cross-reference status: Verified with Example 3.37, Lemma 3.47, Proposition 3.44
