---
concept: Invariant Factors
slug: invariant-factors
category: module-theory
subcategory: classification
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Linear Algebra in a Ring"
chapter_number: 14
pdf_page: 432
section: "14.7 Structure of Abelian Groups"
extraction_confidence: high
aliases: []
prerequisites:
  - structure-theorem-finitely-generated-modules-pid
  - smith-normal-form
extends: []
related:
  - elementary-divisors
contrasts_with:
  - elementary-divisors
answers_questions:
  - "What are invariant factors?"
---

# Quick Definition

The invariant factors of a finitely generated module over a PID are the diagonal entries d_1, ..., d_k (with d_1 | d_2 | ... | d_k) appearing in the Smith normal form of its presentation matrix. They uniquely determine the module up to isomorphism.

# Core Definition

In the structure theorem decomposition V = R/(d_1) + ... + R/(d_k) + L, the elements d_1, ..., d_k with d_1 | d_2 | ... | d_k are called the invariant factors of V. They are the nonunit diagonal entries of the Smith normal form of any presentation matrix for V, and they are uniquely determined by V (Artin, Theorem 14.7.7 for the Z case).

# Prerequisites

- **Structure theorem for finitely generated modules over a PID** -- Invariant factors arise from this theorem
- **Smith normal form** -- Computational method for finding invariant factors

# Key Properties

1. Each invariant factor divides the next: d_1 | d_2 | ... | d_k
2. The invariant factors are uniquely determined by the module
3. Two finitely generated modules are isomorphic iff they have the same invariant factors and the same free rank

# Context & Application

Invariant factors provide a complete set of isomorphism invariants for finitely generated modules over PIDs. For abelian groups, they determine the group up to isomorphism.

# Examples

**Example 1** (p. 443): For an abelian group of order 12 with invariant factors (2, 6), V = C_2 + C_6.

# Relationships

## Builds Upon
- **Structure theorem for finitely generated modules over a PID** -- Source of invariant factors

## Contrasts With
- **Elementary divisors** -- An alternate, finer decomposition into prime powers

# Source Reference

Chapter 14: Linear Algebra in a Ring, Section 14.7, pages 443-448.

# Verification Notes

- Definition source: Synthesized from Artin's treatment
- Confidence rationale: Clearly defined through the structure theorem
- Uncertainties: None
- Cross-reference status: Verified
