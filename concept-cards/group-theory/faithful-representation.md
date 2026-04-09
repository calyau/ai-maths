---
# === CORE IDENTIFICATION ===
concept: Faithful Representation
slug: faithful-representation

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
pdf_page: 100
section: "Matrix representations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - matrix-representation
extends:
  - matrix-representation
related:
  - linear-representation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When does a representation faithfully capture the group structure?"
  - "What does it mean for a representation to be faithful?"
---

# Quick Definition

A representation is faithful if the homomorphism G -> GL_n(F) (or G -> GL(V)) is injective.

# Core Definition

A matrix representation G -> GL_n(F) is said to be **faithful** if the homomorphism is injective. A faithful representation identifies G with a group of n x n matrices. (Milne, Chapter 7, p. 100)

# Prerequisites

- **Matrix representation** — faithful is a property of a representation

# Key Properties

1. Kernel of the representation is trivial
2. G is isomorphic to its image in GL_n(F)
3. Every finite group has a faithful matrix representation (via Cayley's theorem, 7.1b)
4. An infinite finitely generated group with finite exponent has no faithful representation over C (Burnside, Aside 7.2)

# Construction / Recognition

1. Given a representation rho: G -> GL_n(F)
2. Check that ker(rho) = {e}
3. Equivalently, check that distinct group elements map to distinct matrices

# Context & Application

Faithful representations realize abstract groups as concrete matrix groups. Cayley's theorem guarantees their existence for finite groups. The double centralizer theorem (7.22) requires faithfulness of the module.

# Examples

**Example 1** (p. 100, 7.1b): The permutation representation sigma -> I(sigma): S_n -> GL_n(F) is faithful.

**Example 2** (p. 100, 7.1c): The representation sigma^i -> zeta^i: C_n -> GL_1(F) is faithful iff zeta has order exactly n.

**Example 3** (p. 101, 7.1c): When n = p = char(F), the map sigma^i -> (1, i; 0, 1): C_p -> GL_2(F) is a faithful representation of degree 2.

# Relationships

## Builds Upon
- **matrix-representation** — faithful is a property of representations

## Enables
- **double-centralizer-theorem** — requires a faithful module

## Related
- **linear-representation** — faithfulness applies to linear representations as well

## Contrasts With
- Non-faithful (trivial) representations

# Common Errors

- **Error**: Assuming all representations are faithful
  **Correction**: Many useful representations have nontrivial kernels

# Common Confusions

- **Confusion**: Confusing faithfulness of a representation with simplicity/irreducibility
  **Clarification**: A faithful representation need not be irreducible, and an irreducible representation need not be faithful

# Source Reference

Chapter 7: Representations of Finite Groups, pp. 100-101 (7.1, 7.2).

# Verification Notes

- Definition source: Direct from p. 100
- Confidence rationale: HIGH — explicit definition
- Uncertainties: None
