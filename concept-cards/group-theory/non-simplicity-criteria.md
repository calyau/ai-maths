---
# === CORE IDENTIFICATION ===
concept: Non-Simplicity Criteria from Sylow Theory
slug: non-simplicity-criteria

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
  - Sylow non-simplicity arguments

# === TYPED RELATIONSHIPS ===
prerequisites:
  - number-of-sylow-p-subgroups
  - unique-sylow-subgroup-criterion
extends: []
related:
  - simple-group-of-order-60
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I use Sylow theory to prove a group is not simple?"
  - "What is the smallest non-cyclic simple group?"
---

# Quick Definition

Sylow theory provides several methods to prove a finite group is not simple: forcing s_p = 1 (giving a normal Sylow subgroup), or using the conjugation action on Sylow subgroups to embed G into a symmetric group of too-small order.

# Core Definition

**5.18.** Let |G| = 2^m p^n with 1 <= m <= 3, p odd, n >= 1. Then G is not simple.

From Sylow II, s_p | 2^m and s_p congruent to 1 mod p. If s_p != 1, the only cases are:
- s_p = 4, p = 3 (so |G| divides 4! = 24, forcing n = 1)
- s_p = 8, p = 7 (so |G| divides 8! but n = 1, giving |G| = 56 with 48 elements of order 7 and a unique hence normal Sylow 2-subgroup)

In both cases, G has a normal subgroup.

Groups of order pq^r (p < q primes) are also not simple: the Sylow q-subgroup is normal since its index p is the smallest prime dividing |G|.

Conclusion: A_5 (order 60) is the smallest non-cyclic simple group.

(Milne, 5.18, p. 83)

# Prerequisites

- **number-of-sylow-p-subgroups** -- the constraints on s_p
- **unique-sylow-subgroup-criterion** -- s_p = 1 gives normality

# Key Properties

1. If G is simple with s_p > 1, the map G -> Sym(Sylow p-subgroups) is injective
2. This bounds |G| by s_p!
3. Element counting: each Sylow p-subgroup of order p^r contributes up to p^r - 1 elements of p-power order
4. If too many Sylow subgroups are required, the element count exceeds |G|

# Context & Application

These arguments systematically eliminate small orders from having non-cyclic simple groups. Combined with the classification of groups of order < 60, they show A_5 is the smallest non-cyclic simple group.

# Relationships

## Builds Upon
- **number-of-sylow-p-subgroups** -- the main tool

## Enables
- **simple-group-of-order-60** -- the remaining case to analyze

# Source Reference

Chapter 5, 5.18, p. 83.

# Verification Notes

- Definition source: Direct from 5.18
- Confidence rationale: HIGH -- explicit argument
- Uncertainties: None
