---
concept: Pivot
slug: pivot
category: matrices
subcategory: null
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Matrices"
chapter_number: 1
pdf_page: 12
section: "1.2 Row Reduction"
extraction_confidence: high
aliases:
  - "leading 1"
prerequisites:
  - row-echelon-form
extends: []
related:
  - rank
  - row-reduction
contrasts_with: []
answers_questions:
  - "How do I row-reduce a matrix?"
---

# Quick Definition

A pivot is the first nonzero entry in a nonzero row of a row echelon matrix, normalized to 1. The number of pivots equals the rank of the matrix. Columns with pivots correspond to "bound" variables; columns without pivots correspond to "free" variables.

# Core Definition

In a row echelon matrix, the first nonzero entry of each nonzero row is 1; this entry is called a pivot (Artin, p. 20, formula 1.2.12 property (b)). Pivots form a staircase pattern: each pivot is to the right of the one above.

# Prerequisites

- **Row echelon form** — Pivots are defined in echelon form

# Key Properties

1. Each pivot is 1
2. Pivots form a staircase pattern (each is right of the one above)
3. Entries above and below pivots are 0
4. Number of pivots = rank of the matrix
5. Columns without pivots correspond to free variables

# Construction / Recognition

## To Construct:
1. Row-reduce to echelon form
2. The leading 1's are the pivots

## To Recognize:
1. The first nonzero entry in each nonzero row of an echelon matrix

# Context & Application

Pivots determine the structure of the solution set: pivot columns give bound variables, non-pivot columns give free variables. The number of pivots is the rank.

# Examples

**Example 1** (p. 19): In [[1,0,-1,0,3],[0,1,3,0,1],[0,0,0,1,1]], pivots are in columns 1, 2, 4.

# Relationships

## Builds Upon
- **Row echelon form** — Pivots appear in echelon matrices

## Enables
- **Rank** — Number of pivots
- Solutions of linear systems (bound vs. free variables)

# Common Errors

- **Error**: Counting nonzero entries instead of leading 1's
  **Correction**: Only the FIRST nonzero entry (normalized to 1) in each row is a pivot

# Common Confusions

- **Confusion**: Thinking pivots can appear in any position
  **Clarification**: Pivots must form a staircase (each strictly right of the one above)

# Source Reference

Chapter 1: Matrices, Section 1.2, page 20.

# Verification Notes

- Definition source: From (1.2.12), p. 20
- Confidence rationale: Explicitly defined within echelon form
- Uncertainties: None
- Cross-reference status: Verified
