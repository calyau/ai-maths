---
concept: Radical of a Lie Algebra
slug: radical-of-lie-algebra
category: semisimple-theory
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Lie Algebras and Algebraic Groups"
chapter_number: 2
pdf_page: 265
section: "3a Definitions"
extraction_confidence: high
aliases:
  - "r(g)"
prerequisites:
  - solvable-lie-algebra
extends: []
related:
  - semisimple-lie-algebra
  - radical-of-algebraic-group
contrasts_with: []
answers_questions:
  - "What distinguishes the semisimple part from the radical of an algebraic group?"
---

# Quick Definition

The radical r(g) of a finite-dimensional Lie algebra g is its largest solvable ideal. The quotient g/r(g) is semisimple, and g is semisimple iff r(g) = 0.

# Core Definition

The **radical** of a Lie algebra g, denoted r(g), is the largest solvable ideal in g (Milne, Definition 3.5). It exists because the sum of two solvable ideals is again solvable (Proposition 3.3c). The quotient g/r(g) is semisimple (5.4), and g is semisimple iff r(g) = 0 (5.3).

# Prerequisites

- **Solvable Lie algebra** -- The radical is the largest solvable ideal

# Key Properties

1. r(g) exists in any finite-dimensional Lie algebra (Corollary 3.4)
2. g/r(g) is semisimple (5.4)
3. For a connected algebraic group G in char 0: Lie(RG) = r(Lie(G)) (Corollary 5.24)
4. r(g_{k'}) = k' tensor r(g) for any field extension k'/k (Corollary 5.14b)

# Context & Application

The radical provides the fundamental decomposition of any Lie algebra into its solvable part (the radical) and its semisimple part (the quotient). This mirrors the decomposition of algebraic groups via the radical.

# Examples

**Example 1**: For g = gl_n, the radical is the centre k.I (scalar matrices), and gl_n/r(gl_n) = sl_n/centre is semisimple.

# Relationships

## Builds Upon
- **Solvable Lie algebra** -- r(g) is the largest solvable ideal

## Enables
- **Semisimple Lie algebra** -- g is semisimple iff r(g) = 0

## Related
- **Radical of algebraic group** -- Lie(RG) = r(Lie(G)) in char 0

# Source Reference

Chapter II: Lie Algebras and Algebraic Groups, Section 3a, page 265.

# Verification Notes

- Definition source: Direct from Definition 3.5
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
