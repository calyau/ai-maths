---
concept: Third Sylow Theorem
slug: third-sylow-theorem
category: group-theory
subcategory: sylow-theory
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "More Group Theory"
chapter_number: 7
pdf_page: 206
section: "7.7 The Sylow Theorems"
extraction_confidence: high
aliases: []
prerequisites:
  - sylow-p-subgroup
  - second-sylow-theorem
  - normalizer
extends: []
related:
  - first-sylow-theorem
contrasts_with: []
answers_questions:
  - "How many Sylow p-subgroups can a group have?"
  - "How do I apply the Sylow theorems to analyze a finite group?"
---

# Quick Definition

The Third Sylow Theorem states that the number s of Sylow p-subgroups divides m (where |G| = p^e * m) and s is congruent to 1 modulo p. This severely restricts the possible values of s.

# Core Definition

Let G be a finite group of order n = p^e * m (p does not divide m), and let s be the number of Sylow p-subgroups. Then s divides m and s = kp + 1 for some integer k >= 0 (Artin, Theorem 7.7.6, p. 218). The proof uses: s = [G : N(H)] divides m (since N(H) contains H), and the H-orbit decomposition of the set of Sylow subgroups shows only [H] is fixed by H.

# Prerequisites

- **Sylow p-subgroup** — What is being counted
- **Second Sylow theorem** — Conjugacy (transitivity) is used
- **Normalizer** — s = [G : N(H)]

# Key Properties

1. s divides m = |G|/p^e
2. s = 1 mod p
3. s = 1 iff the Sylow p-subgroup is normal
4. Often these two conditions force s = 1

# Construction / Recognition

## To Apply:
1. Write |G| = p^e * m
2. List divisors of m that are congruent to 1 mod p
3. These are the possible values of s

# Context & Application

The Third Sylow Theorem is the counting theorem that makes the Sylow theorems practically useful. The two conditions (s | m and s = 1 mod p) are often so restrictive that s = 1, forcing the Sylow subgroup to be normal. This is the primary method for classifying groups of small order.

# Examples

**Example 1** (p. 218): Order 15: s_3 divides 5 and s_3 = 1 mod 3, so s_3 = 1. Similarly s_5 = 1. Both Sylow subgroups are normal, giving G = C_15.

**Example 2** (p. 218): Order 6: s_3 divides 2 and s_3 = 1 mod 3, so s_3 = 1. s_2 divides 3 and s_2 = 1 mod 2, so s_2 = 1 or 3.

**Example 3** (p. 219): Order 21: s_7 divides 3 and s_7 = 1 mod 7, so s_7 = 1. s_3 divides 7 and s_3 = 1 mod 3, so s_3 = 1 or 7.

# Relationships

## Builds Upon
- **Normalizer** — s = [G : N(H)]
- **Second Sylow theorem** — Transitivity on the set of Sylow subgroups

## Enables
- **Group classification** — Forces normal subgroups when s = 1

# Common Errors

- **Error**: Forgetting to check BOTH conditions (s | m and s = 1 mod p)
  **Correction**: Both conditions must hold simultaneously

# Source Reference

Chapter 7: More Group Theory, Section 7.7, Theorem 7.7.6, pages 218, 221-222.

# Verification Notes

- Definition source: Direct from Theorem 7.7.6
- Confidence rationale: Named theorem, explicitly stated and proved
- Uncertainties: None
- Cross-reference status: Verified
