---
concept: Partition Counting for Abelian Groups
slug: partition-counting-for-abelian-groups
category: group-structure
subcategory: classification-theorems
tier: advanced
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "The Structure of Groups"
chapter_number: 13
pdf_page: 172
section: "Finite Abelian Groups"
extraction_confidence: high
aliases: []
prerequisites:
  - fundamental-theorem-of-finite-abelian-groups
extends: []
related: []
contrasts_with: []
answers_questions:
  - "How many abelian groups of a given order are there?"
---

# Quick Definition

The number of non-isomorphic abelian groups of order $n = p_1^{a_1} \cdots p_k^{a_k}$ equals the product of the number of integer partitions of each exponent $a_i$. This follows from the Fundamental Theorem of Finite Abelian Groups.

# Core Definition

To classify all abelian groups of order $n$: factor $n = p_1^{a_1} \cdots p_k^{a_k}$, then for each $p_i^{a_i}$ determine all ways to partition $a_i$ into positive integer summands. Each partition corresponds to a distinct abelian group.

# Prerequisites

- **Fundamental Theorem of Finite Abelian Groups** — Provides the classification

# Key Properties

1. Number of abelian groups of order $n = \prod_i p(a_i)$ where $p(a_i)$ is the number of partitions of $a_i$
2. Partitions of 1: $\{1\}$ (1 partition)
3. Partitions of 2: $\{2, 1+1\}$ (2 partitions)
4. Partitions of 3: $\{3, 2+1, 1+1+1\}$ (3 partitions)
5. Partitions of 4: $\{4, 3+1, 2+2, 2+1+1, 1+1+1+1\}$ (5 partitions)

# Examples

**Example 1** (p. 172): Order $540 = 2^2 \cdot 3^3 \cdot 5$: partitions of 2 (2 ways) $\times$ partitions of 3 (3 ways) $\times$ partitions of 1 (1 way) $= 6$ abelian groups.

# Relationships

## Builds Upon
- **Fundamental Theorem of Finite Abelian Groups** — The classification theorem

# Source Reference

Chapter 13: The Structure of Groups, Section 13.1, p. 172. Example 13.5.

# Verification Notes

- Definition source: Synthesized from Example 13.5
- Confidence: HIGH
