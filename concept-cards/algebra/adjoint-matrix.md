---
concept: Adjoint Matrix
slug: adjoint-matrix
category: bilinear-forms
subcategory: null
tier: intermediate
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Bilinear Forms"
chapter_number: 8
pdf_page: 240
section: "8.3 Hermitian Forms"
extraction_confidence: high
aliases: ["conjugate transpose"]
prerequisites: []
extends: []
related: [hermitian-matrix, unitary-matrix]
contrasts_with: []
answers_questions: ["What is the adjoint (conjugate transpose) of a matrix?"]
---
# Quick Definition
The adjoint A* of a complex matrix A is the complex conjugate of the transpose: the (i,j) entry of A* is the conjugate of a_{ji}. It satisfies (cA)* = c-bar A*, (AB)* = B*A*, and A** = A.
# Core Definition
The adjoint A* of a complex matrix A = (a_{ij}) is the complex conjugate of the transpose matrix A^t: the (i,j) entry of A* is a-bar_{ji} (Artin, p. 244). The rules (8.3.5): (cA)* = c-bar A*, (A+B)* = A* + B*, (AB)* = B*A*, A** = A.
# Prerequisites
This is a foundational computational tool for the chapter.
# Key Properties
1. A* = conjugate(A^t)
2. (AB)* = B*A*
3. A** = A
4. For real matrices, A* = A^t
5. A is Hermitian iff A* = A; unitary iff A* = A^{-1}
# Examples
**Example 1** (p. 244): [[1, 1+i],[2, i]]* = [[1, 2],[1-i, -i]].
# Relationships
## Enables
- **Hermitian matrix** — A* = A
- **Unitary matrix** — A* = A^{-1}
# Source Reference
Chapter 8: Bilinear Forms, Section 8.3, page 244.
# Verification Notes
- Definition source: Direct from p. 244
- Confidence rationale: Explicitly defined with rules
- Uncertainties: None
- Cross-reference status: Verified
