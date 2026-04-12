---
concept: Direct Sum of Representations
slug: direct-sum-of-representations
category: group-representations
subcategory: null
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Group Representations"
chapter_number: 10
pdf_page: 301
section: "10.2 Irreducible Representations"
extraction_confidence: high
aliases: []
prerequisites: [group-representation, g-invariant-subspace]
extends: []
related: [completely-reducible-representation, maschkes-theorem]
contrasts_with: []
answers_questions: ["What is the direct sum of representations?"]
---
# Quick Definition
If V = W_1 + W_2 is a direct sum of G-invariant subspaces, the representation rho decomposes as alpha + beta, where alpha and beta are the restrictions to W_1 and W_2. In matrix form, R_g = [[A_g, 0],[0, B_g]].
# Core Definition
If V is the direct sum of G-invariant subspaces W_1 and W_2, the representation rho is the direct sum of its restrictions alpha and beta: rho = alpha + beta (Artin, (10.2.6), p. 307). With a basis B = (B_1, B_2), the matrix is block diagonal: R_g = [[A_g, 0],[0, B_g]] (10.2.7). The character of a direct sum is the sum of characters (Proposition 10.4.2(e)).
# Prerequisites
- **Group representation** — Direct sum combines representations
- **G-invariant subspace** — The summands must be G-invariant
# Key Properties
1. V = W_1 + W_2 with both G-invariant
2. Matrix form: R_g = [[A_g, 0],[0, B_g]]
3. Character: chi_{rho} = chi_alpha + chi_beta
4. Extends to direct sums of more than two representations
# Examples
**Example 1** (p. 307): The 3D representation M of S_3 as rotations: M = A + Sigma (standard + sign), with R_g = [[A_g, 0],[0, Sigma_g]].
# Relationships
## Enables
- **Completely reducible representation** — A direct sum of irreducibles
## Related
- **Maschke's theorem** — Guarantees direct sum decomposition exists
# Source Reference
Chapter 10: Group Representations, Section 10.2, pages 306-307.
# Verification Notes
- Definition source: Direct from (10.2.6) and (10.2.7)
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
