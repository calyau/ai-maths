---
concept: "Grotzsch's Theorem"
slug: grotzsch-theorem
category: graph-colouring
subcategory: planar-colouring
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Colouring"
chapter_number: 5
pdf_page: 122
section: "5.1 Colouring maps and planar graphs"
extraction_confidence: medium
aliases:
  - "Theorem 5.1.3"
  - "Grotzsch 1959"
prerequisites:
  - chromatic-number
  - planar-graph
extends: []
related:
  - four-colour-theorem
  - five-colour-theorem
contrasts_with: []
answers_questions:
  - "How many colours suffice for triangle-free planar graphs?"
---

# Quick Definition
Every planar graph containing no triangle is 3-colourable.

# Core Definition
**Theorem 5.1.3** (Grotzsch 1959): "Every planar graph not containing a triangle is 3-colourable" (Diestel, p. 113).

# Prerequisites
- **Chromatic number** and **Planar graph**

# Key Properties
1. Triangle-free planar graphs have chi(G) <= 3
2. The bound is tight: odd cycles of length >= 5 are planar, triangle-free, and 3-chromatic
3. Not stated for choosability: triangle-free planar graphs are not necessarily 3-choosable

# Context & Application
Grotzsch's theorem strengthens the four colour theorem for the special case of triangle-free planar graphs, reducing the bound from 4 to 3. A short proof using list colouring was given by Thomassen.

# Relationships
## Related
- **Four colour theorem** -- Grotzsch gives a better bound for triangle-free case
- **Five colour theorem** -- Also improved by Grotzsch for triangle-free graphs

# Source Reference
Chapter 5, Section 5.1, Theorem 5.1.3, page 113. Stated without proof.

# Verification Notes
- Theorem stated without proof
- Confidence: MEDIUM -- stated as fact, proof not given
