---
# === CORE IDENTIFICATION ===
concept: Groups of Order p^3
slug: groups-of-order-p-cubed

# === CLASSIFICATION ===
category: sylow-theory
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "The Sylow Theorems; Applications"
chapter_number: 5
pdf_page: 82
section: "Examples"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - p-group
  - semidirect-product
  - number-of-sylow-p-subgroups
extends: []
related:
  - nilpotent-group
  - metabelian-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How many nonabelian groups of order p^3 are there for odd prime p?"
---

# Quick Definition

For an odd prime p, there are exactly two nonabelian groups of order p^3: one where every non-identity element has order p (the group (C_p x C_p) rtimes C_p), and one containing elements of order p^2 (the group C_{p^2} rtimes C_p).

# Core Definition

**5.17.** Let G be a noncommutative group of order p^3, p odd.

**Case 1: Every element has order p.** Then the normal subgroup N of order p^2 is isomorphic to C_p x C_p, and G = N rtimes Q for a subgroup Q of order p. The Sylow p-subgroups of Aut(N) = GL_2(F_p) are conjugate, so there is exactly one nonabelian group.

**Case 2: G has elements of order p^2.** Let N = <a> be cyclic of order p^2. Then N is normal (index p, smallest prime). The key facts: Z(G) has order p, G/Z(G) = C_p x C_p, and x -> x^p is a homomorphism G -> G (since (xy)^p = x^p y^p when p is odd). The kernel has order >= p^2, so there exist elements of order p outside N. Hence G = C_{p^2} rtimes C_p.

(Milne, 5.17, pp. 82-83)

# Prerequisites

- **p-group** -- G is a p-group, so Z(G) != 1
- **semidirect-product** -- both groups are semidirect products

# Key Properties

1. Z(G) has order p in both cases
2. G/Z(G) = C_p x C_p (so G is metabelian)
3. G' = Z(G) has order p
4. The map x -> x^p is a homomorphism when p is odd (uses (xy)^p = x^p y^p [y,x]^{p(p-1)/2} and p | p(p-1)/2)

# Examples

**Example 1** (p. 83): For p = 3, the two nonabelian groups of order 27 are the Heisenberg group (C_3 x C_3) rtimes C_3 and C_9 rtimes C_3.

**Example 2**: For p = 2, the nonabelian groups of order 8 are the dihedral group D_4 and the quaternion group Q_8 (constructed differently; see 3.14, 3.15).

# Relationships

## Builds Upon
- **p-group** -- the center is nontrivial
- **semidirect-product** -- structural decomposition

## Related
- **metabelian-group** -- all nonabelian groups of order p^3 are metabelian
- **nilpotent-group** -- all p-groups are nilpotent

# Source Reference

Chapter 5, 5.17, pp. 82-84.

# Verification Notes

- Definition source: Direct from 5.17
- Confidence rationale: HIGH -- explicit classification with two cases
- Uncertainties: None
