---
concept: Index Two Subgroup is Normal
slug: index-two-subgroup-is-normal
category: group-structure
subcategory: subgroup-types
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Normal Subgroups and Factor Groups"
chapter_number: 10
pdf_page: 144
section: "Exercises"
extraction_confidence: high
aliases: []
prerequisites:
  - normal-subgroup
  - index-of-a-subgroup
  - coset
extends: []
related:
  - factor-group
contrasts_with: []
answers_questions:
  - "How do I determine if a subgroup is normal?"
  - "When is a subgroup automatically normal?"
---

# Quick Definition

Any subgroup of index 2 is automatically normal in the ambient group. This is because there are only two cosets, and the subgroup itself is one of them, so the left and right cosets must coincide.

# Core Definition

**Exercise 10.4.10**: "Let $H$ be a subgroup of index 2 of a group $G$. Prove that $H$ must be a normal subgroup of $G$. Conclude that $S_n$ is not simple for $n \geq 3$" (Judson, p. 144).

# Prerequisites

- **Normal subgroup** — The conclusion
- **Index of a subgroup** — Index 2 is the hypothesis
- **Coset** — Only two cosets exist

# Key Properties

1. If $[G:H] = 2$, then $H \trianglelefteq G$
2. There are exactly two cosets: $H$ and $gH$ for any $g \notin H$
3. Since $gH$ and $Hg$ are both the unique coset different from $H$, they must be equal
4. Consequence: $S_n$ has $A_n$ as a normal subgroup (index 2) for all $n \geq 2$

# Context & Application

This is one of the most useful quick tests for normality. It immediately shows that $A_n \trianglelefteq S_n$ and that $S_n$ is not simple for $n \geq 3$.

# Examples

**Example 1**: $A_n$ has index 2 in $S_n$, so $A_n \trianglelefteq S_n$.

**Example 2**: The rotation subgroup $R_n$ has index 2 in $D_n$, so $R_n \trianglelefteq D_n$.

# Relationships

## Builds Upon
- **Normal subgroup** — Provides a sufficient condition

## Enables
- **Non-simplicity of $S_n$** — $A_n$ is a proper normal subgroup

# Source Reference

Chapter 10: Normal Subgroups and Factor Groups, Exercise 10.4.10, p. 144.

# Verification Notes

- Definition source: Exercise 10.4.10
- Confidence: HIGH
