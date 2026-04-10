---
concept: Decomposition of Commutative Algebraic Groups
slug: commutative-algebraic-group-decomposition
category: solvable-groups
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 185
section: "16b Commutative algebraic groups"
extraction_confidence: high
aliases:
  - multiplicative-unipotent decomposition
prerequisites:
  - group-of-multiplicative-type
  - unipotent-group
  - jordan-decomposition
extends: []
related:
  - solvable-algebraic-group
contrasts_with: []
answers_questions:
  - "How do commutative algebraic groups decompose?"
---

# Quick Definition

Every commutative algebraic group G has a largest subgroup G_s of multiplicative type with G/G_s unipotent. Over a perfect field, G = G_s x G_u uniquely, where G_u is the largest unipotent subgroup. This is the group-theoretic version of the Jordan decomposition.

# Core Definition

*Theorem 16.14*: Let G be a commutative algebraic group over k. (a) There exists a largest subgroup G_s of multiplicative type; it is characteristic, and G/G_s is unipotent. (b) If k is perfect, there exists a largest unipotent subgroup G_u, and G = G_s x G_u uniquely. For smooth G over a perfect field, G_s(k^al) consists of the semisimple elements and G_u(k^al) of the unipotent elements (Proposition 16.12, Milne, pp. 185-187).

# Prerequisites

- **Group of multiplicative type** -- G_s is of multiplicative type
- **Unipotent group** -- G_u is unipotent
- **Jordan decomposition** -- The element-wise version for smooth groups

# Key Properties

1. G_s is the largest subgroup of multiplicative type (characteristic subgroup)
2. G/G_s is unipotent
3. Over perfect fields: G = G_s x G_u (unique direct product decomposition)
4. For smooth G over k^al: G_s(k^al) = semisimple elements, G_u(k^al) = unipotent elements
5. Over non-perfect fields, G_u may not exist (Remark 16.16)

# Context & Application

This decomposition is the commutative case of the structure theory of solvable groups. It separates the "diagonalizable" and "nilpotent" parts at the group level, extending the Jordan decomposition from individual elements to the entire group.

# Examples

**Example 1** (p. 185): For T_n (upper triangular), the commutative quotient T_n/DT_n = D_n decomposes trivially (it is already a torus, so G_u = 1).

**Example 2** (p. 187): Over a separably closed non-perfect field, G = (G_m)_{k'/k} with [k':k] = p has G_s = G_m and G/G_m unipotent, but G_u = 1 (no direct product decomposition).

# Relationships

## Builds Upon
- **Group of multiplicative type** -- G_s
- **Unipotent group** -- G_u

## Enables
- **Solvable algebraic group** -- Extends to the non-commutative solvable case via Theorem 16.33

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 16b, pages 185-187. Proposition 16.12, Theorem 16.14.

# Verification Notes

- Definition source: Direct from Theorem 16.14
- Confidence rationale: Explicit theorem with structural decomposition
- Uncertainties: None
- Cross-reference status: Verified
