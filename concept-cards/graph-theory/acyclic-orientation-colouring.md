---
concept: Acyclic Orientations and Colouring
slug: acyclic-orientation-colouring
category: graph-colouring
subcategory: vertex-colouring
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Colouring"
chapter_number: 5
pdf_page: 122
section: "Exercises"
extraction_confidence: medium
aliases: []
prerequisites:
  - chromatic-number
extends: []
related:
  - greedy-colouring
contrasts_with: []
answers_questions:
  - "How do acyclic orientations relate to colouring?"
---

# Quick Definition
chi(G) <= k if and only if G has an acyclic orientation without directed paths of length k - 1 (Exercise 16). This connects vertex colouring to directed graph theory.

# Core Definition
Exercise 16 states three equivalences: (i) chi(G) <= k; (ii) G has an orientation without directed paths of length k - 1; (iii) G has an acyclic such orientation (Diestel, p. 134).

# Prerequisites
- **Chromatic number**

# Key Properties
1. A k-colouring induces an acyclic orientation (orient edges from smaller to larger colour)
2. The longest directed path in this orientation has length <= k - 1
3. Conversely, such orientations yield k-colourings

# Relationships
## Related
- **Greedy colouring** -- Vertex ordering induces an orientation

# Source Reference
Chapter 5, Exercise 16, page 134.

# Verification Notes
- Exercise 16
- Confidence: MEDIUM
