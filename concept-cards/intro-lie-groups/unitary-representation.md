---
# === CORE IDENTIFICATION ===
concept: Unitary Representation
slug: unitary-representation

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - representation-of-lie-group
extends: []
related:
  - completely-reducible-representation
  - g-invariant-inner-product
  - haar-measure
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a unitary representation?"
  - "Why are unitary representations completely reducible?"
---

# Quick Definition

A unitary representation is a representation equipped with a $G$-invariant inner product, meaning each $\rho(g)$ is a unitary operator. Every unitary representation is completely reducible.

# Core Definition

**Definition 4.27** (Kirillov, p. 44): A complex representation $V$ of a group $G$ is called unitary if there is a $G$-invariant inner product: $(\rho(g)v, \rho(g)w) = (v, w)$, or equivalently, $\rho(g) \in U(V)$ for any $g \in G$.

Similarly, a representation $V$ of a Lie algebra $\mathfrak{g}$ is called unitary if there is an inner product which is $\mathfrak{g}$-invariant: $(\rho(x)v, w) + (v, \rho(x)w) = 0$, or equivalently, $\rho(x) \in \mathfrak{u}(V)$ for any $x \in \mathfrak{g}$.

# Prerequisites

- **Representation of a Lie group** — A unitary representation is a special case

# Key Properties

1. Every unitary representation is completely reducible (Theorem 4.29)
2. If $W \subset V$ is a subrepresentation, then $W^\perp$ is also a subrepresentation
3. Every representation of a finite group is unitary (Theorem 4.30)
4. Every finite-dimensional representation of a compact Lie group is unitary (Theorem 4.38)
5. The $\mathfrak{g}$-invariance condition means $\rho(x)$ is skew-Hermitian for all $x \in \mathfrak{g}$

# Construction / Recognition

## To Construct:
1. Start with any positive definite inner product $B(v,w)$ on $V$
2. Average over the group: $\tilde{B}(v,w) = \int_G B(gv, gw)\, dg$ (for compact groups)
3. For finite groups: $\tilde{B}(v,w) = \frac{1}{|G|}\sum_{g \in G} B(gv, gw)$

## To Identify:
1. Check for the existence of a $G$-invariant positive definite Hermitian form
2. For compact groups: always unitary

# Context & Application

Unitarity is the bridge between representation theory and inner product geometry. The proof of complete reducibility is elementary: for any invariant subspace $W$, the orthogonal complement $W^\perp$ is also invariant. This is the key mechanism behind the complete reducibility theorems for compact and finite groups.

# Examples

**Example 4.28** (p. 44): Let $V = F(S)$ be the space of complex-valued functions on a finite set $S$ with a finite group $G$ acting by permutations. Then $(f_1, f_2) = \sum_s f_1(s)\overline{f_2(s)}$ is an invariant inner product.

# Relationships

## Builds Upon
- **Representation of a Lie group** — Special case with additional structure

## Enables
- **Complete reducibility** — Every unitary representation is completely reducible

## Related
- **G-invariant inner product** — The defining structure
- **Haar measure** — Used to construct invariant inner products on compact groups

# Common Confusions

- **Confusion**: Thinking unitarity is a property of the representation alone.
  **Clarification**: Unitarity depends on the choice of inner product. The correct statement is that the representation *admits* a $G$-invariant inner product.

# Source Reference

Chapter 4, Section 4.5, Definition 4.27, Theorems 4.29-4.31, pp. 44-45.

# Verification Notes

- Definition source: Direct from Definition 4.27, p. 44
- Confidence rationale: Explicit definition with complete proof of key theorem
- Uncertainties: None
- Cross-reference status: Verified
