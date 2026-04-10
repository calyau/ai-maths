---
concept: Character of an Affine Group
slug: character-of-affine-group
category: representations
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 115
section: "8p Characters and eigenspaces"
extraction_confidence: high
aliases:
  - character
  - k-character
prerequisites:
  - affine-algebraic-group
  - linear-representation
extends: []
related:
  - group-like-element
  - eigenspace
  - character-group
contrasts_with:
  - cocharacter
answers_questions:
  - "What is a character of an algebraic group?"
  - "How do characters and cocharacters pair in the theory of tori?"
---

# Quick Definition

A character of an affine group G is a homomorphism chi: G -> G_m. Characters correspond bijectively to group-like elements in O(G), and the set X(G) of all characters forms an abelian group under pointwise multiplication.

# Core Definition

A *character* of an affine group G is a homomorphism chi: G -> G_m. Since O(G_m) = k[X, X^{-1}] with Delta(X) = X tensor X, giving a character chi is equivalent to giving an invertible element a(chi) of O(G) such that Delta(a) = a tensor a (a *group-like* element). The character group X(G) is an abelian group with operation (chi + chi')(g) = chi(g) . chi'(g), corresponding to a(chi + chi') = a(chi) . a(chi') (Milne, pp. 115-116).

# Prerequisites

- **Affine algebraic group** -- The source of characters
- **Linear representation** -- Characters are one-dimensional representations

# Key Properties

1. Characters correspond bijectively to group-like elements in O(G)
2. X(G) is an abelian group (written additively) under pointwise multiplication
3. A character defines a representation on any V: g acts as multiplication by chi(g)
4. The eigenspace V_chi = {v in V | rho(v) = v tensor a(chi)} is the largest subspace on which G acts through chi
5. If V = sum V_chi, then V = direct-sum V_chi (Theorem 8.65; uses linear independence of group-like elements)

# Context & Application

Characters are the bridge between abstract group theory and explicit computations. For tori, the character group completely determines the group. Characters also define eigenspace decompositions, which are fundamental to the structure theory of reductive groups.

# Examples

**Example 1** (p. 116): The determinant det: GL_n -> G_m is a character. It corresponds to the group-like element det(X_{ij}) in O(GL_n).

**Example 2** (p. 116): A character chi defines a representation on V = k^n where g acts as chi(g) times the identity matrix.

# Relationships

## Builds Upon
- **Affine algebraic group** -- Characters are homomorphisms from G

## Enables
- **Eigenspace** -- Eigenspaces are defined using characters
- **Diagonalizable group** -- A group is diagonalizable iff O(G) is spanned by characters
- **Group of multiplicative type** -- Classified by their character modules

## Contrasts With
- **Cocharacter** -- A cocharacter is a homomorphism G_m -> G, going the opposite direction

# Source Reference

Chapter I: Basic Theory of Affine Groups, Sections 8p and 14b, pages 115-116, 163-164.

# Verification Notes

- Definition source: Direct from Section 8p
- Confidence rationale: Explicit definition with full algebraic characterization
- Uncertainties: None
- Cross-reference status: Verified
