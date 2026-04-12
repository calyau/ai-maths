---
concept: Permutation
slug: permutation
category: matrices
subcategory: null
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Matrices"
chapter_number: 1
pdf_page: 12
section: "1.5 Permutations"
extraction_confidence: high
aliases:
  - "bijection"
prerequisites: []
extends: []
related:
  - sign-of-a-permutation
  - transposition
  - permutation-matrix
  - symmetric-group
contrasts_with: []
answers_questions:
  - "What is a permutation?"
---

# Quick Definition

A permutation of a set S is a bijective map from S to itself. Permutations of {1, ..., n} can be written in cycle notation such as (341)(25), and composed by performing one after the other.

# Core Definition

A permutation of a set S is a bijective map p: S -> S (Artin, p. 29, formula 1.5.1). The set of all permutations of {1, ..., n} is the symmetric group S_n. Permutations are composed as functions: qp means "first p, then q." Cycle notation groups indices into orbits: (341) means 3->4, 4->1, 1->3 (Artin, pp. 29-31).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Composition of permutations is associative but not commutative
2. Every permutation can be decomposed into disjoint cycles
3. Every permutation can be written as a product of transpositions
4. The cycle notation is not unique (cycles can be rotated, order of disjoint cycles can change)

# Construction / Recognition

## To Construct:
1. Define where each element of {1,...,n} is sent
2. Write as a product of disjoint cycles by following orbits

## To Recognize:
1. A rearrangement of a finite set
2. In cycle notation: parenthesized groups of indices

# Context & Application

Permutations are essential to the theory of determinants (the complete expansion formula sums over all permutations) and provide the first important family of groups (symmetric groups). Artin carefully distinguishes permutations as functions from permutations as lists.

# Examples

**Example 1** (p. 30): The permutation p with p(1)=3, p(2)=5, p(3)=4, p(4)=1, p(5)=2 is written (341)(25) in cycle notation.

**Example 2** (p. 31): Composing q = (1452) and p = (341)(25): qp = (135).

# Relationships

## Enables
- **Symmetric group** — The group of all permutations of n indices
- **Sign of a permutation** — Even or odd classification
- **Determinant** — Complete expansion sums over permutations

## Related
- **Transposition** — A 2-cycle; the simplest nontrivial permutation
- **Permutation matrix** — Matrix representation of a permutation

# Common Errors

- **Error**: Reading cycle notation left-to-right for composition
  **Correction**: qp means first apply p, then q (right to left)

# Common Confusions

- **Confusion**: Thinking cycle notation (341) and (134) are different permutations
  **Clarification**: They are the same cycle, just starting at a different index

# Source Reference

Chapter 1: Matrices, Section 1.5, pages 29-33.

# Verification Notes

- Definition source: Direct from (1.5.1), p. 29
- Confidence rationale: Extensively developed with notation and examples
- Uncertainties: None
- Cross-reference status: Verified
