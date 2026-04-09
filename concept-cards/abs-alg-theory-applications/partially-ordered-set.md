---
# === CORE IDENTIFICATION ===
concept: Partially Ordered Set
slug: partially-ordered-set

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
aliases:
  - "poset"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - partial-order
extends: []
related:
  - lattice
  - upper-bound
  - lower-bound
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a partially ordered set?"
  - "What is a poset?"
---

# Quick Definition

A partially ordered set (poset) is a set $X$ together with a partial order $\preceq$: a reflexive, antisymmetric, transitive relation on $X$.

# Core Definition

"A set $X$ together with a partial order $\preceq$ is called a partially ordered set, or poset" (Judson, p. 252).

# Prerequisites

- **Partial order** — A poset consists of a set and a partial order

# Key Properties

1. Combines a set with a partial order relation
2. Not all elements need be comparable
3. Can be visualized with Hasse diagrams
4. Every subset has at most one least upper bound and greatest lower bound

# Construction / Recognition

## To Construct:
1. Take a set $X$
2. Define a relation $\preceq$ that is reflexive, antisymmetric, and transitive

# Context & Application

Posets are the foundation for lattice theory. They appear in set theory (power sets), number theory (divisibility), and group theory (subgroup lattices).

# Examples

**Example 1** (p. 252): $(\mathbb{Z}, \leq)$ is a poset.

**Example 2** (p. 252): $(\mathcal{P}(X), \subset)$ is a poset.

**Example 3** (p. 253): $(X, |)$ where $X = \{1,2,3,4,6,8,12,24\}$ and $a \preceq b$ if $a | b$.

**Example 4** (p. 253): The set of subgroups of a group $G$, ordered by inclusion.

# Relationships

## Builds Upon
- **Partial order** — A poset is a set with a partial order

## Enables
- **Lattice** — A poset where every pair has a join and meet
- **Upper/lower bounds** — Defined in posets

# Common Errors

- **Error**: Assuming all elements in a poset are comparable
  **Correction**: In $(\{1,2,3,4,6,8,12,24\}, |)$, $4$ and $6$ are incomparable

# Common Confusions

- **Confusion**: Thinking a poset must be finite
  **Clarification**: $(\mathbb{Z}, \leq)$ and $(\mathbb{R}, \leq)$ are infinite posets

# Source Reference

Chapter 19: Lattices and Boolean Algebras, Section 19.1, page 252.

# Verification Notes

- Definition source: Direct from p. 252
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
