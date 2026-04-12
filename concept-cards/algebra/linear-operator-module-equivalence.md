---
concept: Linear Operator and Module Equivalence
slug: linear-operator-module-equivalence
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
aliases: []
prerequisites:
  - module
  - linear-operator
extends: []
related:
  - rational-canonical-form
  - structure-theorem-finitely-generated-modules-pid
contrasts_with: []
answers_questions:
  - "How are linear operators related to modules?"
---

# Quick Definition

A linear operator T: V -> V on an F-vector space is equivalent to an F[t]-module structure on V, where t acts as T. This equivalence connects the structure theorem for F[t]-modules to canonical forms for linear operators.

# Core Definition

Given a linear operator T: V -> V on a vector space over F, one makes V into an F[t]-module by defining f(t)v = f(T)(v) (Artin, equation 14.8.6). In particular, tv = T(v). Conversely, any F[t]-module gives a linear operator by multiplication by t. These are inverse operations (14.8.9): "Linear operator on an F-vector space and F[t]-module are equivalent concepts."

# Prerequisites

- **Module** -- V becomes an F[t]-module
- **Linear operator** -- T provides the module structure

# Key Properties

1. tv = T(v) and f(t)v = [f(T)](v) (14.8.7)
2. F[t]-submodules correspond to T-invariant subspaces
3. Direct sum of submodules corresponds to direct sum of T-invariant subspaces
4. Cyclic F[t]-module corresponds to subspace spanned by w, T(w), T^2(w), ...
5. For finite-dimensional V, the free summand is zero

# Context & Application

This equivalence is the key insight that allows the structure theorem for modules over F[t] to yield canonical forms for linear operators (rational canonical form, Jordan form).

# Examples

**Example 1** (p. 453): The shift operator (a_0, a_1, ...) -> (0, a_0, a_1, ...) corresponds to the free F[t]-module of rank 1.

**Example 2** (p. 455): If V = F[t]/(t^3 - 1), the corresponding operator has matrix [[0,0,1],[1,0,0],[0,1,0]].

# Relationships

## Builds Upon
- **Module** -- V gets an F[t]-module structure

## Enables
- **Rational canonical form** -- Via the structure theorem for F[t]-modules

# Source Reference

Chapter 14: Linear Algebra in a Ring, Section 14.8, pages 449-457. Equation 14.8.9.

# Verification Notes

- Definition source: Direct from Artin (14.8.9)
- Confidence rationale: Explicitly stated as equivalence
- Uncertainties: None
- Cross-reference status: Verified
