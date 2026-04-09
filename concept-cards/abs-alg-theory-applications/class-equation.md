---
concept: Class Equation
slug: class-equation
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
  - "conjugacy class equation"
prerequisites:
  - conjugacy-class
  - center-of-group
  - centralizer-of-element
  - orbit-stabilizer-theorem
extends: []
related:
  - nontrivial-center-of-p-group
  - groups-of-order-p-squared
  - cauchys-theorem
contrasts_with: []
answers_questions:
  - "What is the class equation?"
  - "How does the class equation relate to group actions?"
---

# Quick Definition

The class equation expresses the order of a finite group as $|G| = |Z(G)| + [G:C(x_1)] + \cdots + [G:C(x_k)]$, where $x_1, \ldots, x_k$ represent the nontrivial conjugacy classes and $C(x_i)$ are centralizer subgroups.

# Core Definition

When $G$ acts on itself by conjugation, the orbits partition $G$ into the center and the nontrivial conjugacy classes. The **class equation** is: $|G| = |Z(G)| + [G:C(x_1)] + \cdots + [G:C(x_k)]$, "where $Z(G) = \{g \in G : gx = xg \text{ for all } x \in G\}$ is the center of $G$ and $C(x_i) = \{g \in G : gx_i = x_i g\}$ is the centralizer subgroup of $x_i$" (Judson, p. 184).

# Prerequisites

- **Conjugacy class** — The nontrivial orbits
- **Center of group** — The fixed points under conjugation
- **Centralizer of element** — Stabilizer of $x_i$ under conjugation
- **Orbit-stabilizer theorem** — $|\mathcal{O}_{x_i}| = [G:C(x_i)]$

# Key Properties

1. $|G| = |Z(G)| + n_1 + \cdots + n_k$ where $n_i > 1$
2. Each $n_i = [G:C(x_i)]$ divides $|G|$
3. For $p$-groups: $p$ divides each $n_i$ and $p$ divides $|G|$, so $p$ divides $|Z(G)|$

# Context & Application

The class equation is a powerful tool for proving structural results about groups. It is used to prove: (1) $p$-groups have nontrivial centers, (2) groups of order $p^2$ are abelian, (3) Cauchy's theorem, and (4) the Sylow theorems.

# Examples

**Example 1** (p. 184): $S_3$: $6 = 1 + 2 + 3$.

**Example 2** (p. 185): $D_4$: $8 = 2 + 2 + 2 + 2$.

# Relationships

## Builds Upon
- **Conjugacy class** — Terms of the equation
- **Orbit-stabilizer theorem** — Gives $n_i = [G:C(x_i)]$

## Enables
- **Nontrivial center of p-group** — Key application
- **Groups of order p^2 are abelian** — Corollary
- **Cauchy's theorem** — Proved using class equation
- **First Sylow theorem** — Proved using class equation

# Source Reference

Chapter 14: Group Actions, Section 14.2, p. 184.

# Verification Notes

- Definition source: Direct from p. 184
- Confidence: HIGH
