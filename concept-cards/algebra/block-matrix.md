---
concept: Block Matrix
slug: block-matrix
category: matrices
subcategory: matrix-operations
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Matrices"
chapter_number: 1
pdf_page: 12
section: "1.1 The Basic Operations"
extraction_confidence: high
aliases:
  - "block multiplication"
  - "partitioned matrix"
prerequisites:
  - matrix
  - matrix-multiplication
extends: []
related:
  - augmented-matrix
contrasts_with: []
answers_questions:
  - "What is a matrix and what are its basic operations?"
---

# Quick Definition

A block matrix is a matrix partitioned into rectangular submatrices (blocks). Block multiplication follows the same rules as ordinary matrix multiplication, treating blocks as entries, provided the blocks have compatible sizes.

# Core Definition

Matrices M and M' can be decomposed into blocks and multiplied by treating the blocks as entries. For two-block decomposition: if M = [A|B] and M' = [A'/B'], then MM' = AA' + BB'. For four-block decomposition, the rule mirrors 2x2 multiplication (Artin, pp. 18-19, formulas 1.1.19-1.1.20).

# Prerequisites

- **Matrix** — The containing structure
- **Matrix multiplication** — Block multiplication follows the same rules

# Key Properties

1. Block multiplication follows the same rules as ordinary matrix multiplication
2. Blocks must have compatible sizes for the products to be defined
3. Useful for simplifying computations and proofs by induction

# Construction / Recognition

## To Construct:
1. Partition a matrix into rectangular submatrices along consistent row and column boundaries
2. Ensure block sizes are compatible for any intended multiplication

## To Recognize:
1. A matrix divided into rectangular regions by horizontal and vertical lines

# Context & Application

Block multiplication simplifies computations and is a key tool for proving facts about matrices by induction. It appears in many proofs throughout the text, including the proof of the Jordan decomposition.

# Examples

**Example 1** (p. 19): [[1,0,5],[0,1,3]] * [[2,3,1,1],[4,8,0,0],[1,0,1,0]] computed by block multiplication.

# Relationships

## Builds Upon
- **Matrix multiplication** — Block multiplication extends ordinary multiplication

## Related
- **Augmented matrix** — A block matrix [A|B] used in row reduction

# Common Errors

- **Error**: Partitioning blocks with incompatible sizes for multiplication
  **Correction**: The column partition of the left matrix must match the row partition of the right

# Common Confusions

- **Confusion**: Thinking block multiplication always gives the same result as regular multiplication
  **Clarification**: It does give the same result — it is just a different way to organize the computation

# Source Reference

Chapter 1: Matrices, Section 1.1, pages 18-19.

# Verification Notes

- Definition source: Direct from (1.1.19)-(1.1.20), pp. 18-19
- Confidence rationale: Explicitly defined with verification exercises
- Uncertainties: None
- Cross-reference status: Verified
