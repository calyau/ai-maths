---
concept: Semisimple Root Datum
slug: semisimple-root-datum
category: reductive-groups
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "The Structure of Reductive Groups: The Split Case"
chapter_number: 5
pdf_page: 347
section: "Semisimple and toral root data"
extraction_confidence: high
aliases: []
prerequisites:
  - root-datum
extends:
  - root-datum
related:
  - toral-root-datum
  - root-system
contrasts_with:
  - toral-root-datum
answers_questions:
  - "What is a semisimple root datum?"
---

# Quick Definition

A root datum is semisimple if the roots R generate a subgroup of finite index in X. This corresponds to the reductive group being semisimple (having finite centre).

# Core Definition

A root datum (X, R, X^∨, R^∨) is **semisimple** if R generates a subgroup of finite index in X (Milne, Definition 2.15, p. 347). A split reductive group is semisimple if and only if its root datum is semisimple (Proposition 2.16).

To give a semisimple root datum is equivalent to giving a root system (V, R) together with a lattice X with Q ⊂ X ⊂ P (Proposition 5.17, p. 372).

# Prerequisites

- **Root datum** — A semisimple root datum is a special root datum

# Key Properties

1. G is semisimple iff its root datum is semisimple (Proposition 2.16)
2. Equivalently: X*(Z(G)) = X/ℤR is finite (from formula 172)
3. Classified by root systems + lattice choice Q ⊂ X ⊂ P

# Relationships

## Contrasts With
- **Toral root datum** — R = ∅ (group is a torus)

# Source Reference

Chapter V, Section 2l, Definitions 2.15–2.18, page 347; Section 5b, Proposition 5.17, page 372.

# Verification Notes

- Definition source: Direct from Definition 2.15
- Confidence: HIGH
- Uncertainties: None
