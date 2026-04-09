---
# === CORE IDENTIFICATION ===
concept: Subrepresentation
slug: subrepresentation

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
aliases:
  - "invariant subspace"
  - "sub-module"
  - "G-invariant subspace"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - representation-of-lie-group
extends: []
related:
  - irreducible-representation
  - quotient-representation
  - direct-sum-of-representations
contrasts_with:
  - irreducible-representation

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a subrepresentation?"
  - "What does it mean for a subspace to be invariant under a group action?"
---

# Quick Definition

A subrepresentation of a representation $V$ is a vector subspace $W \subset V$ that is stable (invariant) under the group or algebra action.

# Core Definition

**Definition 4.9** (Kirillov, p. 40): Let $V$ be a representation of $G$ (respectively $\mathfrak{g}$). A subrepresentation is a vector subspace $W \subset V$ stable under the action: $\rho(g)W \subset W$ for all $g \in G$ (respectively, $\rho(x)W \subset W$ for all $x \in \mathfrak{g}$).

If $G$ is a connected Lie group with Lie algebra $\mathfrak{g}$, then $W \subset V$ is a subrepresentation for $G$ if and only if it is a subrepresentation for $\mathfrak{g}$.

# Prerequisites

- **Representation of a Lie group** — The ambient structure containing the subrepresentation

# Key Properties

1. $W$ is itself a representation of $G$ (or $\mathfrak{g}$) with the restricted action
2. The quotient $V/W$ inherits a canonical representation structure (the quotient representation)
3. Every representation has the trivial subrepresentations $\{0\}$ and $V$ itself
4. For connected groups, $G$-invariance is equivalent to $\mathfrak{g}$-invariance

# Construction / Recognition

## To Identify/Recognize:
1. Choose a subspace $W \subset V$
2. Verify $\rho(g)w \in W$ for all $g \in G$ and $w \in W$
3. For Lie algebras: verify $\rho(x)w \in W$ for all $x \in \mathfrak{g}$ and $w \in W$

# Context & Application

Subrepresentations are the key to decomposing representations. Finding subrepresentations is the first step in breaking a representation into simpler pieces. A representation with no non-trivial subrepresentations is irreducible.

# Examples

**Example 4.21** (p. 42): In the representation $\mathbb{C}^n \otimes \mathbb{C}^n$ of $GL(n, \mathbb{C})$, the spaces $S^2\mathbb{C}^n$ (symmetric tensors) and $\Lambda^2\mathbb{C}^n$ (antisymmetric tensors) are subrepresentations.

# Relationships

## Enables
- **Irreducible representation** — Defined as having no non-trivial subrepresentations
- **Quotient representation** — $V/W$ is a representation when $W$ is a subrepresentation
- **Complete reducibility** — Decomposition into irreducible subrepresentations

## Contrasts With
- **Irreducible representation** — An irreducible representation has no proper non-zero subrepresentations

# Common Confusions

- **Confusion**: Thinking every subspace of a representation is a subrepresentation.
  **Clarification**: Only invariant subspaces are subrepresentations. Most subspaces are not invariant.

# Source Reference

Chapter 4, Section 4.2, Definition 4.9, p. 40.

# Verification Notes

- Definition source: Direct from Definition 4.9, p. 40
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
