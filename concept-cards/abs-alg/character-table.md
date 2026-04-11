---
concept: Character Table
slug: character-table
category: representation-theory
subcategory: character-theory
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Representation Theory and Character Theory"
chapter_number: 18
pdf_page: 870
section: "18.3 Character Theory and the Orthogonality Relations"
extraction_confidence: high
aliases: []
prerequisites:
  - character
  - orthogonality-relations
extends: []
related:
  - class-function
contrasts_with: []
answers_questions:
  - "What is a character table?"
---

# Quick Definition
The character table of G is the matrix whose rows are irreducible characters and columns are conjugacy classes. It is a square matrix that encodes the representation theory of G.

# Core Definition
The **character table** of G is the r × r matrix (where r is the number of conjugacy classes) with entries χ_i(g_j), where χ_1,...,χ_r are the irreducible characters and g_1,...,g_r represent the conjugacy classes (p. 870). By the orthogonality relations, the rows are orthogonal and the columns are orthogonal (with appropriate weights).

# Prerequisites
- **character** — Rows are irreducible characters
- **orthogonality-relations** — Determine the table entries

# Key Properties
1. Square matrix (number of irreducible characters = number of conjugacy classes)
2. First row is always the trivial character (all 1's)
3. First column entries are the degrees n_i, and Σn_i^2 = |G|
4. The table determines G up to "isocategorical" equivalence

# Source Reference
Chapter 18, Section 18.3, pages 870-878.

# Verification Notes
- Confidence: HIGH — explicit construction described
