---
concept: Free Module
slug: free-module
category: module-theory
subcategory: module-types
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Linear Algebra in a Ring"
chapter_number: 14
pdf_page: 432
section: "14.2 Free Modules"
extraction_confidence: high
aliases:
  - "free R-module"
  - "free abelian group"
prerequisites:
  - module
extends: []
related:
  - rank-of-free-module
  - finitely-generated-module
contrasts_with:
  - torsion-module
answers_questions:
  - "What is a free module?"
---

# Quick Definition

A free module is a module that has a basis, making it isomorphic to R^k for some k. Free modules are the direct generalization of vector spaces to rings.

# Core Definition

A module V is free if and only if it has a basis -- an ordered set (v_1, ..., v_n) that generates V and is independent (Artin, p. 435). Equivalently, V is free if it is isomorphic to one of the free modules R^k. A free Z-module is also called a free abelian group. Most modules have no basis.

# Prerequisites

- **Module** -- Free modules are a special class of modules

# Key Properties

1. A module V has a basis if and only if it is isomorphic to R^k for some k
2. Any two bases of the same free module over a nonzero ring have the same cardinality (Proposition 14.2.6(b))
3. The matrix of a change of basis in a free module is an invertible R-matrix (14.2.6(a))
4. Most modules have no basis -- finite nonzero abelian groups are not free
5. Lattices in R^2 are free abelian groups

# Construction / Recognition

## To Construct:
1. Choose a ring R and positive integer k
2. R^k with componentwise operations is a free R-module of rank k

## To Recognize:
1. Find a generating set that is also independent (a basis)

# Context & Application

Free modules serve as the building blocks from which all finitely generated modules are constructed via quotients. Presentation matrices express modules as quotients R^m / AR^n of free modules.

# Examples

**Example 1** (p. 432): R^n with standard basis (e_1, ..., e_n) is the prototypical free module.

**Example 2** (p. 435): Lattices in R^2 are free abelian groups.

# Relationships

## Builds Upon
- **Module** -- Free modules are modules with bases

## Enables
- **Presentation matrix** -- Every finitely generated module is a quotient of a free module
- **Smith normal form** -- Diagonalization of maps between free modules

## Contrasts With
- **Torsion module** -- A torsion module has no nonzero free part

# Common Errors

- **Error**: Assuming every finitely generated module is free
  **Correction**: Z/nZ is finitely generated but not free over Z.

# Source Reference

Chapter 14: Linear Algebra in a Ring, Section 14.2, pages 434-436. Proposition 14.2.6.

# Verification Notes

- Definition source: Direct from Artin, p. 435
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
