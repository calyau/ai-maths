---
concept: Symmetric Group
slug: symmetric-group
category: group-theory
subcategory: null
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Groups"
chapter_number: 2
pdf_page: 48
section: "2.2 Groups and Subgroups"
extraction_confidence: high
aliases:
  - "S_n"
prerequisites:
  - group
  - permutation
extends:
  - group
related:
  - alternating-group
  - transposition
  - general-linear-group
contrasts_with: []
answers_questions:
  - "What is a group?"
---

# Quick Definition

The symmetric group S_n is the group of all permutations of {1, 2, ..., n} under composition. It has order n! and is non-abelian for n >= 3.

# Core Definition

The group of permutations of the set {1, 2, ..., n} is the symmetric group S_n (Artin, p. 53, formula 2.2.5). It has n! elements. S_3 has generators x = (123) and y = (12) with relations x^3 = 1, y^2 = 1, yx = x^2y (formula 2.2.6).

# Prerequisites

- **Group** — S_n is a group under composition
- **Permutation** — Elements are permutations

# Key Properties

1. |S_n| = n!
2. Non-abelian for n >= 3
3. Every finite group is isomorphic to a subgroup of some S_n (Cayley's theorem)
4. The alternating group A_n (even permutations) is a normal subgroup of index 2

# Construction / Recognition

## To Construct:
1. List all bijections from {1,...,n} to itself
2. Composition is the group operation

## To Recognize:
1. A group of order n! whose elements are permutations of n objects

# Context & Application

S_n is one of the most important groups in algebra. It provides concrete non-abelian examples, appears in the theory of determinants, and is central to Galois theory (Chapters 15-16).

# Examples

**Example 1** (p. 53): S_3 = {1, x, x^2, y, xy, x^2y} with x = (123), y = (12).

**Example 2** (p. 53): S_2 = {1, (12)} is the unique group of order 2.

# Relationships

## Builds Upon
- **Group** — S_n is a group
- **Permutation** — Elements of S_n

## Enables
- **Alternating group** — A_n = ker(sign) is a subgroup of S_n
- **Determinant** — Complete expansion uses permutations from S_n

## Related
- **General linear group** — Another family of important groups

# Common Errors

- **Error**: Thinking S_n is abelian
  **Correction**: S_n is non-abelian for n >= 3

# Common Confusions

- **Confusion**: Confusing symmetric group with the concept of symmetry
  **Clarification**: The symmetric group is the group of ALL permutations, not just geometric symmetries

# Source Reference

Chapter 2: Groups, Section 2.2, pages 53-54.

# Verification Notes

- Definition source: Direct from (2.2.5), p. 53
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
