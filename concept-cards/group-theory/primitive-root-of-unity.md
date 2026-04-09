---
# === CORE IDENTIFICATION ===
concept: Primitive Root of Unity
slug: primitive-root-of-unity

# === CLASSIFICATION ===
category: representation-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Representations of Finite Groups"
chapter_number: 7
pdf_page: 101
section: "Roots of 1 in fields"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - roots-of-unity-in-fields
extends:
  - roots-of-unity-in-fields
related:
  - matrix-representation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a primitive nth root of unity?"
  - "When does a field contain a primitive nth root of unity?"
---

# Quick Definition

An element zeta in F^x of order n is called a primitive nth root of 1. It generates the cyclic group mu_n(F) of order n.

# Core Definition

An element of order n in F^x is called a **primitive nth root of 1**. To say that F contains a primitive nth root zeta of 1 means that mu_n(F) is a cyclic group of order n and that zeta generates it. This implies that either F has characteristic 0 or characteristic a prime not dividing n. (Milne, Chapter 7, p. 101)

# Prerequisites

- **Roots of unity in fields** — primitive roots are generators of mu_n(F)

# Key Properties

1. zeta is primitive iff it has order exactly n in F^x
2. zeta generates mu_n(F) = {1, zeta, zeta^2, ..., zeta^{n-1}}
3. Existence implies char(F) does not divide n
4. The number of primitive nth roots of unity is phi(n) (Euler's totient)

# Construction / Recognition

1. Find an element zeta in F with zeta^n = 1
2. Verify that zeta^m != 1 for all proper divisors m of n
3. Equivalently, verify that zeta has order exactly n in F^x

# Context & Application

Primitive roots of unity are essential for decomposing representations of cyclic groups. Over a field containing a primitive nth root of 1, every representation of C_n decomposes as a direct sum of eigenspaces (Example 7.3a).

# Examples

**Example 1** (p. 101): zeta = e^{2pi i/n} is a primitive nth root of 1 in C.

**Example 2** (p. 101): If char(F) = p and n = p, there is no primitive pth root of 1 in F since X^p - 1 = (X-1)^p.

# Relationships

## Builds Upon
- **roots-of-unity-in-fields** — primitive roots generate the group of all roots

## Enables
- Decomposition of representations of cyclic and abelian groups (7.3)

## Related
- **matrix-representation** — degree-1 representations of C_n given by primitive roots

## Contrasts With
- Non-primitive roots of unity (elements whose order properly divides n)

# Common Errors

- **Error**: Assuming every field contains primitive nth roots of unity for all n
  **Correction**: Finite fields and fields of positive characteristic may lack them

# Common Confusions

- **Confusion**: Thinking "primitive" means "first" or "basic"
  **Clarification**: "Primitive" means "of maximal order n" among nth roots of unity, i.e., a generator of the cyclic group mu_n(F)

# Source Reference

Chapter 7: Representations of Finite Groups, p. 101.

# Verification Notes

- Definition source: Direct from p. 101
- Confidence rationale: HIGH — explicit definition
- Uncertainties: None
