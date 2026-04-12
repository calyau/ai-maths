---
concept: Tetrahedral Group
slug: tetrahedral-group
category: symmetry
subcategory: geometric-symmetry
tier: intermediate
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Symmetry"
chapter_number: 6
pdf_page: 162
section: "6.12 Finite Subgroups of the Rotation Group"
extraction_confidence: high
aliases:
  - "T"
prerequisites:
  - finite-subgroups-of-rotation-group
extends: []
related:
  - octahedral-group
  - icosahedral-group
contrasts_with: []
answers_questions:
  - "What is the tetrahedral group?"
---

# Quick Definition

The tetrahedral group T is the group of 12 rotational symmetries of a regular tetrahedron. It is isomorphic to the alternating group A_4.

# Core Definition

The tetrahedral group T consists of the 12 rotational symmetries of a regular tetrahedron (Artin, Theorem 6.12.1, p. 194). Its pole data is r_i = 2, 3, 3; n_i = 6, 4, 4; N = 12. It has 14 poles: 4 at face centers, 4 at vertices, and 6 at edge centers. It is isomorphic to A_4 (Example 7.11.5, p. 228).

# Prerequisites

- **Finite subgroups of rotation group** — T is one of the five types

# Key Properties

1. Order 12
2. Isomorphic to A_4
3. Poles: 4+4 (faces/vertices, stabilizer order 3) + 6 (edges, stabilizer order 2)
4. Presented as <x, y | x^3, y^3, xyxy> (Section 7.11)

# Examples

**Example 1** (p. 195): T has 11 non-identity elements: 8 rotations by 2pi/3 about vertices/face centers, and 3 rotations by pi about edge centers.

**Example 2** (p. 228): Todd-Coxeter shows T = <x, y | x^3, y^3, xyxy> with permutation representation x=(234), y=(123), confirming T = A_4.

# Relationships

## Related
- **Octahedral group** — Contains T as a subgroup
- **Generators and relations** — T = <x, y | x^3, y^3, xyxy>

# Source Reference

Chapter 6, Section 6.12; Chapter 7, Sections 7.10-7.11.

# Verification Notes

- Definition source: From Theorem 6.12.1 and Example 6.12.3
- Confidence rationale: Extensively discussed
- Uncertainties: None
- Cross-reference status: Verified
