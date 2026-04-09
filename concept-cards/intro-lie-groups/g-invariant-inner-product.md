---
# === CORE IDENTIFICATION ===
concept: G-Invariant Inner Product
slug: g-invariant-inner-product

# === CLASSIFICATION ===
category: representations
subcategory: basic-definitions
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of Lie Groups and Lie Algebras"
chapter_number: 4
pdf_page: 44
section: "4.5 Complete reducibility of unitary representations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "invariant inner product"
  - "invariant Hermitian form"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - representation-of-lie-group
extends: []
related:
  - unitary-representation
  - invariant-bilinear-form
  - haar-measure
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a G-invariant inner product?"
  - "How do I construct an invariant inner product?"
---

# Quick Definition

A $G$-invariant inner product on a representation $V$ is a positive definite Hermitian form preserved by the group action: $(\rho(g)v, \rho(g)w) = (v, w)$ for all $g \in G$.

# Core Definition

(Kirillov, p. 44): A $G$-invariant inner product is a positive definite Hermitian form $(\ ,\ )$ on a representation $V$ satisfying $(\rho(g)v, \rho(g)w) = (v, w)$ for all $g \in G$, $v, w \in V$. At the Lie algebra level: $(\rho(x)v, w) + (v, \rho(x)w) = 0$ for all $x \in \mathfrak{g}$.

For compact groups, one can always construct such a form by averaging: $\tilde{B}(v,w) = \int_G B(gv, gw)\, dg$.

# Prerequisites

- **Representation of a Lie group** — The representation on which the form is defined

# Key Properties

1. Existence is equivalent to the representation being unitary
2. For compact groups, always exists (Theorem 4.38)
3. Can be constructed by averaging any inner product over $G$ (using Haar measure)
4. If $W$ is a subrepresentation, $W^\perp$ is also a subrepresentation

# Construction / Recognition

## To Construct (compact group or finite group):
1. Start with any positive definite Hermitian form $B$ on $V$
2. Average: $\tilde{B}(v,w) = \int_G B(gv, gw)\, dg$
3. $\tilde{B}$ is automatically $G$-invariant and positive definite

# Examples

**Theorem 4.30** (p. 44): For finite groups, $\tilde{B}(v,w) = \frac{1}{|G|}\sum_{g \in G} B(gv, gw)$ produces a $G$-invariant inner product from any inner product $B$.

# Relationships

## Enables
- **Unitary representation** — Defines the unitary structure
- **Complete reducibility** — Via orthogonal complement argument

## Related
- **Haar measure** — Used in the averaging construction

# Source Reference

Chapter 4, Section 4.5, pp. 44-45. Theorems 4.29-4.30, 4.38.

# Verification Notes

- Definition source: Synthesized from Definition 4.27 and Theorems 4.30, 4.38
- Confidence rationale: Clear from context though not given as a standalone definition
- Uncertainties: None
- Cross-reference status: Verified
