---
concept: Vector Space
slug: vector-space
category: linear-algebra
subcategory: null
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Vector Spaces"
chapter_number: 3
pdf_page: 89
section: "3.3 Vector Spaces"
extraction_confidence: high
aliases: []
prerequisites:
  - field
  - abelian-group
extends: []
related:
  - subspace
  - basis
  - dimension
  - linear-transformation
contrasts_with: []
answers_questions:
  - "What is a vector space?"
---

# Quick Definition

A vector space V over a field F is a set with two operations — vector addition and scalar multiplication — satisfying axioms that generalize the properties of R^n. Elements of V are vectors; elements of F are scalars.

# Core Definition

A vector space V over a field F is a set with addition (V x V -> V) and scalar multiplication (F x V -> V) satisfying (Definition 3.3.1, Artin, p. 97):
- Addition makes V into an abelian group V+
- 1v = v for all v
- (ab)v = a(bv) (associative law for scalars)
- (a+b)v = av + bv and a(v+w) = av + aw (distributive laws)

# Prerequisites

- **Field** — Scalars come from a field
- **Abelian group** — V is an abelian group under addition

# Key Properties

1. F^n (column vectors) is the standard example
2. Every finite-dimensional vector space of dimension n is isomorphic to F^n
3. Subspaces are subsets closed under addition and scalar multiplication
4. Every vector space has a basis

# Construction / Recognition

## To Construct:
1. Define a set V with addition and scalar multiplication over a field F
2. Verify the vector space axioms

## To Recognize:
1. A set with addition (abelian group) and scalar multiplication satisfying the axioms

# Context & Application

Vector spaces are the central objects of linear algebra. They provide the framework for linear equations, linear transformations, eigenvalues, and much more. Artin emphasizes the abstract definition to allow working over any field.

# Examples

**Example 1** (p. 97): F^n (column vectors) with standard operations.

**Example 2** (p. 97): C viewed as a real vector space (forget complex multiplication, keep real scalar multiplication).

**Example 3** (p. 97): The space of real polynomials p(x) = a_n x^n + ... + a_0.

**Example 4** (p. 97): The set of solutions of the differential equation y'' = -y.

# Relationships

## Builds Upon
- **Field** — Scalars form a field

## Enables
- **Subspace** — Vector subspace
- **Basis** — A spanning independent set
- **Dimension** — Number of basis vectors
- **Linear transformation** — Structure-preserving maps between vector spaces

# Common Errors

- **Error**: Forgetting that the zero vector must be in every subspace
  **Correction**: A subspace must contain 0 (or equivalently, be nonempty and closed)

# Common Confusions

- **Confusion**: Thinking vectors must be "arrows" or tuples of numbers
  **Clarification**: Vectors can be polynomials, functions, matrices, etc.

# Source Reference

Chapter 3: Vector Spaces, Section 3.3, pages 97-98.

# Verification Notes

- Definition source: Direct from Definition 3.3.1, p. 97
- Confidence rationale: Central definition of the chapter
- Uncertainties: None
- Cross-reference status: Verified
