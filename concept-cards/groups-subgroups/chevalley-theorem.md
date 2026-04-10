---
concept: Chevalley's Theorem
slug: chevalley-theorem
category: representations
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 112
section: "8m Chevalley's theorem"
extraction_confidence: high
aliases: []
prerequisites:
  - linear-representation
  - stabilizer-subgroup
  - faithful-representation
extends: []
related:
  - normal-subgroup-kernel
contrasts_with: []
answers_questions:
  - "How can subgroups of algebraic groups be characterized via representations?"
---

# Quick Definition

Chevalley's theorem states that every subgroup of an algebraic group G is the stabilizer of a one-dimensional subspace in some finite-dimensional representation of G.

# Core Definition

*Theorem 8.57 (Chevalley)*: Every subgroup of an algebraic group G is the stabilizer of a one-dimensional subspace in a finite-dimensional representation of G. The proof uses the fact that if H is a subgroup with ideal a = Ker(O(G) -> O(H)), one can find a finite-dimensional subcomodule V of O(G) containing generators for a, and then H = G_W where W = a intersect V. The key lemma (8.58) shows that stabilizing a subspace W is equivalent to stabilizing the one-dimensional subspace det(W) in the exterior power (Milne, pp. 112-114).

# Prerequisites

- **Linear representation** -- The representation in which the subgroup appears as a stabilizer
- **Stabilizer subgroup** -- The concept being used to characterize subgroups
- **Faithful representation** -- Ensures enough representations exist

# Key Properties

1. Every subgroup arises as a line stabilizer, not just a subspace stabilizer
2. The key reduction: stabilizing W is equivalent to stabilizing the line det(W) = wedge^{dim W} W
3. Corollary (8.59): Under additional conditions (semisimple representations of H, or characters extend), H is the subgroup fixing a vector in a faithful representation

# Context & Application

Chevalley's theorem is fundamental for reducing structural questions about algebraic groups to linear algebra. It shows that the relationship between a group and its subgroups can always be expressed in terms of one-dimensional actions.

# Examples

**Example 1** (p. 113): The Borel subgroup of GL_n stabilizes the line spanned by e_1 wedge e_2 wedge ... wedge e_m in the m-th exterior power of k^n.

# Relationships

## Builds Upon
- **Stabilizer subgroup** -- Subgroups are characterized as stabilizers

## Enables
- **Normal subgroup kernel** -- Used to show every normal subgroup is a kernel (8.70)

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 8m, pages 112-114. Theorem 8.57, Lemma 8.58, Corollary 8.59.

# Verification Notes

- Definition source: Direct from Theorem 8.57
- Confidence rationale: Explicit theorem with detailed proof
- Uncertainties: None
- Cross-reference status: Verified
