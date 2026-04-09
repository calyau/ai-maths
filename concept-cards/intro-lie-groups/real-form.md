---
# === CORE IDENTIFICATION ===
concept: Real Form
slug: real-form

# === CLASSIFICATION ===
category: lie-algebras
subcategory: definitions
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups and Lie Algebras"
chapter_number: 3
pdf_page: 33
section: "3.9"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - complexification
extends: []
related:
  - compact-real-form
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do the classical groups relate to each other?"
---

# Quick Definition

A real form of a complex Lie algebra $\mathfrak{g}_\mathbb{C}$ is a real Lie algebra $\mathfrak{g}$ such that $\mathfrak{g}_\mathbb{C} = \mathfrak{g} \otimes_\mathbb{R} \mathbb{C}$. A real form of a complex Lie group $G$ is a real Lie subgroup $K$ whose Lie algebra is a real form of $\mathrm{Lie}(G)$.

# Core Definition

**Definition 3.51** (Kirillov): $\mathfrak{g}$ is a real form of $\mathfrak{g}_\mathbb{C}$ when $\mathfrak{g}_\mathbb{C} = \mathfrak{g} \otimes_\mathbb{R} \mathbb{C}$.

**Definition 3.53** (Kirillov): Let $G$ be a connected complex Lie group. A real Lie subgroup $K \subset G$ such that $\mathfrak{k} = \mathrm{Lie}(K)$ is a real form of $\mathfrak{g}$ is called a real form of $G$.

# Prerequisites

- **Complexification** — the operation whose "inverse" gives a real form

# Key Properties

1. A complex algebra can have multiple non-isomorphic real forms.
2. Every real form of $\mathfrak{g}_\mathbb{C}$ can be realized as the Lie algebra of a real subgroup of $G$ (Exercise 3.15).
3. Complexification is trivial at the algebra level but highly nontrivial at the group level: $G$ and $K$ may have very different topology.

# Construction / Recognition

## To Construct/Create:
1. Given a complex Lie algebra $\mathfrak{g}_\mathbb{C}$, find a real subalgebra $\mathfrak{g} \subset \mathfrak{g}_\mathbb{C}$ with $\mathfrak{g}_\mathbb{C} = \mathfrak{g} \oplus i\mathfrak{g}$.

## To Identify/Recognize:
1. A real Lie algebra whose complexification gives the given complex algebra.

# Context & Application

Real forms connect topologically different groups (compact and non-compact) that share algebraic properties. This is used to transfer results between, e.g., $\mathrm{SU}(n)$ and $\mathrm{SL}(n, \mathbb{R})$.

# Examples

**Example** (p. 33-34): Both $\mathfrak{sl}(n, \mathbb{R})$ and $\mathfrak{su}(n)$ are real forms of $\mathfrak{sl}(n, \mathbb{C})$.

**Example** (Exercise 3.17): $\mathfrak{so}(p, q)_\mathbb{C} = \mathfrak{so}(p+q, \mathbb{C})$, so $\mathfrak{so}(p, q)$ is a real form of $\mathfrak{so}(p+q, \mathbb{C})$.

# Relationships

## Builds Upon
- **Complexification** — real forms are the "fibers" of complexification

## Enables
- **Transfer of algebraic properties** — between different real forms

## Related
- **Compact real form** — a distinguished real form

# Common Errors

- **Error**: Assuming a complex algebra has a unique real form.
  **Correction**: There can be many non-isomorphic real forms. E.g., $\mathfrak{sl}(2, \mathbb{C})$ has real forms $\mathfrak{sl}(2, \mathbb{R})$, $\mathfrak{su}(2)$, and $\mathfrak{su}(1,1)$.

# Common Confusions

- **Confusion**: Whether real forms of the same complex algebra are isomorphic.
  **Clarification**: No. $\mathfrak{su}(2)$ is compact (definite Killing form) while $\mathfrak{sl}(2, \mathbb{R})$ is not.

# Source Reference

Chapter 3: Lie Groups and Lie Algebras, Section 3.9, Definitions 3.51, 3.53, pages 33-34.

# Verification Notes

- Definition source: Direct from Definitions 3.51 and 3.53
- Confidence rationale: Explicit definitions
- Uncertainties: None
- Cross-reference status: Verified with examples
