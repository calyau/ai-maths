---
concept: Representation-Comodule Correspondence
slug: representation-comodule-correspondence
category: representations
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 100
section: "8f Representations and comodules"
extraction_confidence: high
aliases:
  - representation-comodule bijection
prerequisites:
  - linear-representation
  - comodule
  - coordinate-ring
extends: []
related:
  - category-of-representations
  - category-of-comodules
contrasts_with: []
answers_questions:
  - "How do representations of algebraic groups relate to comodules?"
---

# Quick Definition

For any affine monoid G and k-vector space V, there is a canonical one-to-one correspondence between linear representations of G on V and O(G)-comodule structures on V. This identifies the category Rep(G) with the category of O(G)-comodules.

# Core Definition

Let G be an affine monoid over k with coordinate ring A = O(G). For any k-vector space V, there is a natural bijection between representations r: G -> End_V and comodule structures rho: V -> V tensor A. Given r, the coaction rho is obtained by applying the universal element u = id_A in G(A) to get rho = r_A(u)|_V. Conversely, given rho, for g in G(R) the representation acts as r_R(g) = (V tensor g) . rho extended R-linearly. Under this correspondence, subrepresentations correspond to subcomodules (Milne, Proposition 8.12, pp. 100-103).

# Prerequisites

- **Linear representation** -- One side of the correspondence
- **Comodule** -- The other side of the correspondence
- **Coordinate ring** -- The Hopf algebra O(G) serves as the coalgebra for comodules

# Key Properties

1. The correspondence is canonical (independent of basis choices)
2. Subrepresentations correspond bijectively to subcomodules (Proposition 8.16)
3. In the finite-dimensional case with basis (e_i), if rho(e_j) = sum e_i tensor a_{ij}, then r_R(g)(e_j tensor 1) = sum e_i tensor g(a_{ij})
4. The tensor product structure on representations corresponds to the tensor product of comodules
5. Contragredient representations correspond to dual comodules

# Construction / Recognition

## To Construct (representation -> comodule):
1. Given r: G -> End_V, evaluate at the universal element u = id_{O(G)} in G(O(G))
2. The restriction of r_{O(G)}(u) to V subset V(O(G)) gives rho: V -> V tensor O(G)

## To Construct (comodule -> representation):
1. Given rho: V -> V tensor O(G), for g in G(R), define r_R(g) on V by composing rho with V tensor g
2. Extend R-linearly to all of V(R)

# Context & Application

This correspondence is the technical foundation for the entire theory. It allows translation between geometric questions about group actions (representations) and algebraic questions about coalgebra structures (comodules). The comodule perspective is often more tractable for proving structural results.

# Examples

**Example 1** (p. 101): With V = k^n and basis (e_i), a matrix (r_{ij}) of elements of O(G) satisfying Delta(r_{ij}) = sum r_{ik} tensor r_{kj} and epsilon(r_{ij}) = delta_{ij} defines simultaneously a coaction rho(e_j) = sum e_i tensor r_{ij} and a homomorphism r: G -> GL_n by r(g) = (r_{ij}(g)).

**Example 2** (p. 103): The regular representation of G on O(G) corresponds to the comodule structure given by the comultiplication Delta.

# Relationships

## Builds Upon
- **Linear representation** -- One side of the bijection
- **Comodule** -- The other side of the bijection

## Enables
- **Category of representations** -- Rep(G) is identified with Comod(O(G))
- **Reconstruction theorem** -- Uses the correspondence to recover G from Rep(G)

# Common Confusions

- **Confusion**: Thinking the correspondence requires finite-dimensionality
  **Clarification**: The correspondence works for all representations; finite-dimensionality is needed only for some auxiliary constructions

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 8f, pages 100-104. Proposition 8.12, Summary 8.13.

# Verification Notes

- Definition source: Direct from Proposition 8.12
- Confidence rationale: Central theorem with detailed proof
- Uncertainties: None
- Cross-reference status: Verified
