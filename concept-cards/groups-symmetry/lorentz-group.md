---
# === CORE IDENTIFICATION ===
concept: Lorentz Group
slug: lorentz-group

# === CLASSIFICATION ===
category: fundamentals
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Axioms"
chapter_number: 2
pdf_page: 13
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - Lorentz boost group

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
extends:
  - group
related:
  - abelian-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a group?"
---

# Quick Definition

The Lorentz group (as presented by Armstrong) is the group of 2x2 matrices of the form [[cosh u, sinh u], [sinh u, cosh u]] combined via matrix multiplication. It arises in special relativity.

# Core Definition

Armstrong presents the Lorentz group as a group whose "elements are matrices of the form [[cosh u, sinh u], [sinh u, cosh u]] and which are combined via matrix multiplication" (Armstrong, Ch. 2, p. 14). The product of two such matrices with parameters u and v is the matrix with parameter u + v, the identity is the matrix with u = 0, and the inverse of the matrix with parameter u is the matrix with parameter -u.

# Prerequisites

- **Group** — The Lorentz group is verified to be a group

# Key Properties

1. Elements are parameterized by a single real number u
2. The product of matrices with parameters u and v has parameter u + v
3. The identity matrix corresponds to u = 0
4. The inverse of the matrix with parameter u has parameter -u
5. The group is abelian (since u + v = v + u)
6. Matrix multiplication is associative, so the associative law holds

# Construction / Recognition

## To Verify Group Axioms:
1. Show the product of two matrices of the given form has the same form (using hyperbolic identities)
2. The identity matrix has the required form (u = 0)
3. The inverse matrix has the required form (u replaced by -u)
4. Associativity is inherited from matrix multiplication

# Context & Application

Armstrong introduces the Lorentz group to show that groups arise naturally in physics. "A physicist learning relativity meets the Lorentz group" (Ch. 2, p. 14). This example demonstrates that groups appear beyond geometry and number theory.

# Examples

**Example 1** (p. 14): The product formula: the product of matrices with parameters u and v gives [[cosh(u+v), sinh(u+v)], [sinh(u+v), cosh(u+v)]], using the hyperbolic addition formulas.

**Example 2** (p. 14): The identity is [[cosh 0, sinh 0], [sinh 0, cosh 0]] = [[1, 0], [0, 1]].

# Relationships

## Builds Upon
- **Group** — This is an example of a group

## Enables
- Demonstrates that matrix groups are an important class of groups

## Related
- **Abelian Group** — The Lorentz group is abelian

# Common Errors

- **Error**: Forgetting to verify that the product of two matrices of the given form stays in the given form
  **Correction**: The hyperbolic addition formulas are needed to show closure

# Common Confusions

- **Confusion**: Thinking the Lorentz group as presented here is the full Lorentz group of physics
  **Clarification**: Armstrong presents a one-parameter subgroup (boosts in one direction); the full Lorentz group is much larger

# Source Reference

Chapter 2: Axioms, pages 7-8 (pdf pp. 14-15).

# Verification Notes

- Definition source: Direct description from p. 14
- Confidence rationale: High — explicit construction with verification
- Uncertainties: None
- Cross-reference status: Verified
