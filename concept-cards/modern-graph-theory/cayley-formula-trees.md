---
# === CORE IDENTIFICATION ===
concept: Cayley's Formula for Trees
slug: cayley-formula-trees

# === CLASSIFICATION ===
category: graph-enumeration
subcategory: tree-enumeration
tier: intermediate

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Graphs, Groups and Matrices"
chapter_number: 8
pdf_page: 283
section: "VIII.4 Enumeration and Pólya's Theorem"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Cayley's tree formula

# === TYPED RELATIONSHIPS ===
prerequisites:
  - prufer-code
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How many labelled trees are there on n vertices?"
---

# Quick Definition

There are $n^{n-2}$ labelled trees on $n$ vertices, as proved by the Prufer code bijection.

# Core Definition

**Theorem 20** (Bollobas, p. 283): There are $n^{n-2}$ trees on $n$ labelled vertices. The proof via Prufer codes establishes a bijection between labelled trees and sequences in $[n]^{n-2}$. **Corollary 21**: The number of labelled trees with degree sequence $(d_1, \ldots, d_n)$ is $\binom{n-2}{d_1-1, d_2-1, \ldots, d_n-1}$.

# Prerequisites

- **Prufer code** -- The proof tool

# Key Properties

1. $n^{n-2}$ labelled trees on $n$ vertices
2. Trees with prescribed degree sequence: multinomial coefficient
3. Originally proved by Cayley; this proof due to Prufer
4. Also provable via the matrix tree theorem (Corollary II.13)

# Construction / Recognition

Not applicable -- this is an enumeration result.

# Context & Application

Cayley's formula is a foundational result in graph enumeration. It appears in random graph theory (counting spanning trees) and algebraic combinatorics.

# Examples

**Example**: For $n = 4$: $4^2 = 16$ labelled trees. For $n = 3$: $3^1 = 3$ labelled trees (the three edges of $K_3$).

# Relationships

## Builds Upon
- **Prufer code** -- Proof technique

## Enables
- Tree enumeration in random graph theory

## Related
- None

## Contrasts With
- None

# Common Errors

- **Error**: Confusing labelled and unlabelled tree counts
  **Correction**: $n^{n-2}$ counts labelled trees; the number of unlabelled trees is much smaller

# Common Confusions

- **Confusion**: Thinking the formula applies to forests
  **Clarification**: The formula counts trees (connected acyclic graphs), not forests

# Source Reference

Chapter VIII, Section VIII.4, Theorem 20 and Corollary 21, pages 283--284.

# Verification Notes

- Definition source: Direct from Theorem 20
- Confidence rationale: Explicit theorem
- Uncertainties: None
- Cross-reference status: Verified
