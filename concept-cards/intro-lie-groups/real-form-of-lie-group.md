---
# === CORE IDENTIFICATION ===
concept: Real Form of a Lie Group
slug: real-form-of-lie-group

# === CLASSIFICATION ===
category: lie-groups
subcategory: classical-groups
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
  - real-form
  - lie-subgroup
extends:
  - real-form
related:
  - compact-real-form
  - complexification
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do the classical groups relate to each other?"
---

# Quick Definition

A real form of a connected complex Lie group $G$ is a real Lie subgroup $K \subset G$ whose Lie algebra $\mathfrak{k} = \mathrm{Lie}(K)$ is a real form of $\mathfrak{g} = \mathrm{Lie}(G)$ (i.e., $\mathfrak{g} = \mathfrak{k} \otimes_\mathbb{R} \mathbb{C}$).

# Core Definition

**Definition 3.53** (Kirillov): Let $G$ be a connected complex Lie group, $\mathfrak{g} = \mathrm{Lie}(G)$, and let $K \subset G$ be a real Lie subgroup such that $\mathfrak{k} = \mathrm{Lie}(K)$ is a real form of $\mathfrak{g}$. Then $K$ is called a real form of $G$.

# Prerequisites

- **Real form** — the Lie algebra concept
- **Lie subgroup** — $K$ is a Lie subgroup of $G$

# Key Properties

1. Every real form $\mathfrak{k} \subset \mathfrak{g}$ can be realized as $\mathrm{Lie}(K)$ for some real form $K \subset G$ (Exercise 3.15).
2. A complex group can have topologically very different real forms (e.g., $\mathrm{SU}(n)$ is compact while $\mathrm{SL}(n, \mathbb{R})$ is not).
3. Going from real to complex is more subtle: not every real group is a real form of a complex group. Complexification $G_\mathbb{C}$ can be defined but $G$ may not embed in $G_\mathbb{C}$.

# Construction / Recognition

## To Construct/Create:
1. Given a real form $\mathfrak{k}$ of $\mathfrak{g}$, define the conjugation $\theta: \mathfrak{g} \to \mathfrak{g}$ by $\theta(x + iy) = x - iy$.
2. Lift $\theta$ to an automorphism of $G$ (Exercise 3.15).
3. $K = G^\theta$ (fixed point set).

## To Identify/Recognize:
1. A real Lie subgroup of a complex group whose complexified Lie algebra equals $\mathfrak{g}$.

# Context & Application

Real forms connect compact and non-compact groups that share algebraic properties. This is used for "Weyl's unitary trick" in representation theory.

# Examples

**Example 3.54** (p. 34): $\mathrm{SU}(n)$ is a compact real form of $\mathrm{SL}(n, \mathbb{C})$.

**Example**: $\mathrm{SL}(n, \mathbb{R})$ is a non-compact real form of $\mathrm{SL}(n, \mathbb{C})$.

# Relationships

## Builds Upon
- **Real form** — the Lie algebra notion

## Enables
- **Weyl's unitary trick** — transfer between compact and non-compact

## Related
- **Compact real form** — the most important special case
- **Complexification** — the inverse operation

# Common Errors

- **Error**: Assuming every real Lie group is a real form of some complex group.
  **Correction**: Some real groups cannot be obtained as real forms. The relationship is more subtle at the group level than at the algebra level.

# Common Confusions

- **Confusion**: Whether the complexification operation is trivial at the group level.
  **Clarification**: It is trivial at the algebra level ($\mathfrak{g}_\mathbb{C} = \mathfrak{g} \oplus i\mathfrak{g}$) but highly non-trivial at the group level, as the topology can change dramatically.

# Source Reference

Chapter 3: Lie Groups and Lie Algebras, Section 3.9, Definition 3.53, pages 33-34.

# Verification Notes

- Definition source: Direct from Definition 3.53
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified with Exercise 3.15, Example 3.54
