---
# === CORE IDENTIFICATION ===
concept: Partition
slug: partition

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
  - "decomposition"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - set
extends: []
related:
  - equivalence-relation
  - equivalence-class
  - left-coset
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a partition of a set?"
  - "How do partitions relate to equivalence relations?"
---

# Quick Definition

A partition of a set $X$ is a decomposition into non-empty subsets, no two of which overlap, whose union is all of $X$.

# Core Definition

A partition of a set $X$ is a decomposition of the set into non-empty subsets, no two of which overlap and whose union is all of $X$ (Armstrong, Ch. 12, p. 68). Armstrong notes that the proof of Lagrange's theorem involved partitioning a group into subsets (the left cosets), each having the same number of elements as a given subgroup.

# Prerequisites

- **Set** — A partition decomposes a set

# Key Properties

1. Every member of the partition is non-empty
2. Distinct members are pairwise disjoint
3. The union of all members equals $X$
4. Every element of $X$ belongs to exactly one member

# Construction / Recognition

## To Recognize a Partition:
1. Verify each piece is non-empty
2. Verify no two pieces overlap
3. Verify their union covers all of $X$

# Context & Application

Armstrong introduces partitions to provide the general framework that underlies Lagrange's theorem. The key result (Theorem 12.2) is that equivalence relations and partitions are two descriptions of the same structure: every equivalence relation induces a partition into equivalence classes, and every partition defines an equivalence relation.

# Examples

**Example 1** (p. 68): The left cosets of a subgroup $H$ in $G$ partition $G$ into pieces of equal size $|H|$.

**Example 2** (p. 69): The congruence classes modulo 3 partition $\mathbb{Z}$ into $\mathcal{R}(0)$, $\mathcal{R}(1)$, $\mathcal{R}(2)$.

**Example 3** (p. 70): The orbits of $SO_3$ acting on $\mathbb{R}^3$ partition $\mathbb{R}^3$ into the origin and concentric spheres.

# Relationships

## Enables
- **Equivalence relation** — Every partition defines one, and vice versa
- **Lagrange's theorem** — Uses the coset partition

## Related
- **Left coset** — Left cosets form a partition of $G$
- **Conjugacy class** — Conjugacy classes partition $G$

# Common Errors

- **Error**: Allowing empty subsets in a partition
  **Correction**: All members of a partition must be non-empty

# Common Confusions

- **Confusion**: Thinking a partition is a specific type of function
  **Clarification**: A partition is a collection of subsets, not a function. It is equivalent to (but not identical with) an equivalence relation

# Source Reference

Chapter 12: Partitions, pp. 68-72 (pdf).

# Verification Notes

- Definition source: Direct from p. 68
- Confidence rationale: HIGH — explicitly defined
- Uncertainties: None
