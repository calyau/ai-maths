---
# === CORE IDENTIFICATION ===
concept: Automorphism Group of a Bilinear Form
slug: automorphism-group-of-a-bilinear-form

# === CLASSIFICATION ===
category: group-fundamentals
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Basic Definitions and Results"
chapter_number: 1
pdf_page: 9
section: "Definitions and examples"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Aut(φ)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
  - general-linear-group
extends:
  - group
related:
  - orthogonal-group
  - symplectic-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the automorphism group of a bilinear form?"
  - "How do bilinear forms give rise to groups?"
---

# Quick Definition

The automorphism group Aut(phi) of a bilinear form phi on a vector space V is the group of all invertible linear maps alpha: V -> V that preserve phi, i.e., phi(alpha v, alpha w) = phi(v, w) for all v, w.

# Core Definition

Let V be a finite-dimensional vector space over a field F with a bilinear form phi: V x V -> F (a mapping that is linear in each variable). An **automorphism** of phi is an isomorphism alpha: V -> V such that phi(alpha v, alpha w) = phi(v, w) for all v, w in V. The automorphisms of phi form a group **Aut(phi)**.

In matrix terms: choosing a basis {e_1, ..., e_n} with matrix P = (phi(e_i, e_j)), the group Aut(phi) is identified with the group of invertible matrices A such that A^T P A = P (1.8, pp. 9-10).

# Prerequisites

- **Group** — Aut(phi) is a group
- **General linear group** — Aut(phi) is a subgroup of GL(V)

# Key Properties

1. Aut(phi) is a subgroup of GL(V)
2. In matrix form: {A in GL_n(F) | A^T P A = P}
3. Specializes to orthogonal group when phi is symmetric and nondegenerate
4. Specializes to symplectic group when phi is skew-symmetric and nondegenerate

# Construction / Recognition

## To Construct:
1. Start with a vector space V and a bilinear form phi
2. Choose a basis to get the matrix P of phi
3. Find all invertible matrices A satisfying A^T P A = P

# Context & Application

This construction unifies the orthogonal and symplectic groups as special cases. It demonstrates how preserving additional structure (a bilinear form) on a vector space gives rise to important subgroups of GL(V).

# Examples

**Example 1** (pp. 9-10, 1.8): When phi is symmetric and nondegenerate, Aut(phi) is the orthogonal group.

**Example 2** (p. 10, 1.8): When phi is skew-symmetric and nondegenerate, Aut(phi) is the symplectic group Sp_{2m}.

# Relationships

## Builds Upon
- **general-linear-group** — Aut(phi) is a subgroup of GL(V)

## Enables
- **orthogonal-group** — the case of symmetric phi
- **symplectic-group** — the case of skew-symmetric phi

# Common Confusions

- **Confusion**: Thinking Aut(phi) depends on the choice of basis
  **Clarification**: Different bases give conjugate matrix groups; the abstract group Aut(phi) is basis-independent

# Source Reference

Chapter 1: Basic Definitions and Results, Example 1.8, pages 9-10.

# Verification Notes

- Definition source: Direct from 1.8, pp. 9-10
- Confidence rationale: HIGH — explicitly defined with matrix characterization
- Uncertainties: None
- Cross-reference status: Verified against planned cards
