---
concept: Canonical Filtration on an Algebraic Group
slug: canonical-filtration
category: group-structure
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 196
section: "17c The canonical filtration on an algebraic group"
extraction_confidence: high
aliases: []
prerequisites:
  - radical-of-algebraic-group
  - semisimple-algebraic-group
extends: []
related:
  - reductive-algebraic-group
contrasts_with: []
answers_questions:
  - "What is a semisimple algebraic group?"
  - "What distinguishes the semisimple part from the radical of an algebraic group?"
---

# Quick Definition

Every algebraic group over a perfect field has a canonical filtration: first extract the connected component, then the smooth part, then the solvable radical (giving a semisimple quotient), then the unipotent radical of the solvable part (giving a multiplicative type quotient).

# Core Definition

Let G be an algebraic group over a field k (Milne, Theorem 17.14):
(a) G contains a unique connected normal subgroup G^0 with G/G^0 etale.
(b) (k perfect) G contains a largest smooth subgroup.
(c) (k perfect, G smooth connected) G has a unique smooth connected normal solvable subgroup N = RG with G/N semisimple.
(d) (k perfect, G smooth connected solvable) G has a unique connected unipotent subgroup N with G/N of multiplicative type.

# Prerequisites

- **Radical of algebraic group** -- The filtration uses RG
- **Semisimple algebraic group** -- G/RG is semisimple

# Key Properties

1. The filtration decomposes G into etale, smooth, solvable, and unipotent parts
2. Each step involves a canonical normal subgroup with a well-understood quotient
3. Over a perfect field, the theory is complete

# Context & Application

The canonical filtration shows that every algebraic group can be systematically decomposed into simpler pieces: etale groups, tori, semisimple groups, and unipotent groups. This is the master framework for the structure theory.

# Examples

**Example 1** (p. 196): For GL_n: G^0 = GL_n (already connected), RG = G_m (the centre), G/RG = PGL_n (semisimple).

# Relationships

## Builds Upon
- **Radical of algebraic group** -- RG appears in step (c)

## Related
- **Semisimple algebraic group** -- G/RG is semisimple
- **Reductive algebraic group** -- G/R_uG is reductive

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 17c, pages 196-197.

# Verification Notes

- Definition source: Direct from Theorem 17.14
- Confidence rationale: Explicit theorem
- Uncertainties: None
- Cross-reference status: Verified
