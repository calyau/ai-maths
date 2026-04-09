---
# === CORE IDENTIFICATION ===
concept: Composition Series Examples
slug: composition-series-examples

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - composition-series
  - composition-factors
extends: []
related:
  - jordan-holder-theorem
  - solvable-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What do composition series look like for familiar groups?"
---

# Quick Definition

Key examples of composition series from the text: S_3 (factors C_2, C_3), S_4 (factors C_2, C_3, C_2, C_2), cyclic groups (factors are cyclic of prime order corresponding to prime factorization), and S_n for n >= 5 (unique series S_n > A_n > 1).

# Core Definition

**Example 6.1.**
(a) S_3 > A_3 > 1 with quotients C_2, C_3.
(b) S_4 > A_4 > V > <(13)(24)> > 1 with quotients C_2, C_3, C_2, C_2 (V is the Klein four-group).
(c) Any maximal flag in F_p^n gives a composition series of length n with all quotients C_p.
(d) C_m: for any factorization m = p_1 ... p_r, there is a composition series with quotients C_{p_1}, ..., C_{p_r}. The Jordan-Holder theorem recovers unique factorization.
(e) Direct product of simple groups H_1 x ... x H_r has composition factors H_1, ..., H_r (in any order).
(f) For n >= 5, S_n > A_n > {1} is the *only* composition series (since A_n is simple and the only nontrivial normal subgroup of S_n).

(Milne, Example 6.1, pp. 87-88)

# Prerequisites

- **composition-series** -- the concept being illustrated

# Key Properties

1. S_3 and S_4 are solvable (all composition factors are cyclic of prime order)
2. S_n for n >= 5 has A_n as a composition factor, which is simple nonabelian, so S_n is not solvable
3. The cyclic group example shows that composition factors = prime factorization of |G|
4. The uniqueness of the series for S_n (n >= 5) is exceptional -- most groups have many composition series

# Relationships

## Builds Upon
- **composition-series** -- the concept

## Related
- **jordan-holder-theorem** -- guarantees same factors regardless of series chosen
- **solvable-group** -- solvable iff all factors cyclic of prime order

# Source Reference

Chapter 6, Example 6.1, pp. 87-88.

# Verification Notes

- Definition source: Direct from Example 6.1
- Confidence rationale: HIGH -- explicit examples
- Uncertainties: None
