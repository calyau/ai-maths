---
concept: Adjoint Algebraic Group
slug: adjoint-algebraic-group
category: semisimple-theory
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "The Structure of Semisimple Lie Algebras and Algebraic Groups in Characteristic Zero"
chapter_number: 3
pdf_page: 324
section: "Classification"
extraction_confidence: high
aliases:
  - "adjoint group"
prerequisites:
  - simply-connected-algebraic-group
  - root-lattice
extends:
  - semisimple-algebraic-group
related:
  - split-semisimple-algebraic-group
contrasts_with:
  - simply-connected-algebraic-group
answers_questions:
  - "What distinguishes a simply connected group from an adjoint group?"
---

# Quick Definition

The adjoint algebraic group of a given root system is the semisimple group with character lattice X*(T) = Q (the root lattice). It has trivial centre and is the quotient of the simply connected group by its full centre.

# Core Definition

A split semisimple algebraic group (G,T) with root system (V,R) is **adjoint** if X*(T) = Q(R) (the root lattice). Equivalently, G = G(𝔤)/Z(G(𝔤)), the quotient of the simply connected group by its entire centre. The adjoint group has trivial centre (Milne, §3e, p. 324).

# Prerequisites

- **Simply connected algebraic group** — The adjoint group is a quotient of this
- **Root lattice** — X*(T) = Q for the adjoint group

# Key Properties

1. Trivial centre: Z(G) = 1
2. X*(T) = Q (the smallest possible character lattice)
3. Every semisimple group G surjects onto the adjoint group G/Z(G)

# Examples

**Example 1**: PGL_{n+1} is the adjoint group of type A_n. Its character lattice is Q = ℤ{e_i − e_j}.

**Example 2**: PGL₂ is the adjoint group of type A₁. It has root datum (ℤ, {1,−1}, ℤ, {2,−2}).

# Relationships

## Contrasts With
- **Simply connected algebraic group** — Has X*(T) = P (largest centre)

# Source Reference

Chapter III, Section 3e, pages 324–325; Chapter V, §2d (PGL₂ example).

# Verification Notes

- Definition source: Synthesized from §3e and Ch. V discussion
- Confidence: HIGH
- Uncertainties: None
