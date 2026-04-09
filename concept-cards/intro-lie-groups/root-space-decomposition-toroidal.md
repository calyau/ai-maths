---
# === CORE IDENTIFICATION ===
concept: Root Space Decomposition for Toroidal Subalgebra
slug: root-space-decomposition-toroidal

# === CLASSIFICATION ===
category: root-systems
subcategory: abstract-root-systems
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Complex Semisimple Lie Algebras"
chapter_number: 7
pdf_page: 83
section: "7.1. Semisimple elements and toroidal subalgebras"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "weight decomposition under toroidal subalgebra"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - toroidal-subalgebra
  - killing-form
extends: []
related:
  - root-decomposition
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does a toroidal subalgebra decompose the Lie algebra?"
---

# Quick Definition

For a toroidal subalgebra $\mathfrak{h} \subset \mathfrak{g}$, the Lie algebra decomposes as $\mathfrak{g} = \bigoplus_{\alpha \in \mathfrak{h}^*} \mathfrak{g}_\alpha$ where $\mathfrak{g}_\alpha$ is the common eigenspace for all $\operatorname{ad} h$ with eigenvalue $\langle \alpha, h \rangle$. Different weight spaces are Killing-orthogonal unless their weights sum to zero.

# Core Definition

**Theorem 7.7** (Kirillov, p. 83): Let $\mathfrak{h} \subset \mathfrak{g}$ be a toroidal subalgebra. Then:
1. $\mathfrak{g} = \bigoplus_{\alpha \in \mathfrak{h}^*} \mathfrak{g}_\alpha$ where $\operatorname{ad} h.x = \langle \alpha, h \rangle x$ for $h \in \mathfrak{h}$, $x \in \mathfrak{g}_\alpha$. In particular, $\mathfrak{h} \subset \mathfrak{g}_0$.
2. $[\mathfrak{g}_\alpha, \mathfrak{g}_\beta] \subset \mathfrak{g}_{\alpha+\beta}$
3. If $\alpha + \beta \neq 0$, then $\mathfrak{g}_\alpha$ and $\mathfrak{g}_\beta$ are Killing-orthogonal
4. The Killing form pairs $\mathfrak{g}_\alpha \otimes \mathfrak{g}_{-\alpha} \to \mathbb{C}$ non-degenerately. In particular, $K|_{\mathfrak{g}_0}$ is non-degenerate.

# Prerequisites

- **Toroidal subalgebra** — The subalgebra producing the decomposition
- **Killing form** — Used for orthogonality and non-degeneracy

# Key Properties

1. Simultaneous diagonalizability of commuting semisimple operators gives the decomposition
2. Only finitely many $\alpha$ have $\mathfrak{g}_\alpha \neq 0$
3. Part (2) follows from $\operatorname{ad} h.[y,z] = \langle \alpha + \beta, h \rangle [y,z]$
4. Part (3): $\operatorname{ad} x \operatorname{ad} y(\mathfrak{g}_\gamma) \subset \mathfrak{g}_{\gamma+\alpha+\beta}$, so diagonal entries of $\operatorname{ad} x \operatorname{ad} y$ are zero when $\alpha + \beta \neq 0$

# Context & Application

This theorem is the precursor to the root decomposition. When $\mathfrak{h}$ is a Cartan subalgebra (maximal toroidal with $\mathfrak{g}_0 = \mathfrak{h}$), this becomes the root decomposition proper.

# Examples

**Example**: For $\mathfrak{sl}(n, \mathbb{C})$ with diagonal Cartan subalgebra, the decomposition gives $\mathfrak{g}_{e_i - e_j} = \mathbb{C} E_{ij}$ for $i \neq j$ (Example 7.17).

# Relationships

## Builds Upon
- **Toroidal subalgebra** — The subalgebra producing the decomposition

## Enables
- **Root decomposition** — When $\mathfrak{h}$ is a Cartan subalgebra

# Source Reference

Chapter 7: Complex Semisimple Lie Algebras, Section 7.1, pages 83-84. Theorem 7.7.

# Verification Notes

- Definition source: Direct from Theorem 7.7
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
