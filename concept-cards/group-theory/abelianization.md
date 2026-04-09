---
# === CORE IDENTIFICATION ===
concept: Abelianization
slug: abelianization

# === CLASSIFICATION ===
category: series-solvability
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Subnormal Series; Solvable and Nilpotent Groups"
chapter_number: 6
pdf_page: 91
section: "Solvable groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "G/G'"
  - maximal abelian quotient

# === TYPED RELATIONSHIPS ===
prerequisites:
  - commutator-subgroup
extends: []
related:
  - solvable-group
  - derived-series
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the largest abelian quotient of a group?"
---

# Quick Definition

The abelianization of a group G is the quotient G/G', where G' is the commutator subgroup. It is the largest abelian quotient of G: any homomorphism from G to an abelian group factors through G/G'.

# Core Definition

**Proposition 6.9.** The commutator subgroup G' is the smallest normal subgroup of G such that G/G' is commutative.

The quotient G/G' is called the *abelianization* of G. It has the universal property: any homomorphism phi: G -> A with A abelian satisfies G' subset Ker(phi), so phi factors as G -> G/G' -> A.

(Milne, Proposition 6.9, p. 91)

# Prerequisites

- **commutator-subgroup** -- G' is the kernel of the abelianization map

# Key Properties

1. G/G' is abelian
2. Any homomorphism to an abelian group factors through G/G'
3. G is abelian iff G' = {1} iff G/G' = G
4. For S_n (n >= 5), G/G' = S_n/A_n = C_2
5. For a perfect group (G' = G), the abelianization is trivial

# Relationships

## Builds Upon
- **commutator-subgroup** -- G' defines the abelianization

## Related
- **derived-series** -- the abelianization is the first step of the derived series quotients
- **solvable-group** -- solvable iff iterated abelianizations eventually exhaust the group

# Source Reference

Chapter 6, Proposition 6.9, p. 91.

# Verification Notes

- Definition source: Direct from Proposition 6.9
- Confidence rationale: HIGH -- explicit characterization
- Uncertainties: None
