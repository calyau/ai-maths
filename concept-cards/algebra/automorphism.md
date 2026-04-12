---
concept: Automorphism
slug: automorphism
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
  - "inner automorphism"
prerequisites:
  - isomorphism
extends:
  - isomorphism
related:
  - conjugate
contrasts_with: []
answers_questions:
  - "What is an isomorphism?"
---

# Quick Definition

An automorphism of a group G is an isomorphism from G to itself. The most important type is conjugation by g: x -> gxg^(-1), which is an inner automorphism.

# Core Definition

An isomorphism phi: G -> G from a group G to itself is called an automorphism (Artin, p. 66). Conjugation by a fixed element g, defined by phi(x) = gxg^(-1), is an automorphism because it is a homomorphism (phi(xy) = phi(x)phi(y)) and bijective (inverse is conjugation by g^(-1)).

# Prerequisites

- **Isomorphism** — An automorphism is an isomorphism G -> G

# Key Properties

1. Bijective homomorphism from G to itself
2. The set of automorphisms forms a group Aut(G)
3. Conjugation by g is always an automorphism (inner automorphism)
4. In abelian groups, conjugation is the identity

# Construction / Recognition

## To Construct:
1. Choose g in G; conjugation by g gives an inner automorphism

## To Recognize:
1. A bijective homomorphism from G to itself

# Context & Application

Automorphisms reveal internal symmetries of a group. Inner automorphisms (conjugation) are the most common type and play a key role in defining normal subgroups.

# Examples

**Example 1** (p. 67): In S_3, conjugation by y interchanges x and x^2.

# Relationships

## Builds Upon
- **Isomorphism** — Special case with G = G'

## Related
- **Conjugate** — Inner automorphisms are given by conjugation

# Common Errors

- **Error**: Assuming all automorphisms are inner
  **Correction**: Outer automorphisms (not given by conjugation) can exist

# Common Confusions

- **Confusion**: Confusing automorphism with endomorphism
  **Clarification**: An automorphism must be bijective; an endomorphism is just a homomorphism G -> G

# Source Reference

Chapter 2: Groups, Section 2.6, pages 66-67.

# Verification Notes

- Definition source: Direct from p. 66
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
