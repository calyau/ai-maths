---
# === CORE IDENTIFICATION ===
concept: Groups of Order 12
slug: groups-of-order-12

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
  - groups-of-order-30
  - groups-of-order-pq
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How many groups of order 12 are there?"
  - "How does the non-normal Sylow case lead to a specific group?"
---

# Quick Definition

There are exactly 5 groups of order 12: two abelian (C_12 and C_2 x C_2 x C_3) and three nonabelian (A_4, C_3 rtimes C_4, and S_3 x C_2). The analysis splits on whether the Sylow 3-subgroup is normal.

# Core Definition

**5.16.** Let |G| = 12 = 2^2 * 3. Then s_3 in {1, 4}.

**Case s_3 = 4 (P not normal):** P contains no nontrivial normal subgroup of G, so G embeds in Sym(G/P) = S_4. The image has order 12 and contains 8 elements of order 3 (from the 4 Sylow 3-subgroups). Since all elements of S_4 of order 3 lie in A_4, the image intersects A_4 in at least 8 elements, forcing G = A_4.

**Case s_3 = 1 (P normal):** G = P rtimes Q where Q is the Sylow 2-subgroup (order 4).
- Q = C_4: unique nontrivial map C_4 -> Aut(C_3) = C_2 gives C_3 rtimes C_4
- Q = C_2 x C_2: three nontrivial maps Q -> Aut(C_3), all giving S_3 x C_2

Total: 3 noncommutative + 2 commutative = 5 groups.

(Milne, 5.16, p. 82)

# Prerequisites

- **number-of-sylow-p-subgroups** -- s_3 in {1, 4} is the branching point
- **semidirect-product** -- the normal Sylow case uses semidirect products

# Examples

**Example 1** (p. 82): When s_3 = 4, the embedding G -> S_4 identifies G with A_4.

**Example 2** (p. 82): When Q = C_2 x C_2, the three maps theta: Q -> Aut(C_3) give isomorphic groups because they differ by an automorphism of Q.

# Relationships

## Builds Upon
- **number-of-sylow-p-subgroups** -- branching on s_3
- **semidirect-product** -- construction in the normal case

## Related
- **groups-of-order-30** -- similar classification technique
- **simple-group-of-order-60** -- A_4 appears as a key subgroup

# Source Reference

Chapter 5, 5.16, p. 82.

# Verification Notes

- Definition source: Direct from 5.16
- Confidence rationale: HIGH -- explicit classification
- Uncertainties: None
