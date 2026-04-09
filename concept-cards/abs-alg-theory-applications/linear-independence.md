---
# === CORE IDENTIFICATION ===
concept: Linear Independence
slug: linear-independence

# === CLASSIFICATION ===
category: linear-algebra
subcategory: vector-spaces
tier: intermediate

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Vector Spaces"
chapter_number: 20
pdf_page: 266
section: "20.3 Linear Independence"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "linearly independent"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - linear-combination
  - vector-space
extends: []
related:
  - basis
  - dimension
contrasts_with:
  - linear-dependence

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does it mean for vectors to be linearly independent?"
  - "Why is linear independence important?"
---

# Quick Definition

A set of vectors $\{v_1, \ldots, v_n\}$ is linearly independent if the only linear combination equal to the zero vector is the trivial one where all scalars are zero.

# Core Definition

A set $S = \{v_1, v_2, \ldots, v_n\}$ is **linearly independent** if

$$\alpha_1 v_1 + \alpha_2 v_2 + \cdots + \alpha_n v_n = \mathbf{0}$$

implies that $\alpha_1 = \alpha_2 = \cdots = \alpha_n = 0$ for any set of scalars $\{\alpha_1, \alpha_2, \ldots, \alpha_n\}$ (Judson, p. 268).

# Prerequisites

- **Linear combination** — Independence is defined via the uniqueness of the trivial linear combination
- **Vector space** — The concept lives within a vector space

# Key Properties

1. If $\{v_1, \ldots, v_n\}$ is linearly independent, then any vector has at most one representation as a linear combination (Proposition 20.9)
2. A linearly independent set has no redundant vectors
3. In an $n$-dimensional vector space, any set of $n$ linearly independent vectors is a basis (Theorem 20.15)
4. A linearly independent set of $k < n$ vectors can be extended to a basis (Theorem 20.15)

# Construction / Recognition

## To Recognize:
1. Set up $\alpha_1 v_1 + \cdots + \alpha_n v_n = \mathbf{0}$
2. Solve the resulting system
3. If the only solution is $\alpha_1 = \cdots = \alpha_n = 0$, the set is linearly independent

# Context & Application

Linear independence guarantees that each vector contributes something new to the span. It is the key condition (alongside spanning) that defines a basis. The concept is essential for understanding dimension and for field extension theory, where the degree of an extension equals the dimension of the extension as a vector space.

# Examples

**Example 1** (p. 269): The standard basis vectors $e_1 = (1,0,0)$, $e_2 = (0,1,0)$, $e_3 = (0,0,1)$ are linearly independent in $\mathbb{R}^3$.

**Example 2** (p. 270): The set $\{1, \sqrt{2}\}$ is linearly independent over $\mathbb{Q}$ in $\mathbb{Q}(\sqrt{2})$.

# Relationships

## Builds Upon
- **Linear combination** — Independence constrains which linear combinations equal zero

## Enables
- **Basis** — A basis is a linearly independent spanning set
- **Dimension** — Determined by the size of a maximal linearly independent set

## Contrasts With
- **Linear dependence** — The negation of linear independence

# Common Errors

- **Error**: Assuming vectors are independent just because they "look different"
  **Correction**: Independence must be verified algebraically; $(1,2)$ and $(2,4)$ look different but are dependent

# Common Confusions

- **Confusion**: Thinking linear independence is a property of individual vectors rather than a set
  **Clarification**: Independence is a property of the entire set; a single nonzero vector is always independent, but the same vector in a larger set may contribute to dependence

# Source Reference

Chapter 20: Vector Spaces, Section 20.3 "Linear Independence," pages 268–270. See Propositions 20.9, 20.10, 20.11.

# Verification Notes

- Definition source: Direct from p. 268
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
