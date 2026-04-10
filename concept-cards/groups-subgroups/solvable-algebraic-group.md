---
concept: Solvable Algebraic Group
slug: solvable-algebraic-group
category: solvable-groups
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 188
section: "16d Solvable algebraic groups"
extraction_confidence: high
aliases:
  - solvable group
prerequisites:
  - derived-group
  - trigonalizable-group
extends: []
related:
  - lie-kolchin-theorem
  - unipotent-radical
  - split-solvable-group
contrasts_with: []
answers_questions:
  - "What is a solvable algebraic group?"
  - "What distinguishes a unipotent group from a solvable group?"
---

# Quick Definition

An algebraic group G is solvable if the derived series G > DG > D^2G > ... terminates with 1. Equivalently, G admits a subnormal series with commutative quotients. By the Lie-Kolchin theorem, a connected smooth solvable group over an algebraically closed field is trigonalizable.

# Core Definition

The *derived group* DG of G is the smallest normal subgroup with commutative quotient (Definition 16.17). An algebraic group G is *solvable* if the derived series G > DG > D^2G > ... terminates with 1 (Definition 16.25). Equivalently, G admits a subnormal series G = G_0 > G_1 > ... > G_n = 1 with commutative quotients G_i/G_{i+1} (Lemma 16.26). Subgroups, quotients, and extensions of solvable groups are solvable (Proposition 16.27, Milne, pp. 186-189).

# Prerequisites

- **Derived group** -- The derived series defines solvability
- **Trigonalizable group** -- Connected smooth solvable groups are trigonalizable over k^al

# Key Properties

1. Subgroups, quotients, and extensions of solvable groups are solvable (Proposition 16.27)
2. (Lie-Kolchin, Theorem 16.31): A connected smooth solvable G over k^al embeds into T_n
3. All hypotheses in Lie-Kolchin are necessary: connected, smooth, solvable, k algebraically closed
4. For connected solvable smooth G over a perfect field, there exists a unique G_u (Theorem 16.33)
5. DG is connected if G is connected (Corollary 16.21)
6. DG is smooth if G is smooth (Corollary 16.21)

# Construction / Recognition

## To Construct:
1. Take subgroups of T_n (upper triangular matrices)
2. Or build extensions of commutative groups

## To Recognize:
1. Compute the derived series and check it terminates
2. Or find a subnormal series with commutative quotients

# Context & Application

Solvable groups occupy the middle ground between commutative groups and general groups. The structure theory shows that a connected solvable smooth group over a perfect field decomposes as an extension of a torus by its unipotent radical G_u.

# Examples

**Example 1** (p. 189): T_n is solvable: T_3 > U_3 > {matrices with 0 in (1,2) and (2,3)} > {matrices with 0 in (1,2), (2,3), (1,3)} > 1. Quotients: G_m^3, G_a^2, G_a.

**Example 2** (p. 189): The group of monomial matrices is solvable iff n <= 4 (because S_n is solvable iff n <= 4).

**Example 3** (p. 189): The Borel subgroup B of GL_n (upper triangular matrices) is solvable and connected.

# Relationships

## Builds Upon
- **Trigonalizable group** -- Solvable groups are trigonalizable over k^al
- **Derived group** -- Solvability is defined via the derived series

## Enables
- **Unipotent radical** -- G_u is defined for connected solvable smooth groups
- **Structure of algebraic groups** -- Solvable radical RG

## Contrasts With
- (implicitly) Semisimple groups -- Groups with trivial solvable radical

# Common Errors

- **Error**: Applying Lie-Kolchin without checking all hypotheses
  **Correction**: All four conditions are needed: connected, smooth, solvable, k algebraically closed. Each has explicit counterexamples (see 16.32).

# Common Confusions

- **Confusion**: Confusing solvable with unipotent
  **Clarification**: Unipotent groups are solvable (D^n(U_n) = 1) but not conversely. A split torus G_m is solvable (even commutative) but not unipotent. Solvable = extension of commutative groups; unipotent = extension of subgroups of G_a.

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 16d, pages 188-192. Definition 16.25, Theorem 16.31, Theorem 16.33.

# Verification Notes

- Definition source: Direct from Definition 16.25
- Confidence rationale: Explicit definition with major structural theorems
- Uncertainties: None
- Cross-reference status: Verified
