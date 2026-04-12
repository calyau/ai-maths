---
concept: Subspace
slug: subspace
category: linear-algebra
subcategory: null
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Vector Spaces"
chapter_number: 3
pdf_page: 89
section: "3.1 Subspaces of R^n"
extraction_confidence: high
aliases:
  - "vector subspace"
prerequisites:
  - vector-space
extends: []
related:
  - null-space
  - column-space
  - row-space
  - span
contrasts_with: []
answers_questions:
  - "What is a vector space?"
---

# Quick Definition

A subspace W of a vector space V is a nonempty subset closed under addition and scalar multiplication: if w, w' are in W and c is a scalar, then w + w' and cw are in W. The zero vector is always in a subspace.

# Core Definition

A subset W of R^n (or more generally, a vector space V) is a subspace if (Artin, p. 89, formula 3.1.2): (a) w + w' is in W for w, w' in W, (b) cw is in W for w in W and scalar c, (c) 0 is in W. Equivalently, W is nonempty and closed under linear combinations (formula 3.1.3).

# Prerequisites

- **Vector space** — A subspace is a subset of a vector space

# Key Properties

1. Must contain the zero vector
2. Closed under addition and scalar multiplication
3. Is itself a vector space
4. The null space of a matrix is a subspace
5. The intersection of subspaces is a subspace
6. dim(W) <= dim(V), with equality iff W = V

# Construction / Recognition

## To Construct:
1. Define W as the solution set of AX = 0, or as the span of some vectors

## To Recognize:
1. Check: (i) W is nonempty, (ii) closed under addition, (iii) closed under scalar multiplication

# Context & Application

Subspaces are the natural sub-objects of vector spaces. The null space, column space, and row space of a matrix are all subspaces. Every subspace of a finite-dimensional space has a basis and a dimension.

# Examples

**Example 1** (p. 89): The set of solutions of AX = 0 is a subspace of R^n (the null space of A).

**Example 2** (p. 90): In R^2, every proper subspace is a line through the origin.

# Relationships

## Builds Upon
- **Vector space** — A subspace is a subset that is a vector space

## Enables
- **Null space** — Subspace of solutions of AX = 0
- **Column space** — Subspace spanned by columns of A
- **Span** — Span of a set of vectors is a subspace

# Common Errors

- **Error**: Forgetting to check that 0 is in W
  **Correction**: If 0 is not in W, then W is not a subspace

# Common Confusions

- **Confusion**: Thinking every subset is a subspace
  **Clarification**: The set {(1,0), (0,1)} is not a subspace of R^2 (not closed under addition)

# Source Reference

Chapter 3: Vector Spaces, Section 3.1, pages 89-90.

# Verification Notes

- Definition source: Direct from (3.1.2), p. 89
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
