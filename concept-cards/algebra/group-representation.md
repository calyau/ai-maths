---
concept: Group Representation
slug: group-representation
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
aliases: ["representation"]
prerequisites: [general-linear-group]
extends: []
related: [matrix-representation, character-of-a-representation, irreducible-representation]
contrasts_with: []
answers_questions: ["What is a group representation?", "What must I know before studying group representations?"]
---
# Quick Definition
A representation of a group G on a complex vector space V is a homomorphism rho: G -> GL(V). It assigns to each group element an invertible linear operator on V, compatible with the group law.
# Core Definition
A representation of a group G on a complex vector space V is a homomorphism rho: G -> GL(V), where GL(V) is the group of invertible linear operators on V (Artin, p. 302). The elements of a finite rotation group acting as orthogonal operators on R^3 give the "standard representation." A matrix representation is a homomorphism R: G -> GL_n, i.e., a representation on the space of column vectors (10.1.1). The dimension of the representation is n.
# Prerequisites
- **General linear group** — The codomain of a representation
# Key Properties
1. rho is a homomorphism: rho_{gh} = rho_g rho_h
2. rho_1 = I (the identity element maps to the identity operator)
3. Every representation on a finite-dimensional space gives a matrix representation after choosing a basis
4. A change of basis conjugates the matrix representation: R'_g = P^{-1} R_g P
5. Equivalent to: an operation of G by linear operators on V
6. Except in Section 10.9, groups are finite and vector spaces are complex
# Construction / Recognition
## To Construct:
1. Choose generators and relations for G
2. Assign matrices to generators satisfying the relations
3. Verify the matrices are invertible
# Context & Application
Representations arise when a structure with symmetry is studied. The symmetry group acts on a "state space" by linear operators. Artin motivates this from chemistry (vibrations of molecules). The goal of Chapter 10 is to classify complex representations of finite groups.
# Examples
**Example 1** (p. 301): The standard representation of S_3 = D_3 on R^2, with A_x = [[c,-s],[s,c]] and A_y = [[1,0],[0,-1]] where c = cos(2pi/3), s = sin(2pi/3).
**Example 2** (p. 302): The sign representation Sigma of S_3: Sigma_x = [1], Sigma_y = [-1].
**Example 3** (p. 302): The trivial representation T: T_g = [1] for all g.
# Relationships
## Enables
- **Character of a representation** — trace of the matrix representation
- **Irreducible representation** — A representation with no proper invariant subspaces
- **Matrix representation** — A representation on C^n
# Common Errors
- **Error**: Forgetting that the representation must be a homomorphism (not just any assignment of matrices)
  **Correction**: The matrices must satisfy all group relations
# Common Confusions
- **Confusion**: Thinking a representation uniquely determines matrices
  **Clarification**: A change of basis conjugates the matrix representation; the representation rho on V is basis-independent
# Source Reference
Chapter 10: Group Representations, Section 10.1, pages 301-305.
# Verification Notes
- Definition source: Direct from (10.1.1) and p. 302
- Confidence rationale: Extensively defined with multiple examples
- Uncertainties: None
- Cross-reference status: Verified
