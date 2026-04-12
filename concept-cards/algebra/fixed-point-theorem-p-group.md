---
concept: Fixed Point Theorem for p-Groups
slug: fixed-point-theorem-p-group
category: group-theory
subcategory: p-groups
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "More Group Theory"
chapter_number: 7
pdf_page: 206
section: "7.3 p-Groups"
extraction_confidence: high
aliases: []
prerequisites:
  - p-group
  - counting-formula
extends: []
related:
  - second-sylow-theorem
contrasts_with: []
answers_questions:
  - "When does a p-group action have a fixed point?"
---

# Quick Definition

If a p-group G acts on a finite set S whose order is not divisible by p, then there is a fixed point -- an element s with gs = s for all g in G.

# Core Definition

Let G be a p-group, and let S be a finite set on which G operates. If the order of S is not divisible by p, there is a fixed point for the operation of G on S (Artin, Theorem 7.3.2, p. 209).

# Prerequisites

- **p-group** — The acting group must be a p-group
- **Counting formula** — Proof uses orbit decomposition

# Key Properties

1. Every orbit size divides |G| = p^e, so is a power of p
2. |S| = sum of orbit sizes; orbits of size 1 are fixed points
3. If p does not divide |S|, then the number of fixed points is not divisible by p, hence nonzero

# Context & Application

This theorem is a key tool in the proof of the second Sylow theorem. There, a p-subgroup K acts on the cosets of a Sylow p-subgroup H, and the fixed point theorem guarantees that K is contained in a conjugate of H.

# Examples

**Example 1** (p. 209): A group of order p^2 acting on a set of 3 elements (p > 3) must have a fixed point.

# Relationships

## Builds Upon
- **p-group** — Applies specifically to p-groups

## Enables
- **Second Sylow theorem** — Uses fixed points to show p-subgroups are contained in Sylow subgroups

# Source Reference

Chapter 7: More Group Theory, Section 7.3, Theorem 7.3.2, p. 209.

# Verification Notes

- Definition source: Direct from Theorem 7.3.2
- Confidence rationale: Explicitly stated theorem
- Uncertainties: None
- Cross-reference status: Verified
