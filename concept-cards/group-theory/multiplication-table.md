---
# === CORE IDENTIFICATION ===
concept: Multiplication Table
slug: multiplication-table

# === CLASSIFICATION ===
category: group-fundamentals
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Basic Definitions and Results"
chapter_number: 1
pdf_page: 11
section: "Multiplication tables"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Cayley table
  - group table

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
  - neutral-element
  - inverse-element
extends: []
related:
  - cancellation-laws
  - groups-of-small-order
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a multiplication table for a group?"
  - "What is a Cayley table?"
  - "How can you read off group properties from the multiplication table?"
---

# Quick Definition

A multiplication table (or Cayley table) displays the binary operation of a finite group in a grid, with the entry in row a and column b giving the product ab. The identity element appears when the first row and column repeat the elements, and inverses exist when each element appears exactly once in each row and column.

# Core Definition

A binary operation on a finite set can be described by its **multiplication table**: a square grid where the entry in row a, column b is the product ab. The element e is an identity element if and only if the first row and column simply repeat the elements. Inverses exist if and only if each element occurs exactly once in each row and in each column (see 1.2e). Verifying associativity requires checking n^3 equalities for a group of n elements (p. 11).

# Prerequisites

- **Group** — the multiplication table describes a group's operation
- **Neutral element** — recognized from the table when the first row/column repeat elements
- **Inverse element** — recognized when each element appears once per row and column

# Key Properties

1. The table is an n x n grid for a group of order n
2. The identity is recognized by a row/column that repeats the header
3. Inverses correspond to each element appearing exactly once per row and column (a Latin square)
4. Verifying associativity from the table requires n^3 checks
5. The number of possible binary operations on n elements is n^{n^2}, but very few give groups

# Construction / Recognition

## To Construct:
1. List all group elements as row and column headers
2. Fill entry (a, b) with the product ab
3. The resulting table is a Latin square

## To Recognize a Group Table:
1. The first row and column should repeat the elements (identity exists)
2. Each element appears exactly once in each row and column (Latin square property)
3. Associativity must be verified separately

# Context & Application

Multiplication tables provide a complete but unwieldy description of finite groups. Enumerating all possible tables is an algorithm for finding groups of a given order, but it is impractical for all but the smallest orders. For n = 8, there are 8^{64} possible binary operations but only 5 isomorphism classes of groups (p. 11).

# Examples

**Example 1** (p. 11): The general multiplication table for a group {e, a, b, c, ...} with entries like ee, ea, ab, etc.

**Example 2** (p. 11): The multiplication table of S_3 appears on the front page of the book, with the Latin square property visualized by colors.

**Example 3** (p. 11): For n = 8, there are 8^{64} ≈ 6.28 x 10^{57} possible binary operations but only 5 groups up to isomorphism.

# Relationships

## Builds Upon
- **group** — the table describes the group operation

## Enables
- **groups-of-small-order** — tables can (in principle) enumerate all groups

## Related
- **cancellation-laws** — equivalent to the Latin square property of the table

# Common Errors

- **Error**: Assuming any Latin square is a group table
  **Correction**: A Latin square satisfies closure and the existence of identity/inverses, but associativity must be verified separately

# Common Confusions

- **Confusion**: Thinking multiplication tables are a practical way to study large groups
  **Clarification**: The table has n^2 entries and associativity needs n^3 checks; for even moderate n this is impractical

# Source Reference

Chapter 1: Basic Definitions and Results, section "Multiplication tables," page 11.

# Verification Notes

- Definition source: Direct from text, p. 11
- Confidence rationale: HIGH — explicitly described with properties
- Uncertainties: None
- Cross-reference status: Verified against planned cards
