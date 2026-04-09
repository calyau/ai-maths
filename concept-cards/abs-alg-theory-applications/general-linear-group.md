---
# === CORE IDENTIFICATION ===
concept: General Linear Group
slug: general-linear-group

# === CLASSIFICATION ===
category: group-theory
subcategory: group-examples
tier: foundational

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Groups"
chapter_number: 3
pdf_page: 48
section: "Definitions and Examples"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "GL_2(R)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
extends: []
related:
  - special-linear-group
  - nonabelian-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a group?"
---

# Quick Definition

The general linear group $GL_2(\mathbb{R})$ is the group of all invertible $2 \times 2$ matrices with real entries under matrix multiplication.

# Core Definition

"Let $GL_2(\mathbb{R})$ be the subset of $M_2(\mathbb{R})$ consisting of invertible matrices; that is, a matrix $A$ is in $GL_2(\mathbb{R})$ if there exists a matrix $A^{-1}$ such that $AA^{-1} = A^{-1}A = I$... For $A$ to have an inverse is equivalent to requiring that the determinant of $A$ be nonzero; that is, $\det A = ad - bc \neq 0$. The set of invertible matrices forms a group called the general linear group" (Judson, p. 48).

# Prerequisites

- **Group** — $GL_2(\mathbb{R})$ is verified to be a group

# Key Properties

1. Identity: the $2 \times 2$ identity matrix $I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$
2. Inverse: $A^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$
3. Nonabelian: $AB \neq BA$ in general
4. Infinite order
5. Product of invertible matrices is invertible ($\det(AB) = \det A \cdot \det B$)

# Construction / Recognition

## To Verify $A \in GL_2(\mathbb{R})$:
1. Compute $\det A = ad - bc$
2. If $\det A \neq 0$, then $A \in GL_2(\mathbb{R})$

# Context & Application

$GL_2(\mathbb{R})$ is a fundamental example of a nonabelian group and appears in linear algebra, geometry, physics, and representation theory. Its subgroups include $SL_2(\mathbb{R})$, orthogonal groups, and rotation groups.

# Examples

**Example 1** (p. 48): The identity matrix $I$ and the inverse formula $A^{-1} = \frac{1}{ad-bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$.

# Relationships

## Builds Upon
- **group** — $GL_2(\mathbb{R})$ satisfies the group axioms

## Enables
- **special-linear-group** — $SL_2(\mathbb{R}) \subset GL_2(\mathbb{R})$

## Related
- **nonabelian-group** — Example of a nonabelian group

# Common Errors

- **Error**: Including singular matrices (det = 0) in $GL_2(\mathbb{R})$
  **Correction**: Only matrices with nonzero determinant are in $GL_2(\mathbb{R})$

# Common Confusions

- **Confusion**: Confusing $GL_2(\mathbb{R})$ with $M_2(\mathbb{R})$
  **Clarification**: $M_2(\mathbb{R})$ is all $2 \times 2$ matrices; $GL_2(\mathbb{R})$ is only the invertible ones

# Source Reference

Chapter 3: Groups, Section 3.2, Example 3.14, page 48.

# Verification Notes

- Definition source: Direct quote from p. 48
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Re-extracted from older card; updated to v3 template referencing Ch. 3
- Uncertainties: None
