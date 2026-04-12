---
concept: Positive Definite Matrix Criterion
slug: positive-definite-matrix-criterion
category: bilinear-forms
subcategory: null
tier: intermediate
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Bilinear Forms"
chapter_number: 8
pdf_page: 240
section: "8.4 Orthogonality"
extraction_confidence: high
aliases: ["leading minor criterion"]
prerequisites: [positive-definite-form]
extends: []
related: []
contrasts_with: []
answers_questions: ["How do I check if a matrix is positive definite?"]
---
# Quick Definition
A symmetric matrix A is positive definite if and only if det(A_k) > 0 for k = 1, ..., n, where A_k is the k x k leading principal minor.
# Core Definition
Theorem 8.4.19: A symmetric form and its matrix A are positive definite if and only if det A_k > 0 for k = 1, ..., n, where A_k denotes the k x k minor formed by the first k rows and columns (Artin, p. 255).
# Prerequisites
- **Positive definite form** — The property being tested
# Key Properties
1. Check leading principal minors: det A_1 > 0, det A_2 > 0, ..., det A_n > 0
2. Only needs n determinant computations
3. Does not require computing eigenvalues
# Examples
**Example 1** (p. 255): A = [[2, 1],[1, 1]] is positive definite because det[2] = 2 > 0 and det A = 1 > 0.
# Relationships
## Builds Upon
- **Positive definite form** — This criterion characterizes positive definiteness
# Common Errors
- **Error**: Only checking det A > 0
  **Correction**: Must check ALL leading minors, not just the full determinant
# Source Reference
Chapter 8: Bilinear Forms, Section 8.4, Theorem 8.4.19, page 255.
# Verification Notes
- Definition source: Direct from Theorem 8.4.19
- Confidence rationale: Theorem stated; proof left as exercise
- Uncertainties: None
- Cross-reference status: Verified
