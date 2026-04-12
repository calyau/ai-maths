---
# === CORE IDENTIFICATION ===
concept: Two-Row Notation
slug: two-row-notation

# === CLASSIFICATION ===
category: permutation-groups
subcategory: notation
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Permutations"
chapter_number: 6
pdf_page: 33
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "matrix notation for permutations"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - permutation
extends: []
related:
  - cycle-notation
contrasts_with:
  - cycle-notation

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I write a permutation in two-row notation?"
---

# Quick Definition

Two-row notation writes a permutation by listing integers $1, \ldots, n$ on the top row and their images on the bottom row: $\begin{bmatrix} 1 & 2 & \cdots & n \\ \alpha(1) & \alpha(2) & \cdots & \alpha(n) \end{bmatrix}$.

# Core Definition

Armstrong introduces permutations in two-row notation (p. 33). For a permutation $\alpha$ of $\{1, \ldots, n\}$, the top row lists the integers in order and the bottom row lists their images: "To find the image of an integer under a particular permutation just look vertically underneath it" (p. 33). This notation is explicit but "when extended to higher values of $n$, this notation is too cumbersome to work with" (p. 33), motivating the switch to cycle notation.

# Prerequisites

- **Permutation** — Two-row notation represents permutations

# Key Properties

1. Top row: $1, 2, \ldots, n$ in order
2. Bottom row: the images $\alpha(1), \alpha(2), \ldots, \alpha(n)$
3. Reading: to find $\alpha(k)$, look below $k$
4. Composition: apply right factor first, using the table to track images
5. Becomes unwieldy for large $n$

# Construction / Recognition

## To Write in Two-Row Notation:
1. List $1, 2, \ldots, n$ as the top row
2. Under each $k$, write $\alpha(k)$

## To Compute a Product $\alpha\beta$:
1. For each $k$: first find $\beta(k)$ from $\beta$'s table, then find $\alpha(\beta(k))$ from $\alpha$'s table
2. Write the result as a new two-row array

# Context & Application

Two-row notation is Armstrong's starting point for permutations. It is completely explicit (every element and its image is listed), making it easy to verify computations. However, it is quickly replaced by the more compact cycle notation.

# Examples

**Example** (p. 33): The six elements of $S_3$ in two-row notation:
$$\varepsilon = \begin{bmatrix} 123 \\ 123 \end{bmatrix}, \begin{bmatrix} 123 \\ 213 \end{bmatrix}, \begin{bmatrix} 123 \\ 321 \end{bmatrix}, \begin{bmatrix} 123 \\ 132 \end{bmatrix}, \begin{bmatrix} 123 \\ 231 \end{bmatrix}, \begin{bmatrix} 123 \\ 312 \end{bmatrix}.$$

**Example** (p. 33): Composition in two-row notation:
$$\begin{bmatrix} 123 \\ 213 \end{bmatrix}\begin{bmatrix} 123 \\ 132 \end{bmatrix} = \begin{bmatrix} 123 \\ 231 \end{bmatrix}.$$

# Relationships

## Builds Upon
- **Permutation** — A notation for permutations

## Contrasts With
- **Cycle notation** — More compact but less explicit

# Common Errors

- **Error**: Applying the left factor first in a product.
  **Correction**: $\alpha\beta$ means apply $\beta$ first, then $\alpha$: $\alpha\beta(x) = \alpha(\beta(x))$.

# Common Confusions

- **Confusion**: Thinking two-row notation and cycle notation represent different objects.
  **Clarification**: They represent the same permutations in different formats. Two-row is more explicit; cycle notation is more compact.

# Source Reference

Chapter 6: Permutations, page 33 (pdf p. 33).

# Verification Notes

- Definition: Direct from p. 33
- Examples: All from source
- Confidence: HIGH — explicit notation with examples
