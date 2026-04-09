---
# === CORE IDENTIFICATION ===
concept: "Non-Simplicity of Groups of Order 2^m p^n"
slug: groups-of-order-2m-4m-8m-pn

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - number-of-sylow-p-subgroups
  - non-simplicity-criteria
extends:
  - non-simplicity-criteria
related:
  - simple-group-of-order-60
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Are groups of order 2p^n, 4p^n, or 8p^n simple?"
---

# Quick Definition

No group of order 2^m p^n (1 <= m <= 3, p odd, n >= 1) is simple. The proof uses Sylow counting: if s_p > 1, the only possibilities are s_p = 4 with p = 3 or s_p = 8 with p = 7, and both lead to contradictions with simplicity.

# Core Definition

**5.18.** Let G have order 2^m p^n, 1 <= m <= 3, p odd, n >= 1. Then G is not simple.

Analysis: s_p | 2^m and s_p congruent to 1 mod p. If s_p != 1, only two cases arise:
- s_p = 4, p = 3: embedding G -> S_4 forces |G| | 24, so n = 1 and |G| = 2^m * 3. The Sylow 2-subgroup has index 3, giving G -> S_3 with nontrivial kernel.
- s_p = 8, p = 7: then |G| = 56 with 48 elements of order 7, leaving only one Sylow 2-subgroup (normal).

Also: groups of order pq^r (p < q primes) are not simple since the Sylow q-subgroup has index p (smallest prime dividing |G|) and is therefore normal.

(Milne, 5.18, p. 83)

# Prerequisites

- **number-of-sylow-p-subgroups** -- the constraints on s_p
- **non-simplicity-criteria** -- the general method

# Relationships

## Builds Upon
- **non-simplicity-criteria** -- specific instances of the general method

## Related
- **simple-group-of-order-60** -- A_5 is the remaining case

# Source Reference

Chapter 5, 5.18, p. 83.

# Verification Notes

- Definition source: Direct from 5.18
- Confidence rationale: HIGH -- explicit argument
- Uncertainties: None
