---
concept: Algebraic Lie Algebra
slug: algebraic-lie-algebra
category: lie-algebras
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Lie Algebras and Algebraic Groups"
chapter_number: 2
pdf_page: 252
section: "1m Algebraic Lie algebras"
extraction_confidence: medium
aliases:
  - "algebraic hull"
  - "algebraic envelope"
prerequisites:
  - lie-algebra-of-algebraic-group
extends: []
related:
  - lie-functor-properties
contrasts_with: []
answers_questions:
  - "How does the Lie algebra functor connect algebraic groups to Lie algebras?"
---

# Quick Definition

A Lie algebra is algebraic if it is the Lie algebra of an algebraic group. The algebraic envelope of a Lie subalgebra h of gl_V is the smallest algebraic Lie subalgebra containing h. Not every Lie subalgebra of gl_V is algebraic.

# Core Definition

A Lie algebra is **algebraic** if it is isomorphic to Lie(G) for some algebraic group G (Milne, p. 252). For a Lie subalgebra h of gl_V, the **algebraic envelope** (or **hull**) is the intersection of all algebraic Lie subalgebras containing h. A necessary condition for h to be algebraic is that the semisimple and nilpotent components of each element (as an endomorphism of V) lie in h, but this is not sufficient.

# Prerequisites

- **Lie algebra of algebraic group** -- Algebraic Lie algebras are those arising from groups

# Key Properties

1. A sum of algebraic Lie algebras is algebraic
2. Not every Lie subalgebra of gl_V is algebraic (Example 1.40)
3. In char 0, a connected algebraic subgroup of GL_n is determined by its Lie algebra as a subalgebra of gl_n (Theorem 2.11)

# Context & Application

Understanding which Lie algebras are algebraic is important for translating Lie algebra results to group-theoretic ones. In characteristic zero, the problem reduces to computing algebraic hulls.

# Examples

**Example 1** (p. 252): The five-dimensional solvable Lie algebra in 1.40 is not algebraic (its image in gl_V never has the closure property for semisimple/nilpotent components).

# Relationships

## Builds Upon
- **Lie algebra of algebraic group** -- Algebraic = arising from a group

## Related
- **Lie functor properties** -- The map H -> Lie(H) is injective on connected subgroups in char 0

# Source Reference

Chapter II: Lie Algebras and Algebraic Groups, Section 1m, pages 252-253.

# Verification Notes

- Definition source: Synthesized from p. 252
- Confidence rationale: Medium -- the section is marked as needing completion
- Uncertainties: Proofs marked as "need to prove"
- Cross-reference status: Verified
