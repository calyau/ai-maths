---
concept: Centralizer
slug: centralizer
category: group-theory
subcategory: conjugation
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "More Group Theory"
chapter_number: 7
pdf_page: 206
section: "7.2 The Class Equation"
extraction_confidence: high
aliases:
  - "Z(x)"
prerequisites:
  - group-action
  - stabilizer
  - conjugacy-class
extends:
  - stabilizer
related:
  - center-of-group
  - class-equation
contrasts_with:
  - normalizer
answers_questions:
  - "What is the centralizer of an element?"
  - "How do centralizers relate to conjugacy classes?"
---

# Quick Definition

The centralizer Z(x) of an element x is the set of all elements that commute with x: Z(x) = {g in G | gx = xg}. It is the stabilizer of x under conjugation, and |G| = |Z(x)| * |C(x)|.

# Core Definition

The stabilizer of an element x for the operation of conjugation is called the centralizer of x, denoted Z(x): Z(x) = {g in G | gxg^{-1} = x} = {g in G | gx = xg} (Artin, (7.2.2), p. 207).

# Prerequisites

- **Group action** — Conjugation is a group action
- **Stabilizer** — The centralizer is the stabilizer for conjugation
- **Conjugacy class** — Z(x) determines |C(x)|

# Key Properties

1. Z(x) = {g in G | gx = xg} (elements commuting with x)
2. Z(x) is a subgroup of G containing x and the center Z
3. Z(x) = G iff x is in the center Z
4. |G| = |Z(x)| * |C(x)|
5. C(x) = {x} iff Z(x) = G

# Construction / Recognition

## To Compute:
1. Find all elements g that commute with x: solve gx = xg
2. These form the centralizer Z(x)

# Context & Application

Computing centralizers is often easier than directly computing conjugacy classes, since the centralizer has subgroup structure. The centralizer size determines the conjugacy class size via |C(x)| = |G|/|Z(x)|.

# Examples

**Example 1** (p. 208): In S_3, Z(x) = <x> has order 3, so |C(x)| = 6/3 = 2.

**Example 2** (p. 208): In SL_2(F_3), for A = [[0,-1],[1,0]], solving PA = AP gives |Z(A)| = 4, so |C(A)| = 24/4 = 6.

# Relationships

## Builds Upon
- **Stabilizer** — Centralizer is the stabilizer for conjugation

## Enables
- **Class equation** — Via |C(x)| = [G : Z(x)]

## Related
- **Center of a group** — Z = intersection of all centralizers

## Contrasts With
- **Normalizer** — Normalizer stabilizes a subgroup; centralizer stabilizes an element

# Source Reference

Chapter 7: More Group Theory, Section 7.2, (7.2.2), pages 207-208.

# Verification Notes

- Definition source: Direct from (7.2.2)
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
