---
concept: Split Semisimple Algebraic Group
slug: split-semisimple-algebraic-group
category: semisimple-theory
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "The Structure of Semisimple Lie Algebras and Algebraic Groups in Characteristic Zero"
chapter_number: 3
pdf_page: 323
section: "Split semisimple algebraic groups"
extraction_confidence: high
aliases: []
prerequisites:
  - semisimple-algebraic-group
  - split-maximal-torus
extends:
  - semisimple-algebraic-group
related:
  - simply-connected-algebraic-group
  - adjoint-algebraic-group
  - split-reductive-group
contrasts_with: []
answers_questions:
  - "What is a split semisimple algebraic group?"
---

# Quick Definition

A split semisimple algebraic group is a pair (G,T) where G is semisimple and T is a split maximal torus. It is classified by a "diagram" (V, R, X): a root system plus a lattice Q ⊂ X ⊂ P.

# Core Definition

A **split semisimple algebraic group** is a pair (G, T) consisting of a semisimple algebraic group G and a split maximal torus T (Milne, Definition 3.16, p. 323).

The roots of (G,T) form a reduced root system R in V = X*(T) ⊗ ℚ, and Q(R) ⊂ X*(T) ⊂ P(R) (Proposition 3.18). A **diagram** (V, R, X) classifies these groups: every diagram arises (Theorem 3.19), and isogenies correspond to maps of diagrams (Theorem 3.21).

# Prerequisites

- **Semisimple algebraic group** — Must be semisimple
- **Split maximal torus** — Must contain a split maximal torus

# Key Properties

1. Classified by diagrams (V, R, X) with Q ⊂ X ⊂ P (Theorems 3.19–3.21)
2. Any two split maximal tori are conjugate by G(k) (Theorem 3.17)
3. X = P gives the simply connected group; X = Q gives the adjoint group

# Examples

**Example 1**: SL_{n+1} is split semisimple of type A_n with X = P (simply connected).

**Example 2**: PGL_{n+1} is split semisimple of type A_n with X = Q (adjoint).

# Source Reference

Chapter III, Sections 3d–3e, pages 322–325.

# Verification Notes

- Definition source: Direct from Definition 3.16
- Confidence: HIGH
- Uncertainties: None
