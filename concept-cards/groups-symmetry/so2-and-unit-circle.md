---
# === CORE IDENTIFICATION ===
concept: SO_2 and the Unit Circle Group
slug: so2-and-unit-circle

# === CLASSIFICATION ===
category: matrix-groups
subcategory: specific-groups
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
aliases:
  - "C ≅ SO_2"
  - "unit circle group"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - special-orthogonal-group
extends: []
related:
  - orthogonal-group
  - isomorphism
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is SO_2?"
  - "What is the unit circle group?"
  - "How are SO_2 and the unit circle group related?"
---

# Quick Definition

$SO_2$ consists of all $2 \times 2$ rotation matrices. It is isomorphic to $C$, the unit circle group in the complex plane, via $e^{i\theta} \mapsto \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$.

# Core Definition

Armstrong classifies the elements of $O_2$ (pp. 53-54). If $A \in O_2$ with first column $(\cos\theta, \sin\theta)^t$, the second column must be perpendicular and unit-length. When $\det(A) = +1$, the matrix is:
$$\begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$$
representing anticlockwise rotation through $\theta$. "We have seen $SO_2$ before, albeit disguised as the unit circle in the complex plane" (p. 54). The correspondence $e^{i\theta} \to \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$ is an isomorphism from $C$ to $SO_2$.

# Prerequisites

- **Special orthogonal group** — $SO_2$ is a specific instance

# Key Properties

1. Every element of $SO_2$ is a rotation matrix parametrized by angle $\theta \in [0, 2\pi)$
2. $SO_2 \cong C$ (the unit circle group under complex multiplication)
3. $SO_2$ is abelian (rotations in 2D commute)
4. Product of rotations: $A_\theta A_\varphi = A_{\theta + \varphi}$
5. The group is infinite and connected

# Construction / Recognition

## To Construct $SO_2$:
1. Take all matrices of the form $\begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$ for $\theta \in [0, 2\pi)$

## The Isomorphism with $C$:
1. Map $e^{i\theta}$ to the rotation matrix for angle $\theta$
2. This preserves multiplication: $e^{i(\theta+\varphi)}$ maps to $A_{\theta+\varphi} = A_\theta A_\varphi$

# Context & Application

The isomorphism $C \cong SO_2$ connects complex analysis with matrix groups. Armstrong uses the notation $C$ for the unit circle group throughout the text. This isomorphism shows that planar rotations can be understood either as complex multiplication or as matrix multiplication.

# Examples

**Example** (p. 54): When $\det(A) = -1$, the matrix
$$\begin{bmatrix} \cos\theta & \sin\theta \\ \sin\theta & -\cos\theta \end{bmatrix}$$
represents reflection in the line at angle $\theta/2$ to the positive $x$-axis.

# Relationships

## Builds Upon
- **Special orthogonal group** — $SO_2$ is an instance of $SO_n$

## Related
- **Orthogonal group** — $O_2$ contains $SO_2$ plus reflections
- **Isomorphism** — The correspondence $C \cong SO_2$

# Common Errors

- **Error**: Confusing the rotation angle $\theta$ with the reflection line angle.
  **Correction**: Rotation by $\theta$ uses angle $\theta$; reflection in a line uses the line at angle $\theta/2$ to get the matrix with parameter $\theta$.

# Common Confusions

- **Confusion**: Thinking $SO_2$ is isomorphic to $\mathbb{R}$.
  **Clarification**: $SO_2 \cong C$ (the circle group), not $\mathbb{R}$. The circle group is compact; $\mathbb{R}$ is not.

# Source Reference

Chapter 9: Matrix Groups, pages 53-54 (pdf pp. 53-54). Classification of $O_2$; isomorphism $C \cong SO_2$.

# Verification Notes

- Classification: Complete on pp. 53-54
- Isomorphism: Explicit on p. 54
- Armstrong's notation $C$ for the unit circle group: Used on p. 54
- Confidence: HIGH — explicit treatment
