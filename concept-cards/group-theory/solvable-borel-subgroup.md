---
# === CORE IDENTIFICATION ===
concept: Solvable Borel Subgroup
slug: solvable-borel-subgroup

# === CLASSIFICATION ===
category: series-solvability
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Subnormal Series; Solvable and Nilpotent Groups"
chapter_number: 6
pdf_page: 89
section: "Solvable groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Borel subgroup solvability

# === TYPED RELATIONSHIPS ===
prerequisites:
  - solvable-group
extends: []
related:
  - maximal-flag-and-sylow
  - solvable-flag-subgroup
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Is the group of upper triangular matrices solvable?"
---

# Quick Definition

The Borel subgroup B (upper triangular invertible matrices) and more generally the flag-preserving subgroup B(F) are solvable. The solvable series is B > U > 1, where U is the unitriangular subgroup.

# Core Definition

**Example 6.5.** Consider the subgroups B = {upper triangular invertible matrices} and U = {upper triangular matrices with 1s on diagonal} of GL_2(F). Then U is normal in B, B/U is isomorphic to F* x F* (commutative), and U is isomorphic to (F, +) (commutative). Hence B is solvable.

**Example 6.8.** More generally, for any maximal flag F in a vector space V over a field k, the flag-preserving subgroup B(F) = {alpha in Aut(V) : alpha(V_j) subset V_j for all j} is solvable. The subgroups B_i = {alpha in B(F) : alpha induces identity on V_j/V_{j-i}} give a solvable series with B_0 = B(F) and the commutator of B_i-elements lies in B_{i+1}.

(Milne, Examples 6.5 and 6.8, pp. 89-91)

# Prerequisites

- **solvable-group** -- the property being verified

# Key Properties

1. B/U is a torus (product of copies of F*), hence commutative
2. U is a unipotent group, solvable (and nilpotent when the field is finite)
3. The series B = B_0 > B_1 > ... > B_n = {1} where B_i enforces identity on n-i diagonals

# Relationships

## Builds Upon
- **solvable-group** -- B is solvable

## Related
- **maximal-flag-and-sylow** -- the Sylow p-subgroup U(F) sits inside B(F)

# Source Reference

Chapter 6, Examples 6.5 and 6.8, pp. 89-91.

# Verification Notes

- Definition source: Direct from Examples 6.5, 6.8
- Confidence rationale: HIGH -- explicit examples
- Uncertainties: None
