---
concept: Conjugacy Classes in Symmetric Groups
slug: conjugacy-classes-in-symmetric-group
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
aliases: []
prerequisites:
  - conjugacy-class
  - symmetric-group
  - cycle-decomposition
extends:
  - conjugacy-class
related:
  - partition
contrasts_with: []
answers_questions:
  - "How are conjugacy classes in S_n determined?"
  - "What determines whether two permutations are conjugate?"
---

# Quick Definition

Two permutations in $S_n$ are conjugate if and only if they have the same cycle type (same lengths in their cycle decompositions). The number of conjugacy classes in $S_n$ equals the number of partitions of $n$.

# Core Definition

"Any two cycles of the same length are conjugate" since $\tau\sigma\tau^{-1} = (\tau(a_1), \ldots, \tau(a_k))$ for $\sigma = (a_1, \ldots, a_k)$ (Judson, p. 184, Example 14.14). More generally, "$\sigma$ is conjugate to every other $\tau \in S_n$ whose cycle decomposition has the same lengths."

# Prerequisites

- **Conjugacy class** — These are specific conjugacy classes
- **Symmetric group** — The setting
- **Cycle decomposition** — Determines conjugacy type

# Key Properties

1. $\tau\sigma\tau^{-1} = (\tau(a_1), \ldots, \tau(a_k))$ for a cycle $\sigma = (a_1, \ldots, a_k)$
2. Two permutations are conjugate iff they have the same cycle type
3. Number of conjugacy classes in $S_n$ = number of partitions of $n$
4. For $S_3$: 3 partitions of 3 give 3 conjugacy classes

# Examples

**Example 1** (p. 184): $S_3$ has 3 conjugacy classes: $\{(1)\}$, $\{(123), (132)\}$, $\{(12), (13), (23)\}$, corresponding to partitions $1+1+1$, $3$, $2+1$.

# Relationships

## Builds Upon
- **Conjugacy class** — Specializes to $S_n$
- **Cycle decomposition** — Determines the class

## Related
- **Partition** — Number of classes = number of partitions of $n$

# Source Reference

Chapter 14: Group Actions, Section 14.2, p. 184. Example 14.14.

# Verification Notes

- Definition source: Example 14.14
- Confidence: HIGH
