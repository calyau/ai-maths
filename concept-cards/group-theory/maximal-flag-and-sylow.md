---
# === CORE IDENTIFICATION ===
concept: Maximal Flag and Sylow Subgroups
slug: maximal-flag-and-sylow

# === CLASSIFICATION ===
category: sylow-theory
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "The Sylow Theorems; Applications"
chapter_number: 5
pdf_page: 80
section: "The Sylow theorems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - sylow-p-subgroup
  - sylow-second-theorem
  - sylow-subgroup-of-gln
extends:
  - sylow-subgroup-of-gln
related:
  - solvable-borel-subgroup
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do Sylow p-subgroups of GL_n(F_p) relate to flags?"
---

# Quick Definition

The Sylow p-subgroups of GL(V) over F_p are precisely the groups U(F) of automorphisms preserving a maximal flag F and acting as the identity on each successive quotient. Conjugate Sylow subgroups correspond to different maximal flags.

# Core Definition

**Example 5.10.** A maximal flag F in V = F_p^n is a chain V = V_n superset V_(n-1) superset ... superset V_1 superset {0} with dim V_i = i. Given such F, let U(F) be the set of linear maps alpha : V -> V such that alpha(V_i) subset V_i for all i, and the induced map on V_i/V_(i-1) is the identity. Then U(F) is a Sylow p-subgroup of GL(V).

The Sylow p-subgroups of GL(V) are precisely the groups U(F) for maximal flags F, and U(gF) = g U(F) g^{-1}.

(Milne, Example 5.10, p. 80)

# Prerequisites

- **sylow-p-subgroup** -- U(F) is being identified as a Sylow p-subgroup
- **sylow-second-theorem** -- conjugacy of Sylow subgroups corresponds to the GL action on flags
- **sylow-subgroup-of-gln** -- the matrix form of U(F)

# Key Properties

1. Relative to an adapted basis, U(F) is the group of upper unitriangular matrices
2. Different flags give conjugate (hence all) Sylow p-subgroups
3. The conjugacy U(gF) = gU(F)g^{-1} is geometric: changing the flag by g conjugates the subgroup by g

# Context & Application

This provides a geometric interpretation of Sylow theory for the general linear group: Sylow p-subgroups biject with maximal flags, and conjugacy of Sylow subgroups corresponds to the transitive action of GL(V) on the set of maximal flags.

# Examples

**Example 1** (p. 80): For V = F_p^2, a maximal flag is a choice of line L in V. The Sylow p-subgroup U(F) fixes L pointwise and acts as the identity on V/L.

# Relationships

## Builds Upon
- **sylow-subgroup-of-gln** -- the matrix realization

## Enables
- **solvable-borel-subgroup** -- the Borel subgroup B(F) preserving the flag is solvable

# Source Reference

Chapter 5, Example 5.10, p. 80.

# Verification Notes

- Definition source: Direct from Example 5.10
- Confidence rationale: HIGH -- explicit geometric description
- Uncertainties: None
