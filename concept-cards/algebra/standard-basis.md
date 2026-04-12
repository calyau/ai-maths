---
concept: Standard Basis
slug: standard-basis
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
  - "E"
  - "e_1, ..., e_n"
prerequisites:
  - basis
  - column-vector
extends:
  - basis
related:
  - coordinates
  - change-of-basis
contrasts_with: []
answers_questions:
  - "What is a basis and what is dimension?"
---

# Quick Definition

The standard basis of F^n is E = (e_1, ..., e_n), where e_i is the column vector with 1 in position i and 0 elsewhere. Every vector X = (x_1, ..., x_n)^t can be written as X = x_1 e_1 + ... + x_n e_n.

# Core Definition

The column vector e_i has a single nonzero entry 1 in position i. The set E = (e_1, ..., e_n) is a basis for F^n called the standard basis. If X is a column vector with entries (x_1, ..., x_n), then X = x_1 e_1 + ... + x_n e_n (Artin, p. 100, referencing (1.1.24)).

# Prerequisites

- **Basis** — The standard basis is a specific basis
- **Column vector** — The basis vectors are column vectors

# Key Properties

1. n elements, each an n x 1 column vector
2. e_i has 1 in position i and 0 elsewhere
3. X = sum of x_i e_i (decomposition of any vector)
4. The coordinates of X with respect to E are just the entries of X

# Construction / Recognition

## To Construct:
1. e_i = (0, ..., 0, 1, 0, ..., 0)^t with 1 in position i

## To Recognize:
1. The "natural" basis of F^n with no preferred structure

# Context & Application

The standard basis is the default basis for F^n. When a linear operator on F^n is given, its matrix with respect to the standard basis is the matrix itself (no basis change needed).

# Examples

**Example 1** (p. 100): E = (e_1, e_2, e_3) for R^3: e_1 = (1,0,0)^t, e_2 = (0,1,0)^t, e_3 = (0,0,1)^t.

# Relationships

## Builds Upon
- **Basis** — The standard basis is a specific basis

## Enables
- **Coordinates** — In the standard basis, coordinates = entries
- **Change of basis** — Other bases are related to E by the matrix [B]

# Common Errors

- **Error**: Assuming the standard basis is always the best choice
  **Correction**: A basis of eigenvectors may be much more useful for a given operator

# Common Confusions

- **Confusion**: Thinking every vector space has a "standard basis"
  **Clarification**: Only F^n has a canonical standard basis; abstract vector spaces don't

# Source Reference

Chapter 3: Vector Spaces, Section 3.4, page 100.

# Verification Notes

- Definition source: From (1.1.24) and Section 3.4
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
