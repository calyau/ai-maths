---
concept: Norm of an Ideal
slug: norm-of-an-ideal
category: number-theory
subcategory: ideal-theory
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Quadratic Number Fields"
chapter_number: 13
pdf_page: 394
section: "Ideal Classes"
extraction_confidence: high
aliases:
  - "N(A)"
prerequisites:
  - ideal-multiplication
  - main-lemma
extends: []
related:
  - norm-quadratic-field
  - class-group
contrasts_with: []
answers_questions:
  - "What is the norm of an ideal?"
---

# Quick Definition

The norm N(A) of a nonzero ideal A is the positive integer n such that A*A-bar = (n). It equals the index [R:A] and is multiplicative: N(AB) = N(A)N(B).

# Core Definition

The norm of a nonzero ideal A is defined as N(A) = n, where n is the positive integer such that A-bar * A = (n) (Artin, formula 13.7.5, p. 412). The norm equals the index [R:A] (Theorem 13.7.8(a)) and is multiplicative: N(AB) = N(A)N(B) (Lemma 13.7.6).

# Prerequisites

- **Ideal multiplication** -- N(A) is defined via A*A-bar
- **Main Lemma** -- Guarantees A*A-bar is principal

# Key Properties

1. N(A) = [R:A] (the number of cosets)
2. N(AB) = N(A)N(B) (multiplicative)
3. For a principal ideal (alpha), N((alpha)) = N(alpha) (the element norm)
4. N(A) = Delta(A)/Delta(R) where Delta is lattice area

# Examples

**Example 1** (p. 412): In Z[sqrt(-5)], N((2, 1+delta)) = 2 since A*A-bar = (2).

# Relationships

## Builds Upon
- **Main Lemma** -- Defines A*A-bar = (n)
- **Ideal multiplication** -- Uses products of ideals

## Related
- **Norm (quadratic field)** -- Element norm and ideal norm agree for principal ideals

# Source Reference

Chapter 13: Quadratic Number Fields, Section 13.7, formula 13.7.5, Theorem 13.7.8, pages 412-414.

# Verification Notes

- Definition source: Direct from formula 13.7.5
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
