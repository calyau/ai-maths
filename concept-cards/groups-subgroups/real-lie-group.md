---
concept: Real Lie Group
slug: real-lie-group
category: lie-groups
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Lie Groups"
chapter_number: 4
pdf_page: 327
section: "Lie groups"
extraction_confidence: high
aliases:
  - "Lie group"
prerequisites:
  - affine-algebraic-group
extends: []
related:
  - complex-lie-group
  - algebraic-lie-group-functor
  - reductive-lie-group
contrasts_with:
  - complex-lie-group
  - affine-algebraic-group
answers_questions:
  - "How do algebraic groups relate to Lie groups?"
---

# Quick Definition

A real Lie group is a smooth manifold G equipped with a group structure such that both the multiplication and inverse maps are smooth (infinitely differentiable).

# Core Definition

A **real Lie group** is a smooth manifold G together with a group structure such that both the multiplication map G × G → G and the inverse map G → G are smooth (where "smooth" means infinitely differentiable) (Milne, Definition 1.1a, p. 327).

A real Lie group is **linear** if it admits a faithful real representation. A real linear Lie group is **reductive** if every real representation is semisimple.

# Prerequisites

- **Affine algebraic group** — Lie groups generalize algebraic groups

# Key Properties

1. Not all Lie groups have faithful representations (Example 2.5, p. 329)
2. Even when a faithful representation exists, the Lie group need not be of the form L(G) for an algebraic group G (Example 2.6, p. 329)
3. There is a canonical functor L from real algebraic groups to real Lie groups (Theorem 2.1)

# Context & Application

The theory of algebraic groups captures "that part of the theory of Lie groups that can be developed using only polynomials (not convergent power series), and hence works over any field" (Milne, p. 326).

# Examples

**Example 1** (p. 327): GL_n(ℝ) with its natural smooth structure is a real Lie group.

# Relationships

## Related
- **Complex Lie group** — Defined similarly with holomorphic maps
- **Algebraic Lie group functor** — Connects algebraic groups to Lie groups

## Contrasts With
- **Affine algebraic group** — More restrictive; polynomial rather than smooth maps

# Source Reference

Chapter IV, Section 1, Definition 1.1a, page 327.

# Verification Notes

- Definition source: Direct from Definition 1.1a
- Confidence: HIGH
- Uncertainties: None
