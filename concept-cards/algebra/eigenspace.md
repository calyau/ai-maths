---
concept: Eigenspace
slug: eigenspace
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
  - "V(lambda)"
prerequisites:
  - eigenvector
  - eigenvalue
  - subspace
extends:
  - subspace
related:
  - diagonalization
  - direct-sum
contrasts_with: []
answers_questions:
  - "What is an eigenvalue/eigenvector?"
---

# Quick Definition

The eigenspace V(lambda) of a linear operator T for eigenvalue lambda is the set of all eigenvectors with eigenvalue lambda, together with the zero vector. It is the kernel of (lambda*I - T), a T-invariant subspace.

# Core Definition

The eigenspace V(lambda) is the set of eigenvectors of T with eigenvalue lambda, together with 0. It equals ker(lambda*I - T) = {v in V : T(v) = lambda*v} (Artin, Exercise 4.1, p. 132). Its dimension is the geometric multiplicity of lambda, which is at most the algebraic multiplicity (the multiplicity of lambda as a root of the characteristic polynomial).

# Prerequisites

- **Eigenvector** — Eigenspace consists of eigenvectors (plus 0)
- **Eigenvalue** — Each eigenspace is associated to an eigenvalue
- **Subspace** — The eigenspace is a subspace

# Key Properties

1. V(lambda) = ker(lambda*I - T)
2. V(lambda) is a T-invariant subspace
3. dim V(lambda) is the geometric multiplicity of lambda
4. geometric multiplicity <= algebraic multiplicity
5. T is diagonalizable iff V = V(lambda_1) ⊕ ... ⊕ V(lambda_k)

# Construction / Recognition

## To Construct:
1. Fix eigenvalue lambda
2. Solve (lambda*I - A)X = 0
3. The solution space is V(lambda)

## To Recognize:
1. The null space of lambda*I - A

# Context & Application

Eigenspaces decompose V when T is diagonalizable: V = V(lambda_1) ⊕ ... ⊕ V(lambda_k). If eigenspaces are too small (geometric < algebraic multiplicity), generalized eigenspaces are needed.

# Examples

**Example 1** (p. 126): For A = [[3,2],[1,4]], eigenspace V(5) = span{(1,1)^t}, eigenspace V(2) = span{(2,-1)^t}.

# Relationships

## Builds Upon
- **Eigenvector** — Eigenspace = {eigenvectors with given eigenvalue} ∪ {0}

## Enables
- **Diagonalization** — Possible iff eigenspaces fill V

## Related
- **Direct sum** — Eigenspace decomposition is a direct sum

# Common Errors

- **Error**: Forgetting that 0 is in the eigenspace (but is NOT an eigenvector)
  **Correction**: V(lambda) is a subspace and must contain 0

# Common Confusions

- **Confusion**: Thinking eigenspaces for different eigenvalues can overlap
  **Clarification**: Eigenspaces for distinct eigenvalues intersect only in {0}

# Source Reference

Chapter 4: Linear Operators, Sections 4.4-4.6.

# Verification Notes

- Definition source: From Exercise 4.1 and Section 4.4
- Confidence rationale: Standard concept used throughout Ch 4
- Uncertainties: None
- Cross-reference status: Verified
