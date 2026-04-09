---
# === CORE IDENTIFICATION ===
concept: Groups of Order 99
slug: groups-of-order-99

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
pdf_page: 81
section: "Examples"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - number-of-sylow-p-subgroups
  - unique-sylow-subgroup-criterion
  - direct-product-of-sylow-subgroups
extends: []
related:
  - groups-of-order-pq
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I use Sylow theory to classify groups of a specific order?"
---

# Quick Definition

Every group of order 99 is commutative and isomorphic to C_9 x C_11 (or equivalently C_99). Both Sylow subgroups are forced to be unique and hence normal.

# Core Definition

**5.13.** Let G have order 99 = 9 * 11. Then:
- s_11 divides 9 and s_11 congruent to 1 mod 11, so s_11 = 1
- s_3 divides 11 and s_3 congruent to 1 mod 3, so s_3 = 1

Both Sylow subgroups are normal, so G is isomorphic to the direct product of its Sylow subgroups. Both are commutative (every group of order p^2 is commutative), so G is commutative.

Alternative: the Sylow 11-subgroup N is normal, Q maps onto G/N, so G = N rtimes Q. But Aut(N) = C_10 has no elements of order 3 or 9, so the action is trivial and G = N x Q.

(Milne, 5.13, p. 81)

# Prerequisites

- **number-of-sylow-p-subgroups** -- to force s_p = 1
- **unique-sylow-subgroup-criterion** -- s_p = 1 implies normality
- **direct-product-of-sylow-subgroups** -- all Sylow subgroups normal implies direct product

# Examples

**Example 1** (p. 81): The only group of order 99 is C_9 x C_11 = C_99.

# Relationships

## Builds Upon
- **number-of-sylow-p-subgroups** -- the key computational step

## Related
- **groups-of-order-pq** -- similar technique, simpler case

# Source Reference

Chapter 5, 5.13, p. 81.

# Verification Notes

- Definition source: Direct from 5.13
- Confidence rationale: HIGH -- explicit worked example
- Uncertainties: None
