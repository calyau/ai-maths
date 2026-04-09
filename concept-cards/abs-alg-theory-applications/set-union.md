---
# === CORE IDENTIFICATION ===
concept: Set Union
slug: set-union

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
  - union

# === TYPED RELATIONSHIPS ===
prerequisites:
  - set
extends: []
related:
  - set-intersection
  - set-complement
  - set-difference
contrasts_with:
  - set-intersection

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
---

# Quick Definition

The union of two sets $A$ and $B$, denoted $A \cup B$, is the set of all elements that belong to $A$ or $B$ (or both).

# Core Definition

"The union $A \cup B$ of two sets $A$ and $B$ is defined as $A \cup B = \{x : x \in A \text{ or } x \in B\}$" (Judson, p. 17).

# Prerequisites

- **Set** — Union is an operation on sets

# Key Properties

1. Commutative: $A \cup B = B \cup A$
2. Associative: $A \cup (B \cup C) = (A \cup B) \cup C$
3. Idempotent: $A \cup A = A$
4. Identity: $A \cup \emptyset = A$
5. Distributes over intersection: $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$
6. De Morgan's Law: $(A \cup B)' = A' \cap B'$

# Construction / Recognition

## To Construct $A \cup B$:
1. Collect all elements from $A$
2. Add all elements from $B$ that are not already included

# Context & Application

Set union is used throughout algebra when combining collections of elements. For example, equivalence classes partition a set: $[0] \cup [1] \cup [2] = \mathbb{Z}$ in mod 3 arithmetic.

# Examples

**Example 1** (p. 17): If $A = \{1, 3, 5\}$ and $B = \{1, 2, 3, 9\}$, then $A \cup B = \{1, 2, 3, 5, 9\}$.

**Example 2** (p. 18): If $A = \{x \in \mathbb{R} : 0 < x \leq 3\}$ and $B = \{x \in \mathbb{R} : 2 \leq x < 4\}$, then $A \cup B = \{x \in \mathbb{R} : 0 < x < 4\}$.

# Relationships

## Builds Upon
- **set** — Union operates on sets

## Related
- **set-intersection** — Dual operation
- **de-morgans-laws** — Relates union and intersection under complementation

## Contrasts With
- **set-intersection** — Union uses "or," intersection uses "and"

# Common Errors

- **Error**: Listing duplicate elements in the result
  **Correction**: Each element appears only once in a set, regardless of how many times it appears in the constituent sets

# Common Confusions

- **Confusion**: Confusing union with disjoint union
  **Clarification**: Elements in $A \cap B$ appear once in $A \cup B$, not twice

# Source Reference

Chapter 1: Preliminaries, Section 1.2, pages 17-18.

# Verification Notes

- Definition source: Direct quote from p. 17
- Confidence: HIGH — explicit definition with examples
- Cross-reference status: Verified
- Uncertainties: None
