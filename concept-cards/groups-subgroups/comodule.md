---
# === CORE IDENTIFICATION ===
concept: Comodule
slug: comodule

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
pdf_page: 96
section: "8d Comodules"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - right comodule
  - C-comodule
  - coalgebra comodule

# === TYPED RELATIONSHIPS ===
prerequisites:
  - coalgebra
  - coordinate-ring
extends: []
related:
  - linear-representation
  - category-of-comodules
contrasts_with:
  - module-over-algebra

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a comodule?"
  - "How do representations of algebraic groups relate to comodules?"
---

# Quick Definition

A right comodule over a k-coalgebra (C, Delta, epsilon) is a k-vector space V equipped with a k-linear coaction map rho: V -> V tensor C satisfying coassociativity and counit axioms -- the dual notion of a module over an algebra, obtained by reversing arrows.

# Core Definition

Let (C, Delta, epsilon) be a k-coalgebra. A *right C-comodule* is a k-vector space V together with a k-linear map rho: V -> V tensor C (called the *coaction*) such that (V tensor Delta) . rho = (rho tensor C) . rho (coassociativity) and (V tensor epsilon) . rho = id_V (counit). A *homomorphism* of comodules (V, rho) -> (V', rho') is a k-linear map alpha: V -> V' such that rho' . alpha = (alpha tensor C) . rho (Milne, Definition 8.4, p. 97).

# Prerequisites

- **Coalgebra** -- The coalgebra C provides the coaction target
- **Coordinate ring** -- O(G) is the coalgebra for comodules corresponding to representations of G

# Key Properties

1. Every comodule is a filtered union of its finite-dimensional sub-comodules (Proposition 8.8)
2. For a basis (e_i) of V with rho(e_j) = sum e_i tensor c_{ij}, the comodule axioms translate to Delta(c_{ij}) = sum c_{ik} tensor c_{kj} and epsilon(c_{ij}) = delta_{ij}
3. The smallest subcoalgebra C_V through which the coaction factors is spanned by the c_{ij}
4. A bialgebra structure on C defines tensor products of comodules; a Hopf structure gives duals
5. Subcomodules are k-subspaces W with rho(W) subset W tensor C

# Construction / Recognition

## To Construct:
1. Start with a coalgebra (C, Delta, epsilon) and a k-vector space V
2. Define a k-linear map rho: V -> V tensor C
3. Verify coassociativity: (V tensor Delta) . rho = (rho tensor C) . rho
4. Verify counit: (V tensor epsilon) . rho = id_V

## To Recognize:
1. A comodule structure on V is determined by a matrix (c_{ij}) of elements of C satisfying the matrix-coalgebra conditions

# Context & Application

Comodules provide the algebraic framework for understanding representations of algebraic groups. The fundamental correspondence (Proposition 8.12) identifies representations of G on V with O(G)-comodule structures on V. This reformulation is essential because comodule structures are purely algebraic objects, making them amenable to Hopf-algebraic techniques.

# Examples

**Example 1** (p. 97): The coalgebra (C, Delta) is itself a right C-comodule. More generally, V tensor Delta: V tensor C -> V tensor C tensor C is the *free comodule* on any k-vector space V.

**Example 2** (p. 97): If (V_1, rho_1) and (V_2, rho_2) are comodules over C_1 and C_2, then V_1 tensor V_2 acquires a C_1 tensor C_2 comodule structure.

# Relationships

## Builds Upon
- **Coalgebra** -- Comodules are defined over coalgebras

## Enables
- **Category of comodules** -- Comod(C) organizes all comodules
- **Representation-comodule correspondence** -- The bijection Rep(G) <-> Comod(O(G))

## Contrasts With
- **Module over algebra** -- Modules use an action mu: A tensor V -> V; comodules reverse the arrows to give rho: V -> V tensor C

# Common Errors

- **Error**: Confusing left and right comodules
  **Correction**: It is right comodules that correspond to left representations. This is why the text uses V tensor R rather than R tensor V.

# Common Confusions

- **Confusion**: Thinking comodules are just the dual of modules
  **Clarification**: While the definition dualizes the module axioms, the categories behave differently: every comodule is a union of finite-dimensional sub-comodules, while modules over infinite-dimensional algebras need not have this property

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 8d, pages 96-99. Definition 8.4 and Examples 8.5.

# Verification Notes

- Definition source: Direct from Definition 8.4, p. 97
- Confidence rationale: Explicit definition with full axioms and multiple examples
- Uncertainties: None
- Cross-reference status: Verified
