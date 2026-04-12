---
concept: Kernel
slug: kernel
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
  - "ker"
prerequisites:
  - homomorphism
extends: []
related:
  - normal-subgroup
  - image
  - first-isomorphism-theorem
  - coset
contrasts_with:
  - image
answers_questions:
  - "What is a homomorphism?"
  - "How does the kernel of a homomorphism relate to normal subgroups?"
---

# Quick Definition

The kernel of a homomorphism phi: G -> G' is the set of elements mapped to the identity: ker(phi) = {a in G : phi(a) = 1}. It is always a normal subgroup of G.

# Core Definition

The kernel of phi, often denoted ker(phi), is the set of elements of G that are mapped to the identity in G': ker(phi) = {a in G : phi(a) = 1} (Artin, p. 62, formula 2.5.5). The kernel is a normal subgroup of G (Proposition 2.5.11). Two elements a, b have the same image iff a^(-1)b is in ker(phi), iff b is in the coset a*ker(phi) (Proposition 2.5.8).

# Prerequisites

- **Homomorphism** — The kernel is defined for a homomorphism

# Key Properties

1. ker(phi) is a subgroup of G
2. ker(phi) is a normal subgroup (Proposition 2.5.11)
3. phi is injective iff ker(phi) = {1} (Corollary 2.5.9)
4. phi(a) = phi(b) iff b is in a*ker(phi)
5. The cosets of ker(phi) are the fibres of phi

# Construction / Recognition

## To Construct:
1. Find all elements a in G with phi(a) = 1

## To Recognize:
1. The set of elements mapping to the identity

# Context & Application

The kernel controls the entire homomorphism: it determines which elements have the same image, and the quotient G/ker(phi) is isomorphic to the image (First Isomorphism Theorem). Every normal subgroup is the kernel of some homomorphism.

# Examples

**Example 1** (p. 62): ker(det: GL_n -> R*) = SL_n (matrices with determinant 1).

**Example 2** (p. 62): ker(sign: S_n -> {+/-1}) = A_n (the alternating group of even permutations).

# Relationships

## Builds Upon
- **Homomorphism** — Kernel is a property of a homomorphism

## Enables
- **Normal subgroup** — Every kernel is normal
- **Quotient group** — G/ker(phi) is the quotient
- **First isomorphism theorem** — G/ker(phi) ≅ im(phi)

## Contrasts With
- **Image** — The image records where elements go; the kernel records what collapses to 1

# Common Errors

- **Error**: Assuming the kernel is always trivial
  **Correction**: The kernel is trivial only when phi is injective

# Common Confusions

- **Confusion**: Confusing kernel of a group homomorphism with null space of a linear map
  **Clarification**: They are analogous concepts; the null space is the kernel of a linear transformation

# Source Reference

Chapter 2: Groups, Section 2.5, pages 62-63.

# Verification Notes

- Definition source: Direct from (2.5.5), p. 62
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
