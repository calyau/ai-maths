---
concept: "Dynkin Diagram D_n"
slug: dynkin-diagram-d-n
category: root-systems
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "The Structure of Semisimple Lie Algebras and Algebraic Groups in Characteristic Zero"
chapter_number: 3
pdf_page: 304
section: "List of indecomposable Dynkin diagrams"
extraction_confidence: high
aliases:
  - "type D"
  - "D_n"
prerequisites:
  - dynkin-diagram
extends: []
related:
  - orthogonal-group
contrasts_with:
  - dynkin-diagram-b-n
answers_questions:
  - "What is the Dynkin diagram of type D_n?"
---

# Quick Definition

The Dynkin diagram D_n (n ≥ 4) is a chain of n−2 nodes with a fork at one end (two nodes branching from the (n−2)-th node). It corresponds to the root system of SO_{2n}.

# Core Definition

**D_n** (n ≥ 4) is the Dynkin diagram consisting of a chain of n−2 nodes with a fork: the (n−2)-th node connects to two terminal nodes. The root system has roots ±χ_i ± χ_j (i ≠ j), with coroots ±λ_i ± λ_j (Milne, Ch. V, §2n, pp. 350–351).

# Prerequisites

- **Dynkin diagram** — D_n is one of the indecomposable types

# Key Properties

1. Rank: n; Number of roots: 2n(n−1)
2. Weyl group: W ≅ (ℤ/2)^{n−1} ⋊ S_n, order 2^{n−1}n!
3. P/Q ≅ ℤ/4ℤ (n odd) or (ℤ/2)² (n even)
4. All roots have the same length
5. Has an outer automorphism of order 2 (swapping the fork nodes) for n ≥ 5, and order 3 for n = 4 (triality)

# Context & Application

The simply connected group of type D_n is the spin group Spin_{2n}. The adjoint group is SO_{2n}/μ₂. The diagram D_4 has an exceptional order-3 symmetry (triality).

# Examples

**Example 1** (Ch. V, pp. 350–351): SO_{2n} with roots ±χ_i ± χ_j (i ≠ j).

# Source Reference

Chapter III, Section 1j, p. 304; Chapter V, Section 2n (D_n example), pp. 350–351.

# Verification Notes

- Definition source: Direct from §1j and Ch. V §2n
- Confidence: HIGH
- Uncertainties: None
