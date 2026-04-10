---
# === CORE IDENTIFICATION ===
concept: Group of Multiplicative Type
slug: multiplicative-type-group

# === CLASSIFICATION ===
category: classical-groups
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 16
section: "Introductory overview"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - affine-algebraic-group
extends: []
related:
  - torus
  - multiplicative-group
contrasts_with:
  - unipotent-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine algebraic group?"
---

# Quick Definition

An algebraic subgroup T of GL(V) is of multiplicative type if, over k^{al}, it can be diagonalized (embedded in D_n). A connected group of multiplicative type is a torus.

# Core Definition

An affine algebraic subgroup T of GL(V) is said to be of **multiplicative type** if, over k^{al}, there exists a basis of V relative to which T is contained in the group D_n of all diagonal matrices (p. 16). The elements of a group of multiplicative type are semisimple endomorphisms.

A connected algebraic group of multiplicative type is a **torus** (p. 16).

# Prerequisites

- **Affine algebraic group** — Groups of multiplicative type are algebraic groups

# Key Properties

1. Over k^{al}, embeds in D_n (diagonal matrices)
2. All elements are semisimple endomorphisms
3. Connected case = torus
4. mu_n (roots of unity) is of multiplicative type but not connected (not a torus)

# Relationships

## Related
- **Torus** — The connected case of multiplicative type
- **Multiplicative group** — G_m is the simplest group of multiplicative type

## Contrasts With
- **Unipotent group** — Semisimple elements vs unipotent elements

# Source Reference

Chapter I, Section 1a (p. 16).

# Verification Notes

- Definition source: Direct from p. 16
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
