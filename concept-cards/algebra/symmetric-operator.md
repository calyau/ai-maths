---
concept: Symmetric Operator
slug: symmetric-operator
category: bilinear-forms
subcategory: null
tier: intermediate
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Bilinear Forms"
chapter_number: 8
pdf_page: 240
section: "8.6 The Spectral Theorem"
extraction_confidence: high
aliases: []
prerequisites: [euclidean-space]
extends: []
related: [self-adjoint-operator, spectral-theorem-symmetric]
contrasts_with: []
answers_questions: ["What is a symmetric operator?"]
---
# Quick Definition
A symmetric operator T on a Euclidean space satisfies (Tv, w) = (v, Tw) for all v, w. It is the real analogue of a Hermitian (self-adjoint) operator, and the spectral theorem guarantees it has an orthonormal basis of eigenvectors with real eigenvalues.
# Core Definition
A symmetric operator T on a Euclidean space V is a linear operator whose matrix with respect to an orthonormal basis is symmetric (Artin, p. 260). Equivalently, (Tv, w) = (v, Tw) for all v and w (Proposition 8.6.9(a)). The Spectral Theorem 8.6.10 applies.
# Prerequisites
- **Euclidean space** — Symmetric operators act on Euclidean spaces
# Key Properties
1. (Tv, w) = (v, Tw) for all v, w
2. Matrix is symmetric (A^t = A) with respect to orthonormal basis
3. All eigenvalues are real
4. Orthonormal basis of eigenvectors exists (Spectral Theorem 8.6.10)
# Examples
**Example 1** (p. 260): Any real symmetric matrix defines a symmetric operator on R^n.
# Relationships
## Related
- **Self-adjoint operator** — The complex generalization
- **Spectral theorem for symmetric operators** — Applies to symmetric operators
# Source Reference
Chapter 8: Bilinear Forms, Section 8.6, Proposition 8.6.9, Theorem 8.6.10, page 260.
# Verification Notes
- Definition source: Direct from p. 260
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
