---
# === CORE IDENTIFICATION ===
concept: Index of a Subgroup
slug: index-of-a-subgroup

# === CLASSIFICATION ===
category: group-structure
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Cosets and Lagrange's Theorem"
chapter_number: 6
pdf_page: 88
section: "6.1 Cosets"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "[G:H]"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - left-coset
extends: []
related:
  - lagranges-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the index of a subgroup?"
  - "How do I compute [G:H]?"
---

# Quick Definition

The index of a subgroup $H$ in $G$, denoted $[G:H]$, is the number of distinct left cosets of $H$ in $G$. For finite groups, $[G:H] = |G|/|H|$.

# Core Definition

"Let $G$ be a group and $H$ be a subgroup of $G$. Define the *index* of $H$ in $G$ to be the number of left cosets of $H$ in $G$. We will denote the index by $[G:H]$" (Judson, p. 88).

# Prerequisites

- **Left Coset** — The index counts left cosets

# Key Properties

1. For finite groups, $[G:H] = |G|/|H|$ (by Lagrange's Theorem)
2. The number of left cosets equals the number of right cosets (Theorem 6.8)
3. If $G \supset H \supset K$, then $[G:K] = [G:H][H:K]$ (Corollary 6.13)
4. $[G:H] = 1$ if and only if $H = G$
5. The index can be infinite for infinite groups

# Construction / Recognition

## To Compute:
1. Enumerate the distinct left cosets of $H$ in $G$
2. Count them
3. Alternatively, for finite groups: $[G:H] = |G|/|H|$

# Context & Application

The index measures "how many copies" of $H$ are needed to tile $G$. It appears in Lagrange's Theorem and its corollaries.

# Examples

**Example 1** (p. 88): $[\mathbb{Z}_6 : \{0,3\}] = 3$.

**Example 2** (p. 88): In $S_3$, $[S_3 : \{(1),(123),(132)\}] = 2$ and $[S_3 : \{(1),(12)\}] = 3$.

# Relationships

## Builds Upon
- **Left Coset** — The index counts cosets

## Enables
- **Lagrange's Theorem** — $|G| = [G:H] \cdot |H|$

# Common Errors

- **Error**: Confusing the index with the order of the subgroup
  **Correction**: $[G:H] = |G|/|H|$, not $|H|$

# Common Confusions

- **Confusion**: Thinking the index must be finite
  **Clarification**: For infinite groups, the index can be infinite (e.g., $[\mathbb{Q}:\mathbb{Z}]$ is infinite)

# Source Reference

Chapter 6: Cosets and Lagrange's Theorem, Section 6.1, page 88.

# Verification Notes

- Definition source: Direct from p. 88
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
