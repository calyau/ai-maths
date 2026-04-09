---
# === CORE IDENTIFICATION ===
concept: Right Coset
slug: right-coset

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
pdf_page: 87
section: "6.1 Cosets"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - left-coset
extends: []
related:
  - index-of-a-subgroup
  - lagranges-theorem
contrasts_with:
  - left-coset

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a right coset?"
  - "When do left and right cosets coincide?"
---

# Quick Definition

A right coset of a subgroup $H$ in $G$ with representative $g \in G$ is the set $Hg = \{hg : h \in H\}$. Right cosets also partition $G$ and have the same number as left cosets.

# Core Definition

"*Right cosets* can be defined similarly by $Hg = \{hg : h \in H\}$" (Judson, p. 87). Right cosets also partition $G$ (Remark 6.5), and the number of right cosets equals the number of left cosets (Theorem 6.8).

# Prerequisites

- **Left Coset** — Right cosets are the mirror concept

# Key Properties

1. Right cosets partition $G$ (Remark 6.5)
2. The number of right cosets equals the number of left cosets (Theorem 6.8)
3. In a commutative group, left and right cosets are always identical
4. Left and right cosets coincide for all $g$ if and only if $H$ is a normal subgroup

# Construction / Recognition

## To Compute:
1. For each $g \in G$, compute $Hg = \{hg : h \in H\}$
2. Multiply each element of $H$ on the right by $g$

# Context & Application

Right cosets are used alongside left cosets. When left and right cosets coincide (normal subgroups), the cosets form a group under coset multiplication (quotient group).

# Examples

**Example 1** (p. 88): For $K = \{(1), (12)\}$ in $S_3$, the right cosets are $K(1) = K(12) = \{(1), (12)\}$, $K(13) = K(132) = \{(13), (132)\}$, $K(23) = K(123) = \{(23), (123)\}$. Note that the left coset $(13)K = \{(13), (123)\}$ differs from $K(13) = \{(13), (132)\}$.

# Relationships

## Builds Upon
- **Left Coset** — Right cosets are the counterpart with multiplication on the right

## Related
- **Normal Subgroup** — A subgroup is normal iff left and right cosets coincide

## Contrasts With
- **Left Coset** — Left multiplication vs. right multiplication

# Common Errors

- **Error**: Assuming $gH = Hg$ for all subgroups
  **Correction**: This holds only for normal subgroups

# Common Confusions

- **Confusion**: Thinking there are more right cosets than left cosets (or vice versa)
  **Clarification**: The number of left and right cosets is always the same (Theorem 6.8)

# Source Reference

Chapter 6: Cosets and Lagrange's Theorem, Section 6.1, pages 87-89, Theorem 6.8.

# Verification Notes

- Definition source: Direct from p. 87
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
