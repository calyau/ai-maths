---
# === CORE IDENTIFICATION ===
concept: Radical of an Algebraic Group
slug: radical-of-algebraic-group

# === CLASSIFICATION ===
category: group-structure
subcategory: radicals
tier: intermediate

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 194
section: "17a Radicals and unipotent radicals"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "RG"
  - "R(G)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - solvable-algebraic-group
  - connected-algebraic-group
  - normal-subgroup
extends: []
related:
  - unipotent-radical
  - semisimple-algebraic-group
  - reductive-algebraic-group
contrasts_with:
  - unipotent-radical

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes the semisimple part from the radical of an algebraic group?"
  - "What is a reductive algebraic group?"
---

# Quick Definition

The radical RG of a smooth algebraic group G is the largest smooth connected normal solvable subgroup of G. It measures how far G is from being semisimple.

# Core Definition

Let G be a smooth algebraic group over a field k. The **radical** RG of G is the unique largest smooth connected normal solvable subgroup of G (Milne, Proposition 17.2a). Its existence follows from the fact that if N and H are normal solvable subgroups of G with H also normal, then HN is again solvable (Lemma 17.1).

# Prerequisites

- **Solvable algebraic group** -- The radical is defined as the largest solvable normal subgroup
- **Connected algebraic group** -- The radical must be connected
- **Normal subgroup** -- The radical is required to be normal in G

# Key Properties

1. RG is smooth, connected, normal, and solvable in G
2. The formation of RG commutes with separable extensions of the base field
3. Over a perfect field, R(G_K) = (RG)_K for any extension field K (Proposition 17.3)
4. R_uG = (RG)_u, i.e., the unipotent radical of G is the unipotent part of the radical (Proposition 17.3)
5. G/RG is semisimple (Proposition 17.9)
6. For a reductive group G, RG = Z(G)^0 is the connected centre, which is a torus (Theorem 17.20)

# Construction / Recognition

## To Construct:
1. Start with a smooth algebraic group G
2. Find all smooth connected normal solvable subgroups
3. The radical is the unique maximal such subgroup (existence guaranteed by Lemma 17.1)

## To Recognize:
1. Check that the subgroup is smooth, connected, normal, and solvable
2. Verify it is not properly contained in another subgroup with these properties

# Context & Application

The radical is central to the structure theory of algebraic groups. It provides the first step in the canonical filtration of an algebraic group (Theorem 17.14): any smooth connected algebraic group over a perfect field has a unique smooth connected normal solvable subgroup N such that G/N is semisimple, and that N is precisely RG. The quotient G/RG gives the semisimple part of G.

# Examples

**Example 1** (p. 196): Let G be the group of invertible matrices of the form (A B; 0 C) with A of size m x m and C of size n x n. The radical of the quotient G/R_uG (which is isomorphic to GL_m x GL_n) is G_m x G_m.

# Relationships

## Builds Upon
- **Solvable algebraic group** -- RG is defined as the largest such subgroup

## Enables
- **Semisimple algebraic group** -- G is semisimple iff RG = 1
- **Reductive algebraic group** -- For reductive G, RG = Z(G)^0 is a torus

## Related
- **Unipotent radical** -- R_uG is the unipotent part of RG

## Contrasts With
- **Unipotent radical** -- RG is the largest solvable normal subgroup; R_uG is the largest unipotent normal subgroup

# Common Errors

- **Error**: Assuming the radical is always unipotent
  **Correction**: The radical is solvable but not necessarily unipotent; the unipotent radical R_uG is a subgroup of RG

# Common Confusions

- **Confusion**: Confusing the radical of an algebraic group with the radical of a Lie algebra
  **Clarification**: These are related but distinct concepts; for a connected algebraic group G in characteristic zero, Lie(RG) = r(Lie(G)) (Corollary 5.24 in Ch II)

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 17a "Radicals and unipotent radicals," pages 193-194.

# Verification Notes

- Definition source: Direct from Proposition 17.2
- Confidence rationale: Explicit definition with clear properties
- Uncertainties: None
- Cross-reference status: Verified against §17b, §17e
