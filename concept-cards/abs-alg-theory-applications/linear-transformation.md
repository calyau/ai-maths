---
# === CORE IDENTIFICATION ===
concept: Linear Transformation
slug: linear-transformation

# === CLASSIFICATION ===
category: foundations
subcategory: set-theory
tier: foundational

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Preliminaries"
chapter_number: 1
pdf_page: 22
section: "Cartesian Products and Mappings"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - linear map

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mapping
extends:
  - mapping
related:
  - general-linear-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
---

# Quick Definition

A linear transformation is a map from $\mathbb{R}^n$ to $\mathbb{R}^m$ given by multiplication by a matrix.

# Core Definition

"Maps from $\mathbb{R}^n$ to $\mathbb{R}^m$ given by matrices are called linear maps or linear transformations" (Judson, p. 22). Given a $2 \times 2$ matrix $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$, we define $T_A: \mathbb{R}^2 \to \mathbb{R}^2$ by $T_A(x, y) = (ax + by, cx + dy)$.

# Prerequisites

- **Mapping** — A linear transformation is a function

# Key Properties

1. Defined by matrix multiplication
2. $T_A$ is invertible iff $\det A \neq 0$
3. $(T_A)^{-1} = T_{A^{-1}}$ when $A$ is invertible
4. Composition corresponds to matrix multiplication: $T_B \circ T_A = T_{BA}$

# Context & Application

Linear transformations provide the connection between matrix groups ($GL_2(\mathbb{R})$, $SL_2(\mathbb{R})$) and geometric transformations, linking linear algebra to group theory.

# Examples

**Example 1** (p. 22): $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ defines $T_A(x,y) = (ax + by, cx + dy)$.

**Example 2** (p. 23): $A = \begin{pmatrix} 3 & 1 \\ 5 & 2 \end{pmatrix}$ gives $T_A(x,y) = (3x+y, 5x+2y)$ with $T_A^{-1}(x,y) = (2x-y, -5x+3y)$.

# Relationships

## Builds Upon
- **mapping** — A linear transformation is a function

## Related
- **general-linear-group** — Invertible linear transformations form $GL_2(\mathbb{R})$

# Source Reference

Chapter 1: Preliminaries, Section 1.2, pages 22-23.

# Verification Notes

- Definition source: Direct quote from p. 22
- Confidence: HIGH — explicit definition
- Re-extracted from older card; updated to v3 template referencing Ch. 1
- Cross-reference status: Verified
- Uncertainties: None
