---
concept: First Isomorphism Theorem for Modules
slug: first-isomorphism-theorem-modules
category: module-theory
subcategory: fundamental-theorems
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
  - module-homomorphism
  - quotient-module
extends:
  - first-isomorphism-theorem-rings
related:
  - correspondence-theorem-modules
contrasts_with: []
answers_questions:
  - "What is the First Isomorphism Theorem for modules?"
---

# Quick Definition

If f: V -> V' is a surjective module homomorphism with kernel W, then V/W is isomorphic to V'. This is the module-theoretic version of the theorem proved for groups and rings.

# Core Definition

Let f: V -> V' be a surjective homomorphism of R-modules whose kernel is equal to W. The induced map f_bar: V/W -> V' is an isomorphism (Artin, Theorem 14.1.6(c)). The Correspondence Theorem (14.1.6(d)) also holds: submodules of V/W correspond bijectively with submodules of V containing W.

# Prerequisites

- **Module homomorphism** -- Applies to surjective homomorphisms
- **Quotient module** -- The domain of the induced isomorphism

# Key Properties

1. V/ker(f) is isomorphic to im(f) for any homomorphism f
2. The Correspondence Theorem: submodules of V/W correspond to submodules of V containing W
3. If S corresponds to S_bar, then V/S is isomorphic to V_bar/S_bar

# Context & Application

This theorem, along with the Correspondence Theorem, provides the foundation for the theory of presentations. It shows that V = R^m/AR^n when V has presentation matrix A.

# Examples

**Example 1** (p. 437): The surjection R^m -> V with kernel AR^n gives V = R^m/AR^n.

# Relationships

## Builds Upon
- **Module homomorphism** and **Quotient module**

## Enables
- **Generators and relations for modules** -- V = R^m/AR^n

# Source Reference

Chapter 14: Linear Algebra in a Ring, Section 14.1, page 434. Theorem 14.1.6(c),(d).

# Verification Notes

- Definition source: Direct from Artin, Theorem 14.1.6
- Confidence rationale: Explicitly stated
- Uncertainties: None
- Cross-reference status: Verified
