---
concept: G-Set
slug: g-set
category: group-structure
subcategory: group-actions
tier: advanced
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Group Actions"
chapter_number: 14
pdf_page: 181
section: "Groups Acting on Sets"
extraction_confidence: high
aliases:
  - "G-space"
prerequisites:
  - group-action
extends: []
related:
  - orbit
  - stabilizer-subgroup
contrasts_with: []
answers_questions:
  - "What is a G-set?"
---

# Quick Definition

A $G$-set is a set $X$ together with a group action of $G$ on $X$. The set $X$ need not be related to $G$ in any way, though the most interesting $G$-sets arise when $X$ has some connection to $G$.

# Core Definition

"Under these considerations $X$ is called a **$G$-set**" (Judson, p. 181), where the "considerations" are the two axioms of a group action: $ex = x$ and $(g_1 g_2)x = g_1(g_2 x)$.

# Prerequisites

- **Group action** — A $G$-set requires a group action

# Key Properties

1. Any set is a $G$-set under the trivial action
2. $G$ itself is a $G$-set under left multiplication, conjugation, etc.
3. The set of cosets $G/H$ is a $G$-set
4. $G$-equivalence partitions $X$ into orbits

# Examples

**Example 1** (p. 181): $\mathbb{R}^2$ is a $GL_2(\mathbb{R})$-set under matrix multiplication.

**Example 2** (p. 181): $\{1,2,3,4\}$ is a $D_4$-set under the permutation action on vertices.

# Relationships

## Builds Upon
- **Group action** — Defines the structure

## Enables
- **Orbit** — Orbits partition the $G$-set
- **Stabilizer subgroup** — Each point has a stabilizer

# Source Reference

Chapter 14: Group Actions, Section 14.1, p. 181.

# Verification Notes

- Definition source: Direct from p. 181
- Confidence: HIGH
