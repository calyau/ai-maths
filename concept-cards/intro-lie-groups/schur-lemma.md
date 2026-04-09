---
# === CORE IDENTIFICATION ===
concept: "Schur's Lemma"
slug: schur-lemma

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
pdf_page: 42
section: "4.4 Intertwining operators and Schur lemma"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Schur lemma"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - irreducible-representation
  - intertwining-operator
extends: []
related:
  - character-of-representation
  - casimir-operator
  - decomposition-using-central-elements
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does Schur's lemma say about morphisms between irreducible representations?"
  - "Why is every intertwining operator on an irreducible representation a scalar?"
---

# Quick Definition

Schur's lemma states that (1) every endomorphism of an irreducible complex representation is a scalar multiple of the identity, and (2) every morphism between non-isomorphic irreducible representations is zero.

# Core Definition

**Lemma 4.22 (Schur Lemma)** (Kirillov, p. 43):

1. Let $V$ be an irreducible complex representation of $G$. Then $\mathrm{Hom}_G(V, V) = \mathbb{C}\,\mathrm{id}$: any endomorphism of an irreducible representation is constant.
2. If $V$ and $W$ are irreducible complex representations which are not isomorphic, then $\mathrm{Hom}_G(V, W) = 0$.

Similar results hold for representations of a Lie algebra $\mathfrak{g}$.

**Proof sketch**: If $\Phi: V \to W$ is an intertwiner, then $\ker \Phi$ and $\mathrm{Im}\, \Phi$ are subrepresentations. By irreducibility, $\Phi$ is either zero or an isomorphism. For part (1): if $\lambda$ is an eigenvalue of $\Phi$, then $\Phi - \lambda\,\mathrm{id}$ is a non-invertible intertwiner, hence zero.

# Prerequisites

- **Irreducible representation** — Schur's lemma applies specifically to irreducible representations
- **Intertwining operator** — The maps constrained by the lemma

# Key Properties

1. Any intertwiner between irreducible representations is either zero or an isomorphism
2. Over $\mathbb{C}$: endomorphisms of irreducibles are scalars (uses existence of eigenvalues)
3. Over $\mathbb{R}$: the conclusion is weaker (endomorphisms form a division algebra)
4. Immediate consequence: irreducible representations of commutative groups are 1-dimensional (Proposition 4.25)

# Construction / Recognition

## To Apply:
1. Identify that the source and target are irreducible representations
2. If non-isomorphic: the intertwiner must be zero
3. If the same irreducible: the intertwiner is $\lambda \cdot \mathrm{id}$ for some $\lambda \in \mathbb{C}$
4. Find $\lambda$ by computing $\Phi(v)$ for any single non-zero vector $v$

# Context & Application

Schur's lemma is the most fundamental result in representation theory. It is used constantly:
- To prove orthogonality of characters
- To show that Casimir operators act as scalars on irreducibles
- To decompose representations using eigenspaces of central elements
- In quantum mechanics: symmetry-adapted quantum numbers correspond to eigenvalues of central operators

# Examples

**Example 4.23** (p. 43): Since $\mathbb{C}^n$ is irreducible as a representation of $GL(n, \mathbb{C})$, every operator commuting with $GL(n, \mathbb{C})$ is scalar. Thus $Z(GL(n, \mathbb{C})) = \{\lambda\,\mathrm{id}, \lambda \in \mathbb{C}^\times\}$ and $\mathfrak{z}(\mathfrak{gl}(n, \mathbb{C})) = \{\lambda\,\mathrm{id}, \lambda \in \mathbb{C}\}$.

**Corollary 4.24** (p. 43): If $V = \bigoplus V_i$ with $V_i$ irreducible and pairwise non-isomorphic, then any intertwining operator is $\Phi = \bigoplus \lambda_i\,\mathrm{id}_{V_i}$.

**Proposition 4.25** (p. 44): If $G$ is commutative, every irreducible complex representation is one-dimensional.

# Relationships

## Builds Upon
- **Irreducible representation** — The hypothesis of the lemma
- **Intertwining operator** — The maps being constrained

## Enables
- **Orthogonality of characters** — Proved using Schur's lemma
- **Decomposition using central elements** — Central elements act as scalars on irreducibles
- **Casimir operator** — Acts as scalar on irreducibles by Schur's lemma
- **Peter-Weyl theorem** — Orthogonality of matrix coefficients follows from Schur

## Related
- **Character of representation** — Characters detect isomorphism classes of irreducibles

# Common Errors

- **Error**: Applying Schur's lemma over $\mathbb{R}$ and concluding endomorphisms are real scalars.
  **Correction**: Over $\mathbb{R}$, endomorphisms form a division algebra (could be $\mathbb{R}$, $\mathbb{C}$, or $\mathbb{H}$). The scalar conclusion requires working over an algebraically closed field.

# Common Confusions

- **Confusion**: Thinking Schur's lemma says non-isomorphic irreducibles are "completely different."
  **Clarification**: It says there are no non-zero intertwiners between them. They can still share properties (same dimension, similar characters restricted to subgroups, etc.).

# Source Reference

Chapter 4, Section 4.4, Lemma 4.22, pp. 42-44. Corollary 4.24, Proposition 4.25.

# Verification Notes

- Definition source: Direct from Lemma 4.22, p. 43
- Confidence rationale: Explicit statement with complete proof
- Uncertainties: None
- Cross-reference status: Verified
