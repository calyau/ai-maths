---
concept: Klein Bottle
slug: klein-bottle
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
  - crosscap
  - sphere
extends:
  - sphere
related:
  - projective-plane
  - torus
contrasts_with:
  - torus
answers_questions:
  - "What is the Klein bottle?"
---

# Quick Definition
The Klein bottle is the surface obtained from the sphere by adding two crosscaps. It has Euler genus 2 and is non-orientable.

# Core Definition
The Klein bottle is S^2 with two crosscaps. By Lemma B.3, epsilon = 0 + 1 + 1 = 2, so chi = 0.

# Prerequisites
- **Surface**, **Crosscap**, **Sphere**

# Key Properties
1. Euler genus epsilon = 2 (same as the torus)
2. Euler characteristic chi = 0 (same as the torus)
3. Non-orientable (unlike the torus)
4. Cannot be embedded in R^3 without self-intersection

# Context & Application
The Klein bottle and the torus have the same Euler genus but differ in orientability. They demonstrate that the Euler genus alone does not determine the surface; orientability provides additional information.

# Relationships
## Builds Upon
- **Sphere** plus two **Crosscaps**

## Contrasts With
- **Torus** -- Same Euler genus but orientable

# Source Reference
Appendix B, pages 362-363.

# Verification Notes
- Derived from classification theorem
- Confidence: HIGH -- standard example
