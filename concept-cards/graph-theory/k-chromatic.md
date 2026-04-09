---
concept: k-Chromatic Graph
slug: k-chromatic
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
  - "k-chromatic"
prerequisites:
  - chromatic-number
extends: []
related:
  - vertex-colouring
contrasts_with:
  - k-colourable
answers_questions:
  - "What does it mean for a graph to be k-chromatic?"
---

# Quick Definition
A graph G is k-chromatic if chi(G) = k, meaning it requires exactly k colours for a proper vertex colouring.

# Core Definition
"A graph G with chi(G) = k is called k-chromatic" (Diestel, p. 111).

# Prerequisites
- **Chromatic number**

# Key Properties
1. k-chromatic means chi(G) = k exactly
2. K^k is k-chromatic
3. Odd cycles are 3-chromatic

# Relationships
## Contrasts With
- **k-colourable** -- chi(G) <= k vs chi(G) = k

# Source Reference
Chapter 5, page 111.

# Verification Notes
- Definition from p. 111
- Confidence: HIGH
