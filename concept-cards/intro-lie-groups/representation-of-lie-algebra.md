---
# === CORE IDENTIFICATION ===
concept: Representation of a Lie Algebra
slug: representation-of-lie-algebra

# === CLASSIFICATION ===
category: representations
subcategory: basic-definitions
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of Lie Groups and Lie Algebras"
chapter_number: 4
pdf_page: 38
section: "4.1 Basic definitions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Lie algebra representation"
  - "g-module"
  - "module over a Lie algebra"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-algebra
extends: []
related:
  - representation-of-lie-group
  - intertwining-operator
  - universal-enveloping-algebra
contrasts_with:
  - representation-of-lie-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a representation of a Lie algebra?"
  - "How does a Lie algebra act on a vector space?"
---

# Quick Definition

A representation of a Lie algebra $\mathfrak{g}$ is a vector space $V$ together with a Lie algebra homomorphism $\rho: \mathfrak{g} \to \mathfrak{gl}(V)$. Equivalently, it is a $\mathfrak{g}$-module.

# Core Definition

**Definition 4.1** (Kirillov, p. 38): A representation of a Lie algebra $\mathfrak{g}$ is a vector space $V$ together with a morphism $\rho: \mathfrak{g} \to \mathfrak{gl}(V)$.

The morphism $\rho$ must be a Lie algebra homomorphism: $\rho([x,y]) = \rho(x)\rho(y) - \rho(y)\rho(x)$ for all $x, y \in \mathfrak{g}$. For a real Lie algebra with a complex representation, $\rho$ is required to be $\mathbb{R}$-linear.

The notion of representation is completely parallel to the notion of module over an associative ring; using the word "module" rather than "representation" for Lie algebras is common (Remark, p. 38).

# Prerequisites

This is a foundational concept. Background assumed:
- **Lie algebra** — the algebraic structure being represented
- Knowledge of $\mathfrak{gl}(V)$ as a Lie algebra of endomorphisms

# Key Properties

1. The map $\rho$ preserves the Lie bracket: $\rho([x,y]) = [\rho(x), \rho(y)]$
2. Categories of complex representations of a real Lie algebra $\mathfrak{g}$ and its complexification $\mathfrak{g}^{\mathbb{C}}$ are equivalent (Lemma 4.4)
3. Every representation of a Lie group $G$ gives a representation of $\mathfrak{g}$ by differentiation
4. If $G$ is connected and simply connected, representations of $\mathfrak{g}$ lift uniquely to representations of $G$ (Theorem 4.3)

# Construction / Recognition

## To Construct:
1. Choose a vector space $V$
2. For each basis element $x_i$ of $\mathfrak{g}$, define a linear operator $\rho(x_i) \in \mathfrak{gl}(V)$
3. Extend linearly to all of $\mathfrak{g}$
4. Verify the bracket relation: $\rho([x_i, x_j]) = [\rho(x_i), \rho(x_j)]$ for all basis elements

## To Identify/Recognize:
1. Check that $V$ is a vector space with a $\mathfrak{g}$-action
2. Verify linearity of the action: $\rho(ax + by) = a\rho(x) + b\rho(y)$
3. Verify the bracket relation holds

# Context & Application

Lie algebra representations are often more tractable than Lie group representations because $\mathfrak{g}$ is a vector space. The equivalence with group representations (for simply connected groups) means one can work with the linear algebraic setting of Lie algebras and lift results to groups.

# Examples

**Example 4.5** (p. 39): The categories of representations of $SL(2, \mathbb{C})$, $SU(2)$, $\mathfrak{sl}(2, \mathbb{C})$, and $\mathfrak{su}(2)$ are all equivalent. This allows reducing the study of representations of the non-compact group $SL(2, \mathbb{C})$ to the compact group $SU(2)$.

**Example** (p. 39): A representation of $\mathfrak{su}(2)$ is a vector space $V$ with three endomorphisms $X, Y, Z$ satisfying $XY - YX = Z$, $YZ - ZY = X$, $ZX - XZ = Y$.

# Relationships

## Builds Upon
- **Lie algebra** — The structure being represented

## Enables
- **Universal enveloping algebra** — Converts Lie algebra representations to associative algebra modules
- **Weight decomposition** — Key tool for studying $\mathfrak{sl}(2,\mathbb{C})$ representations

## Related
- **Representation of a Lie group** — Group-level version, related by differentiation

## Contrasts With
- **Representation of a Lie group** — Uses group homomorphism to $GL(V)$ rather than Lie algebra homomorphism to $\mathfrak{gl}(V)$

# Common Errors

- **Error**: Defining the action on a tensor product as $\rho(x)(v \otimes w) = \rho(x)v \otimes \rho(x)w$.
  **Correction**: The correct formula uses the Leibniz rule: $\rho(x)(v \otimes w) = \rho(x)v \otimes w + v \otimes \rho(x)w$.

# Common Confusions

- **Confusion**: Assuming representations of a Lie algebra always correspond to representations of the associated Lie group.
  **Clarification**: This only holds when the group is connected and simply connected. For non-simply-connected groups (e.g., $SO(3, \mathbb{R})$), only some Lie algebra representations lift to group representations.

# Source Reference

Chapter 4: Representations of Lie Groups and Lie Algebras, Section 4.1 "Basic definitions," pages 38-40. Definition 4.1, Theorem 4.3, Lemma 4.4.

# Verification Notes

- Definition source: Direct from Definition 4.1, p. 38
- Confidence rationale: Explicit definition with clear terminology
- Uncertainties: None
- Cross-reference status: Slugs verified against planned extractions
