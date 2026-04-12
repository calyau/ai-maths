---
concept: Orthogonal Sum
slug: orthogonal-sum
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
aliases: []
prerequisites: [orthogonal-complement]
extends: []
related: [non-degenerate-form]
contrasts_with: []
answers_questions: ["What is an orthogonal sum of subspaces?"]
---
# Quick Definition
A vector space V is an orthogonal sum V = W_1 + ... + W_k if V is a direct sum and W_i is orthogonal to W_j for i != j. When the form is nondegenerate on a subspace W, V = W + W^perp is an orthogonal sum.
# Core Definition
When a vector space V is a direct sum W_1 + ... + W_k and W_i is orthogonal to W_j for i != j, V is said to be the orthogonal sum of the subspaces (Artin, p. 249). Theorem 8.4.5 asserts that if the form is nondegenerate on W, then V is the orthogonal sum of W and W^perp.
# Prerequisites
- **Orthogonal complement** — Provides the summands
# Key Properties
1. V is a direct sum: each vector has a unique decomposition
2. Summands are mutually orthogonal
3. The form on V restricted to each summand is independent
4. Matrix of the form is block diagonal with respect to bases of the summands
# Examples
**Example 1** (p. 249): R^3 with dot product: R^3 = span(e_1) + span(e_2) + span(e_3) is an orthogonal sum.
# Relationships
## Builds Upon
- **Orthogonal complement** — The orthogonal complement provides the decomposition
# Source Reference
Chapter 8: Bilinear Forms, Section 8.4, page 249.
# Verification Notes
- Definition source: Direct from p. 249
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
