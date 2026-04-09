---
# === CORE IDENTIFICATION ===
concept: Haar Measure
slug: haar-measure

# === CLASSIFICATION ===
category: representations
subcategory: basic-definitions
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of Lie Groups and Lie Algebras"
chapter_number: 4
pdf_page: 45
section: "4.6 Haar measure on compact Lie groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "right Haar measure"
  - "left Haar measure"
  - "bi-invariant measure"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-group
extends: []
related:
  - unitary-representation
  - complete-reducibility-of-compact-groups
  - matrix-coefficient
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Haar measure on a compact Lie group?"
  - "How does integration over a Lie group work?"
---

# Quick Definition

A Haar measure on a compact Lie group $G$ is a normalized, bi-invariant measure $dg$ satisfying $\int_G dg = 1$. It enables averaging over the group, which is the key tool for proving complete reducibility.

# Core Definition

**Definition 4.32** (Kirillov, p. 45): A right Haar measure on a real Lie group $G$ is a measure $dg$ such that $\int_G dg = 1$ and which is invariant under the right action of $G$ on itself: $\int f(gh)\, dg = \int f(g)\, dg$ for any $h \in G$.

**Theorem 4.33** (p. 46): Let $G$ be a compact real Lie group. Then it has a unique right Haar measure which is given by some smooth positive density. In addition, this Haar measure is also left-invariant and invariant under $g \mapsto g^{-1}$.

# Prerequisites

- **Lie group** — The group on which the measure is defined

# Key Properties

1. Unique for compact groups (up to normalization, which is fixed by $\int_G dg = 1$)
2. Bi-invariant for compact groups: both left- and right-invariant
3. Also invariant under $g \mapsto g^{-1}$
4. Given by a smooth positive density
5. Constructed from a left-invariant differential form on $G$

# Construction / Recognition

## To Construct:
1. Choose a non-zero element in $\Lambda^n \mathfrak{g}^*$ ($n = \dim G$)
2. Extend to a right-invariant $n$-form $\omega$ on $G$
3. Define $dg = |\omega| / \int_G |\omega|$ (normalize to have total measure 1)
4. Bi-invariance follows from Lemma 4.34: one-dimensional real representations of compact groups have $|\rho(g)| = 1$

# Context & Application

The Haar measure generalizes the sum $\frac{1}{|G|}\sum_{g \in G}$ for finite groups to an integral for Lie groups. It is essential for:
- Constructing $G$-invariant inner products (proving complete reducibility)
- Defining inner products on function spaces $L^2(G)$
- Orthogonality of characters and the Peter-Weyl theorem

# Examples

**Example 4.36** (p. 46): For $G = S^1 = \mathbb{R}/\mathbb{Z}$, the Haar measure is the usual Lebesgue measure $dx$ on $\mathbb{R}/\mathbb{Z}$.

**Example 4.37** (p. 46): For $G = U(n)$ and a conjugation-invariant function $f$:
$$\int_{U(n)} f(g)\, dg = \frac{1}{n!}\int_T f\begin{pmatrix} t_1 & & \\ & \ddots & \\ & & t_n \end{pmatrix} \prod_{i < j} |t_i - t_j|^2\, dt$$
This is a special case of the Weyl integration formula.

# Relationships

## Enables
- **G-invariant inner product** — Constructed by averaging with Haar measure
- **Complete reducibility** — Via invariant inner products
- **Orthogonality of characters** — Inner product on $L^2(G)$ uses Haar measure
- **Peter-Weyl theorem** — Statement involves $L^2(G, dg)$

# Common Errors

- **Error**: Assuming the Haar measure exists for non-compact groups with finite total measure.
  **Correction**: Non-compact groups have Haar measures, but $\int_G dg = \infty$. The normalization $\int_G dg = 1$ only works for compact groups.

# Common Confusions

- **Confusion**: Thinking left-invariant and right-invariant measures are always the same.
  **Clarification**: For compact groups they coincide (Theorem 4.33), but for non-compact groups (e.g., the affine group) they can differ.

# Source Reference

Chapter 4, Section 4.6, Definition 4.32, Theorem 4.33, Examples 4.36-4.37, pp. 45-47.

# Verification Notes

- Definition source: Direct from Definition 4.32 and Theorem 4.33
- Confidence rationale: Explicit definition and existence/uniqueness theorem
- Uncertainties: None
- Cross-reference status: Verified
