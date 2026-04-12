---
concept: Correspondence Theorem
slug: correspondence-theorem
category: group-theory
subcategory: null
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Groups"
chapter_number: 2
pdf_page: 48
section: "2.10 The Correspondence Theorem"
extraction_confidence: high
aliases:
  - "lattice isomorphism theorem"
prerequisites:
  - homomorphism
  - kernel
  - subgroup
extends: []
related:
  - first-isomorphism-theorem
  - quotient-group
contrasts_with: []
answers_questions:
  - "What is a homomorphism?"
---

# Quick Definition

The Correspondence Theorem states that for a surjective homomorphism phi: G -> G' with kernel K, there is a bijection between subgroups of G containing K and subgroups of G'. Normal subgroups correspond to normal subgroups.

# Core Definition

Theorem 2.10.5: Let phi: G -> G' be a surjective homomorphism with kernel K. There is a bijective correspondence between subgroups of G containing K and subgroups of G': H <-> phi(H) and H' <-> phi^(-1)(H'). A subgroup H is normal in G iff phi(H) is normal in G'. If H and H' correspond, |H| = |H'| * |K| (Artin, pp. 76-77).

# Prerequisites

- **Homomorphism** — phi must be a surjective homomorphism
- **Kernel** — K = ker(phi); only subgroups containing K participate
- **Subgroup** — The theorem relates subgroups of G and G'

# Key Properties

1. Bijection: subgroups of G containing K <-> subgroups of G'
2. H -> phi(H) and H' -> phi^(-1)(H')
3. Normal subgroups correspond to normal subgroups
4. |H| = |phi(H)| * |K|

# Construction / Recognition

## To Construct:
1. Given a surjective phi: G -> G' with kernel K
2. Map subgroups of G containing K to their images in G'

## To Recognize:
1. Any bijection between subgroup lattices induced by a homomorphism

# Context & Application

The Correspondence Theorem makes the subgroup structure of a quotient group visible within the original group. It is used extensively to analyze group structure.

# Examples

**Example 1** (pp. 77-78): The homomorphism phi: S_4 -> S_3 has kernel K of order 4. S_3 has 4 proper subgroups, giving 4 proper subgroups of S_4 containing K: one of order 12 (A_4) and three of order 8.

# Relationships

## Builds Upon
- **Homomorphism** — Based on a surjective homomorphism

## Related
- **First isomorphism theorem** — Complementary result about quotients
- **Quotient group** — Subgroups of G/K correspond to subgroups of G containing K

# Common Errors

- **Error**: Applying the theorem to non-surjective homomorphisms
  **Correction**: The correspondence is with subgroups of the IMAGE, not the full codomain

# Common Confusions

- **Confusion**: Thinking ALL subgroups of G participate
  **Clarification**: Only subgroups containing K are in the correspondence

# Source Reference

Chapter 2: Groups, Section 2.10, pages 76-78.

# Verification Notes

- Definition source: Direct from Theorem 2.10.5
- Confidence rationale: Named theorem with proof and example
- Uncertainties: None
- Cross-reference status: Verified
