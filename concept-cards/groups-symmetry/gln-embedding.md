---
# === CORE IDENTIFICATION ===
concept: GL_n Embedding in GL_{n+1}
slug: gln-embedding

# === CLASSIFICATION ===
category: matrix-groups
subcategory: embeddings
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
  - "block diagonal embedding"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - general-linear-group
  - isomorphism
extends: []
related:
  - orthogonal-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does GL_n embed in GL_{n+1}?"
  - "Can smaller matrix groups be viewed inside larger ones?"
---

# Quick Definition

$GL_n$ embeds in $GL_{n+1}$ via $A \mapsto \begin{bmatrix} A & 0 \\ 0 & 1 \end{bmatrix}$. This correspondence is an isomorphism from $GL_n$ to a subgroup of $GL_{n+1}$.

# Core Definition

Armstrong defines (p. 51): if $A \in GL_n$, the $(n+1) \times (n+1)$ matrix $\tilde{A} = \begin{bmatrix} A & 0 \\ 0 & 1 \end{bmatrix}$ belongs to $GL_{n+1}$. "The collection of all matrices formed in this way is a subgroup of $GL_{n+1}$ and the correspondence $A \to \tilde{A}$ shows that $GL_n$ is isomorphic to this subgroup" (p. 51).

Geometrically, identifying $\mathbb{R}^n$ with the subspace of $\mathbb{R}^{n+1}$ having zero last coordinate, $f_{\tilde{A}}$ acts as $f_A$ on $\mathbb{R}^n$ and fixes the last coordinate.

# Prerequisites

- **General linear group** — The groups being embedded
- **Isomorphism** — The embedding is an isomorphism onto its image

# Key Properties

1. $A \mapsto \tilde{A}$ is injective
2. $\widetilde{AB} = \tilde{A}\tilde{B}$ (preserves multiplication)
3. The image is a subgroup of $GL_{n+1}$
4. Geometrically: $f_{\tilde{A}}(\mathbf{x}, z) = (f_A(\mathbf{x}), z)$
5. This gives a chain $GL_1 \hookrightarrow GL_2 \hookrightarrow GL_3 \hookrightarrow \cdots$

# Construction / Recognition

## To Embed:
1. Take $A \in GL_n$
2. Add a column of zeros on the right
3. Add a row of zeros on the bottom, with a 1 in the corner
4. The result is $\tilde{A} \in GL_{n+1}$

# Context & Application

This embedding shows that the general linear groups form an increasing chain. The same construction works for $O_n \hookrightarrow O_{n+1}$ and $SO_n \hookrightarrow SO_{n+1}$. Armstrong uses a variant in Exercise 9.10 to embed $O_2$ into $SO_3$.

# Examples

**Example** (p. 51): $GL_1 \cong \mathbb{R} \setminus \{0\}$ embeds into $GL_2$ via $a \mapsto \begin{bmatrix} a & 0 \\ 0 & 1 \end{bmatrix}$.

# Relationships

## Builds Upon
- **General linear group** — Source and target of the embedding

## Related
- **Orthogonal group** — Analogous embeddings $O_n \hookrightarrow O_{n+1}$

# Common Errors

- **Error**: Placing the extra row/column in the wrong position.
  **Correction**: The convention is: existing matrix in the upper-left block, 1 in the bottom-right corner, zeros elsewhere.

# Common Confusions

- **Confusion**: Thinking the embedding changes the linear transformation.
  **Clarification**: The embedded transformation acts identically on $\mathbb{R}^n$ and fixes the extra coordinate. It is the "same" transformation viewed in a larger space.

# Source Reference

Chapter 9: Matrix Groups, page 51 (pdf p. 51).

# Verification Notes

- Definition: Direct from p. 51
- Geometric interpretation: Explicit on p. 51
- Confidence: HIGH — explicit construction
