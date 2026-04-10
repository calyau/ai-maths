---
concept: Split Reductive Group
slug: split-reductive-group
category: reductive-groups
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "The Structure of Reductive Groups: The Split Case"
chapter_number: 5
pdf_page: 336
section: "Split reductive groups"
extraction_confidence: high
aliases: []
prerequisites:
  - reductive-algebraic-group
  - split-maximal-torus
extends:
  - reductive-algebraic-group
related:
  - root-datum
  - split-semisimple-algebraic-group
contrasts_with:
  - anisotropic-algebraic-group
answers_questions:
  - "What is a split reductive group?"
---

# Quick Definition

A reductive group is split if it contains a split maximal torus. A split reductive group (G,T) is a pair consisting of a reductive group and a chosen split maximal torus, and is classified up to isomorphism by its root datum Ψ(G,T).

# Core Definition

A reductive group G over k is **split** if it contains a split maximal torus T (i.e., a split torus T ⊂ G such that T_{k^{sep}} is maximal in G_{k^{sep}}). A **split reductive group** is a pair (G,T) (Milne, 1.11, p. 337).

Any two split maximal tori are conjugate by an element of G(k) (1.12, proved in 3.22). The root datum Ψ(G,T) determines (G,T) up to isomorphism, and every root datum arises from some (G,T) (1.13–1.16).

# Prerequisites

- **Reductive algebraic group** — Split reductive groups are a special class
- **Split maximal torus** — Required for splitting

# Key Properties

1. A reductive group over a separably closed field is automatically split (p. 336)
2. The isomorphism class of (G,T) depends only on G (since split maximal tori are conjugate)
3. The root datum has nothing to do with the field (1.16)
4. For each reductive group over k^{al}, there is exactly one split reductive group over k that becomes isomorphic to it over k^{al}

# Examples

**Example 1** (p. 336): GL_n is split with split maximal torus 𝔻_n.

**Example 2** (p. 336): The quaternionic group ℍ× over ℝ is not split: its derived group has compact real points, so it cannot contain a split torus.

# Relationships

## Extends
- **Reductive algebraic group** — Split is a special case

## Enables
- **Root datum** — Ψ(G,T) classifies split reductive groups

## Contrasts With
- **Anisotropic algebraic group** — No non-trivial split torus

# Source Reference

Chapter V, Section 1c–1d, pages 336–338.

# Verification Notes

- Definition source: Direct from 1.11
- Confidence: HIGH
- Uncertainties: None
