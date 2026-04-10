---
concept: Rigidity of Groups of Multiplicative Type
slug: rigidity-of-tori
category: multiplicative-groups
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 173
section: "14f Rigidity"
extraction_confidence: high
aliases:
  - rigidity theorem
prerequisites:
  - group-of-multiplicative-type
  - connected-component-group
extends: []
related:
  - algebraic-torus
contrasts_with: []
answers_questions:
  - "Why are automorphisms of tori rigid?"
---

# Quick Definition

Every action of a connected affine group G on an algebraic group H of multiplicative type is trivial. This "rigidity" means that groups of multiplicative type cannot be continuously deformed as subgroups of a larger group.

# Core Definition

*Theorem 14.32*: Every action of a connected affine group G on an algebraic group H of multiplicative type is trivial. The proof has three cases: (1) when H is finite (the action maps G to the discrete group Aut(H), which must be trivial since G is connected); (2) when G is smooth (uses Lemma 14.33: a group automorphism of a finitely generated abelian group acting trivially mod m for all m must be the identity); (3) general case (uses injectivity of the family of maps V tensor k[M] -> V tensor k[M/nM]) (Milne, pp. 173-175).

# Prerequisites

- **Group of multiplicative type** -- The group being acted upon
- **Connected component group** -- G must be connected

# Key Properties

1. Connected groups cannot act nontrivially on multiplicative type groups
2. In particular, the conjugation action of G^0 on any torus subgroup T is trivial (T is central in G^0)
3. This is why maximal tori in connected groups are all conjugate (they cannot vary continuously)

# Context & Application

Rigidity is a key structural property: it implies that maximal tori in connected groups are conjugate (Proposition 16.35 for solvable groups). It also implies that the character lattice X*(T) is a discrete invariant that cannot change under continuous deformations.

# Examples

**Example 1** (p. 173): Any connected algebraic group G acts trivially on mu_n by conjugation, since Aut(mu_n) is a discrete (etale) group and G is connected.

# Relationships

## Builds Upon
- **Group of multiplicative type** -- Rigidity is a property of these groups

## Enables
- **Conjugacy of maximal tori** -- A consequence of rigidity

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 14f, pages 173-175. Theorem 14.32, Lemma 14.33.

# Verification Notes

- Definition source: Direct from Theorem 14.32
- Confidence rationale: Explicit theorem with three-case proof
- Uncertainties: None
- Cross-reference status: Verified
