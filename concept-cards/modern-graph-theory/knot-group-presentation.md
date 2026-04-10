---
# === CORE IDENTIFICATION ===
concept: Knot Group Presentation
slug: knot-group-presentation

# === CLASSIFICATION ===
category: algebraic-graph-theory
subcategory: applications
tier: intermediate

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Graphs, Groups and Matrices"
chapter_number: 8
pdf_page: 263
section: "VIII.1 Cayley and Schreier Diagrams"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Dehn presentation of a knot group

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group-presentation
  - cayley-diagram
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How are group presentations used in knot theory?"
---

# Quick Definition

The fundamental group of a knot complement can be read off from a planar projection: each bounded domain gives a generator and each crossing gives a relator.

# Core Definition

Dehn showed how a presentation of the group of a tame knot (the fundamental group of $\mathbb{R}^3$ minus the knot) can be read from a projection. Each bounded domain corresponds to a generator (the identity to the unbounded domain), and each crossing yields a relator. The trefoil knot group is $\langle a, b, c \mid cb = ba = ac\rangle$, and the figure-eight knot group is $\langle a, b, c, d, e \mid ab^{-1}c, ad^{-1}eb^{-1}, ed^{-1}cb^{-1}, acd^{-1}\rangle$ (Bollobas, p. 263).

# Prerequisites

- **Group presentation** -- The algebraic framework
- **Cayley diagram** -- Used to investigate the resulting groups

# Key Properties

1. Each bounded region of the planar projection gives a generator
2. Each crossing gives a relator of a specific form
3. The presentation can be simplified by Tietze transformations
4. Two knots are inequivalent if their groups are non-isomorphic

# Construction / Recognition

## From Knot Diagram to Group Presentation
1. Project the knot into a plane
2. Label each bounded domain with a generator ($a, b, c, \ldots$)
3. At each crossing, read off the relator from the crossing type (see Fig. VIII.4)
4. Simplify the presentation

# Context & Application

Knot groups are a primary source of groups given by presentations in topology. Dehn was a strong advocate of using Cayley and Schreier diagrams to investigate these groups.

# Examples

**Example 1** (p. 263): The trefoil knot group simplifies to $\langle a, b, c \mid cb = ba = ac\rangle$.

**Example 2** (p. 263): The figure-eight knot has a more complex presentation.

# Relationships

## Builds Upon
- **Group presentation** -- The algebraic framework
- **Cayley diagram** -- Investigative tool

## Enables
- Knot invariant computation

## Related
- None

## Contrasts With
- None

# Common Errors

- **Error**: Forgetting to include the unbounded region as the identity
  **Correction**: The unbounded domain corresponds to the identity element; omitting it changes the presentation

# Common Confusions

- **Confusion**: Thinking non-isomorphic presentations mean non-isomorphic groups
  **Clarification**: Different presentations may give isomorphic groups; proving non-isomorphism requires additional tools

# Source Reference

Chapter VIII, Section VIII.1, pages 263--264. Fig. VIII.4.

# Verification Notes

- Definition source: Direct from pp. 263--264
- Confidence rationale: Explicit description with examples
- Uncertainties: None
- Cross-reference status: Verified
