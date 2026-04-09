---
# === CORE IDENTIFICATION ===
concept: Greatest Lower Bound
slug: greatest-lower-bound

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
  - "infimum"
  - "meet"
  - "glb"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - partially-ordered-set
extends: []
related:
  - least-upper-bound
  - lattice
contrasts_with:
  - least-upper-bound

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a greatest lower bound?"
  - "What is an infimum?"
---

# Quick Definition

The greatest lower bound (or infimum) of a subset $Y$ of a poset $X$ is a lower bound $l$ of $Y$ such that $k \preceq l$ for every other lower bound $k$ of $Y$.

# Core Definition

"An element $l$ in $X$ is said to be a lower bound of $Y$ if $l \preceq a$ for all $a \in Y$. If $l$ is a lower bound of $Y$ such that $k \preceq l$ for every other lower bound $k$ of $Y$, then $l$ is called a greatest lower bound or infimum of $Y$" (Judson, p. 254). The GLB is unique when it exists (Theorem 19.9).

# Prerequisites

- **Partially ordered set** — Greatest lower bounds are defined in posets

# Key Properties

1. A lower bound that is $\succeq$ every other lower bound
2. Unique when it exists (Theorem 19.9)
3. For two elements $a, b$ in a lattice, denoted $a \wedge b$ (the meet)
4. Need not exist in every poset

# Construction / Recognition

## To Find:
1. Identify all lower bounds of $Y$
2. Find the greatest among them (if it exists)

# Context & Application

The greatest lower bound operation, when it exists for all pairs, gives a lattice its meet operation. In the power set lattice, the GLB of $A$ and $B$ is $A \cap B$.

# Examples

**Example 1** (p. 254): In the divisors of 24, $Y = \{2,3,4,6\}$ has only lower bound 1, so $\text{glb}(Y) = 1$.

# Relationships

## Enables
- **Lattice** — A poset where every pair has a GLB and LUB

## Contrasts With
- **Least upper bound** — The dual concept

# Common Errors

- **Error**: Assuming a GLB always exists
  **Correction**: In some posets, certain subsets may not have a GLB

# Common Confusions

- **Confusion**: Confusing GLB with minimum
  **Clarification**: The GLB need not be an element of $Y$; a minimum must be

# Source Reference

Chapter 19: Lattices and Boolean Algebras, Section 19.1, page 254. See Theorem 19.9.

# Verification Notes

- Definition source: Direct from p. 254
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
