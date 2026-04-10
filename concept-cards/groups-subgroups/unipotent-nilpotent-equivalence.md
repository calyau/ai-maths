---
concept: Unipotent-Nilpotent Equivalence
slug: unipotent-nilpotent-equivalence
category: lie-algebras
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Lie Algebras and Algebraic Groups"
chapter_number: 2
pdf_page: 274
section: "4 Unipotent algebraic groups and nilpotent Lie algebras"
extraction_confidence: high
aliases: []
prerequisites:
  - nilpotent-lie-algebra
  - unipotent-algebraic-group
  - hausdorff-series
extends: []
related:
  - lie-algebra-of-algebraic-group
contrasts_with: []
answers_questions:
  - "How does the Lie algebra functor connect algebraic groups to Lie algebras?"
---

# Quick Definition

In characteristic zero, the functor Lie is an equivalence from the category of unipotent algebraic groups to the category of finite-dimensional nilpotent Lie algebras. The quasi-inverse sends a nilpotent Lie algebra g to the group (g_a, Hausdorff multiplication).

# Core Definition

Assume char(k) = 0. The functor g -> g_a (with multiplication from the Hausdorff series) is an equivalence from finite-dimensional nilpotent Lie algebras to unipotent algebraic groups, with quasi-inverse G -> Lie(G) (Milne, Theorem 4.7). A connected smooth algebraic group G is unipotent iff Lie(G) is nilpotent and Z(G) is unipotent (Corollary 4.5).

# Prerequisites

- **Nilpotent Lie algebra** -- One side of the equivalence
- **Unipotent algebraic group** -- The other side
- **Hausdorff series** -- Provides the group multiplication

# Key Properties

1. The equivalence requires char(k) = 0
2. Ado's theorem provides the embedding needed for the construction
3. Commutative Lie algebras correspond to commutative unipotent groups (Remark 4.9)
4. Every Lie subalgebra of gl_V consisting of nilpotent endomorphisms is algebraic (Corollary 4.8)

# Context & Application

This is the strongest connection between algebraic groups and Lie algebras in the nilpotent/unipotent case. In characteristic p, the situation is much more complicated: unipotent groups can be very exotic.

# Examples

**Example 1** (p. 276): Commutative unipotent groups over a char 0 field are equivalent to finite-dimensional vector spaces via U -> Lie(U) and V -> V_a.

# Relationships

## Builds Upon
- **Hausdorff series** -- Provides the group multiplication

## Related
- **Lie algebra of algebraic group** -- The functor Lie provides one direction

# Source Reference

Chapter II: Lie Algebras and Algebraic Groups, Section 4, pages 273-276.

# Verification Notes

- Definition source: Direct from Theorem 4.7
- Confidence rationale: Explicit theorem
- Uncertainties: None
- Cross-reference status: Verified
