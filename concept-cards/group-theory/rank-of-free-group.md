---
# === CORE IDENTIFICATION ===
concept: Rank of a Free Group
slug: rank-of-free-group

# === CLASSIFICATION ===
category: free-groups-presentations
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Free Groups and Presentations; Coxeter Groups"
chapter_number: 2
pdf_page: 34
section: "Free groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - free-group
extends: []
related:
  - nielsen-schreier-theorem
  - rank-of-abelian-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the rank of a free group?"
  - "Can two free groups of different rank be isomorphic?"
---

# Quick Definition

The rank of a free group $G$ is the cardinality of any free generating set (a subset $X$ such that $F_X \to G$ is an isomorphism). Two free groups are isomorphic iff they have the same rank.

# Core Definition

"Two free groups $F_X$ and $F_Y$ are isomorphic if and only if $X$ and $Y$ have the same cardinality. Thus we can define the rank of a free group $G$ to be the cardinality of any free generating set." (Milne, p. 34)

# Prerequisites

- **Free group** — the rank is a property of free groups

# Key Properties

1. The rank is well-defined (any two free generating sets have the same cardinality)
2. $F_X \cong F_Y \iff |X| = |Y|$
3. A subgroup of a free group of rank $n$ and index $i$ has rank $ni - i + 1$ (when both are finite)
4. Subgroups of $F_n$ can have rank greater than $n$, or even infinite rank

# Context & Application

The rank classifies free groups up to isomorphism. The formula for subgroup rank shows the surprising fact that subgroups of free groups can be "larger" (higher rank) than the ambient group.

# Examples

**Example 1**: $F_1 = C_\infty$ has rank 1.

**Example 2** (p. 34): A subgroup of index $i$ in $F_n$ is free of rank $ni - i + 1$. For $n = 2$, $i = 3$: subgroup has rank $2 \cdot 3 - 3 + 1 = 4$.

**Example 3** (p. 34, footnote 2): The commutator subgroup of $F_2$ has infinite rank.

# Relationships

## Builds Upon
- **free-group**

## Related
- **nielsen-schreier-theorem** — subgroups are free, with computable rank
- **rank-of-abelian-group** — distinct concept for abelian groups

# Source Reference

Chapter 2, page 34.

# Verification Notes

- Definition source: Direct from p. 34
- Confidence: HIGH
- Uncertainties: None
