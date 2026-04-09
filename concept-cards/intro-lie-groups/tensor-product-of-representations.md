---
# === CORE IDENTIFICATION ===
concept: Tensor Product of Representations
slug: tensor-product-of-representations

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - representation-of-lie-group
  - representation-of-lie-algebra
extends: []
related:
  - dual-representation
  - direct-sum-of-representations
  - character-of-representation
contrasts_with:
  - direct-sum-of-representations

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I form the tensor product of two representations?"
  - "Why is the Lie algebra action on a tensor product different from the group action?"
---

# Quick Definition

The tensor product $V \otimes W$ of two representations carries a natural representation structure: the group acts by $\rho(g)(v \otimes w) = \rho(g)v \otimes \rho(g)w$, while the Lie algebra acts by the Leibniz rule $\rho(x)(v \otimes w) = \rho(x)v \otimes w + v \otimes \rho(x)w$.

# Core Definition

**Lemma 4.10** (Kirillov, p. 40): Let $V, W$ be representations of $G$ (respectively, $\mathfrak{g}$). Then $V \otimes W$ has a canonical structure of a representation.

For the group: $\rho(g)(v \otimes w) = \rho(g)v \otimes \rho(g)w$.

For the Lie algebra, the naive formula $\rho(x)v \otimes \rho(x)w$ does not work (it is not linear in $x$). Instead, by differentiating the group action using the Leibniz rule:

$$\rho(x)(v \otimes w) = \rho(x)v \otimes w + v \otimes \rho(x)w.$$

# Prerequisites

- **Representation of a Lie group** — The objects being tensored
- **Representation of a Lie algebra** — Needed to understand the Leibniz rule action

# Key Properties

1. $\dim(V \otimes W) = \dim V \cdot \dim W$
2. $\chi_{V \otimes W} = \chi_V \cdot \chi_W$ (Lemma 4.42)
3. The Lie algebra action follows the Leibniz rule (product rule)
4. As a corollary, any tensor space $V^{\otimes k} \otimes (V^*)^{\otimes l}$ is a representation
5. The tensor product is associative and commutative (up to natural isomorphism)

# Construction / Recognition

## To Construct:
1. Form the vector space $V \otimes W$
2. For group action: $g \cdot (v \otimes w) = (g \cdot v) \otimes (g \cdot w)$
3. For algebra action: $x \cdot (v \otimes w) = (x \cdot v) \otimes w + v \otimes (x \cdot w)$

# Context & Application

Tensor products allow constructing new representations from old ones. They are essential for describing multi-particle systems in physics and for constructing higher representations from fundamental ones. Decomposing tensor products into irreducibles (Clebsch-Gordan decomposition) is a central problem.

# Examples

**Example 4.21** (p. 42): The tensor product $\mathbb{C}^n \otimes \mathbb{C}^n$ of the standard representation of $GL(n, \mathbb{C})$ with itself decomposes as $S^2\mathbb{C}^n \oplus \Lambda^2\mathbb{C}^n$.

**Example 4.11** (p. 40): $\mathrm{End}(V) \simeq V \otimes V^*$ is a representation with action $g: A \mapsto \rho(g)A\rho(g^{-1})$.

# Relationships

## Builds Upon
- **Representation of a Lie group** — The objects being combined

## Enables
- **Hom space as representation** — $\mathrm{Hom}(V, W) \simeq V^* \otimes W$
- **Decomposition problems** — Clebsch-Gordan type decompositions

## Contrasts With
- **Direct sum of representations** — Additive vs. multiplicative; dimensions add vs. multiply

# Common Errors

- **Error**: Using $\rho(x)(v \otimes w) = \rho(x)v \otimes \rho(x)w$ for the Lie algebra action.
  **Correction**: Must use the Leibniz rule: $\rho(x)(v \otimes w) = \rho(x)v \otimes w + v \otimes \rho(x)w$.

# Common Confusions

- **Confusion**: Thinking the group and algebra actions on tensor products are defined by the same formula.
  **Clarification**: The group action is multiplicative ($g$ acts on both factors), while the algebra action uses the Leibniz/product rule.

# Source Reference

Chapter 4, Section 4.2, Lemma 4.10, pp. 40-41.

# Verification Notes

- Definition source: Direct from Lemma 4.10, p. 40
- Confidence rationale: Explicit construction with derivation from group action
- Uncertainties: None
- Cross-reference status: Verified
