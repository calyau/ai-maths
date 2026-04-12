---
concept: Conjugacy Class
slug: conjugacy-class
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
aliases: []
prerequisites:
  - group-action
  - orbit
extends: []
related:
  - centralizer
  - class-equation
  - conjugation
contrasts_with: []
answers_questions:
  - "What is a conjugacy class?"
  - "How do conjugacy classes relate to the class equation?"
---

# Quick Definition

The conjugacy class C(x) of an element x is the set of all conjugates gxg^{-1} as g ranges over G. It is the orbit of x under the conjugation action. The counting formula gives |G| = |Z(x)| * |C(x)|.

# Core Definition

The orbit of x for conjugation is called the conjugacy class of x, denoted C(x). It consists of all conjugates gxg^{-1}: C(x) = {x' in G | x' = gxg^{-1} for some g in G} (Artin, (7.2.3), p. 207). The counting formula gives |G| = |Z(x)| * |C(x)| (7.2.4).

# Prerequisites

- **Group action** — Conjugation is a group action
- **Orbit** — Conjugacy classes are orbits

# Key Properties

1. C(x) = {gxg^{-1} | g in G}
2. |G| = |Z(x)| * |C(x)|
3. Conjugacy classes partition the group
4. x is in the center Z iff C(x) = {x}
5. |C(x)| divides |G|
6. In S_n, conjugacy classes are determined by cycle type (Proposition 7.5.1)

# Construction / Recognition

## To Compute:
1. Conjugate x by each element of G
2. Collect distinct results

## To Determine Size:
1. Compute |Z(x)| (centralizer)
2. |C(x)| = |G| / |Z(x)|

# Context & Application

Conjugacy classes are the most important structural feature of a group beyond its subgroups. The class equation (partitioning G by conjugacy classes) is used to prove that the center of a p-group is nontrivial, that groups of order p^2 are abelian, and to establish simplicity of groups.

# Examples

**Example 1** (p. 208): In S_3, the class equation is 6 = 1 + 2 + 3. The conjugacy classes are {1}, {x, x^2}, {y, xy, x^2y}.

**Example 2** (p. 208): In SL_2(F_3) (order 24), the class equation is 24 = 1 + 1 + 4 + 4 + 4 + 4 + 6.

# Relationships

## Builds Upon
- **Orbit** — Conjugacy classes are orbits under conjugation

## Enables
- **Class equation** — Sum of conjugacy class sizes equals |G|
- **Simple group** — Simplicity tested via conjugacy class sizes

## Related
- **Centralizer** — Stabilizer for conjugation; determines class size

# Common Errors

- **Error**: Assuming elements with the same order are conjugate
  **Correction**: Elements of the same order need not be conjugate (e.g., in abelian groups, every element is its own class)

# Common Confusions

- **Confusion**: Thinking conjugation in S_n preserves the individual numbers permuted
  **Clarification**: Conjugation by q relabels: qpq^{-1} has the same cycle structure but different indices

# Source Reference

Chapter 7: More Group Theory, Section 7.2, (7.2.3)-(7.2.4), pages 207-208.

# Verification Notes

- Definition source: Direct from (7.2.3)
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
