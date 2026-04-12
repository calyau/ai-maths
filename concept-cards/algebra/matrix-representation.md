---
concept: Matrix Representation
slug: matrix-representation
category: group-representations
subcategory: null
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Group Representations"
chapter_number: 10
pdf_page: 301
section: "10.1 Definitions"
extraction_confidence: high
aliases: []
prerequisites: [group-representation]
extends: [group-representation]
related: [character-of-a-representation]
contrasts_with: []
answers_questions: ["What is a matrix representation?"]
---
# Quick Definition
A matrix representation of a group G is a homomorphism R: G -> GL_n, assigning an invertible n x n complex matrix R_g to each group element g, with R_{gh} = R_g R_h. The number n is the dimension of the representation.
# Core Definition
A matrix representation R: G -> GL_n is a homomorphism from G to the complex general linear group (Artin, (10.1.1), p. 301). Each R_g is an invertible matrix, and R_{gh} = R_g R_h (10.1.2). A representation rho: G -> GL(V) on a vector space V becomes a matrix representation after choosing a basis. A change of basis conjugates the matrix representation: R'_g = P^{-1} R_g P (10.1.12).
# Prerequisites
- **Group representation** — A matrix representation is a representation on C^n
# Key Properties
1. R: G -> GL_n is a homomorphism
2. n = dimension of the representation
3. Change of basis: R'_g = P^{-1} R_g P
4. Character chi(g) = trace(R_g) is independent of basis choice
# Examples
**Example 1** (p. 301): The standard representation of S_3: A_x = [[cos(2pi/3), -sin(2pi/3)],[sin(2pi/3), cos(2pi/3)]], A_y = [[1,0],[0,-1]].
# Relationships
## Builds Upon
- **Group representation** — Matrix form of a representation
# Source Reference
Chapter 10: Group Representations, Section 10.1, pages 301-302.
# Verification Notes
- Definition source: Direct from (10.1.1)
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
