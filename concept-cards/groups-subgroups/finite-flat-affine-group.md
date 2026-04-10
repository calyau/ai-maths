---
concept: Finite Flat Affine Group
slug: finite-flat-affine-group
category: group-structure
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 144
section: "12 Finite flat affine groups"
extraction_confidence: high
aliases:
  - finite group scheme
  - finite affine group
prerequisites:
  - affine-algebraic-group
  - hopf-algebra
extends:
  - affine-algebraic-group
related:
  - etale-affine-group
  - cartier-duality
  - dieudonne-module
contrasts_with: []
answers_questions:
  - "What is a finite affine group?"
---

# Quick Definition

A finite flat affine group over a field k is an affine group G such that dim_k O(G) is finite. The dimension is called the order of G. Over a field, flatness is automatic for finite groups.

# Core Definition

A *finite flat* affine group over a commutative ring k is an affine group G such that O(G) is finitely generated and projective as a k-module. Over a field k, this simplifies to: a *finite affine group* is an affine group with dim_k O(G) finite. The order of G is dim_k O(G). A finite affine group is a *p-group* if its order is a power of p (Milne, Definition 12.1, p. 144).

# Prerequisites

- **Affine algebraic group** -- Finite groups are a special case
- **Hopf algebra** -- O(G) is a finite-dimensional Hopf algebra

# Key Properties

1. Over a field, every finite affine group is automatically algebraic
2. In characteristic zero, every finite affine group is etale (Cartier's theorem)
3. In characteristic p, the structure is more complex: O(G) may have nilpotent elements
4. For connected finite groups over perfect fields of char p, O(G) is a truncated polynomial algebra (Theorem 12.14)
5. Finite flat commutative groups have Cartier duals (Section 12d)

# Context & Application

Finite group schemes arise naturally as kernels of isogenies between algebraic groups (e.g., mu_n is the kernel of n: G_m -> G_m). They play a fundamental role in arithmetic geometry, particularly in the theory of abelian varieties and p-divisible groups.

# Examples

**Example 1** (p. 144): mu_n has O(mu_n) = k[X]/(X^n - 1), order n.

**Example 2** (p. 144): alpha_p (char p) has O(alpha_p) = k[X]/(X^p), order p. It is connected and non-etale.

# Relationships

## Builds Upon
- **Affine algebraic group** -- Finite groups are a special class

## Enables
- **Etale affine group** -- The smooth finite groups
- **Connected components** -- G^0 and pi_0(G) decompose finite groups

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 12, pages 144-151. Definition 12.1.

# Verification Notes

- Definition source: Direct from Definition 12.1
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
