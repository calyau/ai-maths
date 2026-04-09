---
# === CORE IDENTIFICATION ===
concept: Direct Sum of Representations
slug: direct-sum-of-representations

# === CLASSIFICATION ===
category: representations
subcategory: operations
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of Lie Groups and Lie Algebras"
chapter_number: 4
pdf_page: 40
section: "4.2 Operations on representations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - representation-of-lie-group
  - subrepresentation
extends: []
related:
  - completely-reducible-representation
  - tensor-product-of-representations
contrasts_with:
  - tensor-product-of-representations

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I combine two representations into a larger one via direct sum?"
---

# Quick Definition

The direct sum $V \oplus W$ of two representations is the vector space direct sum with the group acting diagonally: $\rho(g)(v + w) = \rho(g)v + \rho(g)w$.

# Core Definition

**Lemma 4.10** (Kirillov, p. 40): Let $V, W$ be representations of $G$ (respectively, $\mathfrak{g}$). Then $V \oplus W$ has a canonical structure of a representation. The action of $G$ on $V \oplus W$ is given by $\rho(g)(v + w) = \rho(g)v + \rho(g)w$, and similarly for $\mathfrak{g}$.

# Prerequisites

- **Representation of a Lie group** — The objects being summed
- **Subrepresentation** — $V$ and $W$ are subrepresentations of $V \oplus W$

# Key Properties

1. $\dim(V \oplus W) = \dim V + \dim W$
2. $V$ and $W$ are subrepresentations of $V \oplus W$
3. $\chi_{V \oplus W} = \chi_V + \chi_W$ (Lemma 4.42)
4. The direct sum operation is associative and commutative (up to isomorphism)

# Construction / Recognition

## To Construct:
1. Form the vector space direct sum $V \oplus W$
2. Define $\rho_{V \oplus W}(g) = \rho_V(g) \oplus \rho_W(g)$ (block diagonal)

## To Identify/Recognize:
1. Check if the representation splits as $V = V_1 \oplus V_2$ with each $V_i$ invariant
2. Equivalently, look for a complementary invariant subspace to a known subrepresentation

# Context & Application

Direct sum decomposition is the primary goal of representation theory for semisimple groups: every representation decomposes as a direct sum of irreducibles. The multiplicities in such a decomposition encode important structural information.

# Examples

**Example 4.21** (p. 42): $\mathbb{C}^n \otimes \mathbb{C}^n = S^2\mathbb{C}^n \oplus \Lambda^2\mathbb{C}^n$ as a representation of $GL(n, \mathbb{C})$.

# Relationships

## Builds Upon
- **Subrepresentation** — Each summand is a subrepresentation

## Enables
- **Completely reducible representation** — Defined as a direct sum of irreducibles

## Contrasts With
- **Tensor product of representations** — Different operation; tensor product is multiplicative, direct sum is additive

# Common Confusions

- **Confusion**: Assuming every representation with a subrepresentation $W$ decomposes as $V = W \oplus (V/W)$.
  **Clarification**: This requires complete reducibility. Not every short exact sequence of representations splits (Example 4.18).

# Source Reference

Chapter 4, Section 4.2, Lemma 4.10, p. 40.

# Verification Notes

- Definition source: Direct from Lemma 4.10, p. 40
- Confidence rationale: Explicit construction given
- Uncertainties: None
- Cross-reference status: Verified
