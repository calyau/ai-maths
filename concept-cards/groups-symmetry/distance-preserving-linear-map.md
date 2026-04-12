---
# === CORE IDENTIFICATION ===
concept: Distance-Preserving Linear Map
slug: distance-preserving-linear-map

# === CLASSIFICATION ===
category: matrix-groups
subcategory: characterizations
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
  - "isometry fixing the origin"
  - "length-preserving linear transformation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - orthogonal-matrix
extends: []
related:
  - orthogonal-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the relationship between distance-preserving maps and orthogonal matrices?"
  - "Which linear transformations preserve distance?"
---

# Quick Definition

A linear transformation $f: \mathbb{R}^n \to \mathbb{R}^n$ preserves distances if and only if it is represented by an orthogonal matrix.

# Core Definition

Armstrong proves a bidirectional characterization (pp. 52-53):

**Forward**: If $A \in O_n$, then $f_A$ preserves the scalar product ($f_A(\mathbf{x}) \cdot f_A(\mathbf{y}) = \mathbf{x} \cdot \mathbf{y}$), hence preserves length and distance.

**Converse**: If $f: \mathbb{R}^n \to \mathbb{R}^n$ is a linear transformation that preserves length, then it preserves the scalar product (shown using the identity $\mathbf{x} \cdot \mathbf{y} = \frac{1}{2}[\|\mathbf{x}\|^2 - \|\mathbf{x} - \mathbf{y}\|^2 + \|\mathbf{y}\|^2]$), hence maps the standard basis to an orthonormal basis, hence is represented by an orthogonal matrix (p. 53).

# Prerequisites

- **Orthogonal matrix** — The matrices that represent distance-preserving linear maps

# Key Properties

1. $f_A$ preserves scalar product: $f_A(\mathbf{x}) \cdot f_A(\mathbf{y}) = \mathbf{x} \cdot \mathbf{y}$
2. $f_A$ preserves length: $\|f_A(\mathbf{x})\| = \|\mathbf{x}\|$
3. $f_A$ preserves distance: $\|f_A(\mathbf{x}) - f_A(\mathbf{y})\| = \|\mathbf{x} - \mathbf{y}\|$
4. $f_A$ preserves orthogonality: $\mathbf{x} \perp \mathbf{y} \Leftrightarrow f_A(\mathbf{x}) \perp f_A(\mathbf{y})$
5. Each of these properties implies the others for linear maps
6. A linear map with any of these properties is represented by an orthogonal matrix

# Construction / Recognition

## To Verify Distance Preservation:
1. Check $\|f(\mathbf{x})\| = \|\mathbf{x}\|$ for all $\mathbf{x}$ (length preservation)
2. Alternatively, check $f(\mathbf{x}) \cdot f(\mathbf{y}) = \mathbf{x} \cdot \mathbf{y}$ for all $\mathbf{x}, \mathbf{y}$
3. If either holds, the matrix of $f$ is orthogonal

# Context & Application

This characterization shows that the orthogonal group $O_n$ is precisely the group of linear isometries of $\mathbb{R}^n$. It connects the algebraic definition ($A^tA = I$) with the geometric meaning (preserves distances and angles).

# Examples

**Example** (p. 52): For $A \in O_n$:
$$f_A(\mathbf{x}) \cdot f_A(\mathbf{y}) = (\mathbf{x}A^t)(\mathbf{y}A^t)^t = \mathbf{x}A^tA\mathbf{y}^t = \mathbf{x}\mathbf{y}^t = \mathbf{x} \cdot \mathbf{y}.$$

# Relationships

## Builds Upon
- **Orthogonal matrix** — The algebraic characterization

## Related
- **Orthogonal group** — $O_n$ is the group of distance-preserving linear maps

# Common Errors

- **Error**: Assuming any distance-preserving map of $\mathbb{R}^n$ is linear.
  **Correction**: Translations also preserve distances but are not linear (they don't fix the origin). This result is about linear maps specifically.

# Common Confusions

- **Confusion**: Thinking length preservation is weaker than scalar product preservation.
  **Clarification**: For linear maps, they are equivalent. The polarization identity $\mathbf{x} \cdot \mathbf{y} = \frac{1}{2}[\|\mathbf{x}\|^2 - \|\mathbf{x} - \mathbf{y}\|^2 + \|\mathbf{y}\|^2]$ derives the scalar product from lengths.

# Source Reference

Chapter 9: Matrix Groups, pages 52-53 (pdf pp. 52-53). Forward direction on p. 52; converse on p. 53.

# Verification Notes

- Both directions: Proved on pp. 52-53
- Polarization identity: Explicit on p. 53
- Confidence: HIGH — complete bidirectional proof
