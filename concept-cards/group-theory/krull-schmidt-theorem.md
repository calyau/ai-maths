---
# === CORE IDENTIFICATION ===
concept: Krull-Schmidt Theorem
slug: krull-schmidt-theorem

# === CLASSIFICATION ===
category: groups-with-operators
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Subnormal Series; Solvable and Nilpotent Groups"
chapter_number: 6
pdf_page: 97
section: "Krull-Schmidt theorem"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Wedderburn-Remak-Schmidt-Krull-Ore theorem

# === TYPED RELATIONSHIPS ===
prerequisites:
  - indecomposable-group
  - direct-product
extends: []
related:
  - jordan-holder-theorem
  - jordan-holder-for-a-groups
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Is the decomposition of a group into indecomposable factors unique?"
---

# Quick Definition

If a finite group G is written as a direct product of indecomposable subgroups in two ways, G = G_1 x ... x G_s = H_1 x ... x H_t, then s = t and (after reindexing) G_i is isomorphic to H_i. Moreover, partial substitutions are possible: G = G_1 x ... x G_r x H_{r+1} x ... x H_t.

# Core Definition

**Theorem 6.31 (Krull-Schmidt).** Suppose that G is a direct product of indecomposable subgroups G_1, ..., G_s and of indecomposable subgroups H_1, ..., H_t:

G = G_1 x ... x G_s, G = H_1 x ... x H_t.

Then s = t, and there is a re-indexing such that G_i is isomorphic to H_i. Moreover, given r, we can arrange the numbering so that

G = G_1 x ... x G_r x H_{r+1} x ... x H_t.

(Milne, Theorem 6.31, p. 97)

# Prerequisites

- **indecomposable-group** -- the factors in the decomposition
- **direct-product** -- the structural notion

# Key Properties

1. The number of indecomposable factors is an invariant
2. The multiset of isomorphism types of factors is an invariant
3. The "replacement property": any initial segment of one decomposition can replace the corresponding segment of the other
4. The theorem also holds for groups with operators (Remark 6.33b)
5. The theorem holds for infinite groups satisfying both chain conditions (Remark 6.33a)
6. For finite abelian groups, it gives uniqueness of the decomposition into cyclic groups of prime-power order (Remark 6.33c)

# Examples

**Example 1** (p. 98, 6.32): G = F_p x F_p can be decomposed as <(1,0)> x <(0,1)> or as <(1,1)> x <(1,-1)>, with G_1 x H_2 = <(1,0)> x <(1,-1)> also working (the replacement property).

# Relationships

## Builds Upon
- **indecomposable-group** -- the factors

## Related
- **jordan-holder-theorem** -- analogous uniqueness result for composition factors (simple groups) vs. indecomposable factors

# Common Confusions

- **Confusion**: Confusing the Krull-Schmidt decomposition with the composition series
  **Clarification**: Krull-Schmidt is about direct product decomposition into indecomposable groups; Jordan-Holder is about subnormal series with simple quotients. They are parallel but distinct uniqueness results.

# Source Reference

Chapter 6, Theorem 6.31, pp. 97-98. Proof: reference to Rotman 1995, 6.36. Remarks 6.33.

# Verification Notes

- Definition source: Direct from Theorem 6.31
- Confidence rationale: HIGH -- explicit theorem (proof by reference)
- Uncertainties: None
