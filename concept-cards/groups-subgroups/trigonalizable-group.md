---
concept: Trigonalizable Group
slug: trigonalizable-group
category: solvable-groups
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 182
section: "16a Trigonalizable affine groups"
extraction_confidence: high
aliases:
  - triangulable group
  - triagonalizable group
prerequisites:
  - linear-representation
  - unipotent-group
  - diagonalizable-group
extends: []
related:
  - solvable-algebraic-group
  - lie-kolchin-theorem
contrasts_with: []
answers_questions:
  - "What is a trigonalizable algebraic group?"
---

# Quick Definition

An affine group G is trigonalizable if every nonzero representation has a one-dimensional subrepresentation. Equivalently, G embeds into T_n (upper triangular matrices) for some n. Equivalently, G has a normal unipotent subgroup U with G/U diagonalizable.

# Core Definition

An affine group G is *trigonalizable* if every nonzero representation of G has a one-dimensional subrepresentation (Definition 16.1). The equivalent characterizations for algebraic groups are (Theorem 16.3): (a) G is trigonalizable; (b) G embeds into T_n for some n; (c) G has a normal unipotent subgroup U with G/U diagonalizable. Both diagonalizable and unipotent groups are trigonalizable. Subgroups and quotients of trigonalizable groups are trigonalizable (Corollary 16.4, Milne, pp. 182-184).

# Prerequisites

- **Linear representation** -- Trigonalizability is defined via representations
- **Unipotent group** -- The unipotent part in the structure
- **Diagonalizable group** -- The quotient G/U

# Key Properties

1. Equivalent to embedding into T_n (Theorem 16.3)
2. Equivalent to having normal unipotent U with G/U diagonalizable
3. Subgroups and quotients are trigonalizable (Corollary 16.4)
4. Preserved by base field extension (Corollary 16.5)
5. The exact sequence 1 -> U -> G -> G/U -> 1 splits under various conditions (Theorem 16.7): k algebraically closed, k of char 0, k perfect and G/U connected, or U split

# Context & Application

Trigonalizable groups bridge the gap between diagonalizable and unipotent groups. Every solvable group becomes trigonalizable over the algebraic closure (Lie-Kolchin theorem).

# Examples

**Example 1** (p. 189): T_n itself: the subnormal series T_n > G_0 > G_1 > ... > 1 exhibits it as solvable, with G_0 = U_n and T_n/U_n = D_n.

# Relationships

## Builds Upon
- **Unipotent group** -- The normal subgroup U
- **Diagonalizable group** -- The quotient G/U

## Enables
- **Solvable algebraic group** -- Connected smooth solvable groups are trigonalizable over k^al

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 16a, pages 182-184. Definition 16.1, Theorem 16.3.

# Verification Notes

- Definition source: Direct from Definition 16.1
- Confidence rationale: Explicit definition with equivalent characterizations
- Uncertainties: None
- Cross-reference status: Verified
