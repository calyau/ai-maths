---
concept: Conjugate
slug: conjugate
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
  - "conjugation"
  - "conjugacy"
prerequisites:
  - group
extends: []
related:
  - normal-subgroup
  - isomorphism
contrasts_with: []
answers_questions:
  - "What is a group?"
---

# Quick Definition

The conjugate of an element a by g in a group G is the element gag^(-1). Conjugation by g is an automorphism of G. A subgroup N is normal iff it is closed under conjugation.

# Core Definition

If a and g are elements of a group G, the element gag^(-1) is called the conjugate of a by g (Artin, p. 63). Two elements x and x' are conjugate if x' = gxg^(-1) for some g. Conjugation by g (the map x -> gxg^(-1)) is an automorphism of G.

# Prerequisites

- **Group** — Conjugation requires a group structure

# Key Properties

1. Conjugation by g is an automorphism (bijective homomorphism)
2. Conjugate elements have the same order
3. Conjugacy is an equivalence relation
4. N is normal iff gNg^(-1) = N for all g

# Construction / Recognition

## To Construct:
1. Choose g and a in G; compute gag^(-1)

## To Recognize:
1. An element of the form gag^(-1)

# Context & Application

Conjugation is the key operation connecting elements of a group. It defines normal subgroups, automorphisms, and the conjugacy classes that partition any group. In S_n, conjugate permutations have the same cycle type.

# Examples

**Example 1** (p. 63): In S_3, xyx^(-1) = x^2y (conjugating y by x).

**Example 2** (p. 67): Conjugation by g interchanges x and x^2 when g = y in S_3.

# Relationships

## Builds Upon
- **Group** — Uses group multiplication and inverses

## Enables
- **Normal subgroup** — Closed under conjugation
- **Automorphism** — Conjugation is an inner automorphism

# Common Errors

- **Error**: Computing gag instead of gag^(-1)
  **Correction**: Conjugation always includes the inverse on the right

# Common Confusions

- **Confusion**: Thinking conjugation is trivial in all groups
  **Clarification**: Conjugation is trivial (gag^(-1) = a for all g) only in abelian groups

# Source Reference

Chapter 2: Groups, Section 2.5, page 63.

# Verification Notes

- Definition source: Direct from p. 63
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
