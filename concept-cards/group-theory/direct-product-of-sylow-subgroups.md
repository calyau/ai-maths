---
# === CORE IDENTIFICATION ===
concept: Direct Product of Sylow Subgroups
slug: direct-product-of-sylow-subgroups

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
pdf_page: 79
section: "The Sylow theorems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - sylow-p-subgroup
  - unique-sylow-subgroup-criterion
  - direct-product
extends:
  - unique-sylow-subgroup-criterion
related:
  - nilpotent-iff-direct-product-of-sylow
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When is a finite group a direct product of its Sylow subgroups?"
---

# Quick Definition

If a finite group G has a unique Sylow p-subgroup for every prime p dividing |G|, then G is the direct product of its Sylow subgroups.

# Core Definition

**Corollary 5.9.** Suppose that a group G has only one Sylow p-subgroup for each prime p dividing its order. Then G is a direct product of its Sylow p-subgroups.

(Milne, Corollary 5.9, p. 79)

# Prerequisites

- **sylow-p-subgroup** -- the factors of the direct product
- **unique-sylow-subgroup-criterion** -- each Sylow subgroup must be normal (unique)
- **direct-product** -- the structural notion being applied

# Key Properties

1. Each P_i is normal in G (since unique)
2. The product P_1 ... P_k is all of G by order counting
3. For distinct primes, P_i intersect P_j = {1}
4. The proof uses induction: P_1 ... P_{k-1} intersect P_k = {1}, giving a direct product

# Context & Application

This is the structural payoff when all Sylow subgroups are normal. It reduces the study of G to studying each Sylow subgroup separately. This is exactly the condition characterizing finite nilpotent groups (Theorem 6.18).

# Examples

**Example 1** (p. 81, 5.13): A group of order 99 has unique Sylow 3-subgroup and unique Sylow 11-subgroup, so G is isomorphic to C_9 x C_11 (since both subgroups are abelian).

# Relationships

## Builds Upon
- **unique-sylow-subgroup-criterion** -- all Sylow subgroups must be normal

## Enables
- **nilpotent-iff-direct-product-of-sylow** -- this property characterizes nilpotent groups

# Source Reference

Chapter 5, Corollary 5.9, p. 79-80.

# Verification Notes

- Definition source: Direct from Corollary 5.9
- Confidence rationale: HIGH -- explicit corollary with proof
- Uncertainties: None
