---
# === CORE IDENTIFICATION ===
concept: Row and Column Operations
slug: row-column-operations

# === CLASSIFICATION ===
category: structure-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Row and Column Operations"
chapter_number: 22
pdf_page: 132
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "integer row and column operations"
  - "elementary operations"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - coefficient-matrix
extends: []
related:
  - smith-normal-form
  - abelian-group-recognition
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What operations can be performed on the coefficient matrix to simplify it?"
  - "How do row and column operations affect the group presentation?"
---

# Quick Definition

Three types of integer row and column operations are used to reduce the coefficient matrix to Smith normal form: (I) interchange two rows/columns, (II) multiply a row/column by $-1$, (III) add an integer multiple of one row/column to another.

# Core Definition

The following operations are applied to the coefficient matrix $A = (a_{ij})$ of an abelian group presentation (Armstrong, p. 133):

- **(I)** Interchange two rows or two columns
- **(II)** Multiply all entries of a row or a column by $-1$
- **(III)** Add an integer multiple of one row to another row, or an integer multiple of one column to another column

Operations on rows alter the relations; operations on columns alter the generators. Both preserve the isomorphism class of the group $G$ throughout.

# Prerequisites

- **Coefficient matrix** -- the matrix being operated on

# Key Properties

1. Row operations change the generators of the relation subgroup $N$ but preserve $G = A/N$
2. Column operations change the generators of the free abelian group $A$ but preserve $G$
3. The group $G$ is invariant under all three types of operations
4. These are the same as elementary operations over $\mathbb{Z}$ (not over a field -- no division)
5. Type III is the workhorse; Types I and II are for bookkeeping

# Construction / Recognition

## How Each Operation Affects the Presentation:

**Row operations** (change relations):
- Type I: Reorder relations
- Type II: Negate a relation (equivalent relation)
- Type III: Replace relation $R_i$ by $R_i + qR_j$ (new relation is an integer combination of old ones)

**Column operations** (change generators):
- Type I: Reorder generators
- Type II: Replace generator $x_j$ by $-x_j$
- Type III: Replace generator $x_j$ by $x_j + qx_i$ (new generating set)

# Context & Application

These operations are the computational engine for the Smith normal form algorithm. They allow systematic reduction of any integer matrix to diagonal form with the divisibility chain property.

# Examples

**Example (i)** (p. 132): Starting from $\begin{bmatrix} 3 & 5 & -3 \\ 4 & 2 & 0 \end{bmatrix}$, a sequence of row and column operations produces $\begin{bmatrix} 1 & 0 & 0 \\ 0 & 2 & 0 \end{bmatrix}$, revealing $G \cong \mathbb{Z}_2 \times \mathbb{Z}$.

# Relationships

## Builds Upon
- **Coefficient matrix** -- the object being transformed

## Enables
- **Smith normal form** -- achieved through these operations
- **Abelian group recognition** -- the overall procedure

# Common Errors

- **Error**: Dividing a row by an integer (not an allowed operation over $\mathbb{Z}$).
  **Correction**: Unlike linear algebra over fields, only multiplication by $\pm 1$ is allowed (Type II). Type III adds integer multiples, never fractions.

# Common Confusions

- **Confusion**: Thinking row operations change the group.
  **Clarification**: Row operations change the generators of $N$, but $N$ itself (and hence $G = A/N$) is unchanged.

# Source Reference

Chapter 22: Row and Column Operations, page 133. Operations I, II, III defined explicitly.

# Verification Notes

- Definitions: Direct from p. 133
- Interpretation: Direct from p. 133
- Confidence: HIGH -- explicitly listed and explained
