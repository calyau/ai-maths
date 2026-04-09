---
# === CORE IDENTIFICATION ===
concept: Cayley Table
slug: cayley-table

# === CLASSIFICATION ===
category: group-theory
subcategory: group-definitions
tier: foundational

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Groups"
chapter_number: 3
pdf_page: 47
section: "Definitions and Examples"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - multiplication table
  - group table

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
  - binary-operation
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a group?"
  - "How do I determine if a set with an operation forms a group?"
---

# Quick Definition

A Cayley table is a square table that displays the results of a binary operation on every pair of elements in a finite group, with row and column headers listing the group elements.

# Core Definition

"It is often convenient to describe a group in terms of an addition or multiplication table. Such a table is called a Cayley table" (Judson, p. 47).

# Prerequisites

- **Group** — Cayley tables display the structure of groups
- **Binary operation** — The table records the binary operation

# Key Properties

1. The table has $|G|$ rows and $|G|$ columns
2. Each row and column contains every group element exactly once (Latin square property)
3. Commutativity corresponds to symmetry about the main diagonal
4. The identity element's row and column reproduce the headers

# Construction / Recognition

## To Construct a Cayley Table:
1. List all elements of $G$ as row and column headers
2. For each pair $(a, b)$, compute $a \circ b$ and enter it in row $a$, column $b$
3. The resulting table completely describes the group structure

# Context & Application

Cayley tables provide a complete description of finite groups and are useful for verifying group axioms, checking commutativity, finding inverses, and understanding group structure.

# Examples

**Example 1** (p. 47): The Cayley table for $(\mathbb{Z}_5, +)$ is a $5 \times 5$ table showing all sums modulo 5.

**Example 2** (p. 46): The multiplication table for the symmetries of an equilateral triangle (Figure 3.7) shows $S_3$ is nonabelian.

**Example 3** (p. 48): The multiplication table for $U(8) = \{1, 3, 5, 7\}$ under multiplication mod 8.

# Relationships

## Builds Upon
- **group** — Represents group structure
- **binary-operation** — Displays operation results

## Enables
- **abelian-group** — Can verify commutativity from table symmetry
- **subgroup** — Subtables reveal subgroups

# Common Errors

- **Error**: Making errors in modular arithmetic when filling in the table
  **Correction**: Carefully compute each entry, especially when working modulo $n$

# Common Confusions

- **Confusion**: Thinking the Cayley table approach works for infinite groups
  **Clarification**: Cayley tables are practical only for finite groups

# Source Reference

Chapter 3: Groups, Section 3.2, page 47. Figures 3.7, 3.10, 3.12.

# Verification Notes

- Definition source: Direct from p. 47
- Confidence: HIGH — explicit definition with multiple examples
- Cross-reference status: Verified
- Uncertainties: None
