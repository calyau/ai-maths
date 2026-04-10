---
concept: Witt Cancellation Theorem
slug: witt-cancellation-theorem
category: classical-groups
subcategory: quadratic-spaces
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 205
section: "18b Theorems of Witt and Cartan-Dieudonne"
extraction_confidence: high
aliases:
  - "Witt's theorem"
prerequisites:
  - quadratic-form
extends: []
related:
  - witt-index
  - witt-decomposition
contrasts_with: []
answers_questions:
  - "What is a Clifford algebra?"
---

# Quick Definition

Witt's theorem states that any isometry from a subspace of a regular quadratic space into the whole space can be extended to an isometry of the full space. The Witt cancellation theorem says that isometric regular summands can be cancelled from orthogonal decompositions.

# Core Definition

Let (V,q) be a regular quadratic space, and let sigma be an isometry from a subspace W of V into V. Then there exists a composite of reflections V -> V extending sigma (Milne, Theorem 18.2). As a corollary, if (V,q) = (V_1,q_1) + (V_2,q_2) = (V'_1,q'_1) + (V'_2,q'_2) with (V_1,q_1) and (V'_1,q'_1) regular and isometric, then (V_2,q_2) and (V'_2,q'_2) are isometric (Corollary 18.4).

# Prerequisites

- **Quadratic form** -- The theorem concerns regular quadratic spaces

# Key Properties

1. Every isometry of (V,q) is a composite of reflections (Corollary 18.3)
2. All maximal totally isotropic subspaces have the same dimension (Corollary 18.5)
3. The anisotropic part of a Witt decomposition is unique up to isometry (Theorem 18.9)

# Context & Application

Witt's theorem is foundational for the classification of quadratic forms and for the structure theory of orthogonal groups. It ensures that the Witt index and anisotropic part are well-defined invariants of a quadratic space.

# Examples

**Example 1** (p. 206): The Witt decomposition V = H_1 + ... + H_m + V_a decomposes a regular quadratic space into hyperbolic planes and an anisotropic part, both unique up to isometry.

# Relationships

## Builds Upon
- **Quadratic form** -- Concerns regular quadratic spaces

## Enables
- **Witt index** -- Well-defined by Witt cancellation
- **Orthogonal group** -- Structure theory uses Witt's theorem

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 18b, pages 204-206.

# Verification Notes

- Definition source: Direct from Theorem 18.2 and Corollary 18.4
- Confidence rationale: Explicit theorem statements with proofs
- Uncertainties: None
- Cross-reference status: Verified
