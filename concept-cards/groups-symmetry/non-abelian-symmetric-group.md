---
# === CORE IDENTIFICATION ===
concept: Non-Abelianness of S_n
slug: non-abelian-symmetric-group

# === CLASSIFICATION ===
category: permutation-groups
subcategory: properties
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Permutations"
chapter_number: 6
pdf_page: 33
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - symmetric-group
extends: []
related:
  - cycle-notation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Is the symmetric group abelian?"
  - "For which n is S_n non-abelian?"
---

# Quick Definition

$S_n$ is non-abelian for all $n \ge 3$. This is demonstrated by a single explicit computation in $S_3$.

# Core Definition

Armstrong demonstrates: "$(12)(23) = (123)$, whereas $(23)(12) = (132)$. Therefore, $S_3$ is not abelian. We can immediately say that $S_n$ is not abelian when $n \ge 3$" (p. 33-34). The argument extends because $S_3$ embeds as a subgroup of $S_n$ for all $n \ge 3$: the non-commuting permutations $(12)$ and $(23)$ remain non-commuting in the larger group.

# Prerequisites

- **Symmetric group** — The group whose commutativity is studied

# Key Properties

1. $S_1 = \{e\}$ and $S_2 = \{e, (12)\}$ are abelian
2. $S_n$ is non-abelian for $n \ge 3$
3. A single counterexample suffices: $(12)(23) \ne (23)(12)$ in $S_3$
4. $S_3$ embeds in $S_n$ for $n \ge 3$, so non-commutativity propagates

# Construction / Recognition

## To Verify Non-Abelianness:
1. Find two elements that do not commute
2. $(12)(23) = (123)$ but $(23)(12) = (132)$

# Context & Application

Non-abelianness of $S_n$ is one of the first properties Armstrong establishes and is crucial for the theory. It implies that the order of composition matters, which is a fundamental aspect of symmetry.

# Examples

**Example** (p. 33): $(12)(23) = (123)$ whereas $(23)(12) = (132)$.

# Relationships

## Builds Upon
- **Symmetric group** — Property of $S_n$

## Related
- **Cycle notation** — The computation uses cycle notation

# Common Errors

- **Error**: Forgetting that $S_1$ and $S_2$ are abelian.
  **Correction**: Non-abelianness requires $n \ge 3$.

# Common Confusions

- **Confusion**: Thinking that because disjoint cycles commute, $S_n$ might be abelian.
  **Clarification**: Disjoint cycles commute, but non-disjoint cycles generally do not.

# Source Reference

Chapter 6: Permutations, pages 33-34 (pdf pp. 33-34).

# Verification Notes

- Computation: Direct from pp. 33-34
- Confidence: HIGH — explicit computation
