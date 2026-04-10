---
concept: Tannaka Dual
slug: tannaka-dual
category: tannakian-theory
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 235
section: "21b Neutral tannakian categories"
extraction_confidence: high
aliases:
  - "Tannaka group"
  - "Aut^tensor(omega)"
  - "pi(C, omega)"
prerequisites:
  - neutral-tannakian-category
  - fibre-functor
extends: []
related:
  - tannakian-correspondence
contrasts_with: []
answers_questions:
  - "What is a tannakian category?"
---

# Quick Definition

The Tannaka dual of a neutral tannakian category (C, omega) is the affine group G = Aut^tensor(omega) of tensor automorphisms of the fibre functor. It is the group "recovered" from the category of representations.

# Core Definition

The **Tannaka dual** (or **Tannaka group**) of a neutral tannakian category (C, omega) is the affine group G such that G(R) consists of families (lambda_V)_{V in ob(C)} with lambda_V in End_{R-lin}(omega(V)_R), compatible with tensor products, neutral objects, and all morphisms in C (Milne, Theorem 21.10). It is denoted Aut^tensor(omega) or pi(C, omega) (21.14).

# Prerequisites

- **Neutral tannakian category** -- The Tannaka dual is defined for such categories
- **Fibre functor** -- The dual depends on the choice of fibre functor

# Key Properties

1. omega defines an equivalence C -> Rep(G) (Theorem 21.10)
2. If C = Rep(H) and omega is the forgetful functor, then G = H (Example 21.15)
3. An exact tensor functor F: C -> C' with omega' o F = omega gives a homomorphism G' -> G (21.17)
4. If C is semisimple, then G^0 is reductive (Ch II, 6.17)

# Context & Application

The Tannaka dual provides a way to reconstruct groups from their representation categories. This is used in the theory of motives (where one seeks a "motivic Galois group") and in the Langlands program.

# Examples

**Example 1** (21.15): For C = Rep(H) with the forgetful functor, the Tannaka dual is H.

**Example 2** (21.21): If C is semisimple with End(V) = k for simple V, and G = Aut^tensor(omega), then the centre Z of G satisfies X(Z) = M(C) (the universal tensor grading group).

# Relationships

## Builds Upon
- **Neutral tannakian category** -- The Tannaka dual is defined for (C, omega)

## Related
- **Tannakian correspondence** -- Normal subgroups <-> tannakian subcategories

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 21b, pages 235-236.

# Verification Notes

- Definition source: Direct from 21.14
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
