---
concept: "Dynkin Diagram A_n"
slug: dynkin-diagram-a-n
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
  - "type A"
  - "A_n"
prerequisites:
  - dynkin-diagram
  - root-system
extends: []
related:
  - special-linear-group
contrasts_with:
  - dynkin-diagram-b-n
  - dynkin-diagram-d-n
answers_questions:
  - "What is the Dynkin diagram of type A_n?"
---

# Quick Definition

The Dynkin diagram A_n (n ≥ 1) is a chain of n nodes connected by single edges. It corresponds to the root system of sl_{n+1} and the groups SL_{n+1}/μ_d.

# Core Definition

**A_n** (n ≥ 1) is the Dynkin diagram consisting of n nodes in a line, each connected to its neighbors by a single edge (Milne, Theorem 1.17 and §1j, p. 304):

○—○—○— ... —○—○ (n nodes)

The corresponding root system has roots R = {e_i − e_j | i ≠ j, 1 ≤ i,j ≤ n+1} in the hyperplane ∑x_i = 0 of ℝ^{n+1}. Simple roots: α_i = e_i − e_{i+1}.

# Prerequisites

- **Dynkin diagram** — A_n is one of the indecomposable types

# Key Properties

1. Rank: n; Number of roots: n(n+1)
2. Weyl group: W ≅ S_{n+1} (symmetric group), order (n+1)!
3. P/Q ≅ ℤ/(n+1)ℤ (cyclic of order n+1)
4. All roots have the same length
5. Cartan matrix: tridiagonal with 2 on diagonal, −1 on off-diagonals

# Context & Application

A_n is the most classical root system. The simply connected group of type A_n is SL_{n+1}; the adjoint group is PGL_{n+1}. The fundamental representations are the exterior powers ∧^i(k^{n+1}).

# Examples

**Example 1** (pp. 296, 298): A_n with roots e_i − e_j in the hyperplane of ℝ^{n+1}. Base: {e₁−e₂, ..., e_n−e_{n+1}}. Highest root: e₁ − e_{n+1}.

# Source Reference

Chapter III, Section 1j, p. 304; Examples 1.4 and 1.13 (pp. 296–299); §2h (p. 311).

# Verification Notes

- Definition source: Direct from §1j and Examples 1.4/1.13
- Confidence: HIGH
- Uncertainties: None
