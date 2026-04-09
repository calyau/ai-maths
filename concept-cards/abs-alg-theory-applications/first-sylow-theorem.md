---
concept: First Sylow Theorem
slug: first-sylow-theorem
category: group-structure
subcategory: sylow-theory
tier: advanced
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "The Sylow Theorems"
chapter_number: 15
pdf_page: 196
section: "The Sylow Theorems"
extraction_confidence: high
aliases:
  - "Sylow's first theorem"
  - "existence of Sylow subgroups"
prerequisites:
  - cauchys-theorem
  - class-equation
  - factor-group
extends:
  - cauchys-theorem
related:
  - second-sylow-theorem
  - third-sylow-theorem
  - sylow-p-subgroup
contrasts_with: []
answers_questions:
  - "How do I use the Sylow theorems to analyze group structure?"
  - "Does a group contain subgroups of every prime power order dividing its order?"
---

# Quick Definition

The First Sylow Theorem guarantees that if $p^r$ divides $|G|$ for a prime $p$, then $G$ contains a subgroup of order $p^r$. In particular, Sylow $p$-subgroups (of maximal $p$-power order) always exist.

# Core Definition

**Theorem 15.4 (First Sylow Theorem)**: "Let $G$ be a finite group and $p$ a prime such that $p^r$ divides $|G|$. Then $G$ contains a subgroup of order $p^r$" (Judson, p. 196).

# Prerequisites

- **Cauchy's theorem** — The base case $r = 1$
- **Class equation** — Used in the proof
- **Factor group** — Induction step uses quotient groups

# Key Properties

1. $G$ has a subgroup of order $p^r$ for every $p^r$ dividing $|G|$
2. In particular, if $|G| = p^n m$ with $\gcd(p, m) = 1$, then $G$ has a subgroup of order $p^n$ (a Sylow $p$-subgroup)
3. Generalizes Cauchy's theorem ($r = 1$ case)

# Construction / Recognition

## Proof Strategy (induction on $|G|$):
1. Apply the class equation
2. If $p \nmid [G:C(x_i)]$ for some $i$, use induction on $C(x_i)$
3. Otherwise, $p | |Z(G)|$; find element $g$ of order $p$ in $Z(G)$
4. Let $N = \langle g \rangle$; then $N \trianglelefteq G$ and $|G/N| = |G|/p$
5. By induction, $G/N$ has subgroup $H$ of order $p^{r-1}$
6. The preimage $\phi^{-1}(H)$ has order $p^r$ in $G$

# Context & Application

The First Sylow Theorem is a partial converse to Lagrange's Theorem for prime power orders. While Lagrange says subgroups can only have orders dividing $|G|$, the First Sylow Theorem guarantees that prime power divisors actually occur as subgroup orders.

# Examples

**Example 1** (p. 196): $|A_5| = 60 = 2^2 \cdot 3 \cdot 5$. The First Sylow Theorem guarantees subgroups of orders 3, 4, and 5 (the Sylow subgroups).

# Relationships

## Builds Upon
- **Cauchy's theorem** — The $r = 1$ case

## Enables
- **Sylow $p$-subgroup** — Existence guaranteed by this theorem
- **Classification of groups** — Combined with Second and Third Sylow Theorems

## Related
- **Second Sylow theorem** — All Sylow $p$-subgroups are conjugate
- **Third Sylow theorem** — Constrains the number of Sylow $p$-subgroups

# Source Reference

Chapter 15: The Sylow Theorems, Section 15.1, p. 196. Theorem 15.4.

# Verification Notes

- Definition source: Theorem 15.4
- Confidence: HIGH — major theorem with complete proof
