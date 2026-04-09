---
concept: Third Sylow Theorem
slug: third-sylow-theorem
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
  - "Sylow's third theorem"
  - "number of Sylow subgroups"
prerequisites:
  - second-sylow-theorem
  - normalizer
extends: []
related:
  - first-sylow-theorem
contrasts_with: []
answers_questions:
  - "How many Sylow p-subgroups does a group have?"
  - "How do I use the Sylow theorems to analyze group structure?"
---

# Quick Definition

The Third Sylow Theorem states that the number of Sylow $p$-subgroups is congruent to $1 \pmod{p}$ and divides $|G|$. These two constraints often determine the exact number of Sylow subgroups.

# Core Definition

**Theorem 15.8 (Third Sylow Theorem)**: "Let $G$ be a finite group and let $p$ be a prime dividing the order of $G$. Then the number of Sylow $p$-subgroups is congruent to $1 \pmod{p}$ and divides $|G|$" (Judson, p. 197).

# Prerequisites

- **Second Sylow theorem** — All Sylow $p$-subgroups are conjugate
- **Normalizer** — Number of Sylow subgroups $= [G:N(P)]$

# Key Properties

1. Let $n_p$ = number of Sylow $p$-subgroups. Then: $n_p \equiv 1 \pmod{p}$ and $n_p | |G|$
2. $n_p = 1$ implies the unique Sylow $p$-subgroup is normal
3. $n_p = [G:N(P)]$ for any Sylow $p$-subgroup $P$

# Construction / Recognition

## To Determine the Number of Sylow $p$-Subgroups:
1. List all divisors of $|G|$ that are $\equiv 1 \pmod{p}$
2. The number of Sylow $p$-subgroups must be one of these values
3. Often this leaves only $n_p = 1$, proving normality

# Context & Application

The Third Sylow Theorem is the most frequently applied of the three for classification purposes. The congruence condition often severely restricts the possible number of Sylow subgroups.

# Examples

**Example 1** (p. 198): For $A_5$ ($|A_5| = 60$): $n_5$ must divide 60 and $n_5 \equiv 1 \pmod{5}$. Options: 1 or 6. Since $A_5$ is simple, $n_5 \neq 1$, so $n_5 = 6$.

**Example 2** (p. 198): Groups of order $pq$ ($p < q$ primes): $n_q | pq$ and $n_q \equiv 1 \pmod{q}$. Since $1 + q > pq$ unless $q | (p-1)$... wait, since $p < q$, we get $n_q = 1$.

**Example 3** (p. 199): Groups of order 99 ($= 9 \cdot 11$): $n_3 | 11$ and $n_3 \equiv 1 \pmod{3}$, so $n_3 = 1$. Similarly $n_{11} | 9$ and $n_{11} \equiv 1 \pmod{11}$, so $n_{11} = 1$.

# Relationships

## Builds Upon
- **Second Sylow theorem** — Conjugacy gives $n_p = [G:N(P)]$

## Enables
- **Proving non-simplicity** — If $n_p = 1$, the group has a normal subgroup
- **Group classification** — Combined with structure theorems

# Common Errors

- **Error**: Forgetting to check BOTH conditions ($n_p \equiv 1 \pmod{p}$ AND $n_p | |G|$)
  **Correction**: Both conditions must be satisfied simultaneously

# Source Reference

Chapter 15: The Sylow Theorems, Section 15.1, p. 197-198. Theorem 15.8.

# Verification Notes

- Definition source: Theorem 15.8
- Confidence: HIGH — major theorem with complete proof
