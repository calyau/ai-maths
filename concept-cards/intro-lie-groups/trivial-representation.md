---
# === CORE IDENTIFICATION ===
concept: Trivial Representation
slug: trivial-representation

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
pdf_page: 39
section: "4.1 Basic definitions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "trivial module"
  - "scalar representation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - representation-of-lie-group
extends: []
related:
  - invariant-vectors
  - character-of-representation
contrasts_with:
  - adjoint-representation-of-lie-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the trivial representation?"
---

# Quick Definition

The trivial representation is the one-dimensional representation $V = \mathbb{C}$ where every group element acts as the identity (or every Lie algebra element acts as zero).

# Core Definition

**Example 4.7** (Kirillov, p. 39): Trivial representation: $V = \mathbb{C}$, $\rho(g) = \mathrm{id}$ for any $g \in G$ (respectively, $\rho(x) = 0$ for any $x \in \mathfrak{g}$).

# Prerequisites

- **Representation of a Lie group** — The trivial representation is the simplest example

# Key Properties

1. It is one-dimensional: $V = \mathbb{C}$
2. Every group element acts trivially: $\rho(g) = \mathrm{id}$
3. Every Lie algebra element acts as zero: $\rho(x) = 0$
4. Its character is $\chi_V = 1$ (Lemma 4.42)
5. It is irreducible (one-dimensional representations are always irreducible)
6. $\mathrm{Hom}_G(\mathbb{C}, V) \cong V^G$, the space of invariant vectors (Example 4.13)

# Construction / Recognition

## To Construct:
1. Take $V = \mathbb{C}$
2. Define $\rho(g) = \mathrm{id}$ for all $g \in G$

## To Identify/Recognize:
1. Check that $V$ is one-dimensional
2. Check that every group element acts as the identity

# Context & Application

The trivial representation serves as the "unit" for tensor products in representation theory. Invariant vectors in a representation $V$ correspond to copies of the trivial representation inside $V$. The natural pairing $V \otimes V^* \to \mathbb{C}$ is a morphism when $\mathbb{C}$ carries the trivial representation.

# Examples

**Example 4.7** (p. 39): For any Lie group $G$, $V = \mathbb{C}$ with $\rho(g) = \mathrm{id}$ is the trivial representation.

# Relationships

## Builds Upon
- **Representation of a Lie group** — Simplest instance

## Enables
- **Invariant vectors** — $V^G = \mathrm{Hom}_G(\mathbb{C}, V)$
- **Dual representation** — Defined via the pairing $V \otimes V^* \to \mathbb{C}$

## Contrasts With
- **Adjoint representation** — A non-trivial representation that exists for any non-abelian group

# Common Confusions

- **Confusion**: Thinking the trivial representation is uninteresting.
  **Clarification**: Invariant vectors, which are central to many applications, are precisely the copies of the trivial representation within a given representation.

# Source Reference

Chapter 4: Representations of Lie Groups and Lie Algebras, Section 4.1, Example 4.7, p. 39.

# Verification Notes

- Definition source: Direct from Example 4.7, p. 39
- Confidence rationale: Explicit example with clear definition
- Uncertainties: None
- Cross-reference status: Verified
