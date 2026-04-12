---
concept: Class Equation
slug: class-equation
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
  - conjugacy-class
  - counting-formula
extends: []
related:
  - center-of-group
  - p-group
  - simple-group
contrasts_with: []
answers_questions:
  - "What is the class equation?"
  - "How do conjugacy classes relate to the class equation?"
---

# Quick Definition

The class equation of a finite group is |G| = |C_1| + |C_2| + ... + |C_k|, where the C_i are the conjugacy classes. Each |C_i| divides |G|, and at least one term equals 1 (the identity).

# Core Definition

Since conjugacy classes partition the group, the class equation of a finite group is |G| = sum over conjugacy classes C of |C| (Artin, (7.2.6)-(7.2.7), p. 208). The numbers on the right side divide |G|, and at least one equals 1 (7.2.8). The terms equal to 1 correspond to elements of the center Z.

# Prerequisites

- **Conjugacy class** — The terms in the equation
- **Counting formula** — Each term |C_i| = [G : Z(x_i)]

# Key Properties

1. |G| = sum of conjugacy class sizes
2. Each class size divides |G|
3. The number of 1's on the right equals |Z| (order of center)
4. Strong restriction on possible class equations

# Construction / Recognition

## To Compute:
1. Find all conjugacy classes (use centralizers)
2. Compute the size of each class
3. Verify they sum to |G|

# Context & Application

The class equation is one of the most powerful tools in finite group theory. It proves: the center of a p-group is nontrivial (Proposition 7.3.1), groups of order p^2 are abelian (Proposition 7.3.3), the icosahedral group is simple (Theorem 7.4.3).

# Examples

**Example 1** (p. 208): S_3: 6 = 1 + 2 + 3.

**Example 2** (p. 208): SL_2(F_3): 24 = 1 + 1 + 4 + 4 + 4 + 4 + 6.

**Example 3** (p. 209): Icosahedral group I: 60 = 1 + 20 + 12 + 12 + 15.

**Example 4** (p. 214): S_4: 24 = 1 + 3 + 6 + 6 + 8.

# Relationships

## Builds Upon
- **Conjugacy class** — Terms in the equation
- **Counting formula** — Determines class sizes

## Enables
- **p-group results** — Center is nontrivial
- **Simplicity proofs** — Normal subgroups are unions of classes
- **Sylow theorems** — Applications use the class equation

# Common Errors

- **Error**: Forgetting that the class equation includes |C| = 1 terms for each central element
  **Correction**: The identity always contributes 1; other central elements also contribute 1

# Source Reference

Chapter 7: More Group Theory, Section 7.2, (7.2.6)-(7.2.8), pages 208-209.

# Verification Notes

- Definition source: Direct from (7.2.6)
- Confidence rationale: Core concept with multiple examples
- Uncertainties: None
- Cross-reference status: Verified
