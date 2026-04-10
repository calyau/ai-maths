---
# === CORE IDENTIFICATION ===
concept: "Prüfer Code"
slug: prufer-code

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
  - Prufer sequence
  - Prufer encoding

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - cayley-formula-trees
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How are labelled trees enumerated?"
---

# Quick Definition

The Prufer code is a bijection between labelled trees on $n$ vertices and sequences of length $n-2$ from $\{1, \ldots, n\}$, proving there are $n^{n-2}$ labelled trees.

# Core Definition

Given a tree $T$ on $V = \{1, \ldots, n\}$, associate a code as follows: repeatedly remove the endvertex with the smallest label and record the label of the adjacent vertex, until only two vertices remain. The resulting sequence of length $n-2$ is the Prufer code. Each of the $n^{n-2}$ possible codes corresponds to a unique tree. A vertex of degree $d$ appears exactly $d-1$ times in the code (Bollobas, pp. 283--284).

# Prerequisites

This is a foundational combinatorial tool with no prerequisites within this source.

# Key Properties

1. Bijection between trees on $[n]$ and sequences in $[n]^{n-2}$
2. A vertex of degree $d$ appears $d-1$ times in the code
3. Immediately proves Cayley's formula: $n^{n-2}$ labelled trees
4. Yields the multinomial count for trees with prescribed degree sequence

# Construction / Recognition

## To Encode a Tree
1. Find the endvertex with the smallest label
2. Record the label of its neighbor
3. Remove the endvertex
4. Repeat until 2 vertices remain

## To Decode a Sequence
1. Given sequence $(a_1, \ldots, a_{n-2})$, the leaves are vertices not in the sequence
2. Connect the smallest leaf to $a_1$, remove the leaf and $a_1$
3. Continue until two vertices remain; connect them

# Context & Application

The Prufer code gives a constructive proof of Cayley's formula that is independent of the matrix tree theorem. It also yields Corollary 21 on the number of trees with a prescribed degree sequence.

# Examples

**Example** (p. 283, Fig. VIII.12): A specific tree on 11 vertices has Prufer code $(3, 8, 11, 8, 5, 8, 3, 5, 3)$.

# Relationships

## Builds Upon
- No prerequisites

## Enables
- **Cayley's formula for trees** -- Immediate corollary

## Related
- **Cayley's formula for trees** -- The enumeration result

## Contrasts With
- None

# Common Errors

- **Error**: Including the last two vertices in the code
  **Correction**: Stop when 2 vertices remain; the code has length $n-2$

# Common Confusions

- **Confusion**: Thinking the Prufer code preserves graph structure obviously
  **Clarification**: The bijection is not structure-preserving in an obvious way; it cleverly encodes adjacency through the removal sequence

# Source Reference

Chapter VIII, Section VIII.4, Theorem 20, pages 283--284.

# Verification Notes

- Definition source: Direct from pp. 283--284
- Confidence rationale: Explicit algorithm with example
- Uncertainties: None
- Cross-reference status: Verified
