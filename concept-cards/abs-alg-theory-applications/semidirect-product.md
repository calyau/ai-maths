---
concept: Semidirect Product
slug: semidirect-product
category: group-structure
subcategory: group-constructions
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Matrix Groups and Symmetry"
chapter_number: 12
pdf_page: 169
section: "Exercises"
extraction_confidence: high
aliases:
  - "semi-direct product"
prerequisites:
  - normal-subgroup
  - direct-product
extends: []
related:
  - euclidean-group
  - dihedral-group
contrasts_with:
  - direct-product
answers_questions:
  - "What is a semidirect product?"
---

# Quick Definition

A group $G$ is a semidirect product of a normal subgroup $N$ by a subgroup $H$ if $H \cap N = \{e\}$ and $HN = G$. Unlike a direct product, $H$ need not be normal.

# Core Definition

"Let $G$ be a group with a subgroup $H$ (not necessarily normal) and a normal subgroup $N$. Then $G$ is a **semidirect product** of $N$ by $H$ if (1) $H \cap N = \{\text{id}\}$ and (2) $HN = G$" (Judson, p. 169, Exercise 12.4.15).

# Prerequisites

- **Normal subgroup** — $N$ must be normal
- **Direct product** — The semidirect product generalizes this

# Key Properties

1. $N \trianglelefteq G$ but $H$ need not be normal
2. $H \cap N = \{e\}$
3. $HN = G$
4. Every $g \in G$ can be written uniquely as $g = hn$ with $h \in H, n \in N$
5. $|G| = |H| \cdot |N|$

# Examples

**Example 1** (p. 169): $S_3$ is the semidirect product of $A_3$ by $H = \{(1), (12)\}$.

**Example 2** (p. 169): $E(2)$ is the semidirect product of $O(2)$ by the group of translations.

**Example 3** (p. 169): $Q_8$ cannot be written as a semidirect product.

# Relationships

## Contrasts With
- **Direct product** — In a direct product, both factors are normal

## Related
- **Euclidean group** — $E(2)$ is a semidirect product

# Source Reference

Chapter 12: Matrix Groups and Symmetry, Exercise 12.4.15, p. 169.

# Verification Notes

- Definition source: Exercise 12.4.15
- Confidence: HIGH
