---
concept: Central Simple Algebra
slug: central-simple-algebra
category: classical-groups
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 224
section: "19c The forms of M_n(k)"
extraction_confidence: high
aliases:
  - "CSA"
prerequisites: []
extends: []
related:
  - forms-of-algebraic-group
  - involution-of-algebra
contrasts_with: []
answers_questions:
  - "What is a semisimple algebraic group?"
---

# Quick Definition

A central simple algebra over k is a k-algebra whose centre is k and which has no nontrivial two-sided ideals. By Wedderburn's theorem, every CSA is isomorphic to M_n(D) for some division algebra D.

# Core Definition

A k-algebra A is **central** if its centre is k, and **simple** if it has no 2-sided ideals except 0 and A (Milne, Definition 19.18). By Wedderburn's theorem, every simple k-algebra is M_n(D) for some division algebra D (Theorem 19.20). When k is algebraically closed, the only CSAs are M_n(k) (Corollary 19.21).

# Prerequisites

This is a foundational concept in noncommutative algebra.

# Key Properties

1. The k-algebras becoming isomorphic to M_n(k) over k^{al} are exactly the CSAs of degree n^2 (Proposition 19.22)
2. All automorphisms of M_n(k) are inner: X -> YXY^{-1} (Proposition 19.23)
3. CSAs of degree n^2 are classified by H^1(k, PGL_n) (Corollary 19.24)
4. Every CSA has a reduced norm: Nm(a) = det(f(a)) where f: A -> M_n(k^{al}) (Remark 19.25)

# Context & Application

CSAs are the forms of matrix algebras, and their classification is equivalent to classifying the inner forms of SL_n. Over number fields and p-adic fields, CSAs are classified by class field theory (the Brauer group).

# Examples

**Example 1** (p. 224): M_n(k) is central and simple.

**Example 2** (p. 224): The quaternion algebra H(a,b) is central and simple; it is either a division algebra or isomorphic to M_2(k).

# Relationships

## Enables
- **Forms of algebraic group** -- CSAs classify inner forms of SL_n

## Related
- **Involution of algebra** -- CSAs with involution classify classical groups

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 19c, pages 224-226.

# Verification Notes

- Definition source: Direct from Definition 19.18
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
