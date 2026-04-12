---
concept: Normal Subgroups and Galois Extensions
slug: normal-subgroup-galois
category: galois-theory
subcategory: main-results
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Galois Theory"
chapter_number: 16
pdf_page: 488
section: "16.7 The Main Theorem"
extraction_confidence: high
aliases: []
prerequisites:
  - fundamental-theorem-galois-theory
  - normal-subgroup
extends: []
related:
  - galois-extension
  - intermediate-field
contrasts_with: []
answers_questions:
  - "When is an intermediate field a Galois extension of the base field?"
  - "How do normal subgroups relate to Galois extensions?"
---

# Quick Definition

In the Galois correspondence, an intermediate field L is a Galois extension of the base field F if and only if the corresponding subgroup H of G(K/F) is a normal subgroup. When this holds, G(L/F) is isomorphic to G/H.

# Core Definition

Let K/F be a Galois extension with Galois group G, and let L be the fixed field of a subgroup H. Then L/F is a Galois extension if and only if H is a normal subgroup of G. If so, the Galois group G(L/F) is isomorphic to the quotient group G/H (Artin, Theorem 16.7.5). The proof uses the fact that L/F is Galois iff all roots of the minimal polynomial of a primitive element for L/F lie in L, which happens iff sigma(L) = L for all sigma in G, which is equivalent to H being normal.

# Prerequisites

- **Fundamental theorem of Galois theory** -- This extends the main theorem
- **Normal subgroup** -- The group-theoretic condition

# Key Properties

1. H normal in G iff L/F is Galois (16.7.5)
2. G(L/F) = G/H when H is normal
3. The restriction map G -> G(L/F) is surjective with kernel H
4. Non-normal subgroups correspond to intermediate fields that are NOT Galois over F

# Context & Application

This theorem completes the Galois correspondence by identifying which intermediate extensions are themselves Galois. It connects the algebraic notion of normal subgroup to the field-theoretic notion of Galois extension.

# Examples

**Example 1** (p. 501): In K = Q(sqrt(3), sqrt(5)) with G = Klein four group, every subgroup is normal (G is abelian), so every intermediate field is Galois over Q.

**Example 2** (p. 500): For an irreducible cubic with G = S_3, the subgroup A_3 is normal (giving the intermediate field F(delta)), but the three subgroups of order 2 are not normal.

# Relationships

## Builds Upon
- **Fundamental theorem of Galois theory** -- This is the normality extension
- **Normal subgroup** -- The group-theoretic condition

# Source Reference

Chapter 16: Galois Theory, Section 16.7, pages 503-504. Theorem 16.7.5.

# Verification Notes

- Definition source: Direct from Artin, Theorem 16.7.5
- Confidence rationale: Complete proof given
- Uncertainties: None
- Cross-reference status: Verified
