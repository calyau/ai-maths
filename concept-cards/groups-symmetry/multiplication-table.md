---
# === CORE IDENTIFICATION ===
concept: Multiplication Table
slug: multiplication-table

# === CLASSIFICATION ===
category: fundamentals
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Dihedral Groups"
chapter_number: 4
pdf_page: 22
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - Cayley table
  - group table

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
extends: []
related:
  - dihedral-group
  - order-of-a-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I compute a multiplication table for a dihedral group?"
  - "What is a group?"
---

# Quick Definition

A multiplication table (or Cayley table) of a finite group displays all products xy in a square array, where the entry at row x and column y gives the product xy. Each element appears exactly once in every row and column.

# Core Definition

Armstrong introduces the multiplication table for D_3: "The following table, called a multiplication table, shows all 36 possible products xy of ordered pairs of elements x, y taken from D_3. The product xy lies at the intersection of row x with column y" (Armstrong, Ch. 4, p. 24).

# Prerequisites

- **Group** — Multiplication tables display group structure

# Key Properties

1. The table is a square array with rows and columns indexed by group elements
2. Entry at row x, column y is the product xy
3. Each element appears exactly once in every row
4. Each element appears exactly once in every column
5. The row and column of the identity reproduce the elements in order
6. The identity appears exactly once in each row (at the position of x^{-1} in column)
7. The table is symmetric about the main diagonal if and only if the group is abelian

# Construction / Recognition

## To Construct:
1. List all group elements along the top row and left column
2. For each pair (x, y), compute the product xy
3. Place the result at the intersection of row x and column y
4. Verify each element appears exactly once per row and per column

# Context & Application

The multiplication table completely describes a finite group's structure. Armstrong uses it for D_3 to show concretely how the six elements combine. The property that each element appears once per row/column is proved in Exercise 4.4.

# Examples

**Example 1** (p. 24): The multiplication table of D_3 is a 6x6 table. For instance, the entry at row s and column rs is s(rs) = r^2, readable from the table.

**Example 2** (p. 24): "Each element of the group appears exactly once in every row and every column of the table. This is true of the multiplication table of any group."

# Relationships

## Builds Upon
- **Group** — Tables display group structure

## Related
- **Dihedral Group** — Armstrong's primary table example is D_3
- **Order of a Group** — The table is |G| x |G|

# Common Errors

- **Error**: Confusing row x, column y with column x, row y (i.e., computing yx instead of xy)
  **Correction**: Convention is that the product xy is at row x, column y

# Common Confusions

- **Confusion**: Thinking multiplication tables are only for commutative groups
  **Clarification**: Any finite group has a multiplication table; non-abelian groups simply have asymmetric tables

# Source Reference

Chapter 4: Dihedral Groups, page 17 (pdf p. 24). See also Exercise 4.4.

# Verification Notes

- Definition source: Direct quote from p. 24
- Confidence rationale: High — explicitly defined with full example
- Uncertainties: None
- Cross-reference status: Verified
