---
concept: Groups of Order pq
slug: groups-of-order-pq
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
aliases: []
prerequisites:
  - third-sylow-theorem
  - second-sylow-theorem
extends: []
related:
  - simple-group
contrasts_with: []
answers_questions:
  - "What are the possible groups of order pq?"
  - "How do I use the Sylow theorems to analyze group structure?"
---

# Quick Definition

If $p$ and $q$ are distinct primes with $p < q$, then every group of order $pq$ has a unique (hence normal) Sylow $q$-subgroup, so it is not simple. If $q \not\equiv 1 \pmod{p}$, the group is cyclic.

# Core Definition

**Theorem 15.10**: "If $p$ and $q$ are distinct primes with $p < q$, then every group $G$ of order $pq$ has a single subgroup of order $q$ and this subgroup is normal in $G$. Hence, $G$ cannot be simple. Furthermore, if $q \not\equiv 1 \pmod{p}$, then $G$ is cyclic" (Judson, p. 198).

# Prerequisites

- **Third Sylow theorem** — Constrains the number of Sylow subgroups
- **Second Sylow theorem** — Conjugacy of Sylow subgroups

# Key Properties

1. $n_q | p$ and $n_q \equiv 1 \pmod{q}$, so $n_q = 1$ (since $p < q$)
2. The unique Sylow $q$-subgroup is normal
3. If also $q \not\equiv 1 \pmod{p}$, then $n_p = 1$ and $G \cong \mathbb{Z}_{pq}$

# Examples

**Example 1** (p. 199): Every group of order 15 ($= 3 \cdot 5$) is cyclic since $5 \not\equiv 1 \pmod{3}$.

**Example 2** (p. 199): Groups of order $99 = 9 \cdot 11$: unique Sylow 3-subgroup (order 9) and unique Sylow 11-subgroup. The group is $\mathbb{Z}_3 \times \mathbb{Z}_3 \times \mathbb{Z}_{11}$ or $\mathbb{Z}_9 \times \mathbb{Z}_{11}$.

# Relationships

## Builds Upon
- **Third Sylow theorem** — Determines $n_q = 1$

## Enables
- **Classification of small groups** — Classifies groups of order $pq$

# Source Reference

Chapter 15: The Sylow Theorems, Section 15.2, p. 198-199. Theorem 15.10, Examples 15.11-15.12.

# Verification Notes

- Definition source: Theorem 15.10
- Confidence: HIGH
