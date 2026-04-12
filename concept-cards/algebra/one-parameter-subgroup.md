---
concept: One-Parameter Subgroup
slug: one-parameter-subgroup
category: linear-groups
subcategory: null
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Linear Groups"
chapter_number: 9
pdf_page: 264
section: "9.5 One-Parameter Groups"
extraction_confidence: high
aliases: ["one-parameter group"]
prerequisites: [classical-groups]
extends: []
related: [exponential-map, lie-algebra]
contrasts_with: []
answers_questions: ["What is a one-parameter subgroup?"]
---
# Quick Definition
A one-parameter subgroup of GL_n is a differentiable group homomorphism phi: R -> GL_n. Every such homomorphism has the form phi(t) = e^{tA} for a unique matrix A (Theorem 9.5.2).
# Core Definition
A one-parameter group in GL_n is a differentiable homomorphism phi: R+ -> GL_n from the additive group of reals. Theorem 9.5.2 states: (a) phi(t) = e^{tA} is a one-parameter group for any matrix A, and (b) conversely, every differentiable homomorphism phi has this form, where A = phi'(0) (Artin, p. 282).
# Prerequisites
- **Classical groups** — One-parameter subgroups are studied inside classical groups
# Key Properties
1. phi(t) = e^{tA} for a unique matrix A
2. A = phi'(0) is the derivative at the origin
3. e^{(r+s)A} = e^{rA} e^{sA} (homomorphism property)
4. In O_n: A must be skew-symmetric (Proposition 9.5.8)
5. In U_n: A must be skew-Hermitian (Proposition 9.5.8)
6. In SL_n: A must have trace zero (Proposition 9.5.10)
7. One-parameter subgroups are in bijective correspondence with elements of the Lie algebra
# Context & Application
One-parameter subgroups connect the Lie algebra to the group via the exponential map. They are the "straight lines" through the identity in a matrix group, and they provide concrete paths for proving the group is a manifold.
# Examples
**Example 1** (p. 283): A = [[0,1],[0,0]] gives e^{tA} = [[1,t],[0,1]] — a one-parameter group of upper triangular matrices.
**Example 2** (p. 283): A = [[0,-1],[1,0]] gives e^{tA} = [[cos t, -sin t],[sin t, cos t]] — the rotation group SO_2.
**Example 3** (p. 283): alpha = ai gives e^{t alpha} = cos(at) + i sin(at) — the unit circle U_1.
# Relationships
## Enables
- **Lie algebra** — The derivatives at t=0 of one-parameter subgroups form Lie(G)
## Related
- **Exponential map** — phi(t) = e^{tA} is the exponential map restricted to the line tA
# Source Reference
Chapter 9: Linear Groups, Section 9.5, pages 282-284. Theorem 9.5.2.
# Verification Notes
- Definition source: Direct from Theorem 9.5.2
- Confidence rationale: Explicitly defined with classification for classical groups
- Uncertainties: None
- Cross-reference status: Verified
