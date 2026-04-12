---
concept: Coset
slug: coset
category: group-theory
subcategory: null
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Groups"
chapter_number: 2
pdf_page: 48
section: "2.8 Cosets"
extraction_confidence: high
aliases:
  - "left coset"
  - "right coset"
prerequisites:
  - group
  - subgroup
extends: []
related:
  - index
  - lagranges-theorem
  - normal-subgroup
  - quotient-group
contrasts_with: []
answers_questions:
  - "What is a coset?"
  - "How do I find the cosets of a subgroup?"
  - "How do cosets relate to Lagrange's theorem?"
---

# Quick Definition

A left coset of a subgroup H in G is a set aH = {ah : h in H} for some element a in G. The left cosets of H partition G into subsets of equal size, leading to Lagrange's theorem.

# Core Definition

If H is a subgroup of G and a is an element of G, the left coset aH is the set {ah : h in H} (Artin, p. 70, formula 2.8.1). Left cosets partition G (Corollary 2.8.3). All cosets have the same size as H (Lemma 2.8.7). Right cosets Ha = {ha : h in H} are defined analogously (formula 2.8.15). Left and right cosets agree iff H is normal.

# Prerequisites

- **Group** — Cosets live in a group
- **Subgroup** — Cosets are defined relative to a subgroup

# Key Properties

1. Left cosets aH partition G
2. All left cosets have the same number of elements as H
3. aH = bH iff a^(-1)b is in H
4. |G| = |H| * [G:H] (the counting formula)
5. Left and right cosets coincide iff H is normal

# Construction / Recognition

## To Construct:
1. Choose a in G
2. Multiply a by every element of H: aH = {ah : h in H}

## To Recognize:
1. A set of the form aH for some a in G

# Context & Application

Cosets are the foundation for Lagrange's theorem and quotient groups. They partition a group into equal-sized pieces, giving the counting formula |G| = |H|[G:H]. When H is normal, cosets form a group (the quotient group).

# Examples

**Example 1** (p. 71): In S_3 with H = <y> = {1, y}, the three left cosets are H = {1,y}, xH = {x,xy}, x^2H = {x^2, x^2y}.

**Example 2** (p. 72): The right cosets of <y> in S_3 are different from the left cosets: H, Hx = {x, x^2y}, Hx^2 = {x^2, xy}.

# Relationships

## Builds Upon
- **Subgroup** — Cosets are defined relative to a subgroup

## Enables
- **Lagrange's theorem** — |H| divides |G|
- **Index** — The number of cosets [G:H]
- **Quotient group** — When H is normal, cosets form a group

## Related
- **Normal subgroup** — H is normal iff left cosets = right cosets

# Common Errors

- **Error**: Assuming aH is a subgroup
  **Correction**: A coset aH is a subgroup only when a is in H (then aH = H)

# Common Confusions

- **Confusion**: Confusing left and right cosets
  **Clarification**: Left cosets aH and right cosets Ha may differ; they agree iff H is normal

# Source Reference

Chapter 2: Groups, Section 2.8, pages 70-73.

# Verification Notes

- Definition source: Direct from (2.8.1), p. 70
- Confidence rationale: Extensively discussed with examples
- Uncertainties: None
- Cross-reference status: Verified
