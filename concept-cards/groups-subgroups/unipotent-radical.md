---
concept: Unipotent Radical
slug: unipotent-radical
category: group-structure
subcategory: radicals
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 194
section: "17a Radicals and unipotent radicals"
extraction_confidence: high
aliases:
  - "R_uG"
  - "R_u(G)"
prerequisites:
  - unipotent-algebraic-group
  - connected-algebraic-group
  - normal-subgroup
extends: []
related:
  - radical-of-algebraic-group
  - reductive-algebraic-group
  - semisimple-algebraic-group
contrasts_with:
  - radical-of-algebraic-group
answers_questions:
  - "What is a reductive algebraic group?"
  - "What distinguishes a reductive group from a semisimple group?"
---

# Quick Definition

The unipotent radical R_uG of a smooth algebraic group G is the largest smooth connected normal unipotent subgroup of G. A group is reductive precisely when its geometric unipotent radical is trivial.

# Core Definition

Let G be a smooth algebraic group over a field k. The **unipotent radical** R_uG is the unique largest smooth connected normal unipotent subgroup of G (Milne, Proposition 17.2b). The **geometric unipotent radical** is R_uG_{k^{al}}, the unipotent radical computed over the algebraic closure.

# Prerequisites

- **Unipotent algebraic group** -- R_uG must be unipotent
- **Connected algebraic group** -- R_uG is required to be connected
- **Normal subgroup** -- R_uG must be normal in G

# Key Properties

1. R_uG is the unipotent part of the radical: R_uG = (RG)_u (Proposition 17.3)
2. Over a perfect field, formation commutes with base change: R_u(G_K) = (R_uG)_K
3. G/R_uG is reductive (Proposition 17.9)
4. A normal unipotent subgroup acts trivially on every semisimple representation of G (Proposition 17.11)
5. R_uG is contained in the intersection of the kernels of all semisimple representations

# Construction / Recognition

## To Construct:
1. Start with a smooth algebraic group G
2. Find all smooth connected normal unipotent subgroups
3. The unipotent radical is the unique maximal such subgroup

## To Recognize:
1. Check the subgroup is smooth, connected, normal, and unipotent
2. Verify maximality

# Context & Application

The unipotent radical provides the fundamental dichotomy in the structure of algebraic groups: G is reductive if and only if R_uG_{k^{al}} = 1. In characteristic zero, G is reductive if and only if Rep(G) is semisimple, and R_uG equals the intersection of the kernels of all semisimple representations (proved in Ch II).

# Examples

**Example 1** (p. 196): For the group G of invertible matrices (A B; 0 C), the unipotent radical is the subgroup of matrices (I B; 0 I). The quotient G/R_uG is isomorphic to GL_m x GL_n.

# Relationships

## Builds Upon
- **Unipotent algebraic group** -- R_uG is the largest normal connected unipotent subgroup

## Enables
- **Reductive algebraic group** -- G is reductive iff R_uG_{k^{al}} = 1

## Related
- **Radical of algebraic group** -- R_uG = (RG)_u

## Contrasts With
- **Radical of algebraic group** -- RG is solvable; R_uG is the unipotent part of RG

# Common Errors

- **Error**: Assuming R_uG = 1 implies semisimplicity
  **Correction**: R_uG = 1 means reductive, not semisimple; semisimple requires the full radical RG = 1

# Common Confusions

- **Confusion**: Conflating "reductive" and "pseudoreductive" when k is not perfect
  **Clarification**: Over imperfect fields, R_uG = 1 (pseudoreductive) does not imply R_uG_{k^{al}} = 1 (reductive)

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 17a, pages 193-194.

# Verification Notes

- Definition source: Direct from Proposition 17.2b
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
