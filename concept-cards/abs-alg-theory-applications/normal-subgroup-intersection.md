---
concept: Intersection of Normal Subgroups
slug: normal-subgroup-intersection
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
extends:
  - normal-subgroup
related: []
contrasts_with: []
answers_questions:
  - "Is the intersection of normal subgroups normal?"
---

# Quick Definition

The intersection of two normal subgroups is always a normal subgroup. This is because if $gNg^{-1} = N$ and $gMg^{-1} = M$, then $g(N \cap M)g^{-1} = N \cap M$.

# Core Definition

**Exercise 10.4.5**: "Show that the intersection of two normal subgroups is a normal subgroup" (Judson, p. 144).

# Prerequisites

- **Normal subgroup** — Both subgroups must be normal

# Key Properties

1. If $N \trianglelefteq G$ and $M \trianglelefteq G$, then $N \cap M \trianglelefteq G$
2. The intersection of any family of normal subgroups is normal
3. This generalizes to arbitrary (possibly infinite) intersections

# Relationships

## Builds Upon
- **Normal subgroup** — Closure property

# Source Reference

Chapter 10: Normal Subgroups and Factor Groups, Exercise 10.4.5, p. 144.

# Verification Notes

- Definition source: Exercise 10.4.5
- Confidence: HIGH
