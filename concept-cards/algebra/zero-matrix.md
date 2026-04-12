---
concept: Zero Matrix
slug: zero-matrix
category: matrices
subcategory: special-matrices
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
  - "O"
  - "null matrix"
prerequisites:
  - matrix
extends: []
related:
  - identity-matrix
  - matrix-addition
contrasts_with:
  - identity-matrix
answers_questions:
  - "What is a matrix and what are its basic operations?"
---

# Quick Definition

A zero matrix is a matrix all of whose entries are 0. It is the additive identity: A + O = A for any matrix A of the same shape. It is denoted by O.

# Core Definition

A matrix all of whose entries are 0 is called a zero matrix, denoted simply by O when there is no danger of confusion (Artin, p. 16).

# Prerequisites

- **Matrix** — The zero matrix is a special case

# Key Properties

1. All entries are 0
2. Acts as the additive identity: A + O = A
3. AO = O and OA = O for any compatible matrix A
4. Not invertible (has a row of zeros)

# Construction / Recognition

## To Construct:
1. Set every entry to 0

## To Recognize:
1. Every entry is 0

# Context & Application

The zero matrix is the additive identity for matrix addition and plays the role of 0 in the vector space of matrices.

# Examples

**Example 1** (p. 16): The 2x2 zero matrix is [[0,0],[0,0]].

# Relationships

## Builds Upon
- **Matrix** — Special case

## Contrasts With
- **Identity matrix** — The multiplicative identity (all diagonal 1's)

# Common Errors

- **Error**: Treating the zero matrix as invertible
  **Correction**: The zero matrix is never invertible

# Common Confusions

- **Confusion**: Confusing the zero matrix with the number 0
  **Clarification**: The zero matrix is a matrix; its size depends on context

# Source Reference

Chapter 1: Matrices, Section 1.1, page 16.

# Verification Notes

- Definition source: Direct from p. 16
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
