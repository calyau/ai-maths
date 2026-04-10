---
concept: Simply Connected Semisimple Group
slug: simply-connected-semisimple-group
category: group-structure
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 198
section: "17d Semisimple groups"
extraction_confidence: high
aliases: []
prerequisites:
  - semisimple-algebraic-group
  - isogeny
extends:
  - semisimple-algebraic-group
related:
  - almost-simple-algebraic-group
contrasts_with: []
answers_questions:
  - "What is a semisimple algebraic group?"
---

# Quick Definition

A simply connected semisimple algebraic group is one for which every isogeny G' -> G is an isomorphism. Simply connected semisimple groups decompose as direct (not just almost-direct) products of almost-simple factors.

# Core Definition

A semisimple algebraic group G is **simply connected** if every isogeny G' -> G is an isomorphism (Milne, p. 198). For a simply connected group, the almost-direct product decomposition into almost-simple factors becomes a genuine direct product.

# Prerequisites

- **Semisimple algebraic group** -- Simply connected is an additional property of semisimple groups
- **Isogeny** -- The definition uses isogenies

# Key Properties

1. When G is simply connected, G_{k^{sep}} = G_1 x ... x G_r is a product of almost-simple factors
2. Every semisimple group has a finite covering by a simply connected semisimple group
3. Every simply connected semisimple group is a direct product of almost-simple groups (p. 222)
4. Simply connected almost-simple groups over k have the form (G_1)_{K/k} for geometrically almost-simple G_1 over some extension K (Proposition 17.19)

# Context & Application

Simply connected semisimple groups serve as universal covers in algebraic group theory. The classification of semisimple groups over arbitrary fields reduces to classifying simply connected geometrically almost-simple groups, which are described by their Dynkin diagrams and Galois cohomology.

# Examples

**Example 1** (p. 198): SL_n is simply connected. Every isogeny G' -> SL_n is an isomorphism.

# Relationships

## Builds Upon
- **Semisimple algebraic group** -- Simply connected is a strengthening

## Enables
- **Classification of semisimple groups** -- Reduces to classifying simply connected groups

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 17d, pages 198-199.

# Verification Notes

- Definition source: Direct from p. 198
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
