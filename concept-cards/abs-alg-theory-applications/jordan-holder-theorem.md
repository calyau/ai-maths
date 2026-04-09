---
concept: Jordan-Holder Theorem
slug: jordan-holder-theorem
category: group-structure
subcategory: classification-theorems
tier: advanced
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "The Structure of Groups"
chapter_number: 13
pdf_page: 177
section: "Solvable Groups"
extraction_confidence: high
aliases:
  - "Jordan-Holder theorem"
prerequisites:
  - composition-series
  - second-isomorphism-theorem
extends: []
related:
  - simple-group
  - solvable-group
contrasts_with: []
answers_questions:
  - "Are composition series unique?"
  - "What does the Jordan-Holder theorem say?"
---

# Quick Definition

The Jordan-Holder Theorem states that any two composition series of a group $G$ are isomorphic, meaning they have the same length and the same composition factors (up to permutation and isomorphism).

# Core Definition

**Theorem 13.18 (Jordan-Holder)**: "Any two composition series of $G$ are isomorphic" (Judson, p. 177). The proof uses induction on the length of the composition series and the Second Isomorphism Theorem.

# Prerequisites

- **Composition series** — The objects being compared
- **Second isomorphism theorem** — Used in the proof

# Key Properties

1. The composition factors are unique up to permutation and isomorphism
2. The length of a composition series is an invariant of the group
3. This justifies viewing composition factors as the "building blocks" of the group

# Examples

**Example 1** (p. 176): The two composition series of $\mathbb{Z}_{60}$:
- $\mathbb{Z}_{60} \supset \langle 3 \rangle \supset \langle 15 \rangle \supset \langle 30 \rangle \supset \{0\}$ (factors: $\mathbb{Z}_3, \mathbb{Z}_5, \mathbb{Z}_2, \mathbb{Z}_2$)
- $\mathbb{Z}_{60} \supset \langle 2 \rangle \supset \langle 4 \rangle \supset \langle 20 \rangle \supset \{0\}$ (factors: $\mathbb{Z}_2, \mathbb{Z}_2, \mathbb{Z}_5, \mathbb{Z}_3$)

Both have the same factors $\{\mathbb{Z}_2, \mathbb{Z}_2, \mathbb{Z}_3, \mathbb{Z}_5\}$.

# Relationships

## Builds Upon
- **Composition series** — The theorem is about composition series

## Enables
- **Classification via composition factors** — Composition factors are group invariants

# Source Reference

Chapter 13: The Structure of Groups, Section 13.2, p. 177-178. Theorem 13.18.

# Verification Notes

- Definition source: Theorem 13.18
- Confidence: HIGH — major theorem with complete proof
