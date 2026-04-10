---
concept: Solvable Lie Algebra
slug: solvable-lie-algebra
category: semisimple-theory
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Lie Algebras and Algebraic Groups"
chapter_number: 2
pdf_page: 264
section: "3a Definitions"
extraction_confidence: high
aliases: []
prerequisites:
  - lie-algebra
  - ideal-of-lie-algebra
extends: []
related:
  - nilpotent-lie-algebra
  - radical-of-lie-algebra
  - lies-theorem
contrasts_with:
  - nilpotent-lie-algebra
  - semisimple-lie-algebra
answers_questions:
  - "What distinguishes a nilpotent Lie algebra from a solvable Lie algebra?"
---

# Quick Definition

A Lie algebra g is solvable if it admits a filtration by ideals whose successive quotients are abelian -- equivalently, if its derived series g, [g,g], [[g,g],[g,g]], ... terminates with zero.

# Core Definition

A Lie algebra g is **solvable** if it admits a filtration g = a_0 > a_1 > ... > a_r = 0 by ideals such that each a_i/a_{i+1} is abelian (Milne, Definition 3.1). Equivalently, the **derived series** g > g' = [g,g] > g'' = [g',g'] > ... > g^{(i+1)} = [g^{(i)}, g^{(i)}] > ... terminates with zero (Proposition 3.2).

# Prerequisites

- **Lie algebra** -- Solvable is a property of Lie algebras
- **Ideal of Lie algebra** -- The filtration consists of ideals

# Key Properties

1. Subalgebras and quotients of solvable Lie algebras are solvable (Proposition 3.3a)
2. If n is a solvable ideal and g/n is solvable, then g is solvable (3.3b)
3. Every finite-dimensional Lie algebra has a largest solvable ideal (the radical, Corollary 3.4)
4. In char 0, if g is solvable and k is algebraically closed, then g is contained in b_n for some basis (Lie's theorem, 3.14)
5. If g is solvable (char 0), then [g,g] is nilpotent (Corollary 3.15)
6. g is solvable iff Tr(x o y) = 0 for all x,y in [g,g] (Cartan's criterion, 3.25/3.26)

# Context & Application

Solvable Lie algebras correspond to solvable algebraic groups under the Lie functor. The radical r(g) of any Lie algebra g is its largest solvable ideal, and g/r(g) is semisimple. Lie's theorem (the Lie algebra analogue of the Lie-Kolchin theorem) shows solvable subalgebras of gl_V can be simultaneously triangularized over algebraically closed fields of characteristic zero.

# Examples

**Example 1** (p. 264): b_3 (upper triangular 3x3 matrices) is solvable. Its derived algebra is contained in n_3 (strictly upper triangular matrices).

**Example 2** (p. 264): The Lie algebra <x,y | [x,y] = y> is solvable but not nilpotent.

# Relationships

## Builds Upon
- **Lie algebra** -- Solvable is a property of Lie algebras

## Enables
- **Radical of Lie algebra** -- The largest solvable ideal

## Contrasts With
- **Nilpotent Lie algebra** -- Nilpotent implies solvable but not conversely
- **Semisimple Lie algebra** -- r(g) = 0 means no solvable ideals

# Common Confusions

- **Confusion**: Believing every solvable Lie algebra is nilpotent
  **Clarification**: <x,y | [x,y] = y> is solvable but not nilpotent

# Source Reference

Chapter II: Lie Algebras and Algebraic Groups, Sections 3a, 3c, pages 264-268.

# Verification Notes

- Definition source: Direct from Definition 3.1
- Confidence rationale: Explicit definition with examples
- Uncertainties: None
- Cross-reference status: Verified
