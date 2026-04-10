---
concept: "Dynkin Diagram C_n"
slug: dynkin-diagram-c-n
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
  - "type C"
  - "C_n"
prerequisites:
  - dynkin-diagram
extends: []
related:
  - symplectic-group
  - dynkin-diagram-b-n
contrasts_with:
  - dynkin-diagram-b-n
answers_questions:
  - "What is the Dynkin diagram of type C_n?"
---

# Quick Definition

The Dynkin diagram C_n (n ≥ 3) is a chain of n nodes with a double edge (arrow pointing left) between the last two nodes. It corresponds to the root system of Sp_{2n}.

# Core Definition

**C_n** (n ≥ 3) is the Dynkin diagram: ○—○—...—○⇐○ (n nodes, double edge with arrow toward second-to-last node). The root system has roots ±2χ_i and ±χ_i ± χ_j (i ≠ j), with coroots ±λ_i and ±λ_i ± λ_j respectively (Milne, Ch. V, §2n, p. 349).

# Prerequisites

- **Dynkin diagram** — C_n is one of the indecomposable types

# Key Properties

1. Rank: n; Number of roots: 2n²
2. Weyl group: W ≅ (ℤ/2)ⁿ ⋊ S_n, order 2ⁿn!
3. P/Q ≅ ℤ/2ℤ
4. Has two root lengths (long roots ±2χ_i, short roots ±χ_i ± χ_j)

# Context & Application

The simply connected group of type C_n is Sp_{2n} (which is also the adjoint group since P/Q ≅ ℤ/2ℤ and the only quotient is Sp_{2n}/μ₂ = PSp_{2n}).

# Examples

**Example 1** (Ch. V, p. 349): Sp_{2n} with roots ±2χ_i, ±χ_i ± χ_j.

# Relationships

## Contrasts With
- **Dynkin Diagram B_n** — Same Coxeter graph; C_n has long roots ±2χ_i while B_n has short roots ±χ_i

# Source Reference

Chapter III, Section 1j, p. 304; Chapter V, Section 2n (C_n example), pp. 349–350.

# Verification Notes

- Definition source: Direct from §1j and Ch. V §2n
- Confidence: HIGH
- Uncertainties: None
