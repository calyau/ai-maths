---
# === CORE IDENTIFICATION ===
concept: Groups of Small Order
slug: groups-of-small-order

# === CLASSIFICATION ===
category: group-fundamentals
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Basic Definitions and Results"
chapter_number: 1
pdf_page: 14
section: "Groups of small order"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - classification of small groups
  - enumeration of groups

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
  - order-of-a-group
  - isomorphism-of-groups
  - cyclic-group
  - dihedral-group
  - direct-product-of-groups
  - quaternion-group
extends: []
related:
  - p-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How many groups of a given order are there?"
  - "What are all groups of order 4, 6, or 8?"
  - "Why do prime-power orders have more groups?"
---

# Quick Definition

The classification of groups of small order enumerates all groups up to isomorphism for each positive integer. For prime order p there is only one group (C_p); the number of groups grows with the largest prime-power factor of the order.

# Core Definition

For each prime p, there is only one group of order p, namely C_p (referenced as Proposition 1.28). The section provides a classification table for groups of order 4 through 24 (p. 14). The number of isomorphism classes f(n) of groups of order n satisfies f(n) <= n^{(2/27 + o(1))e(n)^2} where e(n) is the largest exponent of a prime dividing n (Pyber 1993).

By 2001, a complete list of groups of order <= 2000 was found: exactly 49,910,529,484 isomorphism classes (Besche et al. 2001).

# Prerequisites

- **Group**, **order of a group**, **isomorphism of groups** — classification is up to isomorphism by order
- **Cyclic group**, **dihedral group**, **direct product of groups**, **quaternion group** — these families appear in the classification

# Key Properties

Selected entries from the classification table (p. 14):

1. Order 4: 2 groups (C_4, C_2 x C_2) — both abelian
2. Order 6: 2 groups (C_6; S_3) — 1 abelian, 1 non-abelian
3. Order 8: 5 groups (C_8, C_2 x C_4, C_2 x C_2 x C_2; Q, D_4) — 3 abelian, 2 non-abelian
4. Order 9: 2 groups (C_9, C_3 x C_3) — both abelian
5. Order 15: 1 group (C_15) — abelian
6. Order 16: 14 groups — 5 abelian, 9 non-abelian
7. Order 24: 15 groups — 3 abelian, 12 non-abelian
8. More prime-power factors in n leads to more groups of order n

# Construction / Recognition

## Pattern for Recognizing Group Counts:
1. Prime order p: exactly 1 group (C_p)
2. Order p^2: exactly 2 groups (C_{p^2} and C_p x C_p)
3. Order 2p (p odd prime): exactly 2 groups (C_{2p} and D_p)
4. Higher prime powers: many more groups

# Context & Application

The classification of groups of small order is a central organizing problem in group theory. Cayley initiated this classification in 1878 (though he famously miscounted for order 6, listing three groups instead of two). The problem becomes intractable for large orders, especially at prime powers: there are 49,487,365,422 groups of order 1024 = 2^{10} alone.

# Examples

**Example 1** (p. 14, table): Order 4 has exactly 2 groups: C_4 and V_4 = C_2 x C_2.

**Example 2** (p. 14, table): Order 8 has exactly 5 groups: three abelian (C_8, C_2 x C_4, C_2^3) and two non-abelian (Q, D_4).

**Example 3** (p. 14): There are exactly 49,910,529,484 groups of order <= 2000 up to isomorphism.

# Relationships

## Builds Upon
- **isomorphism-of-groups** — classification is up to isomorphism
- **cyclic-group**, **dihedral-group**, **quaternion-group**, **direct-product-of-groups** — the building blocks

## Related
- **p-group** — prime-power orders dominate the group count

# Common Errors

- **Error**: Cayley's miscount of groups of order 6 (listing three instead of two)
  **Correction**: C_2 x C_3 and C_6 are isomorphic, so there are only 2 groups of order 6: C_6 and S_3 (p. 14)

# Common Confusions

- **Confusion**: Thinking the number of groups grows simply with the order
  **Clarification**: The growth depends primarily on the largest prime-power factor of the order, not the order itself (e.g., order 15 has 1 group, but order 16 has 14)

# Source Reference

Chapter 1: Basic Definitions and Results, section "Groups of small order," page 14.

# Verification Notes

- Definition source: Direct from the classification table and discussion, p. 14
- Confidence rationale: HIGH — explicit table with references to proofs
- Uncertainties: None
- Cross-reference status: Verified against planned cards
