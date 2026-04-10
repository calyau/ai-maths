---
concept: Reductive Lie Algebra
slug: reductive-lie-algebra
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
  - semisimple-lie-algebra
extends: []
related:
  - reductive-algebraic-group
contrasts_with:
  - semisimple-lie-algebra
answers_questions:
  - "What distinguishes a reductive group from a semisimple group?"
---

# Quick Definition

A Lie algebra g is reductive if its radical equals its centre. Equivalently, g decomposes as g = c x [g,g] with c commutative and [g,g] semisimple.

# Core Definition

A Lie algebra g is **reductive** if its radical equals its centre: r(g) = z(g) (Milne, 5.6). A reductive Lie algebra decomposes as g = c x [g,g] with c commutative (the centre) and [g,g] semisimple.

# Prerequisites

- **Lie algebra** -- Reductive is a property of Lie algebras
- **Radical of Lie algebra** -- Defined via the radical
- **Semisimple Lie algebra** -- The derived algebra is semisimple

# Key Properties

1. g = z(g) x [g,g] with [g,g] semisimple (5.6)
2. semisimple implies reductive (since r(g) = 0 = z(g) for semisimple g with z(g) = 0)
3. For a reductive algebraic group G, Lie(G) need not be reductive as a Lie algebra in the sense that Rep(Lie(G)) is semisimple (Aside 6.6)

# Context & Application

Reductive Lie algebras are the Lie algebra analogue of reductive algebraic groups. However, the correspondence is not perfect: for a reductive group G in char 0, Lie(G) is reductive, but not all representations of Lie(G) are semisimple (some representations of the Lie algebra do not arise from the group).

# Examples

**Example 1**: gl_n = k.I_n x sl_n is reductive: the centre is the scalar matrices and the derived algebra is sl_n.

# Relationships

## Related
- **Reductive algebraic group** -- The group analogue

## Contrasts With
- **Semisimple Lie algebra** -- Semisimple means r(g) = 0; reductive allows r(g) = z(g)

# Source Reference

Chapter II: Lie Algebras and Algebraic Groups, Section 5a, page 277.

# Verification Notes

- Definition source: Direct from 5.6
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
