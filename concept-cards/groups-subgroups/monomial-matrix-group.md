---
# === CORE IDENTIFICATION ===
concept: Group of Monomial Matrices
slug: monomial-matrix-group

# === CLASSIFICATION ===
category: classical-groups
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 17
section: "Introductory overview"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - affine-algebraic-group
  - torus
  - constant-finite-algebraic-group
extends: []
related:
  - semidirect-product-algebraic
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine algebraic group?"
---

# Quick Definition

The group of monomial matrices M consists of invertible matrices with exactly one nonzero entry in each row and column. It is a semidirect product M = D_n rtimes S_n of diagonal matrices and permutation matrices.

# Core Definition

The **group of monomial matrices** M consists of those invertible matrices with exactly one nonzero element in each row and each column (p. 17). It contains both D_n (diagonal matrices) and S_n (permutation matrices). Since M = D_n * S_n and D_n is normal in M (with D_n intersect S_n = 1), M is the semidirect product M = D_n rtimes_theta S_n, where theta: S_n -> Aut(D_n) sends sigma to the automorphism diag(a_1,...,a_n) -> diag(a_{sigma(1)},...,a_{sigma(n)}) (p. 17, equation (3)).

This group is also given a coordinate ring description: O(G) = product_{sigma in S_n} A_sigma where A_sigma = O(GL_n)/(X_ij | j != sigma(i)) (3.12, p. 33).

# Prerequisites

- **Affine algebraic group** — Monomial matrices form an algebraic group
- **Torus** — D_n is the normal subgroup (a torus)
- **Constant finite algebraic group** — S_n is the quotient (a finite group)

# Key Properties

1. M = D_n rtimes S_n (semidirect product)
2. M is not connected (it has |S_n| = n! connected components)
3. O(G) = product of copies of coordinate rings, one per permutation

# Relationships

## Related
- **Semidirect product (algebraic groups)** — M is a prototypical example of a semidirect product

# Source Reference

Chapter I, Section 1b (p. 17), 3.12 (p. 33).

# Verification Notes

- Definition source: Direct from p. 17 and 3.12
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
