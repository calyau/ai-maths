---
# === CORE IDENTIFICATION ===
concept: Permutation
slug: permutation

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
pdf_page: 22
section: "Cartesian Products and Mappings"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - bijection on a set

# === TYPED RELATIONSHIPS ===
prerequisites:
  - bijective-function
extends:
  - bijective-function
related:
  - symmetry
  - function-composition
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
  - "What is a permutation?"
  - "How is a permutation represented?"
---

# Quick Definition

A permutation of a set $S$ is a one-to-one and onto map $\pi : S \to S$. Permutations describe rearrangements of elements and form the basis of permutation groups.

# Core Definition

"For any set $S$, a one-to-one and onto mapping $\pi: S \to S$ is called a permutation of $S$" (Judson, p. 22). Permutations can be written using array notation, where the top row lists the elements and the bottom row shows their images. A set containing $n$ elements has $n!$ permutations. Permutations are further developed in Chapter 5.

# Prerequisites

- **Bijective function** — A permutation is a bijection from a set to itself

# Key Properties

1. A permutation is a function that is both one-to-one (injective) and onto (surjective)
2. The composition of two permutations is again a permutation
3. Every permutation has an inverse that is also a permutation
4. The identity function is a permutation
5. For a finite set with $n$ elements, there are exactly $n!$ permutations

# Construction / Recognition

## To Construct:
1. Start with a finite set $S = \{1, 2, \ldots, n\}$
2. Assign each element of $S$ to a unique image in $S$
3. Verify that every element of $S$ appears exactly once as an image

## To Recognize:
1. Check that the map is defined on all elements of $S$
2. Verify no two elements map to the same image (one-to-one)
3. Verify every element of $S$ is the image of some element (onto)

# Context & Application

Permutations are central to the study of geometric symmetries and to Galois theory, the study of finding solutions of polynomial equations. They also provide abundant examples of nonabelian groups. The six permutations of the vertices of an equilateral triangle correspond to its six symmetries.

# Examples

**Example 1** (p. 22): The permutation of $S = \{1, 2, 3\}$ given by $\pi(1) = 2$, $\pi(2) = 1$, $\pi(3) = 3$ is written:
$$\begin{pmatrix} 1 & 2 & 3 \\ 2 & 1 & 3 \end{pmatrix}$$

**Example 2** (p. 24): The permutation $\pi = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 3 & 1 \end{pmatrix}$ has inverse $\pi^{-1} = \begin{pmatrix} 1 & 2 & 3 \\ 3 & 1 & 2 \end{pmatrix}$.

# Relationships

## Builds Upon
- **bijective-function** — A permutation is a bijection from a set to itself

## Enables
- **symmetry** — Symmetries of figures correspond to permutations of vertices
- **group** — Permutations form groups under composition

## Related
- **function-composition** — Permutations compose under function composition

# Common Errors

- **Error**: Writing a permutation where two elements map to the same image
  **Correction**: Every image must appear exactly once; the function must be bijective

# Common Confusions

- **Confusion**: Thinking permutations must rearrange every element
  **Clarification**: A permutation can fix some elements (the identity fixes all elements)

- **Confusion**: Confusing permutations with combinations
  **Clarification**: A permutation is a rearrangement (order matters); a combination is a selection (order does not matter)

# Source Reference

Chapter 1: Preliminaries, Section 1.2, page 22. Also developed further in Chapter 5: Permutation Groups.

# Verification Notes

- Definition source: Direct from p. 22
- Confidence rationale: Explicit definition given in the text
- Uncertainties: None
- Cross-reference status: Verified
- Re-extracted to reference Ch. 1 where first introduced; Ch. 5 reference preserved
