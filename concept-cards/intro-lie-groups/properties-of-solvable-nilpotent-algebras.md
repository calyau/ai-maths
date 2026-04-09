---
# === CORE IDENTIFICATION ===
concept: Properties of Solvable and Nilpotent Algebras
slug: properties-of-solvable-nilpotent-algebras

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
pdf_page: 68
section: "6.2. Solvable and nilpotent Lie algebras"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - solvable-lie-algebra
  - nilpotent-lie-algebra
extends:
  - solvable-lie-algebra
  - nilpotent-lie-algebra
related:
  - lie-theorem
  - engel-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the basic closure properties of solvable and nilpotent Lie algebras?"
  - "How are solvable and nilpotent Lie algebras related?"
---

# Quick Definition

Theorem 6.13 collects the fundamental closure properties: solvable and nilpotent Lie algebras are closed under subalgebras, quotients, complexification, and (for solvable) extensions. Every nilpotent algebra is solvable.

# Core Definition

**Theorem 6.13** (Kirillov, p. 69):
1. $\mathfrak{g}$ is solvable (resp. nilpotent) iff $\mathfrak{g}^{\mathbb{C}}$ is solvable (resp. nilpotent).
2. Subalgebras and quotients of solvable (resp. nilpotent) algebras are solvable (resp. nilpotent).
3. Nilpotent implies solvable.
4. If $I \subset \mathfrak{g}$ is an ideal with both $I$ and $\mathfrak{g}/I$ solvable, then $\mathfrak{g}$ is solvable.

# Prerequisites

- **Solvable Lie algebra** — These are properties of solvable algebras
- **Nilpotent Lie algebra** — These are properties of nilpotent algebras

# Key Properties

1. Solvability is preserved by complexification (and decomplexification)
2. The class of solvable algebras is closed under extensions (property 4)
3. The class of nilpotent algebras is NOT closed under extensions
4. Property (3) follows from $D^i\mathfrak{g} \subset D_i\mathfrak{g}$

# Construction / Recognition

## To Verify Solvability via Extension:
1. Find an ideal $I \subset \mathfrak{g}$
2. Check if $I$ is solvable
3. Check if $\mathfrak{g}/I$ is solvable
4. If both hold, $\mathfrak{g}$ is solvable

# Context & Application

Property (4) — closure under extensions — is crucial for the theory. It is used to prove the existence and uniqueness of the radical (Proposition 6.23), since the sum of two solvable ideals is again solvable.

# Examples

**Example** (p. 69): Upper-triangular matrices $\mathfrak{b}$: the ideal $\mathfrak{n}$ (strictly upper-triangular) is nilpotent (hence solvable), and $\mathfrak{b}/\mathfrak{n}$ is abelian (hence solvable), so $\mathfrak{b}$ is solvable by property (4).

# Relationships

## Builds Upon
- **Solvable Lie algebra** — States their closure properties
- **Nilpotent Lie algebra** — States their closure properties

## Enables
- **Radical** — Existence proof uses closure of solvable class under sums

# Common Errors

- **Error**: Assuming nilpotent algebras are also closed under extensions
  **Correction**: Only solvable algebras have this closure property. An extension of nilpotent algebras need not be nilpotent.

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.2, pages 68-69. Theorem 6.13.

# Verification Notes

- Definition source: Direct from Theorem 6.13
- Confidence rationale: Explicit theorem statement with proof
- Uncertainties: None
- Cross-reference status: Verified
