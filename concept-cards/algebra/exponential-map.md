---
concept: Exponential Map
slug: exponential-map
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
aliases: ["matrix exponential for groups"]
prerequisites: [lie-algebra, one-parameter-subgroup]
extends: []
related: [classical-groups]
contrasts_with: []
answers_questions: ["What is the exponential map for matrix groups?"]
---
# Quick Definition
The exponential map sends a matrix A in the Lie algebra to e^A in the group. Near the identity, it is a homeomorphism from a neighborhood of 0 in Lie(G) to a neighborhood of I in G.
# Core Definition
The map A -> e^A = I + A/1! + A^2/2! + ... sends matrices in the Lie algebra to elements of the group (Artin, (9.5.1), p. 282). Lemma 9.7.5 states that the exponential maps a small neighborhood of 0 in R^{n x n} homeomorphically to a neighborhood of I in GL_n. The inverse is given by the matrix logarithm log(I + B) = B - B^2/2 + B^3/3 - ... (9.7.6).
# Prerequisites
- **Lie algebra** — Domain of the exponential map
- **One-parameter subgroup** — phi(t) = e^{tA} connects the Lie algebra to the group
# Key Properties
1. e^A is in G when A is in Lie(G) (for the classical groups)
2. Local homeomorphism near the identity
3. det(e^A) = e^{trace A} (Lemma 9.5.9)
4. If A is skew-symmetric, e^A is orthogonal; if A is skew-Hermitian, e^A is unitary
5. The inverse near I is the matrix logarithm
# Context & Application
The exponential map is the bridge between a Lie algebra and its Lie group. It is used to prove that classical groups are manifolds (Proposition 9.7.8) and to compute one-parameter subgroups.
# Examples
**Example 1** (p. 283): e^{t[[0,1],[0,0]]} = [[1,t],[0,1]].
**Example 2** (p. 283): e^{t[[0,-1],[1,0]]} = [[cos t, -sin t],[sin t, cos t]].
# Relationships
## Builds Upon
- **Lie algebra** — Maps from Lie(G) to G
## Related
- **One-parameter subgroup** — t -> e^{tA}
# Source Reference
Chapter 9: Linear Groups, Sections 9.5 and 9.7, pages 282-290.
# Verification Notes
- Definition source: Direct from (9.5.1) and Lemma 9.7.5
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
