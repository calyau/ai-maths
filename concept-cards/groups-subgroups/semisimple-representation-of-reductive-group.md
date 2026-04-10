---
concept: Semisimplicity of Representations of Reductive Groups
slug: semisimple-representation-of-reductive-group
category: semisimple-theory
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Lie Algebras and Algebraic Groups"
chapter_number: 2
pdf_page: 291
section: "6d Representations of reductive groups"
extraction_confidence: high
aliases: []
prerequisites:
  - reductive-algebraic-group
  - weyls-theorem
  - semisimple-algebraic-group
extends: []
related:
  - neutral-tannakian-category
contrasts_with: []
answers_questions:
  - "What is a reductive algebraic group?"
---

# Quick Definition

In characteristic zero, a connected algebraic group G is reductive if and only if every finite-dimensional representation of G is semisimple. More generally, all representations of G are semisimple iff G^0 is reductive.

# Core Definition

The following conditions on a connected algebraic group G (char 0) are equivalent: (a) G is reductive, (b) every finite-dimensional representation of G is semisimple, (c) some faithful representation is semisimple (Milne, Theorem 6.14). For nonconnected G, all representations are semisimple iff G^0 is reductive (Theorem 6.17).

# Prerequisites

- **Reductive algebraic group** -- The theorem characterizes reductivity
- **Weyl's theorem** -- Used for semisimple groups
- **Semisimple algebraic group** -- The derived group DG is semisimple

# Key Properties

1. (a) => (b): G = Z^0 . G' with Z^0 a torus and G' semisimple; decompose using characters of Z^0 and Weyl's theorem for G'
2. (c) => (a): A normal unipotent subgroup acts trivially on any semisimple representation
3. The restriction of a semisimple representation to a normal subgroup is semisimple (Lemma 6.15)
4. For nonconnected groups, averaging over G/G^0 produces equivariant projections (Lemma 6.18)
5. This result is FALSE in nonzero characteristic

# Context & Application

This theorem is the ultimate payoff of the Lie algebra approach to representation theory. It shows that in characteristic zero, the representation theory of a reductive group is "as nice as possible" -- completely reducible. This is the foundation for the use of reductive groups in the Langlands program and geometric representation theory.

# Examples

**Example 1** (p. 292): GL_V is reductive, so all its representations are semisimple (in char 0). A criterion: G = G^t for all bases implies G is reductive (Proposition 6.20).

# Relationships

## Builds Upon
- **Weyl's theorem** -- Provides semisimplicity for the derived group
- **Reductive algebraic group** -- The theorem characterizes reductivity

## Related
- **Neutral tannakian category** -- Rep(G) semisimple iff G^0 reductive (Theorem 6.17 connects to 21.21)

# Source Reference

Chapter II: Lie Algebras and Algebraic Groups, Sections 6d-6e, pages 291-293.

# Verification Notes

- Definition source: Direct from Theorems 6.14, 6.17
- Confidence rationale: Explicit theorems with proofs
- Uncertainties: None
- Cross-reference status: Verified
