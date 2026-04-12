---
concept: Span
slug: span
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
  - "Span S"
  - "linear span"
prerequisites:
  - vector-space
  - linear-combination
extends: []
related:
  - linear-independence
  - basis
  - subspace
contrasts_with:
  - linear-independence
answers_questions:
  - "What distinguishes linear independence from spanning?"
---

# Quick Definition

The span of a set of vectors S = (v_1, ..., v_n) is the set of all linear combinations c_1 v_1 + ... + c_n v_n. It is the smallest subspace containing all vectors in S.

# Core Definition

The set of all vectors that are linear combinations of S = (v_1, ..., v_n) forms a subspace called the span of S, denoted Span S (Artin, p. 99). It is the smallest subspace containing S (Lemma 3.4.5).

# Prerequisites

- **Vector space** — Vectors live in a vector space
- **Linear combination** — Span consists of all linear combinations

# Key Properties

1. Span S is always a subspace
2. Span S is the smallest subspace containing all vectors of S
3. V = Span S means S spans V (every vector is a combination of S)
4. dim(Span S) <= number of vectors in S

# Construction / Recognition

## To Construct:
1. Form all linear combinations c_1 v_1 + ... + c_n v_n with arbitrary scalars c_i

## To Recognize:
1. Every vector in the set can be written as a combination of S

# Context & Application

Spanning and independence are the two properties that define a basis. A set spans V if every vector can be expressed using the set; it is independent if no vector in the set is redundant.

# Examples

**Example 1** (p. 99): The span of a single nonzero vector v is the line {cv : c in F}.

**Example 2** (p. 99): Span{(1,0,1)^t, (1,2,0)^t} is the 2-dimensional solution space of 2x_1 - x_2 - 2x_3 = 0.

# Relationships

## Builds Upon
- **Linear combination** — Span = set of all linear combinations

## Enables
- **Basis** — A spanning independent set

## Contrasts With
- **Linear independence** — Independence means no redundancy; spanning means completeness

# Common Errors

- **Error**: Thinking span includes only the vectors themselves
  **Correction**: Span includes ALL linear combinations, not just the original vectors

# Common Confusions

- **Confusion**: Confusing "S spans V" with "S is a basis of V"
  **Clarification**: S spans V means every vector is a combination; S is a basis only if it also is independent

# Source Reference

Chapter 3: Vector Spaces, Section 3.4, page 99.

# Verification Notes

- Definition source: Direct from p. 99
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
