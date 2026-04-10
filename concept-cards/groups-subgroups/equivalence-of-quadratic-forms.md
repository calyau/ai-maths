---
# === CORE IDENTIFICATION ===
concept: Equivalence of Quadratic Forms
slug: equivalence-of-quadratic-forms

# === CLASSIFICATION ===
category: arithmetic-groups
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Arithmetic Subgroups"
chapter_number: 7
pdf_page: 404
section: "Application to quadratic forms"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - reduced quadratic form
  - equivalence of binary quadratic forms

# === TYPED RELATIONSHIPS ===
prerequisites:
  - arithmetic-subgroup
  - fundamental-domain-sl2
extends: []
related:
  - galois-cohomology-of-algebraic-groups
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do arithmetic subgroups relate to discrete subgroups of Lie groups?"
---

# Quick Definition

Two positive-definite binary quadratic forms are equivalent if one can be obtained from the other by an integer change of variables via $\mathrm{SL}_2(\mathbb{Z})$. Using the fundamental domain for $\mathrm{SL}_2(\mathbb{Z})$, every form is equivalent to a unique reduced form.

# Core Definition

Two positive-definite binary quadratic forms $q(x,y) = ax^2 + bxy + cy^2$ and $q'$ are *equivalent* if there is a matrix $A \in \mathrm{SL}_2(\mathbb{Z})$ such that $Q = A^t Q' A$ where $Q, Q'$ are the associated symmetric matrices (Milne, p. 404).

A form is *reduced* if $|\omega| > 1$ and $-1/2 \leq \Re(\omega) < 1/2$, or $|\omega| = 1$ and $-1/2 \leq \Re(\omega) \leq 0$, where $\omega$ is the root in $\mathcal{H}$ of $q(x,1) = 0$ normalized appropriately. Equivalently, $q = ax^2 + bxy + cy^2$ is reduced iff either $-a < b \leq a < c$ or $0 \leq b \leq a = c$.

# Prerequisites

- **Arithmetic subgroup** — equivalence is defined via the action of $\mathrm{SL}_2(\mathbb{Z})$
- **Fundamental domain for SL₂** — reduced forms correspond to points in the fundamental domain

# Key Properties

1. Every positive-definite binary quadratic form is equivalent to a reduced form (from Proposition 9.1)
2. Two reduced forms are equivalent if and only if they are equal
3. There are finitely many equivalence classes of integral definite binary quadratic forms with a given discriminant $\Delta$
4. The finiteness follows because $4a^2 \leq 4ac = b^2 - \Delta \leq a^2 - \Delta$ constrains $a$ and $b$
5. This is a variant of the finiteness of the class number of a quadratic imaginary field

# Construction / Recognition

## To Reduce a Form:
1. Write $q(x,y) = a(x - \omega y)(x - \bar{\omega} y)$ with $\omega \in \mathcal{H}$
2. Apply the algorithm from Proposition 9.1 to move $\omega$ into the fundamental domain $D$
3. The resulting form is the unique reduced representative

# Context & Application

The classification of binary quadratic forms is one of the oldest applications of what we now recognize as reduction theory. Gauss studied this problem extensively. The connection to arithmetic subgroups (via $\mathrm{SL}_2(\mathbb{Z})$ acting on $\mathcal{H}$) shows how the abstract theory of arithmetic groups has concrete number-theoretic applications.

# Examples

**Example 1** (p. 404): The form $x^2 + y^2$ has $\Delta = -4$, $\omega = i$. Since $i$ is in $D$, the form is already reduced.

**Example 2** (p. 404): The finiteness of reduced forms of discriminant $\Delta < 0$ follows from the bounds $a \leq \sqrt{-\Delta/3}$ and $|b| \leq a$.

# Relationships

## Builds Upon
- **Fundamental domain for SL₂** — reduced forms correspond to points in $D$
- **Arithmetic subgroup** — $\mathrm{SL}_2(\mathbb{Z})$ defines the equivalence relation

## Related
- **Galois cohomology of algebraic groups** — $H^1(k, \mathrm{O}(\phi))$ classifies quadratic forms up to isomorphism

# Common Errors

- **Error**: Using $\mathrm{GL}_2(\mathbb{Z})$ instead of $\mathrm{SL}_2(\mathbb{Z})$ for equivalence
  **Correction**: The text uses $\mathrm{SL}_2(\mathbb{Z})$; using $\mathrm{GL}_2(\mathbb{Z})$ gives a coarser equivalence (improper equivalence)

# Common Confusions

- **Confusion**: Confusing rational equivalence (over $\mathbb{Q}$) with integral equivalence (over $\mathbb{Z}$)
  **Clarification**: The reduction theory here concerns integral equivalence via $\mathrm{SL}_2(\mathbb{Z})$; rational equivalence is a different (coarser) relation

# Source Reference

Chapter VII: Arithmetic Subgroups, Section 10, pages 404-405.

# Verification Notes

- Definition source: Direct from p. 404
- Confidence: HIGH — classical result explicitly stated
- Uncertainties: None
- Cross-reference status: Verified
