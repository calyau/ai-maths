---
# === CORE IDENTIFICATION ===
concept: Linear Representation
slug: linear-representation

# === CLASSIFICATION ===
category: representation-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Representations of Finite Groups"
chapter_number: 7
pdf_page: 101
section: "Linear representations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "representation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
  - matrix-representation
extends:
  - matrix-representation
related:
  - f-g-module
  - irreducible-representation
  - completely-reducible-representation
  - character-of-a-representation
contrasts_with:
  - matrix-representation

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a linear representation of a finite group?"
  - "How does a linear representation relate to a matrix representation?"
---

# Quick Definition

A linear representation of G on an F-vector space V is a group homomorphism G -> GL(V). It is a basis-free version of a matrix representation.

# Core Definition

A **linear representation** of G on V is a homomorphism G -> GL(V), where GL(V) is the group of F-linear automorphisms of V. Equivalently, it is a linear action of G on V: each g in G acts by an invertible linear map g_V: V -> V, and g -> g_V is a group homomorphism. A linear representation on F^n is the same as a matrix representation of degree n. (Milne, Chapter 7, pp. 101-102)

# Prerequisites

- **Group** — the group being represented
- **Matrix representation** — linear representations generalize matrix representations

# Key Properties

1. Basis-independent formulation of representation theory
2. Choosing a basis for V converts a linear representation into a matrix representation
3. The representation is irreducible (simple) if V has no proper nonzero G-invariant subspaces
4. Every linear representation of G yields an F[G]-module structure on V, and conversely

# Construction / Recognition

1. Define a homomorphism rho: G -> GL(V)
2. Verify rho(g_1 g_2) = rho(g_1) o rho(g_2) for all g_1, g_2
3. Equivalently, define a linear action of G on V and verify the group action axioms

# Context & Application

Linear representations are the central objects of study in representation theory. Every linear representation makes V into an F[G]-module, and conversely. This translation allows algebraic tools (module theory, Wedderburn theory) to be applied to representation-theoretic questions.

# Examples

**Example 1** (p. 102, 7.3a): For G = C_n with a primitive nth root zeta in F, a linear representation G -> GL(V) decomposes V into eigenspaces V = direct sum of V_i where sigma acts as zeta^i on V_i.

**Example 2** (p. 102, 7.3b): For G abelian of exponent n with F containing a primitive nth root of 1, a representation decomposes V = direct sum of V_chi indexed by characters chi in G^v.

# Relationships

## Builds Upon
- **group** — the object being represented
- **matrix-representation** — coordinate-dependent version

## Enables
- **f-g-module** — every linear representation gives an F[G]-module
- **irreducible-representation** — a representation with no proper G-invariant subspaces
- **character-of-a-representation** — trace function of a representation

## Related
- **completely-reducible-representation** — direct sum of irreducible representations

## Contrasts With
- **matrix-representation** — depends on choice of basis, while linear representation is basis-free

# Common Errors

- **Error**: Confusing a representation with a single matrix
  **Correction**: A representation is a homomorphism assigning a matrix (or linear map) to each group element

# Common Confusions

- **Confusion**: Thinking linear representations and F[G]-modules are different concepts
  **Clarification**: They are equivalent: a linear representation G -> GL(V) is the same data as an F[G]-module structure on V

# Source Reference

Chapter 7: Representations of Finite Groups, "Linear representations" section, pp. 101-102.

# Verification Notes

- Definition source: Direct from pp. 101-102
- Confidence rationale: HIGH — explicit definition
- Uncertainties: None
