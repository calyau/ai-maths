---
concept: Split Torus
slug: split-torus
category: multiplicative-groups
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 168
section: "14d Diagonalizable groups"
extraction_confidence: high
aliases: []
prerequisites:
  - diagonalizable-group
extends:
  - diagonalizable-group
related:
  - algebraic-torus
  - eigenspace
contrasts_with: []
answers_questions:
  - "What is a split torus?"
---

# Quick Definition

A split torus is an algebraic group isomorphic to a finite product of copies of G_m. Equivalently, it is a connected diagonalizable algebraic group. Under the equivalence M -> D(M), split tori correspond to free abelian groups of finite rank.

# Core Definition

A *split torus* is an algebraic group isomorphic to G_m^n for some n (14.16). Equivalently, it is a connected diagonalizable algebraic group. Under the contravariant equivalence M -> D(M), split tori correspond to free abelian groups M of finite rank. A quotient of a split torus is again a split torus, but a subgroup need not be (e.g., mu_n is a subgroup of G_m) (Milne, p. 168).

# Prerequisites

- **Diagonalizable group** -- Split tori are the connected case

# Key Properties

1. Every representation of a split torus T decomposes as V = direct-sum V_chi (Theorem 14.15)
2. X(T) = Z^n is a free abelian group of rank n = dim T
3. Quotients of split tori are split tori (subgroups of Z^n are free)
4. Subgroups of split tori need not be split tori (mu_n subset G_m)

# Examples

**Example 1** (p. 168): T = G_m x G_m has X(T) = Z^2. The character (m_1, m_2) sends (t_1, t_2) to t_1^{m_1} t_2^{m_2}. A representation V decomposes as V = direct-sum V_{(m_1,m_2)}.

**Example 2** (p. 167): D_n = G_m^n, the diagonal matrices in GL_n.

# Relationships

## Builds Upon
- **Diagonalizable group** -- Split tori are connected diagonalizable groups

## Enables
- **Algebraic torus** -- Tori become split tori over k^sep
- **Eigenspace** -- Eigenspace decompositions for torus representations

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 14d (14.16-14.17), pages 168-169.

# Verification Notes

- Definition source: Direct from 14.16
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
