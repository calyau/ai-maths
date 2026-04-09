---
# === CORE IDENTIFICATION ===
concept: Symmetric Group
slug: symmetric-group

# === CLASSIFICATION ===
category: permutation-groups
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Permutation Groups"
chapter_number: 5
pdf_page: 72
section: "5.1 Definitions and Notation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "$S_n$"
  - "symmetric group on n letters"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - permutation
extends: []
related:
  - permutation-group
  - alternating-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a symmetric group?"
  - "How many elements does $S_n$ have?"
  - "What is $S_n$?"
---

# Quick Definition

The symmetric group on $n$ letters, denoted $S_n$, is the group of all permutations of $\{1, 2, \ldots, n\}$ under composition. It has $n!$ elements.

# Core Definition

"The symmetric group on $n$ letters, $S_n$, is a group with $n!$ elements, where the binary operation is the composition of maps" (Judson, Theorem 5.1, p. 72). If $X$ is a finite set, we can assume $X = \{1, 2, \ldots, n\}$ and write $S_n$ instead of $S_X$.

# Prerequisites

- **Permutation** — Elements of $S_n$ are permutations

# Key Properties

1. $|S_n| = n!$
2. The identity element is the identity map sending each $i$ to $i$
3. Every element has an inverse (since permutations are bijections)
4. The operation (composition) is associative
5. $S_n$ is nonabelian for $n \geq 3$

# Construction / Recognition

## To Construct:
1. Fix $n$ and consider the set $\{1, 2, \ldots, n\}$
2. Enumerate all bijective functions from this set to itself
3. The group operation is composition of functions

## To Recognize:
1. Verify the group consists of all bijections on a set of $n$ elements
2. Check the operation is function composition

# Context & Application

The symmetric group is the "universal" permutation group: every permutation group is a subgroup of some $S_n$. By Cayley's theorem, every group is isomorphic to a subgroup of a symmetric group.

# Examples

**Example 1** (p. 72): $S_3$ consists of the six permutations of $\{A, B, C\}$, corresponding to the symmetries of an equilateral triangle.

**Example 2** (p. 73): The subgroup $G = \{\text{id}, \sigma, \tau, \mu\}$ of $S_5$ is a permutation group (a subgroup of $S_5$) with four elements.

# Relationships

## Builds Upon
- **Permutation** — Elements of $S_n$ are permutations

## Enables
- **Permutation Group** — Any subgroup of $S_n$ is a permutation group
- **Alternating Group** — $A_n$ is the subgroup of even permutations in $S_n$
- **Cayley's Theorem** — Every group embeds into some $S_n$

## Related
- **Dihedral Group** — $D_n$ is a subgroup of $S_n$

# Common Errors

- **Error**: Confusing $|S_n|$ with $n$ or $2n$
  **Correction**: $|S_n| = n!$, which grows very quickly (e.g., $|S_5| = 120$)

# Common Confusions

- **Confusion**: Believing all subgroups of $S_n$ have order dividing $n$
  **Clarification**: Subgroups can have any order that divides $n!$

# Source Reference

Chapter 5: Permutation Groups, Section 5.1, Theorem 5.1, pages 72-73.

# Verification Notes

- Definition source: Direct from Theorem 5.1, p. 72
- Confidence rationale: Explicit theorem statement
- Uncertainties: None
- Cross-reference status: Verified
