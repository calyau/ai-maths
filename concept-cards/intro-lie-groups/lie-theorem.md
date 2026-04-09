---
# === CORE IDENTIFICATION ===
concept: Lie Theorem
slug: lie-theorem

# === CLASSIFICATION ===
category: structure-theory
subcategory: solvable-nilpotent
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Structure Theory of Lie Algebras"
chapter_number: 6
pdf_page: 69
section: "6.3. Lie and Engel theorems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Lie's theorem"
  - "Lie theorem on solvable algebras"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - solvable-lie-algebra
  - representation-lie-algebra
extends: []
related:
  - common-eigenvector
  - engel-theorem
  - cartan-criterion-solvability
contrasts_with:
  - engel-theorem

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does Lie's theorem say about representations of solvable Lie algebras?"
  - "How can representations of solvable algebras be simplified?"
---

# Quick Definition

Lie's theorem states that every complex representation of a solvable Lie algebra can be put in upper-triangular form. Equivalently, there always exists a common eigenvector for the entire algebra.

# Core Definition

**Theorem 6.14** (Kirillov, p. 69): Let $\rho\colon \mathfrak{g} \to \mathfrak{gl}(V)$ be a complex representation of a solvable Lie algebra $\mathfrak{g}$. Then there exists a basis in $V$ such that in this basis, all operators $\rho(x)$ are upper-triangular.

The key step is **Proposition 6.15**: there exists a common eigenvector $v \in V$ for all $\rho(x)$, $x \in \mathfrak{g}$.

# Prerequisites

- **Solvable Lie algebra** — The theorem applies specifically to solvable algebras
- **Representation of a Lie algebra** — The statement is about representations

# Key Properties

1. The theorem requires complex representations (or algebraically closed ground field)
2. The proof proceeds by induction on $\dim \mathfrak{g}$, using the fact that solvable algebras have codimension-1 ideals
3. The common eigenvector is found by constructing a stable subspace

# Construction / Recognition

## To Apply Lie's Theorem:
1. Verify $\mathfrak{g}$ is solvable
2. Find a common eigenvector $v$ (Proposition 6.15)
3. Pass to $V/\mathbb{C}v$ and repeat by induction on $\dim V$
4. The resulting basis makes all $\rho(x)$ upper-triangular

# Context & Application

Lie's theorem is the fundamental structure theorem for representations of solvable Lie algebras. It is the Lie algebra analog of the fact that any single operator over $\mathbb{C}$ can be put in upper-triangular form. Its corollaries include that all irreducible representations of solvable algebras are 1-dimensional.

# Examples

**Corollary 6.16** (p. 70):
1. Any irreducible representation of a solvable Lie algebra is 1-dimensional.
2. If $\mathfrak{g}$ is complex and solvable, there is a chain of ideals $0 \subset I^1 \subset \cdots \subset I^n = \mathfrak{g}$ with $I^{k+1}/I^k$ one-dimensional.
3. $\mathfrak{g}$ is solvable iff $[\mathfrak{g}, \mathfrak{g}]$ is nilpotent.

# Relationships

## Builds Upon
- **Solvable Lie algebra** — The hypothesis of the theorem

## Enables
- **Cartan criterion (solvability)** — Uses Lie theorem in its proof
- **Common eigenvector** — Key intermediate result (Proposition 6.15)

## Contrasts With
- **Engel theorem** — Analogous result for nilpotent algebras; gives strictly upper-triangular form

# Common Errors

- **Error**: Applying Lie's theorem over $\mathbb{R}$
  **Correction**: The theorem requires complex representations (or algebraically closed field); real representations may not admit upper-triangular form

# Common Confusions

- **Confusion**: Expecting Lie's theorem to give diagonal form
  **Clarification**: It gives upper-triangular, not diagonal. Diagonal form would require semisimplicity of the operators, which solvable algebras do not guarantee.

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.3, pages 69-70. Theorem 6.14, Proposition 6.15, Corollary 6.16.

# Verification Notes

- Definition source: Direct from Theorem 6.14
- Confidence rationale: Major named theorem with complete proof in source
- Uncertainties: None
- Cross-reference status: Verified
