---
# === CORE IDENTIFICATION ===
concept: Completely Reducible Representation
slug: completely-reducible-representation

# === CLASSIFICATION ===
category: representations
subcategory: irreducibility
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of Lie Groups and Lie Algebras"
chapter_number: 4
pdf_page: 41
section: "4.3 Irreducible representations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "semisimple representation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - irreducible-representation
  - direct-sum-of-representations
extends: []
related:
  - unitary-representation
  - character-of-representation
contrasts_with:
  - irreducible-representation

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I decompose a representation into irreducibles?"
  - "What is a completely reducible representation?"
---

# Quick Definition

A representation is completely reducible (or semisimple) if it is isomorphic to a direct sum of irreducible representations. For compact groups, all finite-dimensional representations are completely reducible.

# Core Definition

**Definition 4.17** (Kirillov, p. 41): A representation is called completely reducible (or semisimple) if it is isomorphic to a direct sum of irreducible representations: $V \simeq \bigoplus V_i$, $V_i$ irreducible.

One usually groups isomorphic summands: $V \simeq \bigoplus n_i V_i$, where $V_i$ are pairwise non-isomorphic irreducible representations and $n_i \in \mathbb{Z}_+$ are called multiplicities.

# Prerequisites

- **Irreducible representation** — The building blocks of the decomposition
- **Direct sum of representations** — The operation combining irreducibles

# Key Properties

1. The multiplicities $n_i$ are uniquely determined (Corollary 4.44)
2. For compact groups, every finite-dimensional representation is completely reducible (Theorem 4.38)
3. For finite groups, every representation is completely reducible (Theorem 4.31)
4. Not every representation is completely reducible (Example 4.18: representations of $\mathbb{R}$)
5. Multiplicities can be computed via characters: $n_i = (\chi_V, \chi_{V_i})$ (Corollary 4.44)

# Construction / Recognition

## To Decompose:
1. If $V$ is unitary: find a subrepresentation $W$, then $V = W \oplus W^\perp$ (Theorem 4.29)
2. Use central elements or Casimir operators to find eigenspace decomposition (Lemma 4.19, 4.20)
3. Compute character inner products to find multiplicities: $n_i = (\chi_V, \chi_{V_i})$

## To Identify:
1. For compact groups: always completely reducible
2. Check $(\chi_V, \chi_V) = \sum n_i^2$ (from Corollary 4.44)

# Context & Application

Complete reducibility is the foundation of the representation theory of compact and semisimple groups. It guarantees that understanding irreducible representations is sufficient to understand all representations. This fails for non-semisimple groups (e.g., $\mathbb{R}$, solvable groups).

# Examples

**Example 4.18** (p. 42): Representations of $G = \mathbb{R}$ given by $t \mapsto \exp(tA)$. Such a representation is completely reducible iff $A$ is diagonalizable (i.e., $A$ has a complete eigenbasis).

**Example 4.21** (p. 42): $\mathbb{C}^n \otimes \mathbb{C}^n = S^2\mathbb{C}^n \oplus \Lambda^2\mathbb{C}^n$ as a representation of $GL(n, \mathbb{C})$. Both summands are irreducible.

# Relationships

## Builds Upon
- **Irreducible representation** — Building blocks
- **Direct sum** — The structure of the decomposition

## Enables
- **Character theory** — Characters detect and compute multiplicities
- **Representation decomposition** — The practical goal

## Contrasts With
- **Irreducible representation** — A completely reducible representation may have multiple irreducible summands

# Common Errors

- **Error**: Assuming a representation is completely reducible just because it has a subrepresentation.
  **Correction**: Having a subrepresentation $W$ does not guarantee a complementary invariant subspace $V/W$. Complete reducibility requires that every subrepresentation has an invariant complement.

# Common Confusions

- **Confusion**: Thinking "reducible" and "completely reducible" are synonyms.
  **Clarification**: "Reducible" means there exists a non-trivial subrepresentation. "Completely reducible" means the representation splits as a direct sum of irreducibles. A representation can be reducible but not completely reducible.

# Source Reference

Chapter 4, Section 4.3, Definition 4.17, pp. 41-42.

# Verification Notes

- Definition source: Direct from Definition 4.17, p. 41
- Confidence rationale: Explicit definition with counterexample
- Uncertainties: None
- Cross-reference status: Verified
