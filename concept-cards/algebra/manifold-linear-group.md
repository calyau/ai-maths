---
concept: Manifold Structure of Linear Groups
slug: manifold-linear-group
category: linear-groups
subcategory: null
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Linear Groups"
chapter_number: 9
pdf_page: 264
section: "9.7 Translation in a Group"
extraction_confidence: high
aliases: []
prerequisites: [classical-groups, exponential-map]
extends: []
related: [lie-algebra]
contrasts_with: []
answers_questions: ["Are matrix groups manifolds?"]
---
# Quick Definition
Every closed subgroup of GL_n is a manifold, and hence so are all classical groups. The dimension of the manifold equals the dimension of the Lie algebra. The proof uses the matrix exponential as a local homeomorphism.
# Core Definition
A manifold of dimension d is a set in which every point has a neighborhood homeomorphic to an open set in R^d. Theorem 9.7.4 states that a subgroup of GL_n that is a closed subset is a manifold (Artin, p. 289). The proof for O_n (Proposition 9.7.8) shows the exponential map defines a homeomorphism from a neighborhood of 0 in Lie(O_n) to a neighborhood of I in O_n. Homogeneity (left translation) extends this to all points.
# Prerequisites
- **Classical groups** — The groups whose manifold structure is studied
- **Exponential map** — Provides the local homeomorphism
# Key Properties
1. All classical groups are manifolds (closed subgroups of GL_n)
2. dim(manifold) = dim(Lie algebra)
3. dim(O_n) = n(n-1)/2
4. The exponential map provides local coordinates near the identity
5. Homogeneity: left translation carries the local structure at I to any other point
# Context & Application
The manifold structure connects algebra (group operations) to topology and geometry. It is the starting point for the theory of Lie groups. Artin uses it to prove that SO_3 is simple (Proposition 9.7.9, Theorem 9.7.10).
# Examples
**Example 1** (p. 290): O_n is a manifold of dimension n(n-1)/2 (proved using the exponential map and skew-symmetric matrices).
# Relationships
## Builds Upon
- **Exponential map** — Provides local coordinates
- **Classical groups** — The groups being studied
## Related
- **Lie algebra** — Dimension of the manifold = dimension of the Lie algebra
# Source Reference
Chapter 9: Linear Groups, Section 9.7, pages 288-291. Theorem 9.7.4, Proposition 9.7.8.
# Verification Notes
- Definition source: Theorem 9.7.4 and Proposition 9.7.8
- Confidence rationale: Explicitly proved for O_n; general theorem stated
- Uncertainties: General theorem proof deferred
- Cross-reference status: Verified
