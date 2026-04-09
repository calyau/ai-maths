---
# === CORE IDENTIFICATION ===
concept: Casimir Operator
slug: casimir-operator

# === CLASSIFICATION ===
category: enveloping-algebras
subcategory: casimir-elements
tier: advanced

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of Lie Groups and Lie Algebras"
chapter_number: 4
pdf_page: 52
section: "4.8 Universal enveloping algebra"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Casimir element"
  - "quadratic Casimir"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - universal-enveloping-algebra
  - schur-lemma
extends: []
related:
  - decomposition-using-central-elements
  - spherical-laplace-operator
  - adjoint-action-on-enveloping-algebra
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Casimir operator?"
  - "How does the Casimir operator help decompose representations?"
---

# Quick Definition

The Casimir operator is a central element of $U\mathfrak{g}$ constructed from an invariant bilinear form. For $\mathfrak{sl}(2,\mathbb{C})$, it is $C = ef + fe + \frac{1}{2}h^2$. Being central, it acts as a scalar on each irreducible representation.

# Core Definition

**Example 4.55** (Kirillov, p. 52): Let $C = ef + fe + \frac{1}{2}h^2 \in U\mathfrak{sl}(2,\mathbb{C})$. Then $C$ is central in $U\mathfrak{sl}(2,\mathbb{C})$: $eC = Ce$, $fC = Cf$, $hC = Ch$.

The proof proceeds by moving $e$ past other generators using the relations $ef = fe + h$ and $eh = he - 2e$.

The general construction (Proposition 6.54, referenced): Given a Lie algebra $\mathfrak{g}$ with an invariant bilinear form $B$ and dual bases $x_i$, $x^i$ (meaning $B(x_i, x^j) = \delta_i^j$), the Casimir element is $C = \sum x_i x^i \in U\mathfrak{g}$.

# Prerequisites

- **Universal enveloping algebra** — The Casimir lives in $U\mathfrak{g}$
- **Schur's lemma** — Guarantees the Casimir acts as a scalar on irreducibles

# Key Properties

1. $C$ is central in $U\mathfrak{g}$ (commutes with all elements)
2. By Schur's lemma, $C$ acts as a scalar on each irreducible representation
3. Different irreducible representations can have different Casimir eigenvalues
4. For $\mathfrak{sl}(2,\mathbb{C})$: $C$ acts on $V_n$ (highest weight $n$) by $\frac{n(n+2)}{4} \cdot \mathrm{id}$ (from Exercise 4.3)
5. $C$ is in the center $Z\mathfrak{g} = (U\mathfrak{g})^{\mathrm{ad}\,\mathfrak{g}}$ (Proposition 4.56)

# Construction / Recognition

## For $\mathfrak{sl}(2,\mathbb{C})$:
1. $C = ef + fe + \frac{1}{2}h^2$
2. Verify centrality by direct computation: push generators through $C$ using bracket relations

## General construction:
1. Choose an invariant bilinear form $B$ on $\mathfrak{g}$
2. Pick a basis $x_i$ and find the dual basis $x^i$ w.r.t. $B$
3. $C = \sum_i x_i x^i \in U\mathfrak{g}$

# Context & Application

The Casimir operator is the main tool for distinguishing irreducible representations within a direct sum. Its eigenvalues label irreducible components. In physics, the Casimir corresponds to $J^2 = J_x^2 + J_y^2 + J_z^2$ (total angular momentum squared) for $\mathfrak{so}(3)$, and its eigenvalues $l(l+1)$ determine the angular momentum quantum number.

# Examples

**Example 4.55** (p. 52): $C = ef + fe + \frac{1}{2}h^2$ is central in $U\mathfrak{sl}(2,\mathbb{C})$. Under the isomorphism $\mathfrak{so}(3,\mathbb{C}) \cong \mathfrak{sl}(2,\mathbb{C})$, $C$ corresponds to a multiple of $J_x^2 + J_y^2 + J_z^2$ (Exercise 4.3).

**Application** (Section 5.2): The spherical Laplace operator $\Delta_{\mathrm{sph}} = J_x^2 + J_y^2 + J_z^2$ is (up to a factor) the Casimir element of $\mathfrak{so}(3,\mathbb{R})$, which is why it commutes with the $SO(3)$ action.

# Relationships

## Builds Upon
- **Universal enveloping algebra** — Where the Casimir lives
- **Schur's lemma** — Why it acts as scalar on irreducibles

## Enables
- **Decomposition of representations** — Eigenspaces of the Casimir are subrepresentations
- **Spherical Laplace operator** — Is essentially a Casimir element

## Related
- **Adjoint action on $U\mathfrak{g}$** — Casimir is invariant under adjoint action

# Common Errors

- **Error**: Assuming every irreducible has a different Casimir eigenvalue.
  **Correction**: Different irreducibles can share a Casimir eigenvalue. The Casimir separates some but not necessarily all irreducibles. For $\mathfrak{sl}(2,\mathbb{C})$ it does separate all.

# Source Reference

Chapter 4, Section 4.8, Example 4.55, Proposition 4.56, pp. 52-53. See also Exercise 4.3, p. 55.

# Verification Notes

- Definition source: Direct from Example 4.55, p. 52
- Confidence rationale: Explicit construction with verification of centrality
- Uncertainties: Eigenvalue formula from Exercise 4.3, not proved in text
- Cross-reference status: Verified
