---
# === CORE IDENTIFICATION ===
concept: Simple Group of Order 60
slug: simple-group-of-order-60

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
pdf_page: 83
section: "Examples"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - uniqueness of A_5

# === TYPED RELATIONSHIPS ===
prerequisites:
  - number-of-sylow-p-subgroups
  - non-simplicity-criteria
extends: []
related:
  - alternating-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Is there a unique simple group of order 60?"
  - "How does Sylow theory prove G of order 60 simple implies G = A_5?"
---

# Quick Definition

Any simple group of order 60 is isomorphic to A_5. This is proved by analyzing the possible values of s_2 (the number of Sylow 2-subgroups) and showing that only s_2 = 5 is consistent with simplicity, which embeds G as a subgroup of index 2 in S_5, hence G = A_5.

# Core Definition

**5.19.** Let G be a simple group of order 60 = 2^2 * 3 * 5. Let P be a Sylow 2-subgroup with s_2 = (G : N_G(P)). Then s_2 in {1, 3, 5, 15}.

- s_2 = 1: impossible (P would be normal)
- s_2 = 3: impossible (kernel of G -> S_3 gives a normal subgroup)
- s_2 = 5: G embeds in S_5 as a subgroup of index 2, hence G = A_5
- s_2 = 15: counting argument (using s_5 = 6) shows two Sylow 2-subgroups P, Q intersect in order 2. The normalizer of P intersect Q has index 1, 3, or 5; only index 5 avoids contradictions, but that gives s_2(A_5) = 5, contradicting s_2 = 15.

Therefore G = A_5.

(Milne, 5.19, pp. 83-84)

# Prerequisites

- **number-of-sylow-p-subgroups** -- constraints on s_2
- **non-simplicity-criteria** -- the systematic case analysis

# Key Properties

1. A_5 is the unique simple group of order 60 (up to isomorphism)
2. A_5 is the smallest non-cyclic simple group
3. The proof is a case-by-case elimination using Sylow theory and group actions

# Relationships

## Builds Upon
- **non-simplicity-criteria** -- eliminates smaller orders

## Related
- **alternating-group** -- A_5 is the specific group identified

# Source Reference

Chapter 5, 5.19, pp. 83-84.

# Verification Notes

- Definition source: Direct from 5.19
- Confidence rationale: HIGH -- explicit proof by case analysis
- Uncertainties: None
