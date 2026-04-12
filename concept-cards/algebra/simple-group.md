---
concept: Simple Group
slug: simple-group
category: group-theory
subcategory: structure-theorems
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "More Group Theory"
chapter_number: 7
pdf_page: 206
section: "7.4 The Class Equation of the Icosahedral Group"
extraction_confidence: high
aliases: []
prerequisites:
  - conjugacy-class
  - class-equation
extends: []
related:
  - alternating-group-simplicity
  - icosahedral-group
  - normal-subgroup
contrasts_with:
  - normal-subgroup
answers_questions:
  - "What is a simple group?"
  - "What distinguishes a normal subgroup from a general subgroup?"
---

# Quick Definition

A group G is simple if it is nontrivial and contains no proper normal subgroup (no normal subgroup other than {1} and G). Cyclic groups of prime order are simple; the smallest non-abelian simple group is A_5 (= I).

# Core Definition

A group G is simple if it is not the trivial group and if it contains no proper normal subgroup -- no normal subgroup other than <1> and G (Artin, p. 210). A normal subgroup N of G must be a union of conjugacy classes (Lemma 7.4.2), so simplicity can be tested by checking whether any proper subset of conjugacy classes (including {1}) sums to a divisor of |G|.

# Prerequisites

- **Conjugacy class** — Normal subgroups are unions of classes
- **Class equation** — Tool for proving simplicity

# Key Properties

1. No proper normal subgroups
2. Any homomorphism from a simple group is either injective or trivial
3. Cyclic groups of prime order are simple
4. A_5 = I (order 60) is the smallest non-abelian simple group
5. A_n is simple for n >= 5 (Theorem 7.5.4)

# Construction / Recognition

## To Test Simplicity:
1. Compute the class equation
2. Check if any union of conjugacy classes (including {1}) has order dividing |G|
3. If no such proper nontrivial union exists, the group is simple

# Context & Application

Simple groups are the "atoms" of group theory -- every finite group can be built from simple groups via extensions. The classification of finite simple groups is one of the greatest achievements of 20th century mathematics.

# Examples

**Example 1** (p. 210): The icosahedral group I has class equation 60 = 1 + 20 + 12 + 12 + 15. No proper subset including 1 sums to a divisor of 60, so I is simple.

**Example 2** (p. 211): I = A_5, so A_5 is simple. The proof uses the 5 cubes inscribed in a dodecahedron.

# Relationships

## Builds Upon
- **Conjugacy class** — Normal subgroups are unions of classes
- **Class equation** — Tool for proving simplicity

## Related
- **Alternating group simplicity** — A_n is simple for n >= 5
- **Composition series** — Built from simple groups

## Contrasts With
- **Normal subgroup** — Simple groups have none (proper)

# Common Confusions

- **Confusion**: Thinking "simple" means "easy" or "small"
  **Clarification**: "Simple" means "not compound" -- having no proper normal subgroups. Simple groups can be very large and complex.

# Source Reference

Chapter 7: More Group Theory, Section 7.4, Theorem 7.4.3, pages 210-211.

# Verification Notes

- Definition source: Direct from p. 210
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
