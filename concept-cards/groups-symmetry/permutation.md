---
# === CORE IDENTIFICATION ===
concept: Permutation
slug: permutation

# === CLASSIFICATION ===
category: permutation-groups
subcategory: definitions
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
aliases:
  - "bijection of a set"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - symmetric-group
  - cycle-notation
  - transposition
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a permutation?"
  - "How is a permutation defined mathematically?"
---

# Quick Definition

A permutation of a set $X$ is a bijection from $X$ to itself. Permutations compose to form groups under function composition.

# Core Definition

"By a **permutation** of an arbitrary set $X$ we shall mean a bijection from $X$ to itself" (Armstrong, p. 33). The collection of all permutations of $X$ forms a group $S_X$ under composition of functions. If $\alpha: X \to X$ and $\beta: X \to X$ are permutations, the composite $\alpha\beta: X \to X$ defined by $\alpha\beta(x) = \alpha(\beta(x))$ is also a permutation. The identity permutation $\varepsilon$ leaves every point of $X$ fixed, and each permutation $\alpha$ has an inverse $\alpha^{-1}$.

# Prerequisites

- **Bijection** — A permutation is defined as a bijection from a set to itself
- **Function composition** — The group operation on permutations is composition
- **Group axioms** — Understanding that permutations form a group requires knowing the group axioms

# Key Properties

1. A permutation is a bijection (both injective and surjective) from a set to itself
2. Composition of two permutations is again a permutation
3. Composition of functions is associative
4. The identity permutation $\varepsilon$ fixes every element
5. Every permutation has an inverse that is also a permutation
6. If $X$ is infinite, $S_X$ is an infinite group

# Construction / Recognition

## To Construct:
1. Choose a set $X$
2. Define a bijection $\alpha: X \to X$ (specifying where each element is sent)
3. Verify bijectivity (each element has exactly one preimage)

## To Recognize:
1. Check that the function maps a set to itself
2. Verify injectivity (distinct inputs give distinct outputs)
3. Verify surjectivity (every element is in the range)

# Context & Application

Permutations are fundamental in group theory because every group is isomorphic to a group of permutations (Cayley's theorem). They provide concrete, computable examples of groups and arise naturally when studying symmetries of geometric objects — each symmetry permutes the parts of the object.

# Examples

**Example** (p. 33): Interchanging 1 and 3 while leaving 2 fixed gives a permutation of $\{1, 2, 3\}$.

**Example** (p. 33): The two-row notation for an element of $S_6$:
$$\alpha = \begin{bmatrix} 123456 \\ 543612 \end{bmatrix}$$
sends 1 to 5, 2 to 4, 3 to 3, 4 to 6, 5 to 1, and 6 to 2.

# Relationships

## Enables
- **Symmetric group** — The collection of all permutations of a set forms the symmetric group
- **Cycle notation** — Permutations can be decomposed into cyclic permutations
- **Alternating group** — Even permutations form a subgroup

## Related
- **Transposition** — A permutation that swaps exactly two elements
- **Cayley's theorem** — Every group is isomorphic to a group of permutations

# Common Errors

- **Error**: Writing $\alpha\beta$ and applying $\alpha$ first, then $\beta$.
  **Correction**: Armstrong's convention is $\alpha\beta(x) = \alpha(\beta(x))$, meaning $\beta$ is applied first, then $\alpha$.

# Common Confusions

- **Confusion**: Thinking a permutation must rearrange every element.
  **Clarification**: A permutation may fix some or all elements. The identity permutation fixes everything and is still a valid permutation.

- **Confusion**: Believing permutations only apply to finite sets.
  **Clarification**: Permutations are defined for arbitrary sets, including infinite ones. When $X$ is infinite, $S_X$ is an infinite group.

# Source Reference

Chapter 6: Permutations, pages 33-38 (pdf pp. 33-38). Opening paragraphs define permutation and the group $S_X$.

# Verification Notes

- Definition: Direct quote from p. 33
- Key Properties: All explicit in the opening paragraph
- Confidence: HIGH — explicit definition with clear terminology
- Cross-references: All slugs verified against planned extractions
