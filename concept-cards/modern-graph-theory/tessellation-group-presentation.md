---
# === CORE IDENTIFICATION ===
concept: Tessellation from Group Presentation
slug: tessellation-group-presentation

# === CLASSIFICATION ===
category: algebraic-graph-theory
subcategory: geometric-group-theory
tier: intermediate

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Graphs, Groups and Matrices"
chapter_number: 8
pdf_page: 261
section: "VIII.1 Cayley and Schreier Diagrams"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - triangle group tessellation

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cayley-diagram
  - group-presentation
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do Cayley diagrams relate to tessellations?"
---

# Quick Definition

The group $(p, q, r) = \langle a, b, c \mid a^p = b^q = c^r = abc = 1\rangle$ has Cayley diagram that tessellates the sphere ($1/p + 1/q + 1/r > 1$), Euclidean plane (equality), or hyperbolic plane (strict inequality).

# Core Definition

**Theorem 1** (Bollobas, p. 261): If $1/p + 1/q + 1/r > 1$ then $(p,q,r)$ is finite with order $2s$ where $1/s = 1/p + 1/q + 1/r - 1$, and its Cayley diagram is a tessellation of the sphere. If $1/p + 1/q + 1/r \le 1$, the group is infinite; equality gives a Euclidean tessellation, strict inequality gives a hyperbolic tessellation.

# Prerequisites

- **Cayley diagram** -- The graphical object
- **Group presentation** -- The algebraic input

# Key Properties

1. Spherical: $(2,2,n)$, $(2,3,3)$, $(2,3,4)$, $(2,3,5)$ (finite groups)
2. Euclidean: $(2,3,6)$, $(2,4,4)$, $(3,3,3)$ (wallpaper groups)
3. Hyperbolic: all others (infinite groups, hyperbolic tessellations)
4. The finite cases give dihedral groups, $S_4$, $A_5$

# Construction / Recognition

## To Determine the Geometry
1. Compute $1/p + 1/q + 1/r$
2. If $> 1$: sphere (finite group)
3. If $= 1$: Euclidean plane (infinite group)
4. If $< 1$: hyperbolic plane (infinite group)

# Context & Application

This connects group presentations to geometry, showing how Cayley diagrams naturally embed in surfaces of constant curvature. It is a gateway to geometric group theory.

# Examples

**Example** (p. 261, Fig. VIII.3): Cayley diagrams of $(2,3,3)$ (tetrahedron), $(2,3,4)$ (cube/octahedron), $(2,3,5)$ (dodecahedron/icosahedron), and $(2,4,4)$ (square tiling).

# Relationships

## Builds Upon
- **Cayley diagram** -- The graphical representation
- **Group presentation** -- The input

## Enables
- Connections between algebra and geometry

## Related
- None

## Contrasts With
- None

# Common Errors

- **Error**: Forgetting the constraint $p \ge q \ge r \ge 2$
  **Correction**: The notation assumes this ordering; other orderings give isomorphic groups

# Common Confusions

- **Confusion**: Thinking $(p,q,r)$ is always a finite group
  **Clarification**: Only when $1/p + 1/q + 1/r > 1$; otherwise the group is infinite

# Source Reference

Chapter VIII, Section VIII.1, Theorem 1, page 261.

# Verification Notes

- Definition source: Direct from Theorem 1
- Confidence rationale: Explicit theorem
- Uncertainties: None
- Cross-reference status: Verified
