---
# === CORE IDENTIFICATION ===
concept: Conjugacy Classes of O2
slug: conjugacy-classes-of-o2

# === CLASSIFICATION ===
category: conjugacy
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Conjugacy"
chapter_number: 14
pdf_page: 80
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - conjugacy-class
  - orthogonal-group
extends: []
related:
  - centre-of-a-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the conjugacy classes of the orthogonal group O2?"
---

# Quick Definition

The conjugacy classes of $O_2$ are: $\{I\}$, $\{A_\theta, A_{-\theta}\}$ for $0 < \theta < \pi$, $\{A_\pi\}$, and the single class of all reflections $\{B_\varphi \mid 0 \le \varphi < 2\pi\}$.

# Core Definition

Armstrong computes the conjugacy classes of $O_2$ using the matrices $A_\theta$ (rotations) and $B_\varphi$ (reflections) (Ch. 14, Example (v), pp. 83-84). Key computations:

- Conjugate matrices have the same determinant, so rotations and reflections cannot be conjugate
- $A_\theta B_\varphi A_\theta^{-1} = B_{\varphi + 2\theta}$: any two reflections are conjugate
- $A_\varphi A_\theta A_\varphi^{-1} = A_\theta$: rotations commute
- $B_\varphi A_\theta B_\varphi^{-1} = A_{-\theta}$: reflection conjugation sends $A_\theta$ to $A_{-\theta}$

# Prerequisites

- **Conjugacy class** — The concept being computed
- **Orthogonal group** — $O_2$ with its rotation and reflection matrices

# Key Properties

1. All reflections form a single conjugacy class (infinite)
2. Rotation classes are $\{A_\theta, A_{-\theta}\}$ for $0 < \theta < \pi$
3. $\{I\}$ and $\{A_\pi\}$ are singleton classes (central elements)
4. The centre of $O_2$ is $\{I, A_\pi\} = \{I, -I\}$

# Construction / Recognition

## Key Computations:
1. $A_\theta B_\varphi A_\theta^{-1} = B_{\varphi + 2\theta}$ shows all $B_\varphi$ are conjugate
2. $B_\varphi A_\theta B_\varphi^{-1} = A_{-\theta}$ pairs rotations with their inverses

# Context & Application

This example demonstrates conjugacy classes in a continuous (infinite) group, contrasting with the finite examples of $D_6$ and $A_4$. The single class of all reflections contrasts with $D_6$ where reflections split into two classes.

# Examples

**Example 1** (p. 84): The distinct conjugacy classes of $O_2$:
- $\{I\}$
- $\{A_\theta, A_{-\theta}\}$ for each $0 < \theta < \pi$
- $\{A_\pi\}$
- $\{B_\varphi \mid 0 \le \varphi < 2\pi\}$

# Relationships

## Builds Upon
- **Conjugacy class** — Applied to a continuous group

## Related
- **Centre of a group** — $Z(O_2) = \{I, -I\}$

# Common Errors

- **Error**: Thinking $A_\theta$ and $A_{-\theta}$ are in different conjugacy classes
  **Correction**: Conjugation by any reflection sends $A_\theta$ to $A_{-\theta}$, so they are conjugate

# Common Confusions

- **Confusion**: Expecting reflections to split into multiple classes as in $D_6$
  **Clarification**: In $O_2$, the rotation subgroup is large enough ($A_\theta B_\varphi A_\theta^{-1} = B_{\varphi + 2\theta}$ for all $\theta$) to conjugate any reflection to any other

# Source Reference

Chapter 14: Conjugacy, Example (v), pp. 83-84 (pdf).

# Verification Notes

- Definition source: Direct computation from Example (v)
- Confidence rationale: HIGH — explicit matrix calculations
- Uncertainties: None
