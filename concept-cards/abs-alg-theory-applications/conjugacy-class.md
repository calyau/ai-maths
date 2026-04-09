---
concept: Conjugacy Class
slug: conjugacy-class
category: group-structure
subcategory: group-actions
tier: advanced
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Group Actions"
chapter_number: 14
pdf_page: 184
section: "The Class Equation"
extraction_confidence: high
aliases:
  - "conjugacy classes"
prerequisites:
  - group-action
  - orbit
  - conjugation-of-elements
extends:
  - orbit
related:
  - class-equation
  - centralizer-of-element
  - center-of-group
contrasts_with: []
answers_questions:
  - "What is a conjugacy class?"
  - "How do conjugacy classes relate to the class equation?"
---

# Quick Definition

A conjugacy class of a group $G$ is an orbit of $G$ acting on itself by conjugation. The conjugacy class of $x$ is $\{gxg^{-1} : g \in G\}$. Elements in $Z(G)$ form singleton conjugacy classes.

# Core Definition

"The nontrivial orbits of the [conjugation] action are called the **conjugacy classes** of $G$" (Judson, p. 184). When $G$ acts on itself by conjugation $(g, x) \mapsto gxg^{-1}$, the fixed points are the center $Z(G)$, and the nontrivial orbits are the conjugacy classes with more than one element.

# Prerequisites

- **Group action** — Conjugation is a specific group action
- **Orbit** — Conjugacy classes are orbits
- **Conjugation** — The action $(g,x) \mapsto gxg^{-1}$

# Key Properties

1. The conjugacy class of $x$ is $\{gxg^{-1} : g \in G\}$
2. $x \in Z(G)$ iff its conjugacy class is $\{x\}$
3. The size of the conjugacy class of $x$ is $[G:C(x)]$
4. In $S_n$, two elements are conjugate iff they have the same cycle type
5. Conjugacy classes partition $G$
6. The number of conjugacy classes in $S_n$ equals the number of partitions of $n$

# Examples

**Example 1** (p. 184): Conjugacy classes in $S_3$: $\{(1)\}$, $\{(123), (132)\}$, $\{(12), (13), (23)\}$. Class equation: $6 = 1 + 2 + 3$.

**Example 2** (p. 184): Center of $D_4$ is $\{(1), (13)(24)\}$; conjugacy classes are $\{(13), (24)\}$, $\{(1432), (1234)\}$, $\{(12)(34), (14)(23)\}$. Class equation: $8 = 2 + 2 + 2 + 2$.

# Relationships

## Builds Upon
- **Orbit** — Conjugacy classes are orbits under conjugation

## Enables
- **Class equation** — Sums sizes of conjugacy classes

## Related
- **Centralizer of element** — $|$conjugacy class of $x| = [G:C(x)]$
- **Center of group** — Elements with trivial conjugacy class

# Source Reference

Chapter 14: Group Actions, Section 14.2, p. 184. Examples 14.12-14.14.

# Verification Notes

- Definition source: Direct from p. 184
- Confidence: HIGH
