---
concept: Second Sylow Theorem
slug: second-sylow-theorem
category: group-structure
subcategory: sylow-theory
tier: advanced
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "The Sylow Theorems"
chapter_number: 15
pdf_page: 197
section: "The Sylow Theorems"
extraction_confidence: high
aliases:
  - "Sylow's second theorem"
  - "conjugacy of Sylow subgroups"
prerequisites:
  - sylow-p-subgroup
  - first-sylow-theorem
  - normalizer
extends: []
related:
  - third-sylow-theorem
contrasts_with: []
answers_questions:
  - "Are all Sylow p-subgroups conjugate?"
  - "How do I use the Sylow theorems to analyze group structure?"
---

# Quick Definition

The Second Sylow Theorem states that all Sylow $p$-subgroups of a finite group are conjugate to each other. Thus, if $P_1$ and $P_2$ are Sylow $p$-subgroups, there exists $g \in G$ with $gP_1 g^{-1} = P_2$.

# Core Definition

**Theorem 15.7 (Second Sylow Theorem)**: "Let $G$ be a finite group and $p$ a prime dividing $|G|$. Then all Sylow $p$-subgroups of $G$ are conjugate. That is, if $P_1$ and $P_2$ are two Sylow $p$-subgroups, there exists a $g \in G$ such that $gP_1 g^{-1} = P_2$" (Judson, p. 197).

# Prerequisites

- **Sylow $p$-subgroup** — The objects being compared
- **First Sylow theorem** — Guarantees existence
- **Normalizer** — Used in the proof

# Key Properties

1. Any two Sylow $p$-subgroups are conjugate
2. A Sylow $p$-subgroup is normal iff it is the unique Sylow $p$-subgroup
3. The number of Sylow $p$-subgroups equals $[G:N(P)]$

# Context & Application

The Second Sylow Theorem is powerful for proving groups are not simple: if there is only one Sylow $p$-subgroup, it must be normal (invariant under conjugation). This provides a common strategy for showing groups of certain orders have normal subgroups.

# Relationships

## Builds Upon
- **First Sylow theorem** — Existence of Sylow subgroups

## Enables
- **Proving normality** — Unique Sylow subgroup implies normal
- **Third Sylow theorem** — Constrains the count further

## Related
- **Conjugation of subgroups** — Sylow subgroups form a single conjugacy class

# Source Reference

Chapter 15: The Sylow Theorems, Section 15.1, p. 197. Theorem 15.7.

# Verification Notes

- Definition source: Theorem 15.7
- Confidence: HIGH — major theorem with complete proof
