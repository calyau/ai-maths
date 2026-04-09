---
concept: "Cauchy's Theorem"
slug: cauchys-theorem
category: group-structure
subcategory: sylow-theory
tier: advanced
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "The Sylow Theorems"
chapter_number: 15
pdf_page: 195
section: "The Sylow Theorems"
extraction_confidence: high
aliases:
  - "Cauchy's theorem for groups"
prerequisites:
  - class-equation
  - lagranges-theorem
  - fundamental-theorem-of-finite-abelian-groups
extends: []
related:
  - first-sylow-theorem
  - p-group
contrasts_with: []
answers_questions:
  - "Does a group whose order is divisible by p have an element of order p?"
---

# Quick Definition

Cauchy's Theorem states that if $G$ is a finite group and $p$ is a prime dividing $|G|$, then $G$ contains a subgroup (hence an element) of order $p$.

# Core Definition

**Theorem 15.1 (Cauchy)**: "Let $G$ be a finite group and $p$ a prime such that $p$ divides the order of $G$. Then $G$ contains a subgroup of order $p$" (Judson, p. 195).

# Prerequisites

- **Class equation** — Used in the proof
- **Lagrange's theorem** — Order of subgroup divides order of group
- **Fundamental Theorem of Finite Abelian Groups** — Used in Case 2

# Key Properties

1. Guarantees existence of an element of order $p$ whenever $p | |G|$
2. Corollary 15.2: $G$ is a $p$-group if and only if $|G| = p^n$
3. The First Sylow Theorem generalizes this to subgroups of order $p^r$

# Construction / Recognition

## Proof Strategy (by induction on $|G|$):
1. Apply the class equation: $|G| = |Z(G)| + [G:C(x_1)] + \cdots + [G:C(x_k)]$
2. **Case 1**: If $p | |C(x_i)|$ for some $i$, apply induction to $C(x_i)$
3. **Case 2**: If $p \nmid |C(x_i)|$ for all $i$, then $p | |Z(G)|$, and use the Fundamental Theorem of Finite Abelian Groups

# Examples

**Example 1** (p. 196): $|A_5| = 60 = 2^2 \cdot 3 \cdot 5$. Cauchy's Theorem guarantees subgroups of orders 2, 3, and 5.

# Relationships

## Builds Upon
- **Class equation** — Proof technique

## Enables
- **First Sylow theorem** — Generalizes Cauchy from $p$ to $p^r$

## Related
- **$p$-group** — Cauchy's theorem characterizes when $|G| = p^n$

# Source Reference

Chapter 15: The Sylow Theorems, Section 15.1, p. 195-196. Theorem 15.1.

# Verification Notes

- Definition source: Theorem 15.1
- Confidence: HIGH — major theorem with complete proof
