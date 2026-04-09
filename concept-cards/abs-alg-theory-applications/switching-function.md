---
concept: Switching Function
slug: switching-function
category: group-structure
subcategory: applications
tier: advanced
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Group Actions"
chapter_number: 14
pdf_page: 189
section: "Burnside's Counting Theorem"
extraction_confidence: high
aliases:
  - "Boolean function"
prerequisites:
  - burnside-counting-theorem
  - group-action
extends: []
related:
  - orbit
contrasts_with: []
answers_questions:
  - "What is a switching function?"
  - "How does Burnside's theorem apply to circuit design?"
---

# Quick Definition

A switching (or Boolean) function of $n$ variables is a function from $\mathbb{Z}_2^n$ to $\mathbb{Z}_2$. There are $2^{2^n}$ such functions, but many are equivalent under permutations of input variables. Burnside's theorem counts the distinct equivalence classes.

# Core Definition

"We define a **switching** or **Boolean function** of $n$ variables to be a function from $\mathbb{Z}_2^n$ to $\mathbb{Z}_2$. Since any switching function can have two possible values for each binary $n$-tuple and there are $2^n$ binary $n$-tuples, $2^{2^n}$ switching functions are possible for $n$ variables" (Judson, p. 189).

# Prerequisites

- **Burnside's counting theorem** — Used to count equivalence classes
- **Group action** — Permutations of inputs define the group action

# Key Properties

1. $2^{2^n}$ total switching functions for $n$ inputs
2. Two functions are equivalent if one is obtained by permuting inputs
3. For $n = 2$: 16 functions, 12 equivalence classes under $S_2$
4. For $n = 4$ with $D_4$ symmetry: 9616 equivalence classes

# Examples

**Example 1** (p. 189-190): For $n = 2$, the 16 switching functions reduce to 12 classes under $(ab)$, since $f_2 \sim f_4$, $f_3 \sim f_5$, $f_{10} \sim f_{12}$, $f_{11} \sim f_{13}$.

**Example 2** (p. 190-191): For $n = 4$ with 8-element symmetry group: $\frac{1}{8}(2^{16} + 2 \cdot 2^{12} + 2 \cdot 2^6 + 3 \cdot 2^{10}) = 9616$.

# Relationships

## Builds Upon
- **Burnside's counting theorem** — Counting tool

# Source Reference

Chapter 14: Group Actions, Section 14.3, pages 189-191. Table 14.26, 14.27.

# Verification Notes

- Definition source: Direct from p. 189
- Confidence: HIGH
