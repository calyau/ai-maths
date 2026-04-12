---
concept: Module Homomorphism
slug: module-homomorphism
category: module-theory
subcategory: basic-definitions
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Linear Algebra in a Ring"
chapter_number: 14
pdf_page: 432
section: "14.1 Modules"
extraction_confidence: high
aliases:
  - "homomorphism of R-modules"
prerequisites:
  - module
extends:
  - linear-transformation
related:
  - submodule
  - quotient-module
contrasts_with: []
answers_questions:
  - "What is a module homomorphism?"
---

# Quick Definition

A module homomorphism is a map between R-modules that preserves both addition and scalar multiplication, generalizing the notion of a linear transformation between vector spaces.

# Core Definition

A homomorphism phi: V -> W of R-modules is a map compatible with the laws of composition (Artin, p. 433, equation 14.1.4): phi(v + v') = phi(v) + phi(v') and phi(rv) = r*phi(v) for all v, v' in V and r in R. An isomorphism is a bijective homomorphism.

# Prerequisites

- **Module** -- Homomorphisms are maps between modules

# Key Properties

1. The kernel ker(phi) is a submodule of the domain V
2. The image im(phi) is a submodule of the range W
3. Every homomorphism between free modules R^n and R^m is given by left multiplication by an R-matrix (14.2.7)

# Construction / Recognition

## To Construct:
1. Define a map phi: V -> W between R-modules
2. Verify phi(v + v') = phi(v) + phi(v') and phi(rv) = r*phi(v)

# Context & Application

Module homomorphisms are the structure-preserving maps in module theory. They connect to presentation matrices through the representation of homomorphisms between free modules as R-matrices.

# Examples

**Example 1** (p. 435): Left multiplication by an m x n R-matrix A defines a homomorphism R^n -> R^m. The j-th column of A is f(e_j).

# Relationships

## Builds Upon
- **Module** -- Maps between modules

## Enables
- **Quotient module** -- Via the First Isomorphism Theorem
- **Presentation matrix** -- Encodes homomorphisms between free modules

# Common Errors

- **Error**: Checking only additivity and forgetting scalar compatibility
  **Correction**: Both conditions (14.1.4) must be verified.

# Source Reference

Chapter 14: Linear Algebra in a Ring, Section 14.1, page 433.

# Verification Notes

- Definition source: Direct from Artin (14.1.4)
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
