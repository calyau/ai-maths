---
# === CORE IDENTIFICATION ===
concept: Equivalence Class
slug: equivalence-class

# === CLASSIFICATION ===
category: equivalence-partitions
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Partitions"
chapter_number: 12
pdf_page: 68
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "$\\mathcal{R}(x)$"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - equivalence-relation
extends: []
related:
  - partition
  - congruence-class
  - left-coset
  - conjugacy-class
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an equivalence class?"
  - "How do equivalence classes relate to partitions?"
---

# Quick Definition

The equivalence class of $x$ under an equivalence relation $\mathcal{R}$ is the set $\mathcal{R}(x)$ of all elements related to $x$. The distinct equivalence classes form a partition.

# Core Definition

For each $x \in X$, the collection of all points which are related to $x$ is written $\mathcal{R}(x)$ and called the **equivalence class** of $x$ (Armstrong, Ch. 12, p. 68).

**(12.1) Theorem.** $\mathcal{R}(x) = \mathcal{R}(y)$ whenever $(x, y) \in \mathcal{R}$.

**(12.2) Theorem.** The distinct equivalence classes of an equivalence relation on $X$ form a partition of $X$.

# Prerequisites

- **Equivalence relation** — Equivalence classes are defined relative to an equivalence relation

# Key Properties

1. Every equivalence class is non-empty (since $x \in \mathcal{R}(x)$ by reflexivity)
2. Two equivalence classes are either identical or disjoint (Theorem 12.1)
3. The union of all equivalence classes is $X$
4. If $(x, y) \in \mathcal{R}$, then $\mathcal{R}(x) = \mathcal{R}(y)$ — the class does not depend on the choice of representative

# Construction / Recognition

## To Construct:
1. Fix $x \in X$
2. Collect all $y \in X$ with $(x, y) \in \mathcal{R}$
3. This collection is $\mathcal{R}(x)$

# Context & Application

Equivalence classes are the elements of quotient structures throughout group theory. Left cosets, conjugacy classes, and orbits are all equivalence classes of specific equivalence relations. The braid group $B_3$ is defined as a group whose elements are equivalence classes of braids.

# Examples

**Example 1** (p. 68): Under congruence modulo 3 on $\mathbb{Z}$, there are three equivalence classes: $\mathcal{R}(0) = \{\ldots, -3, 0, 3, 6, \ldots\}$, $\mathcal{R}(1) = \{\ldots, -2, 1, 4, 7, \ldots\}$, $\mathcal{R}(2) = \{\ldots, -1, 2, 5, 8, \ldots\}$.

**Example 2** (p. 69): In a group $G$ with subgroup $H$, the equivalence classes under $y^{-1}x \in H$ are the left cosets $gH$.

# Relationships

## Builds Upon
- **Equivalence relation** — Classes are defined by the relation

## Enables
- **Partition** — The distinct classes form a partition
- **Quotient group** — When the equivalence classes are cosets of a normal subgroup

## Related
- **Congruence class** — Equivalence class for modular congruence
- **Left coset** — Equivalence class for the coset relation
- **Conjugacy class** — Equivalence class for conjugacy

# Common Errors

- **Error**: Thinking the equivalence class depends on which representative is chosen
  **Correction**: By Theorem (12.1), $\mathcal{R}(x) = \mathcal{R}(y)$ whenever $x$ and $y$ are related

# Common Confusions

- **Confusion**: Conflating an equivalence class with a single element
  **Clarification**: An equivalence class is a *set* of elements, not a single element. When working in a quotient structure, each class represents a single element of the quotient.

# Source Reference

Chapter 12: Partitions, pp. 68-69 (pdf). Definition and Theorems (12.1), (12.2).

# Verification Notes

- Definition source: Direct from p. 68
- Confidence rationale: HIGH — explicitly defined
- Uncertainties: None
