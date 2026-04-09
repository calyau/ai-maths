---
concept: k-Colourable Graph
slug: k-colourable
category: graph-colouring
subcategory: vertex-colouring
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Colouring"
chapter_number: 5
pdf_page: 122
section: null
extraction_confidence: high
aliases:
  - "k-colourable"
  - "k-colorable"
prerequisites:
  - chromatic-number
extends: []
related:
  - vertex-colouring
  - four-colour-theorem
contrasts_with:
  - k-chromatic
answers_questions:
  - "What does it mean for a graph to be k-colourable?"
---

# Quick Definition
A graph G is k-colourable if chi(G) <= k, meaning it admits a proper vertex colouring with at most k colours.

# Core Definition
"If chi(G) <= k, we call G k-colourable" (Diestel, p. 111).

# Prerequisites
- **Chromatic number**

# Key Properties
1. k-colourable means chi(G) <= k (at MOST k colours suffice)
2. k-chromatic means chi(G) = k (exactly k colours needed)
3. Every graph is (Delta+1)-colourable
4. Every planar graph is 4-colourable (four colour theorem)

# Relationships
## Contrasts With
- **k-chromatic** -- chi(G) = k exactly, not just <= k

# Source Reference
Chapter 5, page 111.

# Verification Notes
- Definition from p. 111
- Confidence: HIGH
