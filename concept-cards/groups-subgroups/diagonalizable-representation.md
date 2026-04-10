---
concept: Diagonalizable Representation
slug: diagonalizable-representation
category: representations
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 166
section: "14d Diagonalizable groups"
extraction_confidence: high
aliases: []
prerequisites:
  - linear-representation
  - character-of-affine-group
extends:
  - linear-representation
related:
  - diagonalizable-group
  - eigenspace
contrasts_with: []
answers_questions:
  - "What is a diagonalizable representation?"
---

# Quick Definition

A representation of an affine group is diagonalizable if it is a sum of one-dimensional representations (equivalently, a direct sum by Lemma 8.68). A group is diagonalizable iff all its representations are diagonalizable.

# Core Definition

A representation of an affine group is *diagonalizable* if it is a sum of one-dimensional representations (Definition 14.14). By Lemma 8.68, this is automatically a direct sum. A finite-dimensional representation (V,r) is diagonalizable iff there exists a basis such that r(G) subset D_n (diagonal matrices). An affine group G is diagonalizable iff every representation is diagonalizable iff V = direct-sum V_chi for all representations (Theorem 14.15, Milne, pp. 166-169).

# Prerequisites

- **Linear representation** -- Diagonalizable is a property of representations
- **Character of affine group** -- The 1-dimensional summands correspond to characters

# Key Properties

1. A sum of 1-dimensional representations is automatically direct (Lemma 8.68)
2. G diagonalizable iff every representation is diagonalizable (Theorem 14.15)
3. Equivalent to V = direct-sum V_chi (eigenspace decomposition)
4. The eigenspaces are indexed by characters of G

# Context & Application

Diagonalizable representations are the simplest type: they decompose completely into characters. For tori, every representation is diagonalizable.

# Examples

**Example 1** (p. 167): For D_n = G_m^n acting on k^n by scalar multiplication in each coordinate, the standard representation is diagonalizable with 1-dimensional eigenspaces.

# Relationships

## Builds Upon
- **Character of affine group** -- Each summand is a character

## Related
- **Diagonalizable group** -- Groups where all representations are diagonalizable
- **Eigenspace** -- The summands in the decomposition

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 14d, pages 166-169. Definition 14.14, Theorem 14.15.

# Verification Notes

- Definition source: Direct from Definition 14.14
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
