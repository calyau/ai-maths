---
concept: Counting Sylow Subgroups
slug: counting-sylow-subgroups
category: group-structure
subcategory: sylow-theory
tier: advanced
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "The Sylow Theorems"
chapter_number: 15
pdf_page: 198
section: "Examples and Applications"
extraction_confidence: high
aliases:
  - "Sylow number analysis"
prerequisites:
  - third-sylow-theorem
  - second-sylow-theorem
  - normalizer
extends:
  - third-sylow-theorem
related:
  - non-simplicity-proofs
  - groups-of-order-pq
contrasts_with: []
answers_questions:
  - "How do I determine the number of Sylow p-subgroups?"
  - "How do I use the Sylow theorems to analyze group structure?"
---

# Quick Definition

To determine the number $n_p$ of Sylow $p$-subgroups, find all positive integers that simultaneously divide $|G|$ and are congruent to 1 modulo $p$. The candidates form a usually small set, often forcing $n_p = 1$.

# Core Definition

The Third Sylow Theorem constrains $n_p$ to values satisfying two conditions: (1) $n_p \equiv 1 \pmod{p}$ and (2) $n_p | |G|$. The systematic analysis of these constraints for each prime dividing $|G|$ is the primary tool for classifying groups and detecting normal subgroups.

# Prerequisites

- **Third Sylow theorem** — Provides the constraints
- **Second Sylow theorem** — $n_p = [G:N(P)]$
- **Normalizer** — $n_p = [G:N(P)]$

# Key Properties

1. $n_p \equiv 1 \pmod{p}$ (Third Sylow Theorem constraint)
2. $n_p$ divides $|G|$ (Third Sylow Theorem constraint)
3. $n_p = [G : N(P)]$ where $N(P)$ is the normalizer of any Sylow $p$-subgroup $P$
4. $n_p = 1$ if and only if the Sylow $p$-subgroup is normal in $G$
5. The intersection of constraints often forces $n_p = 1$, especially for groups of small order

# Construction / Recognition

## Systematic Procedure:
1. Factor $|G| = p_1^{a_1} \cdots p_k^{a_k}$
2. For each prime $p_i$:
   a. List divisors of $|G|$
   b. Filter to those $\equiv 1 \pmod{p_i}$
   c. These are the possible values of $n_{p_i}$
3. If $n_{p_i} = 1$ for any $p_i$, the unique Sylow $p_i$-subgroup is normal

# Examples

**Example 1** (p. 198): $|A_5| = 60$: $n_5 | 60$ and $n_5 \equiv 1 \pmod{5}$, giving $n_5 \in \{1, 6\}$. Since $A_5$ is simple, $n_5 = 6$.

**Example 2** (p. 199): $|G| = 99 = 9 \cdot 11$: $n_3 | 11$, $n_3 \equiv 1 \pmod{3}$, so $n_3 = 1$. Also $n_{11} | 9$, $n_{11} \equiv 1 \pmod{11}$, so $n_{11} = 1$. Both Sylow subgroups are normal.

# Relationships

## Builds Upon
- **Third Sylow theorem** — Provides the constraints

## Enables
- **Non-simplicity proofs** — $n_p = 1$ yields a normal subgroup
- **Group classification** — Determines possible group structures

# Source Reference

Chapter 15: The Sylow Theorems, Section 15.2, pages 198-201.

# Verification Notes

- Definition source: Synthesized from multiple examples
- Confidence: HIGH
