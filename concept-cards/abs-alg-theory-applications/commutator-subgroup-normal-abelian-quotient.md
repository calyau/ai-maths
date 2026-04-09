---
concept: Commutator Subgroup and Abelian Quotients
slug: commutator-subgroup-normal-abelian-quotient
category: group-structure
subcategory: derived-subgroups
tier: advanced
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "The Sylow Theorems"
chapter_number: 15
pdf_page: 199
section: "Examples and Applications"
extraction_confidence: high
aliases:
  - "abelianization"
prerequisites:
  - commutator-subgroup
  - normal-subgroup
  - factor-group
extends:
  - commutator-subgroup
related:
  - solvable-group
  - groups-of-order-pq
contrasts_with: []
answers_questions:
  - "How does the commutator subgroup relate to abelian quotients?"
---

# Quick Definition

The commutator subgroup $G'$ is normal in $G$ and $G/G'$ is abelian (Theorem 15.13). Moreover, $G'$ is contained in any normal subgroup $N$ such that $G/N$ is abelian. Thus $G/G'$ is the "largest abelian quotient" of $G$.

# Core Definition

**Theorem 15.13**: "Let $G' = \langle aba^{-1}b^{-1} : a, b \in G \rangle$ be the subgroup consisting of all finite products of elements of the form $aba^{-1}b^{-1}$ in a group $G$. Then $G'$ is a normal subgroup of $G$ and $G/G'$ is abelian" (Judson, p. 199).

# Prerequisites

- **Commutator subgroup** — The subgroup $G'$
- **Normal subgroup** — $G' \trianglelefteq G$
- **Factor group** — $G/G'$ is abelian

# Key Properties

1. $G' \trianglelefteq G$
2. $G/G'$ is abelian
3. $G/G'$ is the largest abelian quotient: if $G/N$ is abelian then $G' \leq N$
4. Used to prove groups of order 1645 are abelian (Example 15.14)

# Context & Application

This result is used in the Sylow theory to constrain the commutator subgroup. If $G/H$ is abelian for some known $H$, then $G' \leq H$, which limits the possible orders of $G'$.

# Examples

**Example 1** (p. 199): Groups of order $1645 = 5 \cdot 7 \cdot 47$. The unique Sylow 47-subgroup $H_1$ gives $G/H_1$ of order 35, which is abelian. So $G' \leq H_1$, meaning $|G'| | 47$. Further analysis shows $G' = \{e\}$, so $G$ is abelian.

# Relationships

## Builds Upon
- **Commutator subgroup** — The subject

## Enables
- **Classifying groups as abelian** — Via bounding $G'$

# Source Reference

Chapter 15: The Sylow Theorems, Section 15.2, p. 199. Theorem 15.13, Example 15.14.

# Verification Notes

- Definition source: Theorem 15.13
- Confidence: HIGH
