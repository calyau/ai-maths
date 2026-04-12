---
concept: Inner Product Space
slug: inner-product-space
category: bilinear-forms
subcategory: null
tier: intermediate
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Bilinear Forms"
chapter_number: 8
pdf_page: 240
section: "8.5 Euclidean Spaces and Hermitian Spaces"
extraction_confidence: medium
aliases: []
prerequisites: [positive-definite-form]
extends: []
related: [euclidean-space, hermitian-space]
contrasts_with: []
answers_questions: ["What is an inner product space?"]
---
# Quick Definition
An inner product space is a vector space equipped with a positive definite form — either a Euclidean space (real, symmetric form) or a Hermitian space (complex, Hermitian form). The form defines lengths, angles, and orthogonality.
# Core Definition
An inner product space is a vector space with a positive definite form: a Euclidean space (real vector space with positive definite symmetric form) or a Hermitian space (complex vector space with positive definite Hermitian form) (Artin, p. 256). In either case, the form defines |v|^2 = (v, v), the angle via (v, w) = |v||w| cos(theta) (8.5.2), and orthogonality via (v, w) = 0.
# Prerequisites
- **Positive definite form** — The form must be positive definite
# Key Properties
1. Defines length: |v| = sqrt((v, v))
2. Defines angle: cos(theta) = (v, w)/(|v||w|)
3. Defines orthogonality: v _|_ w iff (v, w) = 0
4. For any subspace W, V = W + W^perp (Corollary 8.5.1)
5. Orthonormal bases always exist
# Context & Application
Inner product spaces provide the geometric structure needed for the spectral theorem, Gram-Schmidt process, and projection formulas. They are the setting for all of Chapter 8's main results.
# Examples
**Example 1** (p. 256): R^n with dot product; C^n with X*Y.
# Relationships
## Related
- **Euclidean space** — Real inner product space
- **Hermitian space** — Complex inner product space
# Source Reference
Chapter 8: Bilinear Forms, Section 8.5, pages 256-257.
# Verification Notes
- Definition source: Synthesized from p. 256 (Artin uses the terms "Euclidean space" and "Hermitian space" rather than "inner product space")
- Confidence rationale: Medium — Artin doesn't use the term "inner product space" explicitly but the concept is clearly present
- Uncertainties: Terminology — Artin prefers "Euclidean space" and "Hermitian space"
- Cross-reference status: Verified
