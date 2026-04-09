---
concept: Orientable and Non-Orientable Surfaces
slug: orientable-surface
category: topological-graph-theory
subcategory: surfaces
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Appendix B - Surfaces"
chapter_number: null
pdf_page: 374
section: null
extraction_confidence: high
aliases:
  - "orientability"
  - "two-sided"
  - "one-sided"
prerequisites:
  - surface
  - handle
  - crosscap
extends: []
related:
  - cylinder
  - mobius-strip
contrasts_with: []
answers_questions:
  - "What is an orientable surface?"
  - "What is a non-orientable surface?"
  - "What does it mean for a circle to be one-sided or two-sided?"
---

# Quick Definition
A surface is orientable if it contains no one-sided circles (no Mobius strips as neighbourhoods). Surfaces built from handles only are orientable; adding any crosscap makes the surface non-orientable.

# Core Definition
A circle C in a surface S has a strip neighbourhood that is either a cylinder (C is two-sided) or a Mobius strip (C is one-sided). If C is one-sided, it is non-separating. Surfaces built from handles are orientable; those with crosscaps are non-orientable (Diestel, p. 362).

# Prerequisites
- **Surface**, **Handle**, **Crosscap**

# Key Properties
1. Orientable surfaces: S^2, torus, genus-g surface (handles only)
2. Non-orientable surfaces: projective plane, Klein bottle (crosscaps)
3. A circle is two-sided if its strip neighbourhood is a cylinder
4. A circle is one-sided if its strip neighbourhood is a Mobius strip
5. One-sided circles are always non-separating
6. Two-sided circles can be separating or non-separating

# Relationships
## Related
- **Cylinder** -- Strip neighbourhood of a two-sided circle
- **Mobius strip** -- Strip neighbourhood of a one-sided circle
- **Handle** -- Produces orientable surfaces
- **Crosscap** -- Produces non-orientable surfaces

# Source Reference
Appendix B, page 362.

# Verification Notes
- Definitions from p. 362
- Confidence: HIGH -- explicit definitions
