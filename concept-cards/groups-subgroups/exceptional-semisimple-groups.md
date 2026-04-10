---
concept: Exceptional Semisimple Groups
slug: exceptional-semisimple-groups
category: classical-groups
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 232
section: "20 The exceptional semisimple groups"
extraction_confidence: medium
aliases: []
prerequisites:
  - semisimple-algebraic-group
extends: []
related:
  - classical-semisimple-groups
contrasts_with:
  - classical-semisimple-groups
answers_questions:
  - "What is a semisimple algebraic group?"
---

# Quick Definition

The exceptional semisimple groups are the almost-simple algebraic groups of types G_2, F_4, E_6, E_7, and E_8, which do not belong to the four infinite classical families. The group G_2 is the automorphism group of an octonion algebra.

# Core Definition

Over an algebraically closed field, beyond the four infinite families of classical groups (types A, B, C, D), there are five **exceptional** types: F_4, E_6, E_7, E_8, and G_2 (Milne, p. 232). The group of type G_2 over a field k of characteristic zero is the automorphism group of a Hurwitz (octonion/Cayley) algebra of dimension 8 over k (p. 232).

# Prerequisites

- **Semisimple algebraic group** -- Exceptional groups are semisimple

# Key Properties

1. There are exactly five exceptional types
2. G_2 arises as the automorphism group of an octonion algebra
3. A Hurwitz algebra is a finite k-algebra A with a nondegenerate multiplicative quadratic form N(xy) = N(x)N(y)
4. Possible dimensions of Hurwitz algebras: 1, 2, 4, and 8

# Context & Application

The exceptional groups complete the classification of almost-simple algebraic groups. While each can be constructed explicitly (from their Lie algebras in characteristic zero, or from root systems in all characteristics), uniform proofs involving root systems are generally preferred over case-by-case arguments.

# Examples

**Example 1** (p. 232): For an octonion algebra A over k, the functor R -> Aut_k(R tensor_k A) is an algebraic group of type G_2.

# Relationships

## Builds Upon
- **Semisimple algebraic group** -- Exceptional groups are semisimple

## Contrasts With
- **Classical semisimple groups** -- Classical types A, B, C, D form infinite families; exceptional types are isolated

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 20, pages 232-233.

# Verification Notes

- Definition source: Synthesized from p. 232
- Confidence rationale: Medium -- the section is incomplete/survey-like
- Uncertainties: Section is acknowledged as incomplete by the author
- Cross-reference status: Verified
