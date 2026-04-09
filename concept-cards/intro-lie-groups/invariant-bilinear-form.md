---
# === CORE IDENTIFICATION ===
concept: Invariant Bilinear Form
slug: invariant-bilinear-form

# === CLASSIFICATION ===
category: structure-theory
subcategory: bilinear-forms
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Structure Theory of Lie Algebras"
chapter_number: 6
pdf_page: 73
section: "6.5. Invariant bilinear forms and semisimplicity of classical Lie algebras"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "ad-invariant form"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-algebra
  - lie-algebra-ideal
extends: []
related:
  - trace-form
  - killing-form
  - orthogonal-complement
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an invariant bilinear form on a Lie algebra?"
  - "Why are invariant bilinear forms important for structure theory?"
---

# Quick Definition

An invariant bilinear form on a Lie algebra $\mathfrak{g}$ is a bilinear form $B$ satisfying $B(\operatorname{ad} x.y, z) + B(y, \operatorname{ad} x.z) = 0$ for all $x, y, z \in \mathfrak{g}$. Such forms are the key tool for studying semisimplicity.

# Core Definition

A bilinear form $B$ on $\mathfrak{g}$ is called invariant if (Kirillov, p. 73):

$$B(\operatorname{ad} x.y, z) + B(y, \operatorname{ad} x.z) = 0$$

for any $x, y, z \in \mathfrak{g}$. Equivalently, $B([x,y], z) + B(y, [x,z]) = 0$.

# Prerequisites

- **Lie algebra** — Forms are defined on Lie algebras
- **Lie algebra ideal** — The orthogonal complement of an ideal is an ideal (Lemma 6.29)

# Key Properties

1. If $B$ is invariant and $I \subset \mathfrak{g}$ is an ideal, then $I^\perp$ is also an ideal (Lemma 6.29)
2. $\operatorname{Ker} B = \mathfrak{g}^\perp$ is an ideal
3. On a simple Lie algebra, the invariant form is unique up to a scalar (Exercise 4.4)
4. In general, $I \cap I^\perp$ can be nonzero even for non-degenerate $B$

# Construction / Recognition

## To Construct:
1. Choose any representation $V$ of $\mathfrak{g}$
2. Define $B_V(x,y) = \operatorname{tr}_V(\rho(x)\rho(y))$
3. This gives a symmetric invariant bilinear form (Proposition 6.31)
4. The Killing form is the special case $V = \mathfrak{g}$ (adjoint representation)

# Context & Application

Invariant bilinear forms are the primary tool for the structure theory. Their non-degeneracy detects reductivity and semisimplicity. The Killing form (trace form of the adjoint representation) is the canonical choice for theoretical purposes, while trace forms in specific representations are often more practical for computation.

# Examples

**Example 6.30** (p. 73): For $\mathfrak{g} = \mathfrak{gl}(n, \mathbb{C})$, $B(x,y) = \operatorname{tr}(xy)$ is a symmetric invariant form. Invariance follows from $\operatorname{tr}([x,y]z + y[x,z]) = \operatorname{tr}(xyz - yzx) = 0$.

# Relationships

## Enables
- **Trace form** — Constructed from representations
- **Killing form** — The canonical invariant form using the adjoint representation
- **Orthogonal complement** — Orthogonal complement of an ideal is an ideal

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.5, pages 73-74. Lemma 6.29, Example 6.30, Proposition 6.31.

# Verification Notes

- Definition source: Direct from source, p. 73
- Confidence rationale: Standard definition with clear examples
- Uncertainties: None
- Cross-reference status: Verified
