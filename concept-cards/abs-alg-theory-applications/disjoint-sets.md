---
# === CORE IDENTIFICATION ===
concept: Disjoint Sets
slug: disjoint-sets

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
pdf_page: 17
section: "Sets and Equivalence Relations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - set
  - set-intersection
  - empty-set
extends: []
related:
  - partition
  - equivalence-class
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
---

# Quick Definition

Two sets are disjoint if they have no elements in common, i.e., their intersection is the empty set.

# Core Definition

"When two sets have no elements in common, they are said to be disjoint... Two sets $A$ and $B$ are disjoint exactly when $A \cap B = \emptyset$" (Judson, p. 17).

# Prerequisites

- **Set** — Disjointness is a property of sets
- **Set intersection** — Defined via intersection
- **Empty set** — Disjoint means intersection equals $\emptyset$

# Key Properties

1. $A$ and $B$ are disjoint if and only if $A \cap B = \emptyset$
2. $(A \setminus B) \cap (B \setminus A) = \emptyset$ — always disjoint
3. A collection of sets is **pairwise disjoint** if every pair of distinct sets in the collection is disjoint

# Construction / Recognition

## To Verify Disjointness:
1. Compute $A \cap B$
2. If the result is $\emptyset$, the sets are disjoint

# Context & Application

Disjointness is essential in the theory of partitions and equivalence classes. Equivalence classes of an equivalence relation are either equal or disjoint (Corollary 1.26), which is what makes them form a partition.

# Examples

**Example 1** (p. 17): The set of even integers $E$ and the set of odd integers $O$ are disjoint.

**Example 2** (p. 26): The equivalence classes $[0] = \{\ldots, -3, 0, 3, 6, \ldots\}$, $[1] = \{\ldots, -2, 1, 4, 7, \ldots\}$, $[2] = \{\ldots, -1, 2, 5, 8, \ldots\}$ under mod 3 are pairwise disjoint.

# Relationships

## Builds Upon
- **set-intersection** — Disjointness is defined via intersection

## Enables
- **partition** — Partitions consist of pairwise disjoint nonempty sets
- **equivalence-class** — Distinct equivalence classes are disjoint

# Common Errors

- **Error**: Assuming nonempty sets are never disjoint
  **Correction**: Any two sets whose elements satisfy different conditions can be disjoint

# Common Confusions

- **Confusion**: Confusing disjoint with complementary
  **Clarification**: Complementary sets are disjoint AND their union is the universal set; disjoint sets need not cover the universal set

# Source Reference

Chapter 1: Preliminaries, Section 1.2, page 17.

# Verification Notes

- Definition source: Direct quote from p. 17
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
