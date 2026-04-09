---
# === CORE IDENTIFICATION ===
concept: Decomposition Using Central Elements
slug: decomposition-using-central-elements

# === CLASSIFICATION ===
category: representations
subcategory: irreducibility
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of Lie Groups and Lie Algebras"
chapter_number: 4
pdf_page: 42
section: "4.3 Irreducible representations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - schur-lemma
  - intertwining-operator
extends:
  - schur-lemma
related:
  - casimir-operator
  - completely-reducible-representation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I decompose a representation into irreducibles?"
  - "How can central elements help decompose representations?"
---

# Quick Definition

If a diagonalizable operator commutes with the group action (e.g., a central element), its eigenspaces are subrepresentations, providing a decomposition of the representation.

# Core Definition

**Lemma 4.19** (Kirillov, p. 42): Let $V$ be a representation of $G$ (resp. $\mathfrak{g}$) and $A: V \to V$ a diagonalizable intertwining operator. Let $V^\lambda \subset V$ be the eigenspace for $A$ with eigenvalue $\lambda$. Then each $V^\lambda$ is a subrepresentation, so $V = \bigoplus V^\lambda$ as a representation.

**Lemma 4.20** (p. 42): Let $Z \in Z(G)$ be a central element such that $\rho(Z)$ is diagonalizable. Then $V = \bigoplus V^\lambda$ where $V^\lambda$ is the eigenspace for $\rho(Z)$ with eigenvalue $\lambda$. Similarly for central elements in $\mathfrak{g}$.

# Prerequisites

- **Schur's lemma** — Guarantees central elements act as scalars on irreducibles
- **Intertwining operator** — Central elements are intertwining operators

# Key Properties

1. Eigenspaces of intertwining operators are subrepresentations
2. Central elements of $G$ or $\mathfrak{g}$ always give intertwining operators
3. The Casimir operator is a central element in $U\mathfrak{g}$ useful for decomposition
4. No guarantee that eigenspaces are irreducible

# Construction / Recognition

## To Apply:
1. Find a central element $Z$ in the group or algebra (or in $U\mathfrak{g}$)
2. Compute $\rho(Z)$ in the representation
3. Diagonalize $\rho(Z)$
4. Each eigenspace is a subrepresentation
5. Repeat with additional central elements to refine

# Examples

**Example 4.21** (p. 42): For $GL(n, \mathbb{C})$ acting on $\mathbb{C}^n \otimes \mathbb{C}^n$, the permutation operator $P: v \otimes w \mapsto w \otimes v$ commutes with the action. Its eigenspaces $S^2\mathbb{C}^n$ and $\Lambda^2\mathbb{C}^n$ give the decomposition $\mathbb{C}^n \otimes \mathbb{C}^n = S^2\mathbb{C}^n \oplus \Lambda^2\mathbb{C}^n$.

# Relationships

## Builds Upon
- **Schur's lemma** — Why central elements act as scalars on irreducibles

## Enables
- **Casimir operator decomposition** — Specific application using the Casimir element

# Source Reference

Chapter 4, Section 4.3, Lemmas 4.19-4.20, Example 4.21, p. 42.

# Verification Notes

- Definition source: Direct from Lemmas 4.19-4.20, p. 42
- Confidence rationale: Explicit lemma statements
- Uncertainties: None
- Cross-reference status: Verified
