---
# === CORE IDENTIFICATION ===
concept: Special Linear Group
slug: special-linear-group

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
pdf_page: 51
section: "Subgroups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "SL_2(R)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - general-linear-group
  - subgroup
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a subgroup?"
---

# Quick Definition

The special linear group $SL_2(\mathbb{R})$ is the subgroup of $GL_2(\mathbb{R})$ consisting of all $2 \times 2$ matrices with determinant equal to 1.

# Core Definition

"Let $SL_2(\mathbb{R})$ be the subset of $GL_2(\mathbb{R})$ consisting of matrices of determinant one; that is, a matrix $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ is in $SL_2(\mathbb{R})$ exactly when $ad - bc = 1$" (Judson, p. 51). The group $SL_2(\mathbb{R})$ is called the special linear group.

# Prerequisites

- **General linear group** — $SL_2(\mathbb{R}) \subset GL_2(\mathbb{R})$
- **Subgroup** — $SL_2(\mathbb{R})$ is a subgroup

# Key Properties

1. All matrices have determinant exactly 1
2. The identity matrix $I$ has $\det I = 1$, so $I \in SL_2(\mathbb{R})$
3. If $\det A = 1$, then $A^{-1} = \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$
4. The product of matrices with determinant 1 has determinant 1

# Construction / Recognition

## To Verify $A \in SL_2(\mathbb{R})$:
1. Compute $\det A = ad - bc$
2. Check that $\det A = 1$

# Context & Application

$SL_2(\mathbb{R})$ is important in geometry, number theory (modular forms), and physics. It demonstrates how a subgroup can be defined by an algebraic condition (determinant = 1) on the elements of a larger group.

# Examples

**Example 1** (p. 51): The matrix $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ with $ad - bc = 1$ has inverse $A^{-1} = \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$, which also has determinant 1.

# Relationships

## Builds Upon
- **general-linear-group** — $SL_2(\mathbb{R}) \subset GL_2(\mathbb{R})$

## Related
- **subgroup** — $SL_2(\mathbb{R})$ is a subgroup of $GL_2(\mathbb{R})$

# Common Errors

- **Error**: Confusing the determinant condition with invertibility
  **Correction**: All matrices in $SL_2(\mathbb{R})$ are invertible (det = 1 $\neq$ 0), but not all invertible matrices have det = 1

# Source Reference

Chapter 3: Groups, Section 3.3, Example 3.26, page 51.

# Verification Notes

- Definition source: Direct quote from p. 51
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Re-extracted from older card; updated to v3 template referencing Ch. 3
- Uncertainties: None
