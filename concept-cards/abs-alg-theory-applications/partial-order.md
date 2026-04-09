---
# === CORE IDENTIFICATION ===
concept: Partial Order
slug: partial-order

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
pdf_page: 252
section: "19.1 Lattices"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - set
extends: []
related:
  - partially-ordered-set
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a partial order?"
---

# Quick Definition

A partial order on a set $X$ is a relation $P$ on $X$ that is reflexive, antisymmetric, and transitive.

# Core Definition

"A relation $P$ on $X$ is called a partial order of $X$ if it satisfies the following axioms: (1) reflexive: $(a,a) \in P$ for all $a \in X$; (2) antisymmetric: if $(a,b) \in P$ and $(b,a) \in P$, then $a = b$; (3) transitive: if $(a,b) \in P$ and $(b,c) \in P$, then $(a,c) \in P$" (Judson, p. 252).

# Prerequisites

- **Set** — A partial order is defined on a set

# Key Properties

1. Reflexive: $a \preceq a$ for all $a$
2. Antisymmetric: $a \preceq b$ and $b \preceq a$ implies $a = b$
3. Transitive: $a \preceq b$ and $b \preceq c$ implies $a \preceq c$
4. Not all elements need be comparable (unlike total orders)

# Construction / Recognition

## To Verify:
1. Check reflexivity
2. Check antisymmetry
3. Check transitivity

# Context & Application

Partial orders generalize the familiar $\leq$ on numbers. They appear in set inclusion on power sets, divisibility on integers, and subgroup inclusion in groups.

# Examples

**Example 1** (p. 252): $\leq$ on $\mathbb{Z}$ is a partial order (in fact, a total order).

**Example 2** (p. 252): Set inclusion $\subset$ on $\mathcal{P}(X)$ is a partial order.

**Example 3** (p. 253): Divisibility on $\mathbb{N}$: $a \preceq b$ if $a | b$.

# Relationships

## Enables
- **Partially ordered set** — A set with a partial order
- **Lattice** — A poset where every pair has a join and meet

# Common Errors

- **Error**: Assuming every pair of elements is comparable
  **Correction**: In a partial order, some pairs may be incomparable; $\{1,2\}$ and $\{1,3\}$ are incomparable under $\subset$

# Common Confusions

- **Confusion**: Confusing partial order with total order
  **Clarification**: A total order requires every pair to be comparable; a partial order does not

# Source Reference

Chapter 19: Lattices and Boolean Algebras, Section 19.1, page 252.

# Verification Notes

- Definition source: Direct from p. 252
- Confidence: HIGH — explicit axioms
- Cross-reference status: Verified
- Uncertainties: None
