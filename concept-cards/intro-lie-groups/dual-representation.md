---
# === CORE IDENTIFICATION ===
concept: Dual Representation
slug: dual-representation

# === CLASSIFICATION ===
category: representations
subcategory: operations
tier: intermediate

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
aliases:
  - "contragredient representation"
  - "V*"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - representation-of-lie-group
  - tensor-product-of-representations
extends: []
related:
  - character-of-representation
  - invariant-vectors
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does a group act on the dual of a representation?"
---

# Quick Definition

The dual representation $V^*$ has the group acting by $\rho_{V^*}(g) = \rho_V(g^{-1})^t$ (transpose of the inverse), or equivalently for the Lie algebra, $\rho_{V^*}(x) = -\rho_V(x)^t$.

# Core Definition

**Lemma 4.10** (Kirillov, p. 40): The action on $V^*$ is defined by requiring the natural pairing $V \otimes V^* \to \mathbb{C}$ to be a morphism of representations (with $\mathbb{C}$ the trivial representation). This gives:

$$\langle \rho(g)v, \rho(g)v^* \rangle = \langle v, v^* \rangle$$

so $\rho_{V^*}(g) = \rho_V(g^{-1})^t$. For the Lie algebra: $\langle \rho(x)v, v^* \rangle + \langle v, \rho(x)v^* \rangle = 0$, so $\rho_{V^*}(x) = -(\rho_V(x))^t$.

# Prerequisites

- **Representation of a Lie group** — The representation being dualized
- **Tensor product of representations** — The pairing $V \otimes V^* \to \mathbb{C}$ is a morphism

# Key Properties

1. $\dim V^* = \dim V$
2. $\chi_{V^*} = \overline{\chi_V}$ (Lemma 4.42)
3. $(V^*)^* \cong V$ canonically
4. $\mathrm{Hom}(V, W) \cong V^* \otimes W$ as representations
5. If $V$ is irreducible, then $V^*$ is also irreducible (Exercise 4.4)

# Construction / Recognition

## To Construct:
1. Take the dual vector space $V^*$
2. For group: $(\rho(g) \cdot v^*)(v) = v^*(\rho(g^{-1})v)$ for $v^* \in V^*$, $v \in V$
3. For algebra: $(\rho(x) \cdot v^*)(v) = -v^*(\rho(x)v)$

# Context & Application

The dual representation is essential for constructing invariant bilinear forms, defining characters, and understanding the Hom space between representations. The space of $\mathfrak{g}$-invariant bilinear forms on an irreducible representation $V$ is at most one-dimensional (Exercise 4.4).

# Examples

**Example 4.11** (p. 40): $\mathrm{End}(V) \cong V \otimes V^*$ as a representation, with action $g: A \mapsto \rho(g)A\rho(g^{-1})$.

**Example** (p. 41): The space of bilinear forms on $V$ is also a representation via the dual construction: $gB(v,w) = B(g^{-1}v, g^{-1}w)$.

# Relationships

## Builds Upon
- **Representation of a Lie group** — The original representation

## Enables
- **Character** — $\chi_{V^*} = \overline{\chi_V}$
- **Hom spaces** — $\mathrm{Hom}(V,W) \cong V^* \otimes W$

## Related
- **Invariant bilinear form** — Corresponds to elements of $(V^* \otimes V^*)^G$

# Common Errors

- **Error**: Using $\rho_{V^*}(g) = \rho_V(g)^t$ instead of $\rho_V(g^{-1})^t$.
  **Correction**: The inverse is required to make $\rho_{V^*}$ a homomorphism.

# Common Confusions

- **Confusion**: Thinking $V \cong V^*$ always.
  **Clarification**: This requires a non-degenerate invariant bilinear form on $V$, which does not always exist. For unitary representations, $V \cong V^*$ via the inner product.

# Source Reference

Chapter 4, Section 4.2, Lemma 4.10, pp. 40-41.

# Verification Notes

- Definition source: Direct from Lemma 4.10, p. 40
- Confidence rationale: Explicit construction with derivation
- Uncertainties: None
- Cross-reference status: Verified
