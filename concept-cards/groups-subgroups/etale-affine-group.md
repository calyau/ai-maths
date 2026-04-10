---
concept: Etale Affine Group
slug: etale-affine-group
category: group-structure
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 145
section: "12b Etale affine groups"
extraction_confidence: high
aliases:
  - etale group scheme
prerequisites:
  - finite-flat-affine-group
  - etale-algebra
extends:
  - finite-flat-affine-group
related:
  - connected-component-group
contrasts_with: []
answers_questions:
  - "What is an etale affine group?"
---

# Quick Definition

An affine group G over a field k is etale if O(G) is an etale k-algebra (a finite product of separable field extensions of k). Equivalently, G is finite and smooth. The functor G -> G(k^sep) is an equivalence from etale affine groups to finite groups with continuous Galois action.

# Core Definition

A k-algebra A is *etale* if it is a finite product of separable field extensions of k, equivalently if A tensor k^al is a product of copies of k^al, equivalently if A tensor k^al is reduced (Proposition 12.2). An affine group G is *etale* if O(G) is etale. A finite affine group is etale iff it is smooth (Remark 12.10). In characteristic zero, every finite affine group is etale by Cartier's theorem. The functor G -> G(k^sep) is an equivalence from etale affine groups over k to finite groups with continuous action of Gal(k^sep/k) (Theorem 12.11, Milne, pp. 145-148).

# Prerequisites

- **Finite flat affine group** -- Etale groups are a special case of finite groups
- **Etale algebra** -- O(G) must be etale

# Key Properties

1. Etale = finite + smooth (for affine groups over a field)
2. In characteristic zero, all finite affine groups are etale
3. Classified by finite groups with continuous Galois action (Theorem 12.11)
4. Etale groups are always reduced (no nilpotent elements in O(G))
5. Products, quotients, and subgroups of etale groups are etale (Proposition 12.4)

# Context & Application

Etale groups capture the "discrete" part of an algebraic group's structure. Every algebraic group G has a quotient pi_0(G) that is etale, encoding the group of connected components. Etale groups over separably closed fields are just constant group schemes.

# Examples

**Example 1** (p. 148): Over Q, there are infinitely many non-isomorphic etale groups of order 3, one for each separable quadratic extension K of Q (plus the constant group). For K = Q[sqrt(-3)], the corresponding group is mu_3.

# Relationships

## Builds Upon
- **Finite flat affine group** -- Etale groups are smooth finite groups

## Enables
- **Connected component group** -- pi_0(G) is always etale

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 12b, pages 145-148. Theorem 12.11.

# Verification Notes

- Definition source: Direct from Definition 12.3 and surrounding text
- Confidence rationale: Explicit definitions and classification theorem
- Uncertainties: None
- Cross-reference status: Verified
