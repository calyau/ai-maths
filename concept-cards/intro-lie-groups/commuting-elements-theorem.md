---
# === CORE IDENTIFICATION ===
concept: Commuting Elements Theorem
slug: commuting-elements-theorem

# === CLASSIFICATION ===
category: lie-algebras
subcategory: exponential-map
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups and Lie Algebras"
chapter_number: 3
pdf_page: 29
section: "3.7"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Theorem 3.33"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - exponential-map
  - commutator-bracket
extends: []
related:
  - campbell-hausdorff-formula
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I use the exponential map to go between Lie group and Lie algebra?"
---

# Quick Definition

If $[x, y] = 0$ in the Lie algebra, then $\exp(x)\exp(y) = \exp(x + y) = \exp(y)\exp(x)$ in the Lie group.

# Core Definition

**Theorem 3.33** (Kirillov): Let $x, y \in \mathfrak{g}$ be such that $[x, y] = 0$. Then $\exp(x)\exp(y) = \exp(x+y) = \exp(y)\exp(x)$.

# Prerequisites

- **Exponential map** — the map relating algebra and group
- **Commutator bracket** — the condition $[x, y] = 0$

# Key Properties

1. $[x, y] = 0$ implies $\exp(tx)$ and $\exp(sy)$ commute for all $s, t$.
2. The proof uses that $[\xi, \eta] = 0$ for the corresponding right-invariant fields, which implies their flows commute.
3. This is the proper generalization of the matrix identity: if $xy = yx$ then $e^x e^y = e^{x+y}$.

# Construction / Recognition

## To Construct/Create:
Not applicable (a theorem).

## To Identify/Recognize:
1. Whenever two Lie algebra elements commute, their exponentials commute and multiply additively.

# Context & Application

This is the first indication that the Lie bracket completely controls the group law. It is the $[x,y] = 0$ special case of the Campbell-Hausdorff formula.

# Examples

**Example**: In an abelian Lie group, $[x, y] = 0$ for all $x, y$, so $\exp(x)\exp(y) = \exp(x+y)$ always.

# Relationships

## Builds Upon
- **Commutator bracket** — the vanishing condition
- **Exponential map** — applied to commuting elements

## Enables
- **Campbell-Hausdorff formula** — the general version

# Common Errors

- **Error**: Assuming $\exp(x)\exp(y) = \exp(y)\exp(x)$ implies $[x,y] = 0$.
  **Correction**: The converse is also true (by equation 3.3: $\exp(x)\exp(y)\exp(-x)\exp(-y) = \exp([x,y] + \cdots)$), but the argument is more subtle.

# Common Confusions

- **Confusion**: Whether this is trivial.
  **Clarification**: For matrix groups where $[x,y] = xy - yx$, commutativity of $x, y$ as matrices is obvious. For general Lie groups, $xy$ is not defined in $\mathfrak{g}$, so the statement is non-trivial.

# Source Reference

Chapter 3: Lie Groups and Lie Algebras, Section 3.7, Theorem 3.33, page 29.

# Verification Notes

- Definition source: Direct from Theorem 3.33
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
