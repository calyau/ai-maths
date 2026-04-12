---
concept: Normal Matrix
slug: normal-matrix
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
prerequisites: [hermitian-matrix, unitary-matrix]
extends: []
related: [normal-operator, spectral-theorem-normal]
contrasts_with: []
answers_questions: ["What is a normal matrix?"]
---
# Quick Definition
A normal matrix A commutes with its conjugate transpose: A*A = AA*. Normal matrices are exactly those diagonalizable by a unitary matrix. They include Hermitian (A* = A) and unitary (A* = A^{-1}) matrices as special cases.
# Core Definition
A complex matrix A is normal if A*A = AA* (Artin, p. 258). Normality is the natural class for the Spectral Theorem: A is normal iff there exists a unitary P with P*AP diagonal (Theorem 8.6.6). If P is unitary and A is normal, then P*AP is also normal (Lemma 8.6.2).
# Prerequisites
- **Hermitian matrix** — A special case of normal
- **Unitary matrix** — Another special case of normal
# Key Properties
1. A*A = AA*
2. Diagonalizable by a unitary matrix (Spectral Theorem)
3. Hermitian matrices are normal (A* = A implies commutativity trivially)
4. Unitary matrices are normal (A*A = I = AA*)
5. Preserved under unitary conjugation
# Examples
**Example 1** (p. 258): [[2, i],[-i, 2]] is Hermitian, hence normal.
**Example 2**: Any rotation matrix [[cos t, -sin t],[sin t, cos t]] is orthogonal, hence normal.
# Relationships
## Enables
- **Spectral theorem for normal operators** — Normal = diagonalizable by unitary
## Related
- **Normal operator** — The operator-level concept
# Source Reference
Chapter 8: Bilinear Forms, Section 8.6, pages 258-259.
# Verification Notes
- Definition source: Direct from p. 258
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
