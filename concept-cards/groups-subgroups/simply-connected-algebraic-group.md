---
concept: Simply Connected Algebraic Group
slug: simply-connected-algebraic-group
category: semisimple-theory
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "The Structure of Semisimple Lie Algebras and Algebraic Groups in Characteristic Zero"
chapter_number: 3
pdf_page: 320
section: "An adjoint to the functor Lie"
extraction_confidence: high
aliases:
  - "G(𝔤)"
prerequisites:
  - split-semisimple-lie-algebra
  - weight-lattice
  - root-lattice
extends:
  - semisimple-algebraic-group
related:
  - adjoint-algebraic-group
contrasts_with:
  - adjoint-algebraic-group
answers_questions:
  - "What distinguishes a simply connected group from an adjoint group?"
---

# Quick Definition

The simply connected semisimple algebraic group G(𝔤) with Lie algebra 𝔤 is the Tannaka dual of Rep(𝔤). It is the unique semisimple group with character lattice X*(T) = P (the weight lattice), and every other group with Lie algebra 𝔤 is a quotient of it.

# Core Definition

Let 𝔤 be a semisimple Lie algebra over a field k of characteristic zero. The **simply connected** semisimple algebraic group G(𝔤) is defined as the Tannaka dual of the neutral tannakian category (Rep(𝔤), forget). Then (Milne, Theorem 3.12, p. 321):

(a) η: 𝔤 → Lie(G(𝔤)) is an isomorphism
(b) G(𝔤) is a semisimple algebraic group
(c) For any algebraic group H with 𝔤 ≅ Lie(H), there exists a unique isogeny G(𝔤) → H°
(d) X*(Z(G(𝔤))) ≅ P/Q

The character lattice of a split maximal torus T(𝔥) in G(𝔤) is the full weight lattice P (Theorem 3.14b).

# Prerequisites

- **Split semisimple Lie algebra** — G(𝔤) is constructed from 𝔤
- **Weight lattice** — X*(T) = P for the simply connected group
- **Root lattice** — The adjoint group has X*(T) = Q

# Key Properties

1. G(𝔤) is connected (Lemma 3.9)
2. It has the largest centre among groups with Lie algebra 𝔤
3. Centre Z(G(𝔤)) has character group P/Q (Theorem 3.12d)
4. Universal: every connected algebraic group with Lie algebra 𝔤 is a quotient

# Examples

**Example 1**: SL_{n+1} is simply connected of type A_n. Its centre is μ_{n+1}, and P/Q ≅ ℤ/(n+1)ℤ.

**Example 2**: SL₂ is the simply connected group of type A₁. PGL₂ is the adjoint group.

# Relationships

## Extends
- **Semisimple algebraic group** — A simply connected group is semisimple

## Contrasts With
- **Adjoint algebraic group** — Has X*(T) = Q (smallest centre, trivial)

# Source Reference

Chapter III, Section 3c–3d, Theorems 3.12 and 3.14, pages 320–323.

# Verification Notes

- Definition source: Direct from Theorem 3.12
- Confidence: HIGH
- Uncertainties: None
