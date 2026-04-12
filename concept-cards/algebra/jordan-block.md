---
concept: Jordan Block
slug: jordan-block
category: linear-algebra
subcategory: null
tier: intermediate
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Linear Operators"
chapter_number: 4
pdf_page: 113
section: "4.7 Jordan Form"
extraction_confidence: high
aliases:
  - "J_lambda"
prerequisites:
  - eigenvalue
  - generalized-eigenvector
extends: []
related:
  - jordan-form
contrasts_with: []
answers_questions:
  - "What is the Jordan normal form?"
---

# Quick Definition

A d x d Jordan block J_lambda is a matrix with lambda on the diagonal, 1's on the subdiagonal, and 0's elsewhere. It is the matrix of the restriction of an operator to the span of a generalized eigenvector chain.

# Core Definition

The d x d Jordan block J_lambda has lambda on every diagonal entry, 1 on every subdiagonal entry (position (i+1,i)), and 0 elsewhere (Artin, p. 134, formula 4.7.5). It can be written as J_lambda = lambda*I + J_0, where J_0 is the nilpotent part with 1's on the subdiagonal. The operation of J_0 on the standard basis is e_1 -> e_2 -> ... -> e_d -> 0.

# Prerequisites

- **Eigenvalue** — lambda is an eigenvalue
- **Generalized eigenvector** — The basis comes from a generalized eigenvector chain

# Key Properties

1. The eigenvalue lambda has algebraic multiplicity d
2. The geometric multiplicity is 1 (only one eigenvector, up to scaling)
3. J_lambda = lambda*I + J_0 where J_0 is nilpotent (J_0^d = 0)
4. Powers: J^r = (lambda*I + J_0)^r computed by binomial expansion

# Construction / Recognition

## To Construct:
1. Place lambda on all d diagonal entries
2. Place 1 on all d-1 subdiagonal entries
3. All other entries are 0

## To Recognize:
1. A matrix with a single value on the diagonal and 1's on the subdiagonal

# Context & Application

Jordan blocks are the building blocks of Jordan form. A 1x1 block [lambda] corresponds to an eigenvector; larger blocks indicate generalized eigenvectors. The sizes of blocks determine the structure of the operator.

# Examples

**Example 1** (p. 134): 1x1: [lambda]; 2x2: [[lambda,0],[1,lambda]]; 3x3: [[lambda,0,0],[1,lambda,0],[0,1,lambda]].

# Relationships

## Builds Upon
- **Eigenvalue** — Each block has one eigenvalue
- **Generalized eigenvector** — Basis constructed from generalized eigenvectors

## Enables
- **Jordan form** — Built from Jordan blocks

# Common Errors

- **Error**: Placing 1's above the diagonal instead of below
  **Correction**: In Artin's convention, 1's are on the SUBdiagonal (below)

# Common Confusions

- **Confusion**: Thinking every eigenvalue gets one block
  **Clarification**: An eigenvalue with algebraic multiplicity m may correspond to multiple blocks of various sizes summing to m

# Source Reference

Chapter 4: Linear Operators, Section 4.7, pages 134-135.

# Verification Notes

- Definition source: Direct from (4.7.5), p. 134
- Confidence rationale: Explicitly displayed
- Uncertainties: None (Artin uses subdiagonal convention)
- Cross-reference status: Verified
