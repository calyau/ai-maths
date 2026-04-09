---
# === CORE IDENTIFICATION ===
concept: Irreducible Representation
slug: irreducible-representation

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
  - "simple representation"
  - "irrep"
  - "simple module"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - representation-of-lie-group
  - subrepresentation
extends: []
related:
  - completely-reducible-representation
  - schur-lemma
  - character-of-representation
contrasts_with:
  - completely-reducible-representation
  - reducible-representation

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an irreducible representation?"
  - "How do I determine whether a representation is irreducible?"
---

# Quick Definition

A non-zero representation $V$ is irreducible (or simple) if it has no subrepresentations other than $\{0\}$ and $V$ itself. Irreducible representations are the building blocks for all representations.

# Core Definition

**Definition 4.15** (Kirillov, p. 41): A non-zero representation $V$ of $G$ or $\mathfrak{g}$ is called irreducible or simple if it has no subrepresentations other than $0$, $V$. Otherwise $V$ is called reducible.

# Prerequisites

- **Representation of a Lie group** — The object being tested for irreducibility
- **Subrepresentation** — Irreducibility is defined in terms of subrepresentations

# Key Properties

1. One-dimensional representations are always irreducible
2. For compact groups, any representation decomposes into irreducibles (Theorem 4.38)
3. $V$ is irreducible iff $(\chi_V, \chi_V) = 1$ (Corollary 4.44)
4. By Schur's lemma, $\mathrm{Hom}_G(V, V) = \mathbb{C} \cdot \mathrm{id}$ for irreducible $V$
5. Irreducible representations of commutative groups are one-dimensional (Proposition 4.25)

# Construction / Recognition

## To Identify/Recognize:
1. Show that no proper non-zero subspace is invariant under the action
2. Alternatively, for compact groups: compute $(\chi_V, \chi_V)$ and check if it equals 1
3. For a commutative group: check if $V$ is one-dimensional

## To Construct:
1. For $SL(n, \mathbb{C})$: $\mathbb{C}^n$ is irreducible (Example 4.16)
2. For $\mathfrak{sl}(2, \mathbb{C})$: the representations $V_n$ of dimension $n+1$ (Theorem 5.6)

# Context & Application

The classification of irreducible representations is the central problem of representation theory. For compact and semisimple groups, every representation is a direct sum of irreducibles, so knowing the irreducibles gives complete information. The approach: (1) classify irreducibles, (2) decompose arbitrary representations into irreducibles.

# Examples

**Example 4.16** (p. 41): $\mathbb{C}^n$ is irreducible as a representation of $SL(n, \mathbb{C})$.

**Example 4.18** (p. 42): The only irreducible representations of $\mathbb{R}$ are one-dimensional, of the form $t \mapsto e^{\lambda t}$ for $\lambda \in \mathbb{C}$.

**Example 4.26** (p. 44): Irreducible representations of $S^1 = \mathbb{R}/\mathbb{Z}$ are $V_k$, $k \in \mathbb{Z}$, with action $\rho(a) = e^{2\pi ika}$.

# Relationships

## Builds Upon
- **Subrepresentation** — Irreducibility is defined by absence of proper subrepresentations

## Enables
- **Schur's lemma** — Fundamental result about intertwiners of irreducibles
- **Character theory** — Characters distinguish irreducible representations
- **Classification of sl(2,C) representations** — All irreducibles classified

## Contrasts With
- **Completely reducible representation** — A direct sum of irreducibles (may not be irreducible itself)
- **Reducible representation** — Has a proper non-trivial subrepresentation

# Common Errors

- **Error**: Assuming a reducible representation automatically decomposes as a direct sum.
  **Correction**: A representation can be reducible without being completely reducible (Example 4.18: representations of $\mathbb{R}$ corresponding to non-diagonalizable matrices).

# Common Confusions

- **Confusion**: Conflating "irreducible" with "indecomposable."
  **Clarification**: Indecomposable means cannot be written as a direct sum; irreducible means no proper non-zero subrepresentation. Irreducible implies indecomposable, but not conversely in general.

# Source Reference

Chapter 4, Section 4.3, Definition 4.15, pp. 41-42.

# Verification Notes

- Definition source: Direct from Definition 4.15, p. 41
- Confidence rationale: Explicit definition with examples
- Uncertainties: None
- Cross-reference status: Verified
