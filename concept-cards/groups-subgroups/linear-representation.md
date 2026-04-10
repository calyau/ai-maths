---
# === CORE IDENTIFICATION ===
concept: Linear Representation of an Affine Group
slug: linear-representation

# === CLASSIFICATION ===
category: representations
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 94
section: "8b Definition of a representation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - representation
  - group representation

# === TYPED RELATIONSHIPS ===
prerequisites:
  - affine-algebraic-group
  - coordinate-ring
extends: []
related:
  - comodule
  - regular-representation
  - category-of-representations
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a representation of an algebraic group?"
  - "How are representations of algebraic groups defined functorially?"
---

# Quick Definition

A linear representation of an affine group G on a k-vector space V is a natural transformation r: G -> End_V of functors such that each r_R: G(R) -> End_{R-lin}(V(R)) is a monoid homomorphism. When G is an affine group (not just monoid), r takes values in Aut_V.

# Core Definition

Let V be a vector space over k. A *linear representation* of an affine monoid or group G on V is a natural transformation r: G -> End_V of functors Alg_k -> Mon. In other words, it is a family of homomorphisms of monoids r_R: G(R) -> End_{R-lin}(V(R)), one for each k-algebra R, such that for every homomorphism R -> R' of k-algebras, the obvious naturality diagram commutes. Equivalently, it is an action G x V -> V such that each g in G(R) acts R-linearly on V(R) (Milne, p. 95).

# Prerequisites

- **Affine algebraic group** -- The group being represented
- **Coordinate ring** -- The Hopf algebra O(G) mediates between representations and comodules

# Key Properties

1. A representation is *finite-dimensional* if V is finite-dimensional as a k-vector space
2. A representation is *faithful* if all homomorphisms r_R are injective
3. A subspace W of V is a *subrepresentation* if r_R(g)(W(R)) is contained in W(R) for all R and g in G(R)
4. When V = k^n, a representation is simply a homomorphism G -> GL_n
5. Every representation of G is a union of its finite-dimensional subrepresentations (Proposition 8.17)

# Construction / Recognition

## To Construct:
1. Choose a k-vector space V
2. Define compatible R-linear actions of G(R) on V(R) = V tensor R for all k-algebras R
3. Verify naturality: the actions commute with base change R -> R'

## To Recognize:
1. Check that you have a functorial family of monoid homomorphisms G(R) -> End(V(R))
2. Verify R-linearity of each action map

# Context & Application

Representations are the primary tool for studying algebraic groups concretely. The fundamental theorem (8.31) states that every algebraic group admits a faithful finite-dimensional representation, meaning every algebraic group can be realized as a subgroup of GL_n for some n. This makes matrix methods available for studying arbitrary algebraic groups.

# Examples

**Example 1** (p. 95): For G = G_a, a representation on a finite-dimensional V is determined by a sequence of endomorphisms rho_0, rho_1, ... satisfying rho_0 = id and the binomial composition rule rho_i . rho_j = C(i+j,i) rho_{i+j}. In characteristic zero, r_R(t) = exp(rho_1 t).

**Example 2** (p. 96): For G = GL_n acting on M_n by conjugation (P,A) -> PAP^{-1}, the orbits over an algebraically closed field are the similarity classes represented by Jordan matrices.

# Relationships

## Builds Upon
- **Affine algebraic group** -- The group being represented

## Enables
- **Comodule** -- Representations correspond bijectively to comodule structures
- **Category of representations** -- Rep(G) organizes all representations
- **Jordan decomposition** -- Defined via behavior on all representations

## Related
- **Regular representation** -- The canonical representation on O(G)
- **Faithful representation** -- Representations that embed G into GL_n

# Common Errors

- **Error**: Defining a representation only at the level of k-points G(k)
  **Correction**: A representation must be defined functorially for all k-algebras R

# Common Confusions

- **Confusion**: Thinking representations are only about matrices
  **Clarification**: A representation is a functorial family of actions; matrix form requires choosing a basis

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 8b, pages 95-96. See Examples 8.1-8.3.

# Verification Notes

- Definition source: Direct from Definition 8.b, p. 95
- Confidence rationale: Explicit definition with multiple equivalent formulations
- Uncertainties: None
- Cross-reference status: Verified against comodule correspondence (8.12)
