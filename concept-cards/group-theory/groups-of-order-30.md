---
# === CORE IDENTIFICATION ===
concept: Groups of Order 30
slug: groups-of-order-30

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
  - number-of-sylow-p-subgroups
  - semidirect-product
extends: []
related:
  - groups-of-order-pq
  - groups-of-order-12
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How many groups of order 30 are there?"
  - "How does element counting complement Sylow theory?"
---

# Quick Definition

There are exactly 4 groups of order 30, all of the form (C_3 x C_5) rtimes C_2. They are distinguished by the action of C_2 on C_3 x C_5, which is determined by choosing inversions on each factor independently.

# Core Definition

**5.15.** Let |G| = 30 = 2 * 3 * 5. Sylow constraints give s_3 in {1, 10} and s_5 in {1, 6}. An element counting argument shows at least one must equal 1 (otherwise 20 elements of order 3 and 24 of order 5). So H = PQ (where P, Q are the Sylow 3- and 5-subgroups) is a subgroup of order 15. Since 3 does not divide 4 = 5 - 1, H = C_3 x C_5 = C_15. Then G = (C_3 x C_5) rtimes_theta C_2.

The four groups correspond to four choices for theta(c) where c generates C_2:
1. a -> a, b -> b (centre of order 30, cyclic)
2. a -> a, b -> b^{-1} (centre of order 3)
3. a -> a^{-1}, b -> b (centre of order 5)
4. a -> a^{-1}, b -> b^{-1} (centre of order 1)

These are pairwise non-isomorphic (distinguished by the size of their centres).

(Milne, 5.15, pp. 82-83)

# Prerequisites

- **number-of-sylow-p-subgroups** -- to constrain s_3, s_5
- **semidirect-product** -- the classification uses semidirect products

# Key Properties

1. Element counting is needed beyond pure Sylow constraints
2. The subgroup of order 15 is always cyclic (unique group of order 15)
3. Aut(C_3 x C_5) = Aut(C_3) x Aut(C_5) = C_2 x C_4
4. Elements of order 2 in the automorphism group determine the four homomorphisms

# Examples

**Example 1** (p. 83): The third group has generators a, b, c with a^3 = b^5 = c^2 = 1, ab = ba, cac^{-1} = a^{-1}, cbc^{-1} = b, and has centre of order 5.

# Relationships

## Builds Upon
- **number-of-sylow-p-subgroups** -- initial constraints
- **semidirect-product** -- structural decomposition

## Related
- **groups-of-order-pq** -- the subgroup of order 15 is analyzed this way
- **groups-of-order-12** -- another worked classification

# Source Reference

Chapter 5, 5.15, pp. 82-83.

# Verification Notes

- Definition source: Direct from 5.15
- Confidence rationale: HIGH -- explicit classification with four groups listed
- Uncertainties: None
