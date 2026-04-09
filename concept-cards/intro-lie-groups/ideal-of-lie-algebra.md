---
# === CORE IDENTIFICATION ===
concept: Ideal of a Lie Algebra
slug: ideal-of-lie-algebra

# === CLASSIFICATION ===
category: lie-algebras
subcategory: subalgebras-ideals
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups and Lie Algebras"
chapter_number: 3
pdf_page: 25
section: "3.4"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Lie ideal"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-algebra
  - lie-subalgebra
extends:
  - lie-subalgebra
related:
  - quotient-lie-algebra
  - center-of-lie-algebra
contrasts_with:
  - lie-subalgebra

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Lie algebra?"
---

# Quick Definition

An ideal $\mathfrak{h} \subset \mathfrak{g}$ is a subalgebra satisfying the stronger condition $[x, y] \in \mathfrak{h}$ for all $x \in \mathfrak{g}$ and $y \in \mathfrak{h}$. Ideals are the Lie algebra analog of normal subgroups.

# Core Definition

**Definition 3.18** (Kirillov): A subspace $\mathfrak{h} \subset \mathfrak{g}$ is called an ideal if for any $x \in \mathfrak{g}$, $y \in \mathfrak{h}$, we have $[x, y] \in \mathfrak{h}$.

**Theorem 3.19 part (2)**: If $H$ is a normal Lie subgroup, then $\mathfrak{h} = T_1H$ is an ideal, and $\mathrm{Lie}(G/H) = \mathfrak{g}/\mathfrak{h}$. Conversely, if $H$ is connected and $\mathfrak{h}$ is an ideal, then $H$ is normal.

# Prerequisites

- **Lie algebra** — the ambient algebra
- **Lie subalgebra** — every ideal is a subalgebra

# Key Properties

1. Every ideal is a subalgebra (since $[\mathfrak{h}, \mathfrak{h}] \subset [\mathfrak{g}, \mathfrak{h}] \subset \mathfrak{h}$).
2. If $\mathfrak{h}$ is an ideal, $\mathfrak{g}/\mathfrak{h}$ has a canonical Lie algebra structure.
3. Normal subgroups $\leftrightarrow$ ideals (for connected subgroups, Theorem 3.19).
4. The center $\mathfrak{z}(\mathfrak{g})$ is always an ideal (Definition 3.31).
5. The kernel of any Lie algebra morphism is an ideal.

# Construction / Recognition

## To Construct/Create:
1. Take a subspace $\mathfrak{h}$ of $\mathfrak{g}$.
2. Verify $[\mathfrak{g}, \mathfrak{h}] \subset \mathfrak{h}$ (bracket with any element of $\mathfrak{g}$, not just of $\mathfrak{h}$).

## To Identify/Recognize:
1. A subspace closed under bracketing with all of $\mathfrak{g}$.
2. Equivalently: a subspace invariant under $\mathrm{ad}\, x$ for all $x \in \mathfrak{g}$.

# Context & Application

Ideals are essential for building quotient algebras and for the structure theory of Lie algebras (semisimple, solvable, nilpotent decompositions).

# Examples

**Example** (p. 25): $\mathfrak{z}(\mathfrak{g})$ is an ideal.

**Example**: $\mathfrak{sl}(n) \subset \mathfrak{gl}(n)$ is an ideal (since $[A, B] = AB - BA$ always has trace $0$).

# Relationships

## Builds Upon
- **Lie subalgebra** — every ideal is a subalgebra

## Enables
- **Quotient Lie algebra** — $\mathfrak{g}/\mathfrak{h}$ when $\mathfrak{h}$ is an ideal

## Related
- **Center of Lie algebra** — always an ideal
- **Normal subgroup** — the group-level analog

## Contrasts With
- **Lie subalgebra** — only requires $[\mathfrak{h}, \mathfrak{h}] \subset \mathfrak{h}$, not $[\mathfrak{g}, \mathfrak{h}] \subset \mathfrak{h}$

# Common Errors

- **Error**: Assuming every subalgebra is an ideal.
  **Correction**: In general, $[\mathfrak{g}, \mathfrak{h}]$ may not be contained in $\mathfrak{h}$ even if $[\mathfrak{h}, \mathfrak{h}] \subset \mathfrak{h}$.

# Common Confusions

- **Confusion**: Whether there are "left ideals" and "right ideals" as in ring theory.
  **Clarification**: No. Because the bracket is skew-symmetric, $[\mathfrak{g}, \mathfrak{h}] = -[\mathfrak{h}, \mathfrak{g}]$, so left and right ideals coincide.

# Source Reference

Chapter 3: Lie Groups and Lie Algebras, Section 3.4, Definition 3.18, Theorem 3.19, page 25.

# Verification Notes

- Definition source: Direct from Definition 3.18
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified with Theorem 3.19, Definition 3.31
