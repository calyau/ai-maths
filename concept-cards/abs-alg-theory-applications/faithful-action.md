---
concept: Faithful Action
slug: faithful-action
category: group-structure
subcategory: group-actions
tier: advanced
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Group Actions"
chapter_number: 14
pdf_page: 193
section: "Exercises"
extraction_confidence: high
aliases:
  - "effective action"
prerequisites:
  - group-action
extends:
  - group-action
related:
  - left-regular-representation
contrasts_with: []
answers_questions:
  - "What is a faithful group action?"
---

# Quick Definition

A group action is faithful if the identity is the only element of $G$ that fixes every element of $X$. Equivalently, no two distinct elements of $G$ have the same action on $X$.

# Core Definition

"A group acts **faithfully** on a $G$-set $X$ if the identity is the only element of $G$ that leaves every element of $X$ fixed" (Judson, p. 193, Exercise 14.5.20).

# Prerequisites

- **Group action** — Faithfulness is a property of an action

# Key Properties

1. $G$ acts faithfully iff $gx = x$ for all $x \in X$ implies $g = e$
2. Equivalently: the kernel of the homomorphism $G \to S_X$ is trivial
3. The left regular representation is always faithful
4. Faithful action means $G$ embeds in $S_X$

# Relationships

## Builds Upon
- **Group action** — Faithfulness is an additional property

## Related
- **Left regular representation** — Always faithful

# Source Reference

Chapter 14: Group Actions, Exercise 14.5.20, p. 193.

# Verification Notes

- Definition source: Exercise 14.5.20
- Confidence: HIGH
