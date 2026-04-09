---
# === CORE IDENTIFICATION ===
concept: Classical Group Theorem
slug: classical-group-theorem

# === CLASSIFICATION ===
category: lie-groups
subcategory: classical-groups
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups: Basic Definitions"
chapter_number: 2
pdf_page: 16
section: "2.5"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Theorem 2.29"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - general-linear-group
  - matrix-exponential
extends: []
related:
  - special-linear-group
  - orthogonal-group
  - unitary-group
  - symplectic-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I compute the Lie algebra of a matrix Lie group?"
  - "How do the classical groups relate to each other?"
---

# Quick Definition

The classical group theorem states that for each classical group $G \subset \mathrm{GL}(n, \mathbb{K})$, the logarithmic map identifies a neighborhood of $1$ in $G$ with a neighborhood of $0$ in a vector subspace $\mathfrak{g} \subset \mathfrak{gl}(n, \mathbb{K})$, proving each is a Lie group.

# Core Definition

**Theorem 2.29** (Kirillov): For each classical group $G \subset \mathrm{GL}(n, \mathbb{K})$, there exists a vector space $\mathfrak{g} \subset \mathfrak{gl}(n, \mathbb{K})$ such that for some neighborhood $U$ of $1$ in $\mathrm{GL}(n, \mathbb{K})$ and some neighborhood $\mathfrak{u}$ of $0$ in $\mathfrak{gl}(n, \mathbb{K})$, the maps $\exp$ and $\log$ are mutually inverse between $U \cap G$ and $\mathfrak{u} \cap \mathfrak{g}$.

**Corollary 2.30**: Each classical group is a Lie group, with $T_1G = \mathfrak{g}$ and $\dim G = \dim \mathfrak{g}$.

# Prerequisites

- **General linear group** — ambient group
- **Matrix exponential** — the tool used in the proof

# Key Properties

The Lie algebras of classical groups are:
1. $\mathfrak{gl}(n, \mathbb{K})$: all matrices. Dim $= n^2$.
2. $\mathfrak{sl}(n, \mathbb{K})$: $\mathrm{tr}(x) = 0$. Dim $= n^2 - 1$.
3. $\mathfrak{o}(n, \mathbb{K}) = \mathfrak{so}(n, \mathbb{K})$: $x + x^t = 0$. Dim $= n(n-1)/2$.
4. $\mathfrak{u}(n)$: $x + x^* = 0$. Dim $= n^2$.
5. $\mathfrak{su}(n)$: $x + x^* = 0$, $\mathrm{tr}(x) = 0$. Dim $= n^2 - 1$.
6. $\mathfrak{sp}(2n, \mathbb{K})$: $x + Jx^tJ^{-1} = 0$. Dim $= n(2n+1)$.

# Construction / Recognition

## To Construct/Create:
1. Write the defining condition of $G$ (e.g., $AA^t = I$).
2. Substitute $A = \exp(x)$ and use properties of exp.
3. Simplify to get a linear condition on $x$ defining $\mathfrak{g}$.

## To Identify/Recognize:
1. The Lie algebra is the linear condition obtained by "differentiating" the group condition.

# Context & Application

This is the fundamental method for computing Lie algebras of matrix groups. The key idea is that the exponential map provides local coordinates, and the group conditions become linear at the Lie algebra level.

# Examples

**Example** (p. 16): For $\mathrm{O}(n)$: $XX^t = I \implies \exp(x)\exp(x^t) = I \implies x + x^t = 0$ (using commutativity of $x$ and $x^t$ near $I$).

**Example** (p. 17): For $\mathrm{U}(n)$: $xx^* = I \implies x + x^* = 0$, but $x + x^* = 0$ does NOT imply $\mathrm{tr}(x) = 0$ (diagonal entries are purely imaginary), so $\mathfrak{u}(n) \neq \mathfrak{su}(n)$.

# Relationships

## Builds Upon
- **Matrix exponential** — the tool used in all proofs

## Enables
- **All classical group Lie algebras** — computed by this method
- **Dimension formulas** — $\dim G = \dim \mathfrak{g}$

## Related
- **Closed subgroup theorem** (Theorem 2.8) — alternative approach to proving groups are Lie groups

# Common Errors

- **Error**: Trying to prove classical groups are Lie groups using the implicit function theorem directly.
  **Correction**: The exponential map approach is much easier. The implicit function theorem approach requires computing the rank of $n^2$ equations defining $\mathrm{O}(n)$, which is intractable.

# Common Confusions

- **Confusion**: Whether $\mathfrak{o}(n)$ and $\mathfrak{so}(n)$ are different.
  **Clarification**: They are the same vector space, since $x + x^t = 0$ automatically forces $\mathrm{tr}(x) = 0$ when $x$ is skew-symmetric.

# Source Reference

Chapter 2: Lie Groups: Basic Definitions, Section 2.5, Theorem 2.29, Corollary 2.30, pages 16-17.

# Verification Notes

- Definition source: Direct from Theorem 2.29 and its proof
- Confidence rationale: Explicit theorem with case-by-case proof
- Uncertainties: None
- Cross-reference status: Verified with all classical group entries
