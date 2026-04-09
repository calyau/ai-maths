---
# === CORE IDENTIFICATION ===
concept: p-Group
slug: p-group

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
pdf_page: 8
section: "Definitions and examples"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - prime-power group

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
  - order-of-a-group
extends:
  - group
related:
  - groups-of-small-order
  - cyclic-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a p-group?"
  - "What does it mean for a group to have prime-power order?"
---

# Quick Definition

A p-group is a finite group whose order is a power of a prime p. For example, any group of order 4 = 2^2 or 8 = 2^3 is a 2-group.

# Core Definition

A finite group whose order is a power of a prime p is called a **p-group** (p. 8).

# Prerequisites

- **Group** — a p-group is a special kind of group
- **Order of a group** — the defining condition is on |G|

# Key Properties

1. |G| = p^k for some prime p and integer k >= 1
2. The number of groups of order p^k grows rapidly with k
3. For order 16 = 2^4, there are 14 groups (p. 14, table)
4. Every group of prime order p is cyclic, isomorphic to C_p (referenced as 1.28)

# Construction / Recognition

## To Recognize:
1. Compute |G|
2. Check if |G| is a power of a prime

# Context & Application

p-groups are among the most intensively studied classes of groups. The classification of groups of small order shows that the most groups occur at prime-power orders — for example, order 16 has 14 groups while order 15 has only 1 (p. 14). The general bound f(n) <= n^{(2/27 + o(1))e(n)^2} shows the number of groups grows with the largest prime-power factor of n (p. 14).

# Examples

**Example 1** (p. 14): Groups of order 4 = 2^2: C_4 and C_2 x C_2 (two 2-groups).

**Example 2** (p. 14): Groups of order 8 = 2^3: C_8, C_2 x C_4, C_2 x C_2 x C_2, Q, D_4 (five 2-groups).

**Example 3** (p. 14): Groups of order 9 = 3^2: C_9 and C_3 x C_3 (two 3-groups).

# Relationships

## Builds Upon
- **order-of-a-group** — p-groups are defined by their order

## Enables
- **groups-of-small-order** — p-groups dominate the classification at prime-power orders

## Related
- **cyclic-group** — every group of prime order is cyclic

# Common Errors

- **Error**: Assuming all p-groups are abelian
  **Correction**: The quaternion group Q and D_4 are non-abelian 2-groups of order 8

# Common Confusions

- **Confusion**: Thinking "p-group" means a group of order p
  **Clarification**: A p-group has order p^k for any k >= 1, not just k = 1

# Source Reference

Chapter 1: Basic Definitions and Results, page 8.

# Verification Notes

- Definition source: Direct from text, p. 8
- Confidence rationale: HIGH — explicitly defined in one sentence
- Uncertainties: None
- Cross-reference status: Verified against planned cards
