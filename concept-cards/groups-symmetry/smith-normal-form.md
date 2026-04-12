---
# === CORE IDENTIFICATION ===
concept: Smith Normal Form
slug: smith-normal-form

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
section: "Theorem 22.1"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "diagonal form"
  - "Smith form"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - row-column-operations
  - coefficient-matrix
extends: []
related:
  - abelian-group-recognition
  - classification-of-fg-abelian-groups
  - torsion-coefficients
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Smith normal form of an integer matrix?"
  - "How do I classify finitely generated abelian groups using row/column operations?"
---

# Quick Definition

The Smith normal form of an $m \times n$ integer matrix $A$ is a diagonal matrix $D$ with non-negative diagonal entries $d_1, d_2, \ldots, d_k$ (where $k = \min(m, n)$) satisfying $d_1 \mid d_2 \mid \cdots \mid d_k$, obtained from $A$ by integer row and column operations.

# Core Definition

**(22.1) Theorem.** Given an $m \times n$ matrix $A$ whose entries are integers, there is a finite sequence of operations of type I, II, III that converts $A$ into a diagonal matrix $D$ for which $d_{ii} \ge 0$, $1 \le i \le k$, and $d_{11} \mid d_{22} \mid \cdots \mid d_{kk}$, where $k = \min(m, n)$ (Armstrong, p. 133).

# Prerequisites

- **Row and column operations** -- the tools used to achieve the form
- **Coefficient matrix** -- the matrix being reduced

# Key Properties

1. $D$ is diagonal with non-negative entries
2. The diagonal entries satisfy the divisibility chain $d_1 \mid d_2 \mid \cdots \mid d_k$
3. The diagonal entries are unique (they are invariants of the matrix)
4. If $d_1 = \cdots = d_s = 1$, those generators are redundant
5. If $d_{t+1} = \cdots = d_k = 0$, those generators have infinite order
6. The group determined by the matrix is $\mathbb{Z}_{d_{s+1}} \times \cdots \times \mathbb{Z}_{d_t} \times \mathbb{Z}^{n-t}$

# Construction / Recognition

## Algorithm (Outline, pp. 134--135):
1. If $A$ is zero, done. Otherwise, use Type I and II to make $a_{11}$ positive
2. Use Type III column operations and Type I interchanges to make $a_{11}$ divide every entry in row 1
3. Subtract multiples of column 1 to zero out the rest of row 1
4. Similarly use row operations to zero out the rest of column 1, yielding $\begin{bmatrix} c_{11} & 0 \\ 0 & C_1 \end{bmatrix}$
5. Check: does $c_{11}$ divide every entry of $C_1$? If not, add an offending row to row 1 and restart (this reduces $c_{11}$)
6. Once $c_{11}$ divides every entry of $C_1$, set $d_1 = c_{11}$ and repeat the process on $C_1$
7. Continue until fully diagonal with the divisibility chain

# Context & Application

Smith normal form is the computational procedure for determining the canonical form of a finitely generated abelian group from its generators and relations. It makes the classification theorem (21.1) effective and algorithmic.

# Examples

**Example (i)** (p. 132): $\begin{bmatrix} 3 & 5 & -3 \\ 4 & 2 & 0 \end{bmatrix} \to \begin{bmatrix} 1 & 0 & 0 \\ 0 & 2 & 0 \end{bmatrix}$. So $G \cong \mathbb{Z}_2 \times \mathbb{Z}$ (the $d_1 = 1$ generator is redundant, $d_2 = 2$ gives $\mathbb{Z}_2$, and the third generator has no relation, giving $\mathbb{Z}$).

**Example (ii)** (p. 135): $\begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix} \to \begin{bmatrix} 1 & 0 \\ 0 & 6 \end{bmatrix}$. So $\mathbb{Z}_2 \times \mathbb{Z}_3 \cong \mathbb{Z}_6$.

**Example (iii)** (p. 135): A $4 \times 5$ matrix reduces to $\begin{bmatrix} 1 & 0 & 0 & 0 & 0 \\ 0 & 2 & 0 & 0 & 0 \\ 0 & 0 & 4 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}$, giving $G \cong \mathbb{Z}_2 \times \mathbb{Z}_4 \times \mathbb{Z} \times \mathbb{Z}$.

# Relationships

## Builds Upon
- **Row and column operations** -- the tools for reduction
- **Coefficient matrix** -- the starting point

## Enables
- **Abelian group recognition** -- the canonical form is read from the Smith normal form

## Related
- **Classification of f.g. abelian groups** -- Smith normal form makes the classification computational
- **Torsion coefficients** -- the non-unit, non-zero diagonal entries in the Smith normal form

# Common Errors

- **Error**: Stopping at a diagonal matrix without checking the divisibility chain.
  **Correction**: As Armstrong warns (p. 134), a diagonal matrix whose entries do not satisfy $d_1 \mid d_2 \mid \cdots \mid d_k$ is NOT in Smith normal form. One must check that $d_1$ divides every entry of the remaining submatrix and restart if necessary.

- **Error**: Forgetting that zeros on the diagonal correspond to free ($\mathbb{Z}$) factors.
  **Correction**: A zero diagonal entry means the corresponding generator has infinite order and contributes a $\mathbb{Z}$ factor.

# Common Confusions

- **Confusion**: Thinking Smith normal form is unique to group theory.
  **Clarification**: Smith normal form exists for any integer matrix and is used in many areas of algebra (module theory, algebraic topology, etc.).

# Source Reference

Chapter 22: Row and Column Operations, Theorem 22.1, pages 133--136. Algorithm outline pp. 134--135, examples pp. 132--136.

# Verification Notes

- Theorem and algorithm: Direct from pp. 133--135
- All three examples verified against source
- Confidence: HIGH -- central theorem with detailed algorithm and examples
