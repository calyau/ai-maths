---
# === CORE IDENTIFICATION ===
concept: Nielsen-Schreier Theorem
slug: nielsen-schreier-theorem

# === CLASSIFICATION ===
category: algebraic-graph-theory
subcategory: free-group-theory
tier: advanced

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Graphs, Groups and Matrices"
chapter_number: 8
pdf_page: 265
section: "VIII.1 Cayley and Schreier Diagrams"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Nielsen-Schreier subgroup theorem"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - free-group
  - schreier-diagram
  - reidemeister-schreier-process
extends: []
related:
  - group-presentation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Are subgroups of free groups always free?"
---

# Quick Definition

A subgroup of a free group is free. If $A$ is free of rank $k$ and $B$ has index $n$, then $B$ has rank $(k-1)n + 1$.

# Core Definition

**Theorem 4** (Bollobas, p. 265): A subgroup of a free group is free. Furthermore, if $A$ is a free group of rank $k$ and $B$ is a subgroup of index $n$, then $B$ has rank $(k-1)n + 1$. The proof uses the Reidemeister-Schreier process: the presentation of $B$ given by Theorem 3 is a free presentation on the set of chords of the Schreier diagram, and there are $kn - (n-1) = (k-1)n + 1$ chords.

# Prerequisites

- **Free group** -- The ambient group
- **Schreier diagram** -- The tool for the proof
- **Reidemeister-Schreier process** -- The method for obtaining the presentation

# Key Properties

1. The rank formula $(k-1)n + 1$ is exact
2. The proof is constructive: free generators of $B$ correspond to chords of the Schreier diagram
3. The theorem implies the rank of a free group is well-defined (proven using the formula for index-2 subgroups)

# Construction / Recognition

## Proof Outline
1. Construct the Schreier diagram of $A$ mod $B$ (has $n$ vertices)
2. There are $kn$ edges total and $n-1$ tree edges
3. The $(k-1)n + 1$ chords freely generate $B$
4. The presentation of $B$ from Theorem 3 has no relations (since $A$ has none)

# Context & Application

This is a fundamental result in combinatorial group theory, beautifully proved using the graphical machinery of Schreier diagrams. It implies, for instance, that a subgroup of index 2 in a free group of rank 2 is free of rank 3.

# Examples

**Example** (p. 265): A free group of rank $k \ge 2$ has $2^k - 1$ subgroups of index 2, since there are $2^k$ regularly colored multigraphs of order 2, minus one disconnected one.

# Relationships

## Builds Upon
- **Free group** -- The ambient group
- **Schreier diagram** -- Tool for the proof
- **Reidemeister-Schreier process** -- Obtains the subgroup presentation

## Enables
- Well-definedness of the rank of a free group

## Related
- **Group presentation** -- Free presentations of subgroups

## Contrasts With
- None

# Common Errors

- **Error**: Applying the rank formula when the ambient group is not free
  **Correction**: The formula $(k-1)n+1$ only applies when the ambient group is free

# Common Confusions

- **Confusion**: Thinking a subgroup of a finitely generated free group must be finitely generated
  **Clarification**: This is true for finite-index subgroups, but infinite-index subgroups of $F_2$ can have infinite rank

# Source Reference

Chapter VIII: Graphs, Groups and Matrices, Section VIII.1, Theorem 4, page 265.

# Verification Notes

- Definition source: Direct from Theorem 4, p. 265
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
