---
# === CORE IDENTIFICATION ===
concept: G-invariant Subspace
slug: g-invariant-subspace

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
pdf_page: 102
section: "Maschke's theorem"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "invariant subspace"
  - "G-stable subspace"
  - "subrepresentation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - linear-representation
extends: []
related:
  - irreducible-representation
  - maschke-theorem
  - f-g-module
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a G-invariant subspace?"
  - "What is a subrepresentation?"
---

# Quick Definition

A subspace W of a representation space V is G-invariant if gW is contained in W for all g in G.

# Core Definition

Let G -> GL(V) be a linear representation. A subspace W of V is said to be **G-invariant** if gW is contained in W for all g in G. The G-invariant subspaces of V are exactly the F[G]-submodules of V. (Milne, Chapter 7, p. 102)

# Prerequisites

- **Linear representation** — G-invariant subspaces are defined within a representation

# Key Properties

1. A G-invariant subspace W inherits a representation structure: G -> GL(W)
2. The submodules of V as an F[G]-module are exactly the G-invariant subspaces
3. The intersection and sum of G-invariant subspaces are G-invariant
4. V and {0} are always G-invariant

# Construction / Recognition

1. Given a subspace W of V
2. Check that gw is in W for all g in G and all w in W
3. Equivalently, check on generators of G and a basis of W

# Context & Application

G-invariant subspaces are the building blocks for decomposing representations. Finding all G-invariant subspaces of V is equivalent to finding all submodules of V as an F[G]-module. Maschke's theorem says every G-invariant subspace has a G-invariant complement (when char(F) does not divide |G|).

# Examples

**Example 1** (p. 102): In the representation C_p -> GL_2(F) over a field of characteristic p via the matrix (1, 1; 0, 1), the subspace F(1; 0) = {(a; 0)} is G-invariant, but no complementary G-invariant subspace exists.

# Relationships

## Builds Upon
- **linear-representation** — defined within the context of a representation

## Enables
- **irreducible-representation** — no proper nonzero G-invariant subspaces
- **maschke-theorem** — guarantees G-invariant complements

## Related
- **f-g-module** — G-invariant subspaces = F[G]-submodules

## Contrasts With
- Arbitrary (non-invariant) subspaces

# Common Errors

- **Error**: Assuming every subspace of a representation space is G-invariant
  **Correction**: Most subspaces are not G-invariant; only special ones are preserved by all group elements

# Common Confusions

- **Confusion**: Confusing "G-invariant subspace" with "fixed-point subspace V^G"
  **Clarification**: A G-invariant subspace W satisfies gW contained in W; the fixed-point subspace V^G = {v : gv = v for all g} consists of vectors fixed pointwise

# Source Reference

Chapter 7: Representations of Finite Groups, p. 102.

# Verification Notes

- Definition source: Direct from p. 102
- Confidence rationale: HIGH — explicit definition
- Uncertainties: None
