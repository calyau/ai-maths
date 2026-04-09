---
# === CORE IDENTIFICATION ===
concept: Unsolvability of the Quintic
slug: galois-unsolvability

# === CLASSIFICATION ===
category: group-actions
subcategory: applications
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Groups Acting on Sets"
chapter_number: 4
pdf_page: 69
section: "Permutation groups"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - Abel-Ruffini theorem

# === TYPED RELATIONSHIPS ===
prerequisites:
  - simplicity-of-alternating-groups
  - solvable-group
extends: []
related:
  - alternating-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why can't the general quintic be solved by radicals?"
---

# Quick Definition

Since $A_n$ is simple for $n \geq 5$, the groups $S_n$ and $A_n$ are not solvable, which by Galois theory means the general polynomial of degree $\geq 5$ cannot be solved by radicals.

# Core Definition

"$A_n$ (also $S_n$) is not solvable if $n \geq 5$. ... In Galois theory, one attaches to $f$ a subgroup $G_f$ of the group of permutations of the roots of $f$, and shows that the roots of $f$ can be obtained from the coefficients by the algebraic operations of addition, subtraction, multiplication, division, and the extraction of $m$th roots if and only if $G_f$ is solvable" (Milne, Aside 4.39, p. 69).

# Prerequisites

- **Simplicity of alternating groups** — $A_n$ simple for $n \geq 5$
- **Solvable group** — The key property linking to radical solvability

# Key Properties

1. $A_n$ is not solvable for $n \geq 5$ (it is simple and non-abelian)
2. For every $n$, there exist polynomials of degree $n$ with $G_f \approx S_n$
3. Hence for $n \geq 5$, there exist polynomials not solvable by radicals

# Relationships

## Builds Upon
- **simplicity-of-alternating-groups**, **solvable-group**

# Source Reference

Chapter 4: Groups Acting on Sets, Aside 4.39, page 69.

# Verification Notes

- Definition source: Aside 4.39, p. 69
- Confidence: MEDIUM — briefly described as aside
- Uncertainties: Full Galois theory not developed in source
