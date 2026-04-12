---
# === CORE IDENTIFICATION ===
concept: Coefficient Matrix of Relations
slug: coefficient-matrix

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
  - "relation matrix"
  - "presentation matrix"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - relation-between-generators
  - finitely-generated-abelian-group
extends: []
related:
  - smith-normal-form
  - row-column-operations
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How are the relations of a finitely generated abelian group encoded as a matrix?"
---

# Quick Definition

The coefficient matrix of a finitely generated abelian group presented by generators $x_1, \ldots, x_n$ and relations $\sum_j a_{ij} x_j = 0$ is the $m \times n$ integer matrix $A = (a_{ij})$, where rows correspond to relations and columns to generators.

# Core Definition

If $G$ is the abelian group determined by generators $x_1, x_2, \ldots, x_n$ and relations $a_{i1}x_1 + a_{i2}x_2 + \cdots + a_{in}x_n = 0$ for $i = 1, \ldots, m$, we form the **coefficient matrix** $A = (a_{ij})$, an $m \times n$ matrix of integers (Armstrong, p. 133).

Row operations on $A$ change the relations (generators of the relation subgroup $N$). Column operations change the generators of the group. Both preserve the isomorphism class of $G$.

# Prerequisites

- **Relation between generators** -- the matrix encodes relations
- **Finitely generated abelian group** -- the group being presented

# Key Properties

1. $A$ is an $m \times n$ integer matrix ($m$ relations, $n$ generators)
2. Row operations change the generating set of $N$ (the relation subgroup) but preserve $G \cong A/N$
3. Column operations change the generators of the free abelian group $A$ but preserve $G$
4. The goal is to reduce $A$ to Smith normal form using these operations

# Construction / Recognition

## To Form the Coefficient Matrix:
1. Write each relation in additive notation: $\sum_j a_{ij} x_j = 0$
2. The $i$th row of $A$ is $(a_{i1}, a_{i2}, \ldots, a_{in})$
3. The matrix has as many rows as relations and as many columns as generators

# Context & Application

The coefficient matrix is the starting point for the abelian group recognition procedure. Reducing it to Smith normal form via row and column operations reveals the canonical form of the group.

# Examples

**Example (i)** (p. 132): Relations $3x + 5y - 3z = 0$ and $4x + 2y = 0$ give the coefficient matrix:
$$\begin{bmatrix} 3 & 5 & -3 \\ 4 & 2 & 0 \end{bmatrix}$$

**Example (iii)** (p. 135): Four relations in five generators give a $4 \times 5$ matrix.

# Relationships

## Builds Upon
- **Relation between generators** -- each relation becomes a row

## Enables
- **Smith normal form** -- the matrix is reduced to diagonal form
- **Row and column operations** -- the tools for reduction

# Source Reference

Chapter 22: Row and Column Operations, pages 132--133.

# Verification Notes

- Definition: Direct from p. 133
- Confidence: HIGH -- explicit definition with examples
