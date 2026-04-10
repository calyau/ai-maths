---
concept: Split Semisimple Lie Algebra
slug: split-semisimple-lie-algebra
category: semisimple-theory
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "The Structure of Semisimple Lie Algebras and Algebraic Groups in Characteristic Zero"
chapter_number: 3
pdf_page: 308
section: "Split semisimple Lie algebras"
extraction_confidence: high
aliases:
  - "splittable semisimple Lie algebra"
prerequisites:
  - cartan-subalgebra
extends: []
related:
  - root-space-decomposition
  - root-system
  - classification-of-semisimple-lie-algebras
contrasts_with: []
answers_questions:
  - "What is a split semisimple Lie algebra?"
---

# Quick Definition

A split semisimple Lie algebra is a pair (𝔤, 𝔥) consisting of a semisimple Lie algebra 𝔤 and a splitting Cartan subalgebra 𝔥 (one whose eigenvalues on 𝔤 all lie in the base field).

# Core Definition

A **split semisimple Lie algebra** is a pair (𝔤, 𝔥) consisting of a semisimple Lie algebra 𝔤 and a splitting Cartan subalgebra 𝔥 (Definition 2.16, p. 308). More loosely, a semisimple Lie algebra is *split* if it contains a splitting Cartan subalgebra.

The root system of (𝔤, 𝔥) is the set R of nonzero α ∈ 𝔥^∨ such that the eigenspace 𝔤^α ≠ 0 in the decomposition 𝔤 = 𝔥 ⊕ ⊕_{α∈R} 𝔤^α.

# Prerequisites

- **Cartan subalgebra** — A splitting Cartan subalgebra is needed to define the splitting

# Key Properties

1. The root system R is a reduced root system in 𝔥^∨ (Theorem 2.23)
2. Each root space 𝔤^α is one-dimensional (Theorem 2.22a)
3. The root system determines (𝔤, 𝔥) up to isomorphism (Theorem 2.36)
4. Every root system arises from a split semisimple Lie algebra (Theorem 2.35)

# Examples

**Example 1** (p. 311): (sl_{n+1}, 𝔥) where 𝔥 is the diagonal matrices of trace 0. Root system is A_n.

# Relationships

## Enables
- **Root space decomposition** — 𝔤 = 𝔥 ⊕ ⊕_α 𝔤^α
- **Classification of semisimple Lie algebras** — Via root systems

# Source Reference

Chapter III, Section 2c–2d, pages 308–309.

# Verification Notes

- Definition source: Direct from Definition 2.16
- Confidence: HIGH
- Uncertainties: None
