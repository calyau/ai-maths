---
concept: F-Automorphism
slug: f-automorphism
category: galois-theory
subcategory: core-definitions
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Galois Theory"
chapter_number: 16
pdf_page: 488
section: "16.4 Isomorphisms of Field Extensions"
extraction_confidence: high
aliases:
  - "F-isomorphism"
  - "automorphism of field extension"
prerequisites:
  - field-extension
extends: []
related:
  - galois-group
contrasts_with: []
answers_questions:
  - "What is an F-automorphism?"
  - "How does the Galois group relate to field automorphisms?"
---

# Quick Definition

An F-automorphism of an extension field K is an automorphism of K that fixes every element of the base field F. The F-automorphisms form the Galois group G(K/F).

# Core Definition

An F-isomorphism sigma: K -> K' is an isomorphism whose restriction to the subfield F is the identity map. An F-automorphism of K is an F-isomorphism from K to itself (Artin, p. 492, Definition 15.2.9). F-automorphisms permute roots of polynomials with coefficients in F (Lemma 16.4.2(a)), and are determined by their action on generators (16.4.2(b)).

# Prerequisites

- **Field extension** -- F-automorphisms act on extension fields

# Key Properties

1. An F-automorphism sends any root of f(x) in F[x] to another root of f(x) (16.4.2(a))
2. An F-automorphism is determined by its action on generators of K (16.4.2(b))
3. If alpha and beta are roots of the same irreducible f in F[x], there is a unique F-isomorphism F(alpha) -> F(beta) sending alpha to beta (16.4.2(c))
4. The F-automorphisms of K form the Galois group G(K/F)

# Context & Application

F-automorphisms are the symmetries of a field extension. They form the Galois group, which is the central object of Galois theory.

# Examples

**Example 1** (p. 492): Complex conjugation is the unique nontrivial R-automorphism of C.

**Example 2** (p. 492): The map a + b*sqrt(2) -> a - b*sqrt(2) is the nontrivial Q-automorphism of Q(sqrt(2)).

# Relationships

## Builds Upon
- **Field extension** -- F-automorphisms act on extensions

## Enables
- **Galois group** -- The set of F-automorphisms

# Source Reference

Chapter 16: Galois Theory, Section 16.4, pages 492-494. Definition 15.2.9, Lemma 16.4.2.

# Verification Notes

- Definition source: Direct from Artin, p. 492 and Definition 15.2.9
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
