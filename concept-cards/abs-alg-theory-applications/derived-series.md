---
concept: Derived Series
slug: derived-series
category: group-structure
subcategory: series-of-subgroups
tier: advanced
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "The Structure of Groups"
chapter_number: 13
pdf_page: 179
section: "Exercises"
extraction_confidence: high
aliases:
  - "commutator series"
prerequisites:
  - commutator-subgroup
  - solvable-group
extends: []
related:
  - subnormal-series
contrasts_with: []
answers_questions:
  - "What is the derived series of a group?"
  - "How does the derived series characterize solvability?"
---

# Quick Definition

The derived series of a group $G$ is the sequence $G^{(0)} = G, G^{(1)} = G', G^{(2)} = (G')', \ldots$ formed by iterating the commutator subgroup. A group is solvable if and only if its derived series reaches $\{e\}$.

# Core Definition

"We can define a series of subgroups of $G$ by $G^{(0)} = G$, $G^{(1)} = G'$, and $G^{(i+1)} = (G^{(i)})'$... The series $G^{(0)} = G \supset G^{(1)} \supset G^{(2)} \supset \cdots$ is called the **derived series** of $G$" (Judson, p. 179, Exercise 13.4.20). $G$ is solvable if and only if $G^{(n)} = \{e\}$ for some integer $n$.

# Prerequisites

- **Commutator subgroup** — Each term is the commutator of the previous
- **Solvable group** — The derived series characterizes solvability

# Key Properties

1. $G^{(i+1)} \trianglelefteq G^{(i)}$ for all $i$
2. $G$ is solvable iff $G^{(n)} = \{e\}$ for some $n$
3. For abelian $G$: $G^{(1)} = \{e\}$
4. Each quotient $G^{(i)}/G^{(i+1)}$ is abelian

# Relationships

## Builds Upon
- **Commutator subgroup** — Each term is a commutator subgroup

## Enables
- **Solvable group** — Solvability is equivalent to derived series terminating

# Source Reference

Chapter 13: The Structure of Groups, Exercise 13.4.20, p. 179.

# Verification Notes

- Definition source: Exercise 13.4.20
- Confidence: HIGH
