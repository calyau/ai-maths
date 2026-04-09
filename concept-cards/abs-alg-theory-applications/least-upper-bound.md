---
# === CORE IDENTIFICATION ===
concept: Least Upper Bound
slug: least-upper-bound

# === CLASSIFICATION ===
category: lattice-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Lattices and Boolean Algebras"
chapter_number: 19
pdf_page: 254
section: "19.1 Lattices"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "supremum"
  - "join"
  - "lub"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - partially-ordered-set
extends: []
related:
  - greatest-lower-bound
  - lattice
contrasts_with:
  - greatest-lower-bound

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a least upper bound?"
  - "What is a supremum?"
---

# Quick Definition

The least upper bound (or supremum) of a subset $Y$ of a poset $X$ is an upper bound $u$ of $Y$ that is less than or equal to every other upper bound of $Y$.

# Core Definition

"An element $u$ in $X$ is an upper bound of $Y$ if $a \preceq u$ for every element $a \in Y$. If $u$ is an upper bound of $Y$ such that $u \preceq v$ for every other upper bound $v$ of $Y$, then $u$ is called a least upper bound or supremum of $Y$" (Judson, p. 254). The least upper bound is unique when it exists (Theorem 19.9).

# Prerequisites

- **Partially ordered set** — Least upper bounds are defined in posets

# Key Properties

1. An upper bound that is $\preceq$ every other upper bound
2. Unique when it exists (Theorem 19.9)
3. For two elements $a, b$ in a lattice, denoted $a \vee b$ (the join)
4. Need not exist in every poset

# Construction / Recognition

## To Find:
1. Identify all upper bounds of $Y$
2. Find the smallest among them (if it exists)

# Context & Application

The least upper bound operation, when it exists for all pairs, gives a lattice its join operation. In the power set lattice, the LUB of $A$ and $B$ is $A \cup B$.

# Examples

**Example 1** (p. 254): In the divisors of 24, $Y = \{2,3,4,6\}$ has upper bounds 12 and 24, with least upper bound 12.

# Relationships

## Enables
- **Lattice** — A poset where every pair has a LUB and GLB

## Contrasts With
- **Greatest lower bound** — The dual concept

# Common Errors

- **Error**: Assuming a LUB always exists
  **Correction**: In some posets, certain subsets may not have a LUB

# Common Confusions

- **Confusion**: Confusing LUB with maximum
  **Clarification**: The LUB need not be an element of $Y$; a maximum must be

# Source Reference

Chapter 19: Lattices and Boolean Algebras, Section 19.1, page 254. See Theorem 19.9.

# Verification Notes

- Definition source: Direct from p. 254
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
