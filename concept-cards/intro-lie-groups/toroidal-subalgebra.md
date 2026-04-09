---
# === CORE IDENTIFICATION ===
concept: Toroidal Subalgebra
slug: toroidal-subalgebra

# === CLASSIFICATION ===
category: root-systems
subcategory: abstract-root-systems
tier: foundational

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
  - "toral subalgebra"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - semisimple-element
  - semisimple-lie-algebra
extends: []
related:
  - cartan-subalgebra
  - root-space-decomposition-toroidal
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a toroidal subalgebra?"
  - "How does a toroidal subalgebra relate to the root decomposition?"
---

# Quick Definition

A toroidal subalgebra $\mathfrak{h} \subset \mathfrak{g}$ is a commutative subalgebra consisting entirely of semisimple elements. The operators $\operatorname{ad} h$ for $h \in \mathfrak{h}$ are simultaneously diagonalizable, producing a weight space decomposition of $\mathfrak{g}$.

# Core Definition

**Definition 7.6** (Kirillov, p. 83): A subalgebra $\mathfrak{h} \subset \mathfrak{g}$ is called toroidal if it is commutative and consists of semisimple elements.

# Prerequisites

- **Semisimple element** — All elements of $\mathfrak{h}$ must be semisimple
- **Semisimple Lie algebra** — The context is complex semisimple algebras

# Key Properties

1. Since $\mathfrak{h}$ is commutative and all $\operatorname{ad} h$ are diagonalizable, they are simultaneously diagonalizable (Theorem 7.7)
2. $\mathfrak{g} = \bigoplus_{\alpha \in \mathfrak{h}^*} \mathfrak{g}_\alpha$ where $\mathfrak{g}_\alpha = \{x \mid [h, x] = \langle \alpha, h \rangle x\}$
3. $[\mathfrak{g}_\alpha, \mathfrak{g}_\beta] \subset \mathfrak{g}_{\alpha+\beta}$
4. $\mathfrak{g}_\alpha$ and $\mathfrak{g}_\beta$ are Killing-orthogonal when $\alpha + \beta \neq 0$
5. The Killing form restricted to $\mathfrak{g}_0$ is non-degenerate
6. $\mathfrak{h} \subset \mathfrak{g}_0$

# Construction / Recognition

## To Construct:
1. Find a semisimple element $h_1 \in \mathfrak{g}$
2. Find another semisimple element $h_2$ commuting with $h_1$
3. Continue until no more commuting semisimple elements can be added

# Context & Application

Toroidal subalgebras are the building blocks for Cartan subalgebras. The root decomposition arises from a maximal toroidal subalgebra. The terminology comes from the corresponding torus subgroup in the Lie group.

# Examples

**Example**: In $\mathfrak{sl}(n, \mathbb{C})$, the diagonal traceless matrices form a toroidal subalgebra. Each diagonal matrix is semisimple, and they all commute.

# Relationships

## Builds Upon
- **Semisimple element** — A toroidal subalgebra consists of semisimple elements

## Enables
- **Cartan subalgebra** — A maximal toroidal subalgebra that equals its centralizer
- **Root space decomposition (toroidal)** — Eigenspace decomposition for $\operatorname{ad} \mathfrak{h}$

# Source Reference

Chapter 7: Complex Semisimple Lie Algebras, Section 7.1, pages 83-84. Definition 7.6, Theorem 7.7.

# Verification Notes

- Definition source: Direct from Definition 7.6
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
