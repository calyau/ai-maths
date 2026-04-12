---
concept: Linear Combination
slug: linear-combination
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
aliases: []
prerequisites:
  - vector-space
extends: []
related:
  - span
  - linear-independence
  - basis
contrasts_with: []
answers_questions:
  - "What is a vector space?"
---

# Quick Definition

A linear combination of vectors v_1, ..., v_n is a vector of the form w = c_1 v_1 + ... + c_n v_n, where c_i are scalars from the field F.

# Core Definition

Let V be a vector space over a field F, and let S = (v_1, ..., v_n) be an ordered set of elements of V. A linear combination of S is a vector w = c_1 v_1 + ... + c_n v_n with c_i in F (Artin, p. 98, formula 3.4.1). In matrix notation, SX = (v_1, ..., v_n)[x_1, ..., x_n]^t.

# Prerequisites

- **Vector space** — Linear combinations use vector addition and scalar multiplication

# Key Properties

1. The set of all linear combinations of S is the span of S
2. A linear relation is a combination that equals 0
3. Every vector in a vector space is a combination of a basis

# Construction / Recognition

## To Construct:
1. Choose scalars c_1, ..., c_n
2. Compute c_1 v_1 + ... + c_n v_n

## To Recognize:
1. Any expression of the form sum of scalar times vector

# Context & Application

Linear combinations are the fundamental operation in linear algebra. Span, independence, and basis are all defined in terms of linear combinations.

# Examples

**Example 1** (p. 98): w_1 y_1 + w_2 y_2 = [y_1 + y_2, 2y_2, y_1]^t for specific basis vectors w_1, w_2 of a solution space.

# Relationships

## Builds Upon
- **Vector space** — Uses its two operations

## Enables
- **Span** — Set of all linear combinations
- **Linear independence** — No nontrivial combination equals 0
- **Basis** — Independent spanning set

# Common Errors

- **Error**: Forgetting that coefficients must come from the field
  **Correction**: Scalars must be elements of F, not just integers

# Common Confusions

- **Confusion**: Thinking linear combination includes infinite sums
  **Clarification**: In algebra, linear combinations are always finite

# Source Reference

Chapter 3: Vector Spaces, Section 3.4, page 98.

# Verification Notes

- Definition source: Direct from (3.4.1), p. 98
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
