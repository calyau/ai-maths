---
concept: Conjugation in the Symmetric Group
slug: conjugation-in-symmetric-group
category: group-theory
subcategory: conjugation
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "More Group Theory"
chapter_number: 7
pdf_page: 206
section: "7.5 Conjugation in the Symmetric Group"
extraction_confidence: high
aliases: []
prerequisites:
  - conjugacy-class
  - conjugation
extends:
  - conjugation
related:
  - alternating-group-simplicity
contrasts_with: []
answers_questions:
  - "When are two permutations conjugate in S_n?"
---

# Quick Definition

Two permutations in S_n are conjugate if and only if they have the same cycle type. Conjugation by q relabels indices: if p = (134)(25), then qpq^{-1} has the same cycle structure with relabeled entries.

# Core Definition

Two permutations p and p' are conjugate elements of the symmetric group if and only if their cycle decompositions have the same orders (Artin, Proposition 7.5.1, p. 213). Conjugation by q acts as relabeling: if phi is the relabeling map, the conjugate is phi * p * phi^{-1}.

# Prerequisites

- **Conjugacy class** — Conjugation in S_n is the key example
- **Conjugation** — The general concept

# Key Properties

1. Conjugacy class = set of permutations with same cycle type
2. Conjugation by q relabels indices according to q
3. The number of conjugacy classes equals the number of partitions of n
4. The class equation of S_4: 24 = 1 + 3 + 6 + 6 + 8

# Examples

**Example 1** (p. 213): p = (134)(25) conjugated by q = (1452) gives qpq^{-1} = (435)(12). Same cycle structure: one 3-cycle and one 2-cycle.

**Example 2** (p. 214): S_4 class equation 24 = 1 + 3 + 6 + 6 + 8, corresponding to partitions 1111, 22, 211, 4, 31.

**Example 3** (p. 214): S_5 class equation 120 = 1 + 10 + 15 + 20 + 20 + 30 + 24.

# Relationships

## Builds Upon
- **Conjugation** — Specialized to S_n

## Enables
- **Alternating group simplicity** — Uses conjugacy of 3-cycles in A_n

# Source Reference

Chapter 7: More Group Theory, Section 7.5, Proposition 7.5.1, pages 212-214.

# Verification Notes

- Definition source: Direct from Proposition 7.5.1
- Confidence rationale: Explicitly stated and applied
- Uncertainties: None
- Cross-reference status: Verified
