---
# === CORE IDENTIFICATION ===
concept: Number of Sylow p-Subgroups
slug: number-of-sylow-p-subgroups

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
pdf_page: 78
section: "The Sylow theorems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - s_p constraints
  - Sylow number

# === TYPED RELATIONSHIPS ===
prerequisites:
  - sylow-p-subgroup
  - sylow-second-theorem
  - normalizer-and-sylow
extends:
  - sylow-second-theorem
related:
  - unique-sylow-subgroup-criterion
  - groups-of-order-pq
  - groups-of-order-12
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I compute the number of Sylow p-subgroups?"
  - "What constraints does the Sylow theorem place on s_p?"
---

# Quick Definition

The number s_p of Sylow p-subgroups of a finite group G with |G| = p^r m satisfies two constraints: s_p divides m and s_p is congruent to 1 mod p. These constraints often force s_p = 1, making the Sylow subgroup normal.

# Core Definition

Let G be a finite group with |G| = p^r m, gcd(p, m) = 1, and let P be a Sylow p-subgroup. The number s_p of Sylow p-subgroups satisfies:

1. s_p congruent to 1 (mod p)
2. s_p divides m
3. s_p = (G : N_G(P))

(Milne, Theorem 5.6(b), p. 78)

# Prerequisites

- **sylow-p-subgroup** -- the objects being counted
- **sylow-second-theorem** -- establishes these constraints
- **normalizer-and-sylow** -- s_p equals the index of the normalizer

# Key Properties

1. s_p = 1 if and only if the Sylow p-subgroup is normal
2. s_p = (G : N_G(P)) for any Sylow p-subgroup P, since conjugates biject with cosets of the normalizer
3. Both constraints must hold simultaneously, which often pins down s_p
4. Each Sylow p-subgroup contributes elements to G; counting elements can further constrain s_p

# Construction / Recognition

## To Compute s_p:
1. Factor |G| = p^r m with gcd(p, m) = 1
2. List all d dividing m with d congruent to 1 mod p
3. Each such d is a candidate for s_p
4. Use additional arguments (element counting, group actions) to narrow further

## Element Counting Argument:
If distinct Sylow p-subgroups intersect only in {1}, then each contributes p^r - 1 elements of order a power of p. This gives at most (|G| - 1)/(p^r - 1) Sylow subgroups.

# Context & Application

Computing s_p is the standard first step when classifying groups of a given order. When the constraints force s_p = 1, the Sylow subgroup is normal, greatly simplifying the group structure (often leading to semidirect product decompositions).

# Examples

**Example 1** (p. 81, 5.13): For |G| = 99 = 9 * 11: s_11 divides 9 and s_11 congruent to 1 mod 11, so s_11 = 1. Also s_3 divides 11 and s_3 congruent to 1 mod 3, so s_3 = 1.

**Example 2** (p. 82, 5.15): For |G| = 30: s_3 divides 10 and s_3 congruent to 1 mod 3, giving s_3 in {1, 10}. Similarly s_5 divides 6 and s_5 congruent to 1 mod 5, giving s_5 in {1, 6}. An element counting argument shows at least one equals 1.

**Example 3** (p. 82, 5.16): For |G| = 12: s_3 divides 4 and s_3 congruent to 1 mod 3, giving s_3 in {1, 4}.

# Relationships

## Builds Upon
- **sylow-second-theorem** -- source of the constraints

## Enables
- **groups-of-order-pq** -- s_p constraints classify these groups
- **groups-of-order-12** -- s_3 determines the structure
- **non-simplicity-criteria** -- s_p = 1 implies a normal subgroup

## Related
- **unique-sylow-subgroup-criterion** -- s_p = 1 iff normal

# Common Errors

- **Error**: Using s_p divides |G| instead of s_p divides m
  **Correction**: s_p divides the p'-part m, not the full order |G|

- **Error**: Forgetting the congruence condition and only using the divisibility condition
  **Correction**: Both conditions must be applied together; the congruence condition s_p congruent to 1 mod p is often the more restrictive one

# Common Confusions

- **Confusion**: Thinking s_p = 1 means the group is abelian
  **Clarification**: s_p = 1 means the Sylow p-subgroup is normal, but the group may still be nonabelian (e.g., S_3 has s_3 = 1 but is nonabelian)

# Source Reference

Chapter 5, Theorem 5.6(b), p. 78-79. Applications throughout Section "Examples," pp. 81-84.

# Verification Notes

- Definition source: Direct from Theorem 5.6(b)
- Confidence rationale: HIGH -- explicitly stated constraints
- Uncertainties: None
