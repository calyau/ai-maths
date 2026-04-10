---
concept: Cartan Matrix
slug: cartan-matrix
category: root-systems
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "The Structure of Semisimple Lie Algebras and Algebraic Groups in Characteristic Zero"
chapter_number: 3
pdf_page: 301
section: "Cartan matrices"
extraction_confidence: high
aliases: []
prerequisites:
  - root-system
  - base-of-root-system
  - coroot
extends: []
related:
  - dynkin-diagram
  - coxeter-graph
contrasts_with: []
answers_questions:
  - "What is a Cartan matrix?"
---

# Quick Definition

The Cartan matrix of a root system R (relative to a base S) is the integer matrix (n(α,β))_{α,β∈S} where n(α,β) = ⟨α, β^∨⟩ = 2(α,β)/(β,β). It determines the root system up to isomorphism.

# Core Definition

Let (V, R) be a root system and S a base. The **Cartan matrix** of R (relative to S) is the matrix (n(α, β))_{α,β ∈ S} where n(α, β) = ⟨α, β^∨⟩ ∈ ℤ. Its diagonal entries n(α, α) equal 2, and the remaining entries are negative or zero (Milne, §1g, p. 301).

The Cartan matrix is independent of the choice of S (up to reindexing) and determines (V, R) up to isomorphism (Proposition 1.14).

# Prerequisites

- **Root system** — The Cartan matrix encodes root system data
- **Base of root system** — The matrix is indexed by simple roots
- **Coroot** — Entries involve the pairing ⟨α, β^∨⟩

# Key Properties

1. Diagonal entries are all 2
2. Off-diagonal entries are non-positive integers (0, −1, −2, or −3)
3. Independent of choice of base (up to simultaneous row/column permutation)
4. Determines the root system up to isomorphism (Proposition 1.14)
5. n(wα, wβ) = n(α, β) for all w ∈ W

# Examples

**Example 1** (p. 301): The Cartan matrices of the rank 2 root systems:
- A₁ × A₁: diag(2,2)
- A₂: [[2,−1],[−1,2]]
- B₂: [[2,−1],[−2,2]]
- G₂: [[2,−1],[−3,2]]

**Example 2** (p. 301): For A_n, the Cartan matrix is tridiagonal with 2 on the diagonal and −1 on the super/sub-diagonals.

# Relationships

## Builds Upon
- **Root system** — Encodes the root system structure

## Enables
- **Dynkin diagram** — Read off from the Cartan matrix
- **Classification of root systems** — Via the Cartan matrix

# Source Reference

Chapter III, Section 1g, pages 301–302.

# Verification Notes

- Definition source: Direct from §1g
- Confidence: HIGH — explicit definition with examples
- Uncertainties: None
