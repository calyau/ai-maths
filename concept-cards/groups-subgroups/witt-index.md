---
concept: Witt Index
slug: witt-index
category: classical-groups
subcategory: quadratic-spaces
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 206
section: "18b Theorems of Witt and Cartan-Dieudonne"
extraction_confidence: high
aliases:
  - "hyperbolic plane"
prerequisites:
  - quadratic-form
  - witt-cancellation-theorem
extends: []
related:
  - witt-decomposition
contrasts_with: []
answers_questions:
  - "What is a Clifford algebra?"
---

# Quick Definition

The Witt index of a regular quadratic space is the maximum dimension of a totally isotropic subspace. A hyperbolic plane is a 2-dimensional regular isotropic quadratic space.

# Core Definition

The **(Witt) index** of a regular quadratic space (V,q) is the maximum dimension of a totally isotropic subspace of V (Milne, Definition 18.7). A **hyperbolic plane** is a regular isotropic quadratic space of dimension 2 (Definition 18.8). The **Witt decomposition** (Theorem 18.9) gives V = H_1 + ... + H_m + V_a with the H_i hyperbolic planes and V_a anisotropic, where m is the Witt index and V_a is unique up to isometry.

# Prerequisites

- **Quadratic form** -- The Witt index is an invariant of a quadratic space
- **Witt cancellation theorem** -- Ensures the Witt index is well-defined

# Key Properties

1. The Witt index equals the number of hyperbolic planes in the Witt decomposition
2. V_a is uniquely determined up to isometry (Theorem 18.9)
3. A hyperbolic plane has matrix (0 1; 1 0) and discriminant -1 mod squares (Definition 18.8)

# Context & Application

The Witt index is a fundamental invariant for classifying quadratic forms. Over algebraically closed fields, the Witt index completely determines the form (up to dimension), but over other fields the anisotropic part V_a carries additional information.

# Examples

**Example 1** (p. 206): A hyperbolic plane has basis e_1, e_2 with phi(e_1,e_2) = 1 and q(e_1) = q(e_2) = 0.

# Relationships

## Builds Upon
- **Quadratic form** -- The Witt index is an invariant of (V,q)

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 18b, pages 206-207.

# Verification Notes

- Definition source: Direct from Definitions 18.7, 18.8 and Theorem 18.9
- Confidence rationale: Explicit definitions
- Uncertainties: None
- Cross-reference status: Verified
