---
concept: Strip Neighbourhood
slug: strip-neighbourhood
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
aliases: []
prerequisites:
  - surface
  - cylinder
  - mobius-strip
extends: []
related:
  - orientable-surface
  - separating-circle
contrasts_with: []
answers_questions:
  - "What is a strip neighbourhood of a circle on a surface?"
---

# Quick Definition
A strip neighbourhood of a circle C on a surface S is either a cylinder or a Mobius strip N containing C as its middle circle. If N is a cylinder, C is two-sided; if N is a Mobius strip, C is one-sided.

# Core Definition
"Every circle C in a surface S is the middle circle of a suitable cylinder or Mobius strip N in S, which can be chosen small enough to avoid any given compact subset of S \ C. If this strip neighbourhood is a cylinder, then N \ C has two components and we call C two-sided; if it is a Mobius strip, then N \ C has only one component and we call C one-sided" (Diestel, p. 362).

# Prerequisites
- **Surface**, **Cylinder**, **Mobius strip**

# Key Properties
1. Every circle has a strip neighbourhood
2. Determines whether the circle is one-sided or two-sided
3. Can be chosen arbitrarily small (avoiding any compact set)

# Relationships
## Enables
- **Orientable surface** -- Determines one-sided vs two-sided circles

# Source Reference
Appendix B, page 362.

# Verification Notes
- From p. 362
- Confidence: HIGH
