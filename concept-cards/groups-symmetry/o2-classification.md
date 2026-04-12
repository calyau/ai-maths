---
# === CORE IDENTIFICATION ===
concept: Classification of O_2 Elements
slug: o2-classification

# === CLASSIFICATION ===
category: matrix-groups
subcategory: classification
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
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - orthogonal-group
  - orthogonal-matrix
extends: []
related:
  - special-orthogonal-group
  - so2-and-unit-circle
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the elements of O_2?"
  - "How do rotations and reflections appear as 2x2 matrices?"
---

# Quick Definition

Every element of $O_2$ is either a rotation matrix (det $+1$) or a reflection matrix (det $-1$). The two types are completely classified by a single angle parameter.

# Core Definition

Armstrong classifies all elements of $O_2$ (pp. 53-54). If $A = \begin{bmatrix} a & c \\ b & d \end{bmatrix} \in O_2$, then $(a,b)$ lies on the unit circle, so $a = \cos\theta$, $b = \sin\theta$. The second column $(c,d)$ must be perpendicular to $(a,b)$ and of unit length. There are exactly two choices:

**Rotation** ($\det = +1$): $\begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$ — anticlockwise rotation through $\theta$.

**Reflection** ($\det = -1$): $\begin{bmatrix} \cos\theta & \sin\theta \\ \sin\theta & -\cos\theta \end{bmatrix}$ — reflection in the line at angle $\theta/2$ to the positive $x$-axis.

# Prerequisites

- **Orthogonal group** — This classifies elements of $O_2$
- **Orthogonal matrix** — Elements satisfy $A^tA = I_2$

# Key Properties

1. Every $2 \times 2$ orthogonal matrix is determined by a single angle $\theta$
2. Det $+1$ gives rotation; det $-1$ gives reflection
3. Product rules (Exercise 9.5): $A_\theta A_\varphi = A_{\theta+\varphi}$, $A_\theta B_\varphi = B_{\theta+\varphi}$, $B_\theta A_\varphi = B_{\theta-\varphi}$, $B_\theta B_\varphi = A_{\theta-\varphi}$
4. These product rules match the structure of dihedral groups

# Construction / Recognition

## To Classify an Element of $O_2$:
1. Compute the determinant
2. If det $= +1$: rotation matrix, find $\theta$ from $a = \cos\theta$, $b = \sin\theta$
3. If det $= -1$: reflection matrix, the line of reflection makes angle $\theta/2$ with the $x$-axis

# Context & Application

This classification connects abstract matrix groups to concrete geometric transformations. It shows that $O_2$ is the group of plane isometries that fix the origin, decomposing into rotations ($SO_2$) and reflections.

# Examples

**Example** (Exercise 9.4): The symmetries of an equilateral triangle with vertices at $(1, -\sqrt{3})$, $(1, \sqrt{3})$, $(-2, 0)$ can be written as matrices in $O_2$.

# Relationships

## Builds Upon
- **Orthogonal group** — Classification of its 2D case
- **Orthogonal matrix** — Geometric interpretation

## Related
- **Special orthogonal group** — $SO_2$ is the rotation half of $O_2$
- **SO_2 and the unit circle group** — $SO_2 \cong C$

# Common Errors

- **Error**: Using the wrong formula for the reflection line angle.
  **Correction**: The reflection matrix with parameter $\theta$ reflects in the line at angle $\theta/2$ (not $\theta$).

# Common Confusions

- **Confusion**: Thinking reflections in $O_2$ can reflect in any line.
  **Clarification**: Elements of $O_2$ fix the origin, so reflections are only in lines through the origin.

# Source Reference

Chapter 9: Matrix Groups, pages 53-54 (pdf pp. 53-54). Complete classification with geometric interpretation.

# Verification Notes

- Classification: Complete on pp. 53-54
- Product rules: Exercise 9.5
- Confidence: HIGH — thorough analysis with explicit matrices
