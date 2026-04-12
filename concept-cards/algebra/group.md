---
concept: Group
slug: group
category: group-theory
subcategory: null
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Groups"
chapter_number: 2
pdf_page: 48
section: "2.2 Groups and Subgroups"
extraction_confidence: high
aliases: []
prerequisites:
  - law-of-composition
extends: []
related:
  - abelian-group
  - subgroup
  - order-of-a-group
  - general-linear-group
  - symmetric-group
contrasts_with: []
answers_questions:
  - "What is a group?"
  - "What distinguishes a group from a monoid?"
---

# Quick Definition

A group is a set G with an associative law of composition that has an identity element and in which every element has an inverse. If the law is also commutative, G is an abelian group.

# Core Definition

A group is a set G together with a law of composition that has the following properties (Artin, p. 52):
- Associativity: (ab)c = a(bc) for all a, b, c in G
- Identity: G contains an element 1 such that 1a = a and a1 = a for all a in G
- Inverses: Every element a of G has an inverse b such that ab = 1 and ba = 1

An abelian group is a group whose law of composition is commutative.

# Prerequisites

- **Law of composition** — A group has a specific law of composition

# Key Properties

1. The identity element is unique
2. The inverse of each element is unique
3. Cancellation law holds: ab = ac implies b = c (Proposition 2.2.3)
4. (ab)^(-1) = b^(-1)a^(-1) (inverses reverse order)
5. Powers a^n are well-defined for all integers n

# Construction / Recognition

## To Construct:
1. Define a set G and a law of composition
2. Verify associativity, existence of identity, and existence of inverses

## To Recognize:
1. A set with a binary operation satisfying the three group axioms

# Context & Application

Groups are the central algebraic structure studied throughout the book. They model symmetry, appear as matrix groups (GL_n), permutation groups (S_n), and in number theory (Z/nZ). Artin emphasizes concrete examples before abstraction.

# Examples

**Example 1** (p. 52): The set of nonzero real numbers under multiplication is an abelian group.

**Example 2** (p. 52): The general linear group GL_n of invertible n x n matrices under matrix multiplication is a non-abelian group (for n >= 2).

**Example 3** (p. 53): The symmetric group S_3, with generators x = (123) and y = (12), satisfying x^3 = 1, y^2 = 1, yx = x^2 y.

# Relationships

## Builds Upon
- **Law of composition** — Underlying operation

## Enables
- **Subgroup** — A subset that is itself a group
- **Homomorphism** — A structure-preserving map between groups
- **Coset** — Partitioning a group by a subgroup
- **Quotient group** — Group of cosets of a normal subgroup

## Related
- **Abelian group** — A commutative group
- **General linear group** — Group of invertible matrices
- **Symmetric group** — Group of permutations

# Common Errors

- **Error**: Assuming every group is abelian
  **Correction**: Many important groups (GL_n, S_n for n >= 3) are non-abelian

# Common Confusions

- **Confusion**: Confusing "group" with "set"
  **Clarification**: A group is a set PLUS a law of composition satisfying three axioms

- **Confusion**: Thinking a monoid (set with associative operation and identity) is automatically a group
  **Clarification**: A group also requires inverses for every element

# Source Reference

Chapter 2: Groups, Section 2.2, pages 52-54.

# Verification Notes

- Definition source: Direct from Section 2.2, p. 52
- Confidence rationale: The central definition of the chapter
- Uncertainties: None
- Cross-reference status: Verified
