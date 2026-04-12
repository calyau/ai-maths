---
# === CORE IDENTIFICATION ===
concept: Special Unitary Group
slug: special-unitary-group

# === CLASSIFICATION ===
category: matrix-groups
subcategory: definitions
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Matrix Groups"
chapter_number: 9
pdf_page: 51
section: null

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - "SU_n"
  - "SU(n)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - unitary-group
extends:
  - unitary-group
related:
  - special-orthogonal-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the special unitary group?"
---

# Quick Definition

The special unitary group $SU_n$ consists of all $n \times n$ unitary matrices with determinant equal to $+1$.

# Core Definition

"Those elements of $U_n$ which have determinant equal to $+1$ form the *Special Unitary Group*" (Armstrong, p. 56). $SU_n$ is thus a subgroup of $U_n$, defined by the additional constraint that the determinant is exactly $1$ (not just of modulus 1).

# Prerequisites

- **Unitary group** — $SU_n$ is a subgroup of $U_n$

# Key Properties

1. $SU_n$ is a subgroup of $U_n$
2. All elements have determinant exactly $+1$
3. $SU_n$ is the complex analogue of $SO_n$
4. For $n = 2$: elements of $SU_2$ are obtained from the general $U_2$ form by setting $\theta = 0$ (Exercise 9.14)

# Construction / Recognition

## To Check Membership:
1. Verify $U^{*t}U = I_n$ (unitarity)
2. Verify $\det(U) = +1$

# Context & Application

The special unitary group plays an important role in physics, particularly in quantum mechanics and particle physics ($SU(2)$ for spin, $SU(3)$ for the strong force). Armstrong introduces it briefly at the end of Chapter 9 alongside the unitary group.

# Examples

**Example** (Exercise 9.14): Elements of $SU_2$ have the form
$$\begin{bmatrix} z & w \\ -w^* & z^* \end{bmatrix}$$
where $zz^* + ww^* = 1$ (the $\theta = 0$ case of the general $U_2$ element).

# Relationships

## Builds Upon
- **Unitary group** — $SU_n \le U_n$

## Related
- **Special orthogonal group** — Real analogue of $SU_n$

# Common Errors

- **Error**: Confusing det $= +1$ with $|\det| = 1$.
  **Correction**: $U_n$ requires $|\det| = 1$; $SU_n$ requires $\det = +1$ exactly.

# Common Confusions

- **Confusion**: Thinking $SU_n$ and $SO_n$ are isomorphic.
  **Clarification**: They are analogues over different fields ($\mathbb{C}$ vs $\mathbb{R}$) but generally not isomorphic.

# Source Reference

Chapter 9: Matrix Groups, page 56 (pdf p. 56). Brief definition at chapter's end; Exercise 9.14.

# Verification Notes

- Definition: Direct from p. 56
- $SU_2$ form: From Exercise 9.14 (setting $\theta = 0$)
- Confidence: MEDIUM — defined but with minimal discussion in the source
