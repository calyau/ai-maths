---
# === CORE IDENTIFICATION ===
concept: Partition
slug: partition

# === CLASSIFICATION ===
category: foundations
subcategory: set-theory
tier: foundational

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Preliminaries"
chapter_number: 1
pdf_page: 25
section: "Equivalence Relations and Partitions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - set
  - disjoint-sets
extends: []
related:
  - equivalence-relation
  - equivalence-class
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
---

# Quick Definition

A partition of a set $X$ is a collection of nonempty, pairwise disjoint subsets whose union is $X$. Partitions correspond bijectively to equivalence relations on $X$.

# Core Definition

"A partition $\mathcal{P}$ of a set $X$ is a collection of nonempty sets $X_1, X_2, \ldots$ such that $X_i \cap X_j = \emptyset$ for $i \neq j$ and $\bigcup_k X_k = X$" (Judson, p. 25).

**Theorem 1.25**: Given an equivalence relation $\sim$ on a set $X$, the equivalence classes form a partition of $X$. Conversely, if $\mathcal{P} = \{X_i\}$ is a partition, then defining $x \sim y$ when $x$ and $y$ are in the same partition element gives an equivalence relation with equivalence classes $X_i$.

# Prerequisites

- **Set** — A partition divides a set
- **Disjoint sets** — Partition elements must be pairwise disjoint

# Key Properties

1. Every element of $X$ belongs to exactly one part
2. No part is empty
3. Different parts are disjoint
4. The parts cover all of $X$
5. Partitions and equivalence relations on $X$ are in bijective correspondence

# Construction / Recognition

## To Verify a Partition:
1. Check that every element of $X$ is in at least one part
2. Check that no part is empty
3. Check that distinct parts have empty intersection

# Context & Application

Partitions underlie the construction of quotient structures in algebra. The integers modulo $n$ partition $\mathbb{Z}$ into $n$ classes, which then become the elements of the group $\mathbb{Z}_n$.

# Examples

**Example 1** (p. 26): Under congruence mod 3, the partition of $\mathbb{Z}$ is $\{[0], [1], [2]\}$ where $[0] \cup [1] \cup [2] = \mathbb{Z}$ and the sets are pairwise disjoint.

# Relationships

## Builds Upon
- **disjoint-sets** — Parts must be pairwise disjoint

## Enables
- **equivalence-relation** — Every partition defines an equivalence relation
- **integers-mod-n** — Constructed via partition of $\mathbb{Z}$

## Related
- **equivalence-class** — Equivalence classes form a partition

# Common Errors

- **Error**: Including the empty set as a part of a partition
  **Correction**: All parts of a partition must be nonempty

# Common Confusions

- **Confusion**: Thinking a partition requires parts of equal size
  **Clarification**: Parts can have different sizes; they only need to be nonempty, pairwise disjoint, and cover $X$

# Source Reference

Chapter 1: Preliminaries, Section 1.2, page 25. Theorem 1.25.

# Verification Notes

- Definition source: Direct quote from p. 25
- Confidence: HIGH — explicit definition and theorem
- Cross-reference status: Verified
- Uncertainties: None
