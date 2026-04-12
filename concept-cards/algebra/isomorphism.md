---
concept: Isomorphism
slug: isomorphism
category: group-theory
subcategory: null
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Groups"
chapter_number: 2
pdf_page: 48
section: "2.6 Isomorphisms"
extraction_confidence: high
aliases:
  - "group isomorphism"
  - "≅"
prerequisites:
  - homomorphism
extends:
  - homomorphism
related:
  - automorphism
  - conjugation
contrasts_with:
  - homomorphism
answers_questions:
  - "What is an isomorphism?"
  - "What distinguishes a homomorphism from an isomorphism?"
---

# Quick Definition

An isomorphism phi: G -> G' is a bijective homomorphism. Two groups are isomorphic (G ≅ G') if there exists an isomorphism between them; they then have identical group-theoretic properties.

# Core Definition

An isomorphism phi: G -> G' is a bijective group homomorphism — a bijective map such that phi(ab) = phi(a)phi(b) (Artin, p. 65). The inverse map phi^(-1): G' -> G is also an isomorphism (Lemma 2.6.2). Two groups are isomorphic if there exists an isomorphism between them.

# Prerequisites

- **Homomorphism** — An isomorphism is a special homomorphism

# Key Properties

1. Bijective (injective and surjective)
2. The inverse is also an isomorphism
3. Isomorphic groups have identical group-theoretic properties
4. A homomorphism is an isomorphism iff ker = {1} and im = G'
5. An isomorphism from G to itself is called an automorphism

# Construction / Recognition

## To Construct:
1. Define a homomorphism phi: G -> G'
2. Verify it is bijective (or: verify ker = {1} and im = G')

## To Recognize:
1. A bijective map preserving the group operation

# Context & Application

Isomorphisms identify groups that are "the same" algebraically. Classifying groups means describing the isomorphism classes. An automorphism (isomorphism from G to itself) reveals internal symmetry; conjugation by g is the most important type.

# Examples

**Example 1** (p. 65): exp: R+ -> R*_+ (positive reals under multiplication) is an isomorphism.

**Example 2** (p. 65): S_n is isomorphic to the group of n x n permutation matrices.

**Example 3** (p. 66): Conjugation by g: x -> gxg^(-1) is an automorphism of G.

# Relationships

## Builds Upon
- **Homomorphism** — An isomorphism is a bijective homomorphism

## Enables
- **Automorphism** — An isomorphism from G to itself
- **Isomorphism class** — Groups isomorphic to each other

## Contrasts With
- **Homomorphism** — Need not be bijective

# Common Errors

- **Error**: Assuming two groups of the same order are isomorphic
  **Correction**: There can be multiple non-isomorphic groups of the same order

# Common Confusions

- **Confusion**: Thinking isomorphic groups are "the same group"
  **Clarification**: They are different sets with the same algebraic structure

# Source Reference

Chapter 2: Groups, Section 2.6, pages 65-68.

# Verification Notes

- Definition source: Direct from Section 2.6, p. 65
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
