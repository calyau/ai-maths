---
concept: Eigenvalue
slug: eigenvalue
category: linear-algebra
subcategory: canonical-forms
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Modules over Principal Ideal Domains"
chapter_number: 12
pdf_page: 474
section: "12.2 The Rational Canonical Form"
extraction_confidence: high
aliases:
  - "eigenvector"
  - "eigenspace"
prerequisites:
  - linear-transformation
  - characteristic-polynomial
extends: []
related:
  - jordan-canonical-form
  - generalized-eigenspace
contrasts_with: []
answers_questions:
  - "What is an eigenvalue?"
---

# Quick Definition
An eigenvalue of T is a scalar $\lambda \in F$ such that $T(v) = \lambda v$ for some nonzero vector v (the corresponding eigenvector). Eigenvalues are the roots of the characteristic polynomial.

# Core Definition
An element $\lambda \in F$ is an eigenvalue of the linear transformation T if there exists a nonzero vector $v \in V$ with $T(v) = \lambda v$; the vector v is an eigenvector. The eigenspace for $\lambda$ is $\{v \in V \mid T(v) = \lambda v\}$. Equivalently (Proposition 12), $\lambda$ is an eigenvalue iff $\lambda I - T$ is singular iff $\det(\lambda I - T) = 0$ (Dummit & Foote, pp. 474-475).

# Prerequisites
- **linear-transformation**, **characteristic-polynomial**

# Key Properties
1. $\lambda$ is an eigenvalue iff $\det(\lambda I - T) = 0$
2. The eigenspace is a subspace (possibly trivial)
3. Eigenvectors for distinct eigenvalues are linearly independent
4. T has at most $n = \dim V$ distinct eigenvalues

# Relationships
## Builds Upon
- **linear-transformation**, **characteristic-polynomial**

## Related
- **jordan-canonical-form**, **generalized-eigenspace**

# Source Reference
Chapter 12, Section 12.2, pp. 474-475.

# Verification Notes
- Confidence: HIGH — standard definition
