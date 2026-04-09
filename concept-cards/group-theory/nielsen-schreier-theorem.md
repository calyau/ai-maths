---
# === CORE IDENTIFICATION ===
concept: Nielsen-Schreier Theorem
slug: nielsen-schreier-theorem

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
  - rank-of-free-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Are subgroups of free groups also free?"
  - "What is the Nielsen-Schreier theorem?"
---

# Quick Definition

Subgroups of free groups are free. Moreover, if $H$ is a subgroup of index $i$ in a free group of finite rank $n$, then $H$ is free of rank $ni - i + 1$.

# Core Definition

"Subgroups of free groups are free." (Milne, Theorem 2.6, p. 34)

Nielsen (1921) proved this for finitely generated subgroups; Schreier (1927) proved the general case.

# Prerequisites

- **Free group** — the theorem concerns subgroups of free groups

# Key Properties

1. Every subgroup of a free group is free
2. The best proof uses algebraic topology (covering spaces)
3. For finitely generated subgroups, there is an algorithm to find free generators from arbitrary generators
4. Index-rank formula: if $G$ has rank $n$ and $H$ has index $i$, then $H$ has rank $ni - i + 1$
5. Subgroups can have higher rank than the ambient group

# Context & Application

This is a remarkable structural theorem: the class of free groups is closed under taking subgroups. This is unusual -- most algebraic properties are not preserved by subgroups. The topological proof via covering spaces is considered the most elegant.

# Examples

**Example 1** (p. 34): The commutator subgroup of $F_2$ (the free group on 2 generators) has infinite rank, despite $F_2$ having rank 2.

**Example 2**: A subgroup of index 2 in $F_2$ is free of rank $2 \cdot 2 - 2 + 1 = 3$.

# Relationships

## Builds Upon
- **free-group**

## Related
- **rank-of-free-group** — the theorem gives a formula for subgroup rank

# Source Reference

Chapter 2, Theorem 2.6, page 34. References: Serre 1980, Rotman 1995.

# Verification Notes

- Definition source: Direct from Theorem 2.6
- Confidence: HIGH — stated without proof but with references
- Uncertainties: None
