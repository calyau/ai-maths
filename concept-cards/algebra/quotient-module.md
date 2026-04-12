---
concept: Quotient Module
slug: quotient-module
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
  - submodule
extends: []
related:
  - module-homomorphism
  - first-isomorphism-theorem-modules
contrasts_with: []
answers_questions:
  - "What is a quotient module?"
---

# Quick Definition

The quotient module V/W is formed from a module V and a submodule W by identifying elements that differ by an element of W. Scalar multiplication is r*v_bar = (rv)_bar.

# Core Definition

Let W be a submodule of an R-module V. The quotient module V/W is the group of additive cosets v_bar = [v + W], made into an R-module by r*v_bar = (rv)_bar (Artin, p. 433, equation 14.1.5). The canonical map pi: V -> V/W is surjective with kernel W. The First Isomorphism Theorem (14.1.6(c)) and Correspondence Theorem (14.1.6(d)) hold as for groups and rings.

# Prerequisites

- **Module** -- The ambient module
- **Submodule** -- The submodule being factored out

# Key Properties

1. The canonical map pi: V -> V/W is a surjective homomorphism with kernel W
2. First Isomorphism Theorem: if f is surjective with kernel W, then V/W = V' (14.1.6(c))
3. Correspondence Theorem: submodules of V/W correspond to submodules of V containing W (14.1.6(d))
4. A presentation matrix A presents the module R^m / AR^n

# Context & Application

Quotient modules are the fundamental construction for presenting modules by generators and relations. Every finitely generated module over a PID is a quotient of a free module.

# Examples

**Example 1** (p. 437): Z/5Z = Z^1 / [5]Z^1 is the cyclic group C_5, presented by the 1x1 matrix [5].

# Relationships

## Builds Upon
- **Module** and **Submodule**

## Enables
- **Generators and relations for modules** -- Modules as quotients R^m/AR^n

# Source Reference

Chapter 14: Linear Algebra in a Ring, Section 14.1, pages 433-434. Theorem 14.1.6.

# Verification Notes

- Definition source: Direct from Artin (14.1.5)
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
