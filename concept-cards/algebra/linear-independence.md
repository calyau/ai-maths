---
concept: Linear Independence
slug: linear-independence
category: linear-algebra
subcategory: null
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Vector Spaces"
chapter_number: 3
pdf_page: 89
section: "3.4 Bases and Dimension"
extraction_confidence: high
aliases:
  - "independent"
  - "linearly independent"
prerequisites:
  - vector-space
  - linear-combination
extends: []
related:
  - basis
  - span
contrasts_with:
  - span
answers_questions:
  - "What distinguishes linear independence from spanning?"
---

# Quick Definition

An ordered set of vectors S = (v_1, ..., v_n) is linearly independent if the only solution to v_1 x_1 + ... + v_n x_n = 0 is x_1 = ... = x_n = 0. A set that is not independent is dependent.

# Core Definition

An ordered set S = (v_1, ..., v_n) is independent (or linearly independent) if there is no linear relation SX = 0 except the trivial one X = 0, i.e., the only solution to v_1 x_1 + ... + v_n x_n = 0 has all x_i = 0 (Definition 3.4.8, Artin, p. 99).

# Prerequisites

- **Vector space** — Vectors live in a vector space
- **Linear combination** — Independence is about linear relations

# Key Properties

1. No vector in an independent set is zero
2. No vector in an independent set is repeated
3. Any subset of an independent set is independent
4. An independent set has at most dim(V) elements (Theorem 3.4.18)
5. For F^n: check independence by row-reducing the matrix of column vectors

# Construction / Recognition

## To Construct:
1. Start with one nonzero vector; it is independent
2. Add vectors one at a time, checking that each is not in the span of the previous ones

## To Recognize:
1. The equation v_1 x_1 + ... + v_n x_n = 0 has only the trivial solution
2. For column vectors: the matrix with these vectors as columns has only the trivial null space

# Context & Application

Linear independence, together with spanning, defines a basis. Independence means no vector is redundant; each contributes essential information. Testing independence reduces to solving a homogeneous system.

# Examples

**Example 1** (p. 99): (v_1, v_2, v_3) in R^3 with coordinate vectors [1,0,1]^t, [1,2,0]^t, [2,1,2]^t is dependent (the 3x3 matrix of column vectors has a nontrivial null space).

**Example 2** (p. 99): The first three columns of the same matrix form a 3x3 matrix with det = 1, so (v_1, v_2, v_3) with those three vectors is independent.

# Relationships

## Builds Upon
- **Linear combination** — Independence means no nontrivial linear relation

## Enables
- **Basis** — A basis is an independent spanning set

## Contrasts With
- **Span** — Spanning means every vector is reachable; independence means no redundancy

# Common Errors

- **Error**: Confusing independent with orthogonal
  **Correction**: Orthogonal vectors are independent, but independent vectors need not be orthogonal

# Common Confusions

- **Confusion**: Thinking linear independence depends on the order of vectors
  **Clarification**: Any reordering of an independent set is independent

# Source Reference

Chapter 3: Vector Spaces, Section 3.4, pages 99-100.

# Verification Notes

- Definition source: Direct from Definition 3.4.8, p. 99
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
