---
# === CORE IDENTIFICATION ===
concept: Jordan-Holder Theorem
slug: jordan-holder-theorem

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
pdf_page: 87
section: "Subnormal Series"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Jordan-Hoelder theorem"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - composition-series
  - composition-factors
  - simple-group
extends: []
related:
  - jordan-holder-for-a-groups
  - solvable-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Are the composition factors of a group unique?"
  - "What background is needed for the Jordan-Holder theorem?"
---

# Quick Definition

Any two composition series of a finite group have the same length and the same composition factors (up to reordering and isomorphism). This is the group-theoretic analogue of unique prime factorization.

# Core Definition

**Theorem 6.2 (Jordan-Holder).** Let G be a finite group. If

G = G_0 > G_1 > ... > G_s = {1} and G = H_0 > H_1 > ... > H_t = {1}

are two composition series for G, then s = t and there is a permutation sigma of {1, 2, ..., s} such that G_i/G_{i+1} is isomorphic to H_{sigma(i)}/H_{sigma(i)+1}.

Jordan showed that corresponding quotients have the same order; Holder showed they are isomorphic.

(Milne, Theorem 6.2, p. 87)

# Prerequisites

- **composition-series** -- the objects being compared
- **composition-factors** -- the quotients whose uniqueness is asserted
- **simple-group** -- the factors are simple, which is used in the proof (maximality of normal subgroups)

# Key Properties

1. The number of composition factors is an invariant of G
2. The multiset of composition factors (up to isomorphism) is an invariant of G
3. Applied to C_m, the theorem recovers the fundamental theorem of arithmetic
4. The proof uses induction on |G|, with two cases: G_1 = H_1 (use induction) and G_1 != H_1 (use the isomorphism theorems and the "butterfly" argument)

# Construction / Recognition

## Proof Strategy:
- **Case I** (G_1 = H_1): Apply induction to G_1.
- **Case II** (G_1 != H_1): Set K_2 = G_1 intersect H_1. Then G/G_1 = H_1/K_2 and G/H_1 = G_1/K_2 (isomorphism theorems). Choose a composition series for K_2 and use induction on G_1 and H_1 to match all factors.

# Context & Application

The Jordan-Holder theorem is fundamental to the program of classifying finite groups: it says that every finite group has a well-defined set of "prime factors" (simple groups), even though the group may not be uniquely determined by these factors. It generalizes to groups with operators (Theorem 6.29) and to infinite groups with finite composition series (Remark 6.3a).

# Examples

**Example 1** (p. 87, 6.1d): For C_m = <a>, different factorizations m = p_1 ... p_r of m give different composition series, but the Jordan-Holder theorem says the multiset {p_1, ..., p_r} is the same -- recovering unique factorization.

**Example 2** (p. 87, 6.1e): For G = H_1 x ... x H_r with H_i simple, any permutation gives a composition series with the same factors in different order.

# Relationships

## Builds Upon
- **composition-series** -- the theorem concerns composition series

## Enables
- **composition-factors** -- well-defined as invariants of G
- **solvable-group** -- solvability can be checked on any composition series

## Related
- **jordan-holder-for-a-groups** -- the generalization to groups with operators

# Common Errors

- **Error**: Thinking the theorem says the composition *series* are the same
  **Correction**: Only the multiset of composition *factors* is invariant; the series themselves can be quite different

# Common Confusions

- **Confusion**: Thinking the theorem determines G from its composition factors
  **Clarification**: Many non-isomorphic groups have the same composition factors. The theorem gives uniqueness of factors, not uniqueness of the group.

# Source Reference

Chapter 6, Theorem 6.2, pp. 87-88. Remark 6.3 on extensions to infinite groups.

# Verification Notes

- Definition source: Direct from Theorem 6.2
- Confidence rationale: HIGH -- explicitly stated and proved theorem
- Uncertainties: None
