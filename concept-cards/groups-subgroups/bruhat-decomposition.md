---
concept: Bruhat Decomposition
slug: bruhat-decomposition
category: reductive-groups
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "The Structure of Reductive Groups: The Split Case"
chapter_number: 5
pdf_page: 363
section: "Applications"
extraction_confidence: high
aliases:
  - "Bruhat-Tits decomposition"
prerequisites:
  - borel-subgroup
  - weyl-group-algebraic
extends: []
related:
  - borel-subgroup
  - weyl-group
contrasts_with: []
answers_questions:
  - "How do I compute the Bruhat decomposition?"
---

# Quick Definition

The Bruhat decomposition states that for a connected reductive group G with Borel subgroup B and Weyl group W, G = BWB (a disjoint union of double cosets BwB as w ranges over W).

# Core Definition

**Theorem 3.41 (Bruhat Decomposition)**: For any Borel subgroup B of a connected algebraic group G with maximal torus T and Weyl group W, G = BWB (Milne, p. 363).

This means G(k) is a disjoint union ⨆_{w∈W} B(k)wB(k) where w denotes a representative in N_G(T)(k).

# Prerequisites

- **Borel subgroup** — B is a Borel subgroup
- **Weyl group** — W indexes the double cosets

# Key Properties

1. The decomposition is disjoint: G = ⨆_{w∈W} BwB
2. Implies the normalizer theorem: N_G(B) = B (Theorem 3.42)
3. Implies W = N_G(T)/C_G(T) (Corollary 3.43)
4. Used to prove connectedness of torus centralizers (Theorem 3.44)

# Context & Application

The Bruhat decomposition is fundamental in representation theory, the geometry of flag varieties, and the theory of buildings. It provides a cell decomposition of the flag variety G/B (the Schubert decomposition).

# Examples

**Example 1**: For GL₂ with B = upper triangular: GL₂ = B ⊔ B·((0,1),(1,0))·B. Every matrix is either upper triangular or can be brought to upper triangular form after multiplying by the Weyl element.

# Source Reference

Chapter V, Section 3h, Theorem 3.41, page 363.

# Verification Notes

- Definition source: Direct from Theorem 3.41
- Confidence: HIGH — major named theorem
- Uncertainties: None
