---
# === CORE IDENTIFICATION ===
concept: Set Intersection
slug: set-intersection

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
pdf_page: 16
section: "Sets and Equivalence Relations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - intersection

# === TYPED RELATIONSHIPS ===
prerequisites:
  - set
extends: []
related:
  - set-union
  - disjoint-sets
contrasts_with:
  - set-union

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
---

# Quick Definition

The intersection of two sets $A$ and $B$, denoted $A \cap B$, is the set of all elements that belong to both $A$ and $B$.

# Core Definition

"The intersection of $A$ and $B$ is defined by $A \cap B = \{x : x \in A \text{ and } x \in B\}$" (Judson, p. 17).

# Prerequisites

- **Set** — Intersection is an operation on sets

# Key Properties

1. Commutative: $A \cap B = B \cap A$
2. Associative: $A \cap (B \cap C) = (A \cap B) \cap C$
3. Idempotent: $A \cap A = A$
4. $A \cap \emptyset = \emptyset$
5. Distributes over union: $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$
6. De Morgan's Law: $(A \cap B)' = A' \cup B'$

# Construction / Recognition

## To Construct $A \cap B$:
1. Examine each element of $A$
2. Include it in the result only if it also belongs to $B$

# Context & Application

Set intersection is used in algebra to define and verify disjoint sets, which are central to partitions and equivalence classes. The intersection of two subgroups of a group is also a subgroup.

# Examples

**Example 1** (p. 17): If $A = \{1, 3, 5\}$ and $B = \{1, 2, 3, 9\}$, then $A \cap B = \{1, 3\}$.

**Example 2** (p. 18): If $A = \{x \in \mathbb{R} : 0 < x \leq 3\}$ and $B = \{x \in \mathbb{R} : 2 \leq x < 4\}$, then $A \cap B = \{x \in \mathbb{R} : 2 \leq x \leq 3\}$.

# Relationships

## Builds Upon
- **set** — Intersection operates on sets

## Related
- **set-union** — Dual operation
- **disjoint-sets** — Two sets are disjoint when $A \cap B = \emptyset$

## Contrasts With
- **set-union** — Intersection uses "and," union uses "or"

# Common Errors

- **Error**: Forgetting to check membership in both sets
  **Correction**: An element must be in both $A$ and $B$ to be in $A \cap B$

# Common Confusions

- **Confusion**: Thinking $A \cap B$ is always nonempty when both $A$ and $B$ are nonempty
  **Clarification**: Disjoint nonempty sets have empty intersection

# Source Reference

Chapter 1: Preliminaries, Section 1.2, pages 17-18.

# Verification Notes

- Definition source: Direct quote from p. 17
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
