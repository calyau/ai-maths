---
# === CORE IDENTIFICATION ===
concept: General Linear Group
slug: general-linear-group

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
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "GL_n"
  - "GL_n(R)"
  - "GL_n(C)"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - orthogonal-group
  - special-orthogonal-group
  - unitary-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the general linear group?"
  - "What are matrix groups?"
---

# Quick Definition

The general linear group $GL_n$ (or $GL_n(\mathbb{R})$) is the group of all invertible $n \times n$ matrices with real entries under matrix multiplication.

# Core Definition

"The set of all invertible $n \times n$ matrices with real numbers as entries forms a group under matrix multiplication" (Armstrong, p. 51). "For these reasons the group is called the **General Linear Group**, $GL_n$. If we wish to emphasise that the matrices all have real entries, then we write $GL_n(\mathbb{R})$. Changing $\mathbb{R}$ to $\mathbb{C}$ gives the corresponding group $GL_n(\mathbb{C})$ of $n \times n$ invertible complex matrices" (p. 51).

Each matrix $A \in GL_n$ determines an invertible linear transformation $f_A: \mathbb{R}^n \to \mathbb{R}^n$ defined by $f_A(\mathbf{x}) = \mathbf{x}A^t$.

# Prerequisites

This is a foundational concept for matrix groups, requiring basic linear algebra.

# Key Properties

1. $GL_n$ is a group under matrix multiplication
2. The identity element is the $n \times n$ identity matrix $I_n$
3. The inverse of $AB$ is $B^{-1}A^{-1}$
4. $GL_n$ is non-abelian for $n \ge 2$
5. $GL_1 \cong \mathbb{R} \setminus \{0\}$ (non-zero reals under multiplication)
6. $GL_n$ embeds into $GL_{n+1}$ via $A \mapsto \begin{bmatrix} A & 0 \\ 0 & 1 \end{bmatrix}$
7. $GL_n$ is an infinite group for all $n \ge 1$
8. The product $AB$ corresponds to the composite linear transformation $f_A \circ f_B$

# Construction / Recognition

## To Verify Membership:
1. Check that the matrix is $n \times n$
2. Check that the determinant is non-zero (equivalently, the matrix is invertible)

# Context & Application

The general linear group is the "largest" matrix group: all other matrix groups in this chapter ($O_n$, $SO_n$, $U_n$, $SU_n$) are subgroups of appropriate general linear groups. The connection between matrices and linear transformations means that studying $GL_n$ is equivalent to studying invertible linear maps on $\mathbb{R}^n$.

# Examples

**Example** (p. 51): $GL_1$ consists of all non-zero real numbers under multiplication, so $GL_1 \cong \mathbb{R} \setminus \{0\}$.

**Example** (p. 51): Every $A \in GL_n$ can be embedded into $GL_{n+1}$ by adding a row and column, giving an isomorphic copy of $GL_n$ inside $GL_{n+1}$.

# Relationships

## Enables
- **Orthogonal group** — $O_n$ is a subgroup of $GL_n$
- **Special orthogonal group** — $SO_n$ is a subgroup of $GL_n$
- **Unitary group** — $U_n$ is a subgroup of $GL_n(\mathbb{C})$

# Common Errors

- **Error**: Forgetting that the zero matrix is not in $GL_n$.
  **Correction**: $GL_n$ consists of *invertible* matrices; the zero matrix has determinant 0 and is excluded.

# Common Confusions

- **Confusion**: Confusing $GL_n(\mathbb{R})$ with the set of all $n \times n$ matrices.
  **Clarification**: $GL_n(\mathbb{R})$ contains only invertible matrices. The set of all $n \times n$ matrices is not a group under multiplication (no inverses for singular matrices).

# Source Reference

Chapter 9: Matrix Groups, page 51 (pdf p. 51). Definition and basic properties.

# Verification Notes

- Definition: Direct from p. 51
- Linear transformation correspondence: Explicit on p. 51
- Confidence: HIGH — explicit definition
