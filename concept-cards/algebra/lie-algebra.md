---
concept: Lie Algebra
slug: lie-algebra
category: linear-groups
subcategory: null
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Linear Groups"
chapter_number: 9
pdf_page: 264
section: "9.6 The Lie Algebra"
extraction_confidence: high
aliases: []
prerequisites: [classical-groups]
extends: []
related: [lie-bracket, one-parameter-subgroup, exponential-map]
contrasts_with: []
answers_questions: ["What is a Lie algebra?", "What must I know before studying group representations?"]
---
# Quick Definition
The Lie algebra of a matrix group G, denoted Lie(G), is the space of tangent vectors to G at the identity. It is a real vector space with an additional operation called the bracket [A, B] = AB - BA.
# Core Definition
The Lie algebra of a matrix group G is the space of tangent vectors to G at the identity, denoted Lie(G) (Artin, p. 284). If phi(t) is a differentiable path in G with phi(0) = I, then phi'(0) is an element of Lie(G). For the classical groups: Lie(O_n) = skew-symmetric matrices (Proposition 9.6.1), Lie(SL_n) = trace-zero matrices (Proposition 9.6.4), Lie(U_n) = skew-Hermitian matrices. An abstract Lie algebra is a real vector space V with a bracket [v, w] satisfying bilinearity, skew symmetry, and the Jacobi identity (Definition 9.6.7).
# Prerequisites
- **Classical groups** — Lie algebras are defined for matrix groups
# Key Properties
1. Lie(G) is a real vector space of matrices
2. If A is in Lie(G), then e^{tA} is a one-parameter group in G
3. The bracket [A, B] = AB - BA is closed on Lie(G)
4. The bracket satisfies: bilinearity, skew symmetry [v,w] = -[w,v], Jacobi identity
5. Lie(O_n) = {A | A^t = -A}, dimension n(n-1)/2
6. Lie(SL_n) = {A | trace A = 0}, dimension n^2 - 1
7. Lie algebras are easier to work with than groups because they are vector spaces
8. Many linear groups are "nearly determined" by their Lie algebras (p. 286)
# Construction / Recognition
## To Compute Lie(G):
1. Let phi(t) be a path in G with phi(0) = I
2. Differentiate the defining relation of G at t = 0
3. The resulting conditions on A = phi'(0) define Lie(G)
# Context & Application
Lie algebras are the linearization of Lie groups at the identity. They capture the local structure of the group and are far easier to compute with. Artin introduces them through concrete matrix groups — a distinctive feature of his approach to algebra. Lie algebras are essential prerequisites for understanding representations.
# Examples
**Example 1** (p. 284): The Lie algebra of SO_2 is spanned by [[0,-1],[1,0]], a one-dimensional space.
**Example 2** (p. 284): Lie(O_n) = skew-symmetric matrices, proved by differentiating phi(t)^t phi(t) = I.
# Relationships
## Enables
- **Lie bracket** — The additional algebraic structure on Lie(G)
- **Exponential map** — Maps Lie(G) to G via A -> e^A
## Related
- **One-parameter subgroup** — In bijective correspondence with elements of Lie(G)
# Common Errors
- **Error**: Confusing the Lie algebra (tangent space at I) with the group itself
  **Correction**: The Lie algebra is a linear approximation; it captures local but not global information
# Common Confusions
- **Confusion**: Thinking the Lie bracket is associative
  **Clarification**: The bracket [A, B] = AB - BA is NOT associative in general; it satisfies the Jacobi identity instead
# Source Reference
Chapter 9: Linear Groups, Section 9.6, pages 284-286. Definition 9.6.7.
# Verification Notes
- Definition source: Direct from p. 284 and Definition 9.6.7
- Confidence rationale: Explicitly defined for specific groups and abstractly
- Uncertainties: None
- Cross-reference status: Verified
