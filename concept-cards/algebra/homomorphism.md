---
concept: Homomorphism
slug: homomorphism
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
  - "group homomorphism"
prerequisites:
  - group
extends: []
related:
  - kernel
  - image
  - isomorphism
  - normal-subgroup
contrasts_with:
  - isomorphism
answers_questions:
  - "What is a homomorphism?"
  - "What distinguishes a homomorphism from an isomorphism?"
---

# Quick Definition

A homomorphism phi: G -> G' is a map between groups that preserves the law of composition: phi(ab) = phi(a)phi(b). It maps identity to identity and inverses to inverses.

# Core Definition

A homomorphism phi: G -> G' is a map from G to G' such that phi(ab) = phi(a)phi(b) for all a, b in G (Artin, p. 60, formula 2.5.1). It follows that phi(1) = 1 and phi(a^(-1)) = phi(a)^(-1) (Proposition 2.5.3).

# Prerequisites

- **Group** — A homomorphism maps between groups

# Key Properties

1. phi(ab) = phi(a)phi(b)
2. phi(1_G) = 1_{G'} (maps identity to identity)
3. phi(a^(-1)) = phi(a)^(-1) (maps inverses to inverses)
4. The image im(phi) is a subgroup of G'
5. The kernel ker(phi) is a normal subgroup of G
6. phi is injective iff ker(phi) = {1} (Corollary 2.5.9)

# Construction / Recognition

## To Construct:
1. Define a map phi: G -> G'
2. Verify phi(ab) = phi(a)phi(b) for all a, b

## To Recognize:
1. A map between groups that respects the group operations

# Context & Application

Homomorphisms are the structure-preserving maps between groups. They provide ways to relate different groups, detect substructure (via kernels), and build quotient groups. Every normal subgroup arises as the kernel of some homomorphism.

# Examples

**Example 1** (p. 61): det: GL_n(R) -> R* is a homomorphism (det(AB) = det(A)det(B)).

**Example 2** (p. 61): The sign map sigma: S_n -> {+/-1} is a homomorphism.

**Example 3** (p. 61): The exponential exp: R+ -> R*_+ defined by x -> e^x is a homomorphism (e^(a+b) = e^a * e^b).

# Relationships

## Builds Upon
- **Group** — Maps between groups

## Enables
- **Kernel** — ker(phi) is a normal subgroup
- **Image** — im(phi) is a subgroup
- **First isomorphism theorem** — G/ker(phi) is isomorphic to im(phi)

## Contrasts With
- **Isomorphism** — A bijective homomorphism

# Common Errors

- **Error**: Assuming a homomorphism is injective
  **Correction**: Check the kernel; phi is injective iff ker(phi) = {1}

# Common Confusions

- **Confusion**: Confusing homomorphism with isomorphism
  **Clarification**: An isomorphism is a bijective homomorphism; a homomorphism need not be bijective

# Source Reference

Chapter 2: Groups, Section 2.5, pages 60-63.

# Verification Notes

- Definition source: Direct from (2.5.1), p. 60
- Confidence rationale: Central definition with many examples
- Uncertainties: None
- Cross-reference status: Verified
