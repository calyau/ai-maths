---
# === CORE IDENTIFICATION ===
concept: Torus (Algebraic)
slug: torus

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
aliases:
  - algebraic torus

# === TYPED RELATIONSHIPS ===
prerequisites:
  - affine-algebraic-group
  - multiplicative-group
extends:
  - multiplicative-type-group
related:
  - multiplicative-group
contrasts_with:
  - unipotent-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine algebraic group?"
---

# Quick Definition

A torus is a connected algebraic group of multiplicative type. Over an algebraically closed field, a torus is isomorphic to a product of copies of G_m (diagonal matrices).

# Core Definition

An affine algebraic subgroup T of GL(V) is said to be of **multiplicative type** if, over k^{al}, there exists a basis of V relative to which T is contained in the group D_n of all diagonal matrices (p. 16). A connected algebraic group of multiplicative type is a **torus**.

Tori are one of the five building block types of algebraic groups (Section 1a, p. 14-16).

# Prerequisites

- **Affine algebraic group** — Tori are algebraic groups
- **Multiplicative group** — G_m is the simplest torus

# Key Properties

1. Over k^{al}, every torus is isomorphic to G_m^n for some n
2. Elements of a torus are semisimple endomorphisms
3. Tori are commutative
4. A connected solvable group modulo its unipotent radical is a torus (summary 1c, p. 17)
5. A reductive group modulo its semisimple part has a torus as centre

# Examples

**Example 1** (p. 16): G_m = GL_1 is a one-dimensional torus.

**Example 2** (p. 16): D_n, the group of diagonal matrices in GL_n, is a torus isomorphic to G_m^n.

# Relationships

## Extends
- **Multiplicative type group** — A torus is the connected case

## Contrasts With
- **Unipotent group** — Tori have semisimple elements; unipotent groups have unipotent elements

# Source Reference

Chapter I, Section 1a (p. 16).

# Verification Notes

- Definition source: Direct from p. 16
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
