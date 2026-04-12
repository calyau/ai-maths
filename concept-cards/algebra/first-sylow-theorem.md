---
concept: First Sylow Theorem
slug: first-sylow-theorem
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
  - operation-on-subsets
extends: []
related:
  - cauchys-theorem
  - second-sylow-theorem
  - third-sylow-theorem
contrasts_with: []
answers_questions:
  - "Does every finite group have a Sylow p-subgroup?"
  - "How do I apply the Sylow theorems to analyze a finite group?"
---

# Quick Definition

The First Sylow Theorem states that a finite group whose order is divisible by a prime p contains a Sylow p-subgroup (a subgroup of order p^e, where p^e is the largest power of p dividing |G|).

# Core Definition

A finite group whose order is divisible by a prime p contains a Sylow p-subgroup (Artin, Theorem 7.7.2, p. 217). The proof uses the action of G by left multiplication on the set S of all subsets of order p^e. Since the number of such subsets is not divisible by p (Lemma 7.7.10), some orbit has order not divisible by p. The stabilizer of a subset in that orbit has order p^e.

# Prerequisites

- **Sylow p-subgroup** — What the theorem asserts exists
- **Operation on subsets** — The proof uses this action

# Key Properties

1. Guarantees existence of a subgroup of order p^e
2. Corollary: G contains an element of order p (Corollary 7.7.3)
3. This is stronger than Cauchy's theorem
4. Proof is combinatorial, using action on subsets

# Construction / Recognition

## Proof Strategy:
1. G acts by left multiplication on subsets of order p^e
2. The number N of such subsets is not divisible by p
3. So some orbit has order not divisible by p
4. The stabilizer of a subset in this orbit has order p^e

# Context & Application

The First Sylow Theorem is the existence theorem. It guarantees that the "largest possible" p-subgroups actually exist. Combined with the other Sylow theorems, it provides the primary tool for classifying groups of small order.

# Examples

**Example 1** (p. 217): Corollary 7.7.3: A group of order 6 must contain elements of orders 2 and 3. The naive hope that G might consist of 1 and five elements of order 2 is impossible.

# Relationships

## Builds Upon
- **Operation on subsets** — Proof mechanism

## Enables
- **Cauchy's theorem** — Immediate corollary
- **Group classification** — Combined with 2nd and 3rd Sylow theorems

## Related
- **Second Sylow theorem** — Conjugacy of Sylow subgroups
- **Third Sylow theorem** — Count of Sylow subgroups

# Source Reference

Chapter 7: More Group Theory, Section 7.7, Theorem 7.7.2, Corollary 7.7.3, Lemmas 7.7.9-7.7.10, pages 217, 220-221.

# Verification Notes

- Definition source: Direct from Theorem 7.7.2
- Confidence rationale: Named theorem, explicitly stated and proved
- Uncertainties: None
- Cross-reference status: Verified
