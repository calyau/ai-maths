---
# === CORE IDENTIFICATION ===
concept: Normal Lie Subgroup
slug: normal-lie-subgroup

# === CLASSIFICATION ===
category: lie-groups
subcategory: subgroups
tier: foundational

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-subgroup
  - ideal-of-lie-algebra
extends:
  - lie-subgroup
related:
  - quotient-lie-group
  - quotient-lie-algebra
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does a Lie algebra relate to its Lie group?"
---

# Quick Definition

A normal Lie subgroup $H \trianglelefteq G$ is a Lie subgroup that is also a normal subgroup ($gHg^{-1} = H$ for all $g$). Its Lie algebra $\mathfrak{h} = T_1H$ is an ideal in $\mathfrak{g}$, and $G/H$ is a Lie group.

# Core Definition

**Theorem 3.19, part (2)** (Kirillov): Let $H$ be a normal Lie subgroup in $G$. Then $\mathfrak{h} = T_1H$ is an ideal in $\mathfrak{g}$, and $\mathrm{Lie}(G/H) = \mathfrak{g}/\mathfrak{h}$. Conversely, if $H$ is a connected Lie subgroup and $\mathfrak{h}$ is an ideal, then $H$ is normal.

# Prerequisites

- **Lie subgroup** — a normal Lie subgroup is a Lie subgroup
- **Ideal of Lie algebra** — the algebra-level correspondent

# Key Properties

1. Normal subgroup $\leftrightarrow$ ideal (for connected subgroups).
2. $G/H$ is a Lie group with $\mathrm{Lie}(G/H) = \mathfrak{g}/\mathfrak{h}$.
3. The kernel of any Lie group morphism is a normal Lie subgroup (Theorem 2.12).
4. $G^0$ is always a normal Lie subgroup (Theorem 2.4).

# Construction / Recognition

## To Construct/Create:
1. Take the kernel of a Lie group morphism.
2. Or: find an ideal $\mathfrak{h} \subset \mathfrak{g}$ and take the corresponding connected subgroup.

## To Identify/Recognize:
1. A Lie subgroup closed under conjugation by all group elements.
2. Equivalently (for connected $H$): $T_1H$ is an ideal in $\mathfrak{g}$.

# Context & Application

Normal Lie subgroups are needed to form quotient Lie groups, which appear throughout the theory (homomorphism theorem, quotient by center, etc.).

# Examples

**Example**: $\mathrm{SL}(n) \trianglelefteq \mathrm{GL}(n)$ with $\mathrm{GL}(n)/\mathrm{SL}(n) \cong \mathbb{R}^*$ (or $\mathbb{C}^*$).

**Example**: $Z(G) \trianglelefteq G$ (the center is always normal).

**Example**: $\mathrm{Ker}(f) \trianglelefteq G_1$ for any morphism $f: G_1 \to G_2$.

# Relationships

## Builds Upon
- **Lie subgroup** — must be a Lie subgroup
- **Ideal of Lie algebra** — the algebra-level analog

## Enables
- **Quotient Lie group** — $G/H$ is a Lie group

## Related
- **Homomorphism theorem** — $G/\mathrm{Ker}(f) \cong \mathrm{Im}(f)$

# Common Errors

- **Error**: Assuming a disconnected Lie subgroup with ideal Lie algebra is normal.
  **Correction**: The converse (ideal $\Rightarrow$ normal) requires $H$ to be connected.

# Common Confusions

- **Confusion**: Whether every ideal corresponds to a normal subgroup.
  **Clarification**: Every ideal corresponds to a connected immersed subgroup (Theorem 3.43), which is normal if it is a Lie subgroup.

# Source Reference

Chapter 3: Lie Groups and Lie Algebras, Section 3.4, Theorem 3.19 part (2), pages 25.

# Verification Notes

- Definition source: Direct from Theorem 3.19
- Confidence rationale: Explicit theorem
- Uncertainties: None
- Cross-reference status: Verified with Theorem 2.4, 2.12
