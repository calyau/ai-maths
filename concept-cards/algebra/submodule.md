---
concept: Submodule
slug: submodule
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
aliases: []
prerequisites:
  - module
extends: []
related:
  - ideal
  - module-homomorphism
contrasts_with: []
answers_questions:
  - "What is a submodule?"
---

# Quick Definition

A submodule W of an R-module V is a nonempty subset that is closed under addition and scalar multiplication, inheriting the module structure from V.

# Core Definition

A submodule W of an R-module V is a nonempty subset that is closed under addition and under scalar multiplication by elements of R (Artin, p. 433). The laws of composition on V make a submodule W into a module in its own right.

# Prerequisites

- **Module** -- Submodules are subsets of modules that inherit the module structure

# Key Properties

1. Every submodule is itself a module under the inherited operations
2. Submodules of the R-module R^1 are exactly the ideals of R (Proposition 14.1.3)
3. The kernel of a module homomorphism is a submodule of the domain
4. The image of a module homomorphism is a submodule of the range

# Construction / Recognition

## To Recognize:
1. Verify the subset is nonempty
2. Check closure under addition
3. Check closure under scalar multiplication

# Context & Application

Submodules play the same role in module theory that subspaces play in linear algebra and ideals play in ring theory. The quotient module V/W generalizes the quotient constructions for rings and groups.

# Examples

**Example 1** (p. 433): The ideals of a ring R are exactly the submodules of R viewed as an R-module over itself (Proposition 14.1.3).

# Relationships

## Builds Upon
- **Module** -- Submodules live inside modules

## Enables
- **Quotient module** -- Formed by taking cosets of a submodule

## Related
- **Ideal** -- An ideal is a submodule of R as an R-module

# Common Errors

- **Error**: Forgetting to check closure under scalar multiplication
  **Correction**: Both closure conditions must hold for a subset to be a submodule.

# Common Confusions

- **Confusion**: Confusing submodules with ideals
  **Clarification**: Ideals are submodules of R as a module over itself; submodules are the general notion.

# Source Reference

Chapter 14: Linear Algebra in a Ring, Section 14.1, page 433.

# Verification Notes

- Definition source: Direct from Artin, p. 433
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
