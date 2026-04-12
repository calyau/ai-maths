---
concept: Rational Canonical Form
slug: rational-canonical-form
category: module-theory
subcategory: linear-operators
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Linear Algebra in a Ring"
chapter_number: 14
pdf_page: 432
section: "14.8 Application to Linear Operators"
extraction_confidence: high
aliases:
  - "rational form"
prerequisites:
  - structure-theorem-finitely-generated-modules-pid
  - linear-operator
extends: []
related:
  - jordan-canonical-form
  - companion-matrix
contrasts_with:
  - jordan-canonical-form
answers_questions:
  - "What is the rational canonical form?"
  - "How does the structure theorem apply to linear operators?"
---

# Quick Definition

The rational canonical form is a block diagonal matrix representation of a linear operator, where each block is a companion matrix corresponding to a cyclic F[t]-module. It is the best available canonical form over an arbitrary field.

# Core Definition

Let T: V -> V be a linear operator on a finite-dimensional vector space over F. By viewing V as an F[t]-module via the action f(t)v = f(T)(v) (Artin, equation 14.8.6), the structure theorem decomposes V into a direct sum of cyclic F[t]-submodules. Choosing appropriate bases, the matrix of T has block diagonal form where each block is a companion matrix (Theorem 14.8.11). The characteristic polynomial of each companion matrix is the corresponding invariant factor.

# Prerequisites

- **Structure theorem for finitely generated modules over a PID** -- Provides the decomposition
- **Linear operator** -- The rational canonical form represents an operator

# Key Properties

1. Linear operator on F-vector space and F[t]-module are equivalent concepts (14.8.9)
2. The companion matrix for f(t) = t^n + a_{n-1}t^{n-1} + ... + a_0 has 1s below the diagonal and -a_i in the last column
3. The characteristic polynomial of the companion matrix is f(t)
4. For finite-dimensional V, the free summand is zero
5. The rational canonical form works over any field

# Context & Application

The rational canonical form demonstrates the power of abstract algebra: the structure theorem for modules, applied to F[t]-modules, yields a canonical form for linear operators. This is the best available form over an arbitrary field; over an algebraically closed field, it can be refined to Jordan canonical form.

# Examples

**Example 1** (p. 455): A matrix in rational canonical form for t^3 - 1 is the permutation matrix [[0,0,1],[1,0,0],[0,1,0]]. Since t^3 - 1 = (t-1)(t^2+t+1), this decomposes further into blocks [[1]] and [[0,-1],[1,-1]] (14.8.13).

# Relationships

## Builds Upon
- **Structure theorem for finitely generated modules over a PID** -- Applied to F[t]-modules

## Related
- **Jordan canonical form** -- A refinement over algebraically closed fields
- **Companion matrix** -- The building blocks of rational canonical form

# Source Reference

Chapter 14: Linear Algebra in a Ring, Section 14.8, pages 449-457. Theorem 14.8.11.

# Verification Notes

- Definition source: Direct from Artin, Theorem 14.8.11
- Confidence rationale: Complete treatment with examples
- Uncertainties: None
- Cross-reference status: Verified
