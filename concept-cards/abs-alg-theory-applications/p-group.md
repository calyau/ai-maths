---
concept: p-Group
slug: p-group
category: group-structure
subcategory: group-classification
tier: advanced
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "The Structure of Groups"
chapter_number: 13
pdf_page: 172
section: "Finite Abelian Groups"
extraction_confidence: high
aliases:
  - "prime power group"
prerequisites:
  - group
  - order-of-element
extends: []
related:
  - fundamental-theorem-of-finite-abelian-groups
  - p-subgroup
  - sylow-p-subgroup
  - cauchys-theorem
contrasts_with: []
answers_questions:
  - "What is a p-group?"
  - "When is a group a p-group?"
---

# Quick Definition

A group $G$ is a $p$-group if every element of $G$ has order a power of the prime $p$. A finite group is a $p$-group if and only if its order is a power of $p$.

# Core Definition

"Letting $p$ be prime, we define a group $G$ to be a **$p$-group** if every element in $G$ has as its order a power of $p$" (Judson, p. 172). By Lemma 13.7, "A finite abelian group is a $p$-group if and only if its order is a power of $p$" (p. 173). This extends to all finite groups by Corollary 15.2.

# Prerequisites

- **Group** — The base structure
- **Order of element** — Orders must be powers of $p$

# Key Properties

1. A finite group is a $p$-group iff $|G| = p^n$ for some $n$
2. $\mathbb{Z}_2 \times \mathbb{Z}_2$ and $\mathbb{Z}_4$ are 2-groups; $\mathbb{Z}_{27}$ is a 3-group
3. Every $p$-group of order $> 1$ has a nontrivial center (Theorem 14.15)
4. Every group of order $p^2$ is abelian (Corollary 14.16)
5. A finite abelian $p$-group is a direct product of cyclic $p$-groups

# Examples

**Example 1** (p. 172): $\mathbb{Z}_2 \times \mathbb{Z}_2$ and $\mathbb{Z}_4$ are both 2-groups; $\mathbb{Z}_{27}$ is a 3-group.

# Relationships

## Enables
- **Fundamental Theorem of Finite Abelian Groups** — Reduces to classifying finite abelian $p$-groups
- **Sylow p-subgroup** — Maximal $p$-subgroups

## Related
- **Cauchy's theorem** — Guarantees elements of order $p$ in groups whose order is divisible by $p$

# Source Reference

Chapter 13: The Structure of Groups, Section 13.1, p. 172. Lemma 13.7, p. 173.

# Verification Notes

- Definition source: Direct quote from p. 172
- Equivalence: Lemma 13.7
- Confidence: HIGH
