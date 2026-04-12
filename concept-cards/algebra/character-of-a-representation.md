---
concept: Character of a Representation
slug: character-of-a-representation
category: group-representations
subcategory: null
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Group Representations"
chapter_number: 10
pdf_page: 301
section: "10.4 Characters"
extraction_confidence: high
aliases: ["character"]
prerequisites: [group-representation]
extends: []
related: [character-table, irreducible-character, orthogonality-of-characters, class-function]
contrasts_with: []
answers_questions: ["How do characters relate to representations?", "What is a character?"]
---
# Quick Definition
The character chi of a representation rho is the function chi(g) = trace(rho_g). Characters are constant on conjugacy classes, and two representations are isomorphic if and only if their characters are equal.
# Core Definition
The character chi of a representation rho is the complex-valued function defined by chi(g) = trace(rho_g) (Artin, (10.4.1), p. 308). Characters encode the essential information of a representation while discarding the complicated matrix entries. Corollary 10.4.8(c): Two representations are isomorphic if and only if their characters are equal.
# Prerequisites
- **Group representation** — Characters are defined from representations
# Key Properties
1. chi(1) = dimension of the representation (Proposition 10.4.2(a))
2. Constant on conjugacy classes: chi(hgh^{-1}) = chi(g) (Proposition 10.4.2(b))
3. chi(g^{-1}) = conjugate of chi(g) (Proposition 10.4.2(d))
4. Character of a direct sum is the sum of characters (Proposition 10.4.2(e))
5. Isomorphic representations have the same character (Proposition 10.4.2(f))
6. Two representations are isomorphic iff their characters are equal (Corollary 10.4.8(c))
7. chi(g) is a sum of d roots of unity, where d = dim(rho) and the roots relate to the order of g
# Construction / Recognition
## To Compute:
1. For each conjugacy class, pick a representative g
2. Compute trace(R_g) using any convenient basis
3. Record values — one per conjugacy class
# Context & Application
Characters reduce the problem of classifying representations to computing traces. "The secret to understanding representations is to throw out most of the information that the matrices contain, keeping only one essential part, its trace, or character" (Artin, p. 303).
# Examples
**Example 1** (p. 303): Characters of the three representations of S_3: chi_T = (1,1,1), chi_Sigma = (1,1,-1), chi_A = (2,-1,0), listed on elements 1, x, y.
# Relationships
## Builds Upon
- **Group representation** — Characters are traces of representation matrices
## Enables
- **Character table** — Table of irreducible characters
- **Orthogonality of characters** — Characters are orthonormal with respect to a Hermitian product
# Common Errors
- **Error**: Thinking a character of dimension > 1 is a homomorphism
  **Correction**: Only one-dimensional characters are homomorphisms (Warning, p. 316)
# Common Confusions
- **Confusion**: Thinking the character depends on the choice of basis
  **Clarification**: The trace is independent of basis, so the character is intrinsic to the representation
# Source Reference
Chapter 10: Group Representations, Sections 10.1 and 10.4, pages 303, 308-312.
# Verification Notes
- Definition source: Direct from (10.4.1)
- Confidence rationale: Central concept, extensively developed
- Uncertainties: None
- Cross-reference status: Verified
