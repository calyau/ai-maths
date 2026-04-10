---
concept: Semisimple Lie Algebra
slug: semisimple-lie-algebra
category: semisimple-theory
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Lie Algebras and Algebraic Groups"
chapter_number: 2
pdf_page: 277
section: "5a Semisimple Lie algebras"
extraction_confidence: high
aliases: []
prerequisites:
  - lie-algebra
  - radical-of-lie-algebra
  - killing-form
extends: []
related:
  - semisimple-algebraic-group
  - simple-lie-algebra
  - reductive-lie-algebra
contrasts_with:
  - solvable-lie-algebra
  - reductive-lie-algebra
answers_questions:
  - "What is the Killing form?"
  - "What distinguishes a reductive group from a semisimple group?"
---

# Quick Definition

A Lie algebra g is semisimple if its only abelian ideal is {0} -- equivalently, if its radical is zero, or if its Killing form is nondegenerate. Every semisimple Lie algebra is a direct product of simple Lie algebras.

# Core Definition

A Lie algebra g is **semisimple** if its only abelian ideal is {0} (Milne, Definition 5.1). Equivalently: (1) r(g) = 0 (5.3), (2) the Killing form kappa_g is nondegenerate (Theorem 5.13, the Cartan-Killing criterion), (3) g is a direct product of simple Lie algebras (Theorem 5.16).

# Prerequisites

- **Lie algebra** -- Semisimple is a property of Lie algebras
- **Radical of Lie algebra** -- r(g) = 0 characterizes semisimplicity
- **Killing form** -- Nondegeneracy of kappa characterizes semisimplicity

# Key Properties

1. g is semisimple iff every abelian ideal is zero (Definition 5.1)
2. g is semisimple iff kappa_g is nondegenerate (Theorem 5.13)
3. A semisimple g decomposes: g = a_1 x ... x a_r with a_i simple (Theorem 5.16)
4. Every ideal and quotient of a semisimple algebra is semisimple (Corollary 5.17)
5. If g is semisimple, then [g,g] = g (Corollary 5.18)
6. Every derivation of a semisimple g is inner: ad: g -> Der(g) is an isomorphism (Theorem 5.21)
7. In char 0, G is semisimple iff Lie(G) is semisimple (Theorem 5.23)
8. Every trace form on a semisimple g (for a faithful representation) is nondegenerate (Proposition 5.9)

# Construction / Recognition

## To Recognize:
1. Check that no abelian ideal exists (other than 0)
2. Or compute the Killing form and check nondegeneracy
3. Or check that the radical r(g) is zero

# Context & Application

Semisimple Lie algebras are the Lie algebra counterpart of semisimple algebraic groups. Their structure is completely understood via Dynkin diagrams. The classification (over algebraically closed fields of char 0) identifies them with direct products of simple Lie algebras of types A_n, B_n, C_n, D_n, E_6, E_7, E_8, F_4, G_2.

# Examples

**Example 1** (p. 277): The zero algebra is semisimple, but no algebra of dimension 1 or 2 is.

**Example 2** (p. 278): sl_2 is semisimple (confirmed by computing its Killing form, which has nonzero determinant -128).

**Example 3** (p. 277): A product g_1 x ... x g_n of semisimple algebras is semisimple (5.5).

# Relationships

## Builds Upon
- **Killing form** -- Nondegeneracy characterizes semisimplicity
- **Radical of Lie algebra** -- r(g) = 0 characterizes semisimplicity

## Enables
- **Simple Lie algebra** -- Semisimple decomposes into simple factors
- **Semisimple algebraic group** -- In char 0, Lie(G) semisimple iff G semisimple

## Contrasts With
- **Solvable Lie algebra** -- Solvable means r(g) = g; semisimple means r(g) = 0
- **Reductive Lie algebra** -- Reductive means r(g) = z(g); semisimple means r(g) = 0

# Common Confusions

- **Confusion**: Believing a Lie algebra of dimension 1 could be semisimple
  **Clarification**: One-dimensional Lie algebras are abelian, hence not semisimple (they ARE an abelian ideal of themselves)

# Source Reference

Chapter II: Lie Algebras and Algebraic Groups, Section 5a, pages 277-282.

# Verification Notes

- Definition source: Direct from Definition 5.1
- Confidence rationale: Explicit definition with multiple equivalent characterizations
- Uncertainties: None
- Cross-reference status: Verified
