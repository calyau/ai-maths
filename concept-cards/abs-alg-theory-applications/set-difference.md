---
# === CORE IDENTIFICATION ===
concept: Set Difference
slug: set-difference

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
aliases:
  - relative complement

# === TYPED RELATIONSHIPS ===
prerequisites:
  - set
  - set-complement
extends: []
related:
  - set-intersection
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
---

# Quick Definition

The difference of two sets $A$ and $B$, denoted $A \setminus B$, is the set of all elements in $A$ that are not in $B$.

# Core Definition

"We define the difference of two sets $A$ and $B$ to be $A \setminus B = A \cap B' = \{x : x \in A \text{ and } x \notin B\}$" (Judson, p. 17).

# Prerequisites

- **Set** — Set difference operates on sets
- **Set complement** — Defined as $A \cap B'$

# Key Properties

1. $A \setminus A = \emptyset$
2. $(A \setminus B) \cap (B \setminus A) = \emptyset$
3. $A \setminus B = A \cap B'$

# Construction / Recognition

## To Construct $A \setminus B$:
1. Take all elements of $A$
2. Remove any elements that are also in $B$

# Context & Application

Set difference appears when discussing elements that belong to one algebraic structure but not another, such as elements of a group that are not in a particular subgroup.

# Examples

**Example 1** (p. 18): If $A = \{x \in \mathbb{R} : 0 < x \leq 3\}$ and $B = \{x \in \mathbb{R} : 2 \leq x < 4\}$, then $A \setminus B = \{x \in \mathbb{R} : 0 < x < 2\}$.

# Relationships

## Builds Upon
- **set** — Operates on sets
- **set-complement** — $A \setminus B = A \cap B'$

## Related
- **set-intersection** — Used in the definition of set difference

# Common Errors

- **Error**: Assuming $A \setminus B = B \setminus A$
  **Correction**: Set difference is not commutative; in general $A \setminus B \neq B \setminus A$

# Common Confusions

- **Confusion**: Confusing set difference with symmetric difference
  **Clarification**: $A \setminus B$ removes elements of $B$ from $A$; symmetric difference removes elements common to both

# Source Reference

Chapter 1: Preliminaries, Section 1.2, page 17.

# Verification Notes

- Definition source: Direct quote from p. 17
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
