---
# === CORE IDENTIFICATION ===
concept: Groups of Order pq
slug: groups-of-order-pq

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
  - sylow-second-theorem
  - number-of-sylow-p-subgroups
  - semidirect-product
extends: []
related:
  - groups-of-order-99
  - groups-of-order-12
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How many groups of order pq are there (p < q primes)?"
  - "How do I classify groups of small order using Sylow theory?"
---

# Quick Definition

For primes p < q, there is exactly one group of order pq (the cyclic group C_pq) unless p divides q - 1, in which case there is also exactly one nonabelian group, a semidirect product C_q rtimes C_p.

# Core Definition

**5.14.** Let |G| = pq with p < q primes. The Sylow q-subgroup Q is normal (since (G : Q) = p is the smallest prime dividing |G|). Then G = Q rtimes P where P is a Sylow p-subgroup, and the structure depends on the homomorphism theta: P -> Aut(Q).

Since Aut(Q) is cyclic of order q - 1:
- If p does not divide q - 1: only the trivial homomorphism exists, so G = C_q x C_p = C_pq
- If p divides q - 1: there is a unique subgroup of order p in Aut(Q), giving exactly one nonabelian group with generators a, b and relations a^p = 1, b^q = 1, aba^{-1} = b^{i_0} where i_0 has order p in (Z/qZ)*.

(Milne, 5.14, p. 81-82)

# Prerequisites

- **sylow-second-theorem** -- to determine normality of Q
- **number-of-sylow-p-subgroups** -- to compute s_p, s_q
- **semidirect-product** -- the nonabelian case is a semidirect product

# Key Properties

1. Q = C_q is always normal (index p, smallest prime dividing |G|)
2. G = Q rtimes P, so the group is determined by theta: C_p -> Aut(C_q) = C_{q-1}
3. Different nontrivial homomorphisms give isomorphic groups (different generators of P)
4. There are exactly 1 or 2 groups of order pq

# Examples

**Example 1** (p. 81, 5.13): Order 99 = 9 * 11. Since 9 does not divide 10 = 11 - 1, the only group is C_99. (Here p = 9, q = 11 is adapted; but 99 = 9 * 11 where gcd(9, 10) = 1.)

**Example 2**: Order 6 = 2 * 3. Since 2 | 3 - 1 = 2, there are two groups: C_6 and S_3.

**Example 3**: Order 15 = 3 * 5. Since 3 does not divide 4 = 5 - 1, the only group is C_15.

# Relationships

## Builds Upon
- **number-of-sylow-p-subgroups** -- determines whether Sylow subgroups are normal
- **semidirect-product** -- the nonabelian group is constructed this way

## Enables
- Classification of groups of small order

## Related
- **groups-of-order-99** -- similar analysis
- **groups-of-order-12** -- more complex case

# Common Errors

- **Error**: Forgetting to check whether p | q - 1
  **Correction**: This divisibility condition determines whether a nonabelian group exists

# Source Reference

Chapter 5, 5.14, pp. 81-82.

# Verification Notes

- Definition source: Direct from 5.14
- Confidence rationale: HIGH -- explicit classification
- Uncertainties: None
