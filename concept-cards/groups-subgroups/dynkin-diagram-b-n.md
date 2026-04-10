---
concept: "Dynkin Diagram B_n"
slug: dynkin-diagram-b-n
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
  - "type B"
  - "B_n"
prerequisites:
  - dynkin-diagram
extends: []
related:
  - orthogonal-group
  - dynkin-diagram-c-n
contrasts_with:
  - dynkin-diagram-c-n
answers_questions:
  - "What is the Dynkin diagram of type B_n?"
---

# Quick Definition

The Dynkin diagram B_n (n ≥ 2) is a chain of n nodes with a double edge (arrow pointing right) between the last two nodes. It corresponds to the root system of SO_{2n+1}.

# Core Definition

**B_n** (n ≥ 2) is the Dynkin diagram: ○—○—...—○⇒○ (n nodes, double edge with arrow toward last node, indicating the last simple root is shorter). The root system has roots ±χ_i and ±χ_i ± χ_j (i ≠ j), with coroots ±2λ_i and ±λ_i ± λ_j respectively (Milne, Ch. V, §2n, p. 348).

# Prerequisites

- **Dynkin diagram** — B_n is one of the indecomposable types

# Key Properties

1. Rank: n; Number of roots: 2n²
2. Weyl group: W ≅ (ℤ/2)ⁿ ⋊ S_n, order 2ⁿn!
3. P/Q ≅ ℤ/2ℤ
4. Has two root lengths (short roots ±χ_i, long roots ±χ_i ± χ_j)

# Context & Application

The simply connected group of type B_n is the spin group Spin_{2n+1}; the adjoint group is SO_{2n+1}. The Coxeter graph of B_n equals that of C_n; only the Dynkin diagram (with its arrow) distinguishes them.

# Examples

**Example 1** (Ch. V, p. 348): SO_{2n+1} with roots ±χ_i, ±χ_i ± χ_j (i ≠ j).

# Relationships

## Contrasts With
- **Dynkin diagram C_n** — Same Coxeter graph but arrow direction reversed; B_n has short roots ±χ_i while C_n has long roots ±2χ_i

# Source Reference

Chapter III, Section 1j, p. 304; Chapter V, Section 2n (B_n example), pp. 348–349.

# Verification Notes

- Definition source: Direct from §1j and Ch. V §2n
- Confidence: HIGH
- Uncertainties: None
