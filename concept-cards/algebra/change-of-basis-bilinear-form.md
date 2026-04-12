---
concept: Change of Basis for Bilinear Forms
slug: change-of-basis-bilinear-form
category: bilinear-forms
subcategory: null
tier: intermediate
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Bilinear Forms"
chapter_number: 8
pdf_page: 240
section: "8.1 Bilinear Forms"
extraction_confidence: high
aliases: ["congruence transformation"]
prerequisites: [matrix-of-a-bilinear-form]
extends: []
related: [signature, sylvesters-law-of-inertia]
contrasts_with: []
answers_questions: ["How does the matrix of a bilinear form change under a change of basis?"]
---
# Quick Definition
Under a change of basis B' = BP, the matrix of a bilinear form transforms as A' = P^t A P (for symmetric forms) or A' = P* A P (for Hermitian forms). This "congruence" transformation is distinct from the similarity transformation P^{-1}AP used for linear operators.
# Core Definition
Proposition 8.1.7: If A and A' are the matrices of a bilinear form with respect to bases B and B', and P is the change-of-basis matrix (B' = BP), then A' = P^t A P (Artin, p. 241). For Hermitian forms, A' = P* A P (8.3.9). The matrices representing the same form are exactly P^t A P (resp. P* A P) for invertible P (Corollaries 8.1.8, 8.3.10).
# Prerequisites
- **Matrix of a bilinear form** — The object being transformed
# Key Properties
1. A' = P^t A P for symmetric (bilinear) forms
2. A' = P* A P for Hermitian forms
3. Distinct from similarity transformation P^{-1}AP for operators
4. Preserves: symmetry, skew-symmetry, Hermitian property, rank, signature, determinant (up to a square)
# Examples
**Example 1** (p. 242): Dot product (A = I) under change of basis B' = EP becomes A' = P^t I P = P^t P.
# Relationships
## Builds Upon
- **Matrix of a bilinear form** — The matrix being transformed
## Enables
- **Signature** — Invariant under congruence transformation
- **Sylvester's law of inertia** — The signature is preserved
# Common Errors
- **Error**: Using P^{-1}AP (similarity) instead of P^t AP (congruence)
  **Correction**: Bilinear forms use congruence; linear operators use similarity
# Source Reference
Chapter 8: Bilinear Forms, Sections 8.1 and 8.3, pages 241-242, 245.
# Verification Notes
- Definition source: Direct from Proposition 8.1.7
- Confidence rationale: Explicitly proved
- Uncertainties: None
- Cross-reference status: Verified
