---
concept: Chromatic Number Edge Bound
slug: chromatic-number-edge-bound
category: graph-colouring
subcategory: vertex-colouring
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Colouring"
chapter_number: 5
pdf_page: 122
section: "5.2 Colouring vertices"
extraction_confidence: high
aliases:
  - "Proposition 5.2.1"
prerequisites:
  - chromatic-number
extends: []
related:
  - colouring-number
contrasts_with: []
answers_questions:
  - "How does the chromatic number relate to the number of edges?"
---

# Quick Definition
Every graph G with m edges satisfies chi(G) <= 1/2 + sqrt(2m + 1/4). This follows from the fact that a k-colouring requires at least k(k-1)/2 edges (one between each pair of colour classes).

# Core Definition
**Proposition 5.2.1**: "Every graph G with m edges satisfies chi(G) <= 1/2 + sqrt(2m + 1/4)" (Diestel, p. 114).

# Prerequisites
- **Chromatic number**

# Key Properties
1. In a k-colouring, there is at least one edge between any two colour classes
2. Therefore m >= k(k-1)/2
3. Solving for k gives the bound

# Relationships
## Related
- **Colouring number** -- Provides a sharper bound (Proposition 5.2.2)

# Source Reference
Chapter 5, Section 5.2, Proposition 5.2.1, page 114.

# Verification Notes
- Proposition from p. 114
- Confidence: HIGH
