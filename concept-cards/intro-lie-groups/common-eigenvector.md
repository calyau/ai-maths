---
# === CORE IDENTIFICATION ===
concept: Common Eigenvector
slug: common-eigenvector

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
  - "simultaneous eigenvector"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - solvable-lie-algebra
  - representation-lie-algebra
extends: []
related:
  - lie-theorem
  - weight-decomposition
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When does a family of operators have a common eigenvector?"
  - "Why do representations of solvable algebras have common eigenvectors?"
---

# Quick Definition

A common eigenvector for a representation $\rho$ of a Lie algebra $\mathfrak{g}$ is a nonzero vector $v \in V$ satisfying $\rho(x)v = \lambda(x)v$ for all $x \in \mathfrak{g}$. Proposition 6.15 guarantees existence for solvable algebras over $\mathbb{C}$.

# Core Definition

**Proposition 6.15** (Kirillov, p. 69): Let $\rho\colon \mathfrak{g} \to \mathfrak{gl}(V)$ be a complex representation of a solvable Lie algebra $\mathfrak{g}$. Then there exists $v \in V$ which is a common eigenvector of all $\rho(x)$, $x \in \mathfrak{g}$: $\rho(x)v = \lambda(x)v$ for some linear functional $\lambda\colon \mathfrak{g} \to \mathbb{C}$.

# Prerequisites

- **Solvable Lie algebra** — The existence result requires solvability
- **Representation of a Lie algebra** — The setting is a representation

# Key Properties

1. The eigenvalue $\lambda$ is a linear functional on $\mathfrak{g}$
2. $\lambda$ vanishes on $[\mathfrak{g}, \mathfrak{g}]$ (since trace of a commutator is zero)
3. The proof uses induction on $\dim \mathfrak{g}$ and the fact that $[\mathfrak{g}, \mathfrak{g}] \neq \mathfrak{g}$

# Construction / Recognition

## To Find:
1. Since $\mathfrak{g}$ is solvable, choose a codimension-1 ideal $\mathfrak{g}' \supset [\mathfrak{g}, \mathfrak{g}]$
2. By induction, find a common eigenvector $v$ for $\mathfrak{g}'$
3. Construct the stable subspace $W = \operatorname{span}(v, \rho(x)v, \rho(x)^2 v, \ldots)$
4. Show $W$ is stable under $\mathfrak{g}'$ and find an eigenvector for $x$ in $W$

# Context & Application

The existence of a common eigenvector is the key step in proving Lie's theorem. It generalizes the fact that a single operator over $\mathbb{C}$ always has an eigenvector. The proof technique — working with a codimension-1 ideal and a stable subspace — is a prototype for many arguments in representation theory.

# Examples

**From proof** (p. 69): For $\mathfrak{g}' \subset \mathfrak{g}$ of codimension 1, after finding $v$ with $\rho(h)v = \lambda(h)v$ for all $h \in \mathfrak{g}'$, the space $W = \operatorname{span}(v, \rho(x)v, \ldots)$ satisfies $\rho(h)v^k = \lambda(h)v^k + \text{lower terms}$, so $\operatorname{tr}_W \rho(h) = (n+1)\lambda(h)$. This forces $\lambda([h,x]) = 0$.

# Relationships

## Builds Upon
- **Solvable Lie algebra** — Existence requires solvability

## Enables
- **Lie theorem** — The common eigenvector is the inductive step

## Related
- **Weight decomposition** — Common eigenvectors generalize to weight spaces for semisimple algebras

# Common Errors

- **Error**: Assuming common eigenvectors exist for non-solvable algebras
  **Correction**: For semisimple algebras, one gets simultaneous eigenspaces for a Cartan subalgebra, not for the whole algebra

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.3, pages 69-70. Proposition 6.15.

# Verification Notes

- Definition source: Direct from Proposition 6.15
- Confidence rationale: Explicit proposition with detailed proof
- Uncertainties: None
- Cross-reference status: Verified
