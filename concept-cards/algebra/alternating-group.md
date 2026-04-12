---
concept: Alternating Group
slug: alternating-group
category: group-theory
subcategory: null
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Groups"
chapter_number: 2
pdf_page: 48
section: "2.5 Homomorphisms"
extraction_confidence: high
aliases:
  - "A_n"
prerequisites:
  - symmetric-group
  - sign-of-a-permutation
  - kernel
extends:
  - subgroup
related:
  - normal-subgroup
contrasts_with: []
answers_questions:
  - "What is a group? What is a subgroup?"
---

# Quick Definition

The alternating group A_n is the group of even permutations — those with sign +1. It is the kernel of the sign homomorphism S_n -> {+/-1} and is a normal subgroup of S_n of order n!/2.

# Core Definition

The kernel of the sign homomorphism S_n -> {+/-1} is the alternating group A_n, consisting of the even permutations (Artin, p. 62, formula 2.5.6). It is a normal subgroup of S_n. Since the sign map is surjective with image of order 2, |A_n| = n!/2 (p. 73).

# Prerequisites

- **Symmetric group** — A_n is a subgroup of S_n
- **Sign of a permutation** — A_n consists of even permutations
- **Kernel** — A_n is the kernel of the sign homomorphism

# Key Properties

1. |A_n| = n!/2
2. Normal subgroup of S_n (index 2)
3. Half of all permutations are even, half are odd
4. A_n is simple for n >= 5 (proved in Chapter 7)

# Construction / Recognition

## To Construct:
1. Take all permutations in S_n that are products of an even number of transpositions

## To Recognize:
1. A permutation is in A_n iff its sign is +1

# Context & Application

A_n is the prototypical normal subgroup and plays a key role in Galois theory (the unsolvability of the quintic depends on the simplicity of A_5).

# Examples

**Example 1** (p. 62): A_3 = {1, (123), (132)} — the even permutations of 3 elements, forming a cyclic group of order 3.

# Relationships

## Builds Upon
- **Symmetric group** — A_n is a subgroup of S_n
- **Kernel** — A_n = ker(sign)

## Related
- **Normal subgroup** — A_n is normal in S_n

# Common Errors

- **Error**: Thinking A_n contains all cyclic permutations
  **Correction**: Only even permutations; a k-cycle is even iff k is odd

# Common Confusions

- **Confusion**: Confusing A_n with "alternating" sequences
  **Clarification**: "Alternating" refers to the alternating signs in the determinant formula

# Source Reference

Chapter 2: Groups, Section 2.5, page 62.

# Verification Notes

- Definition source: Direct from (2.5.6), p. 62
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
