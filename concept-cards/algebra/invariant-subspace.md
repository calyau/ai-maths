---
concept: Invariant Subspace
slug: invariant-subspace
category: linear-algebra
subcategory: null
tier: intermediate
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Linear Operators"
chapter_number: 4
pdf_page: 113
section: "4.4 Eigenvectors"
extraction_confidence: high
aliases:
  - "T-invariant subspace"
prerequisites:
  - linear-operator
  - subspace
extends:
  - subspace
related:
  - eigenvector
  - eigenspace
  - direct-sum
contrasts_with: []
answers_questions:
  - "What is a linear transformation?"
---

# Quick Definition

A subspace W of V is T-invariant if T carries W into itself: T(W) ⊆ W. When W is invariant, T restricts to a linear operator on W. Eigenvectors span one-dimensional invariant subspaces.

# Core Definition

A subspace W of V is invariant (or T-invariant) if TW ⊆ W, meaning T(w) is in W whenever w is in W (Artin, p. 121, formula 4.4.1). When W is invariant, T defines a linear operator on W called its restriction T|_W. If a basis starts with a basis of W, the matrix has block form [[A,B],[0,D]].

# Prerequisites

- **Linear operator** — T: V -> V
- **Subspace** — W is a subspace of V

# Key Properties

1. T(W) ⊆ W
2. The restriction T|_W is a linear operator on W
3. If V = W_1 ⊕ W_2 with both invariant, the matrix is block diagonal
4. Eigenvectors span 1-dimensional invariant subspaces
5. Eigenspaces are invariant subspaces

# Construction / Recognition

## To Construct:
1. An eigenspace is always invariant
2. ker(T) and im(T) are invariant for T

## To Recognize:
1. Check that T(w) is in W for all w in W

# Context & Application

Invariant subspaces are the key to analyzing linear operators. Finding enough invariant subspaces decomposes the operator into simpler pieces, leading to diagonalization or Jordan form.

# Examples

**Example 1** (p. 121): If v is an eigenvector, span{v} is a 1-dimensional invariant subspace.

**Example 2** (p. 121): If V = W_1 ⊕ W_2 with both T-invariant, the matrix is block diagonal [[A_1,0],[0,A_2]].

# Relationships

## Builds Upon
- **Subspace** — An invariant subspace is a subspace with extra property
- **Linear operator** — Invariance is relative to an operator

## Enables
- **Eigenvector** — Spans a 1-dimensional invariant subspace
- **Jordan form** — Built from chains of invariant subspaces

# Common Errors

- **Error**: Assuming ker(T) is not invariant
  **Correction**: ker(T) is always T-invariant (T sends 0 to 0)

# Common Confusions

- **Confusion**: Thinking every subspace is invariant
  **Clarification**: Most subspaces are NOT invariant under a given operator

# Source Reference

Chapter 4: Linear Operators, Section 4.4, pages 121-122.

# Verification Notes

- Definition source: Direct from (4.4.1), p. 121
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
