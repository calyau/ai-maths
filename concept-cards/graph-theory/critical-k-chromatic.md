---
concept: Critically k-Chromatic Graph
slug: critical-k-chromatic
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
aliases:
  - "critical graph"
  - "colour-critical graph"
prerequisites:
  - chromatic-number
extends: []
related:
  - brooks-theorem
contrasts_with: []
answers_questions:
  - "What is a critically k-chromatic graph?"
---

# Quick Definition
A k-chromatic graph G is critically k-chromatic if chi(G - v) < k for every vertex v. Critical graphs have minimum degree at least k - 1.

# Core Definition
"A k-chromatic graph is called critically k-chromatic, or just critical, if chi(G - v) < k for every v in V(G)" (Diestel, p. 134, Exercise 10).

# Prerequisites
- **Chromatic number**

# Key Properties
1. Every k-chromatic graph has a critical k-chromatic induced subgraph
2. Any critical k-chromatic graph has delta(G) >= k - 1
3. Every critical k-chromatic graph is (k-1)-edge-connected (Exercise 12)

# Relationships
## Related
- **Brooks' theorem** -- Applies to critical graphs

# Source Reference
Chapter 5, Exercise 10, page 134.

# Verification Notes
- Exercise definition
- Confidence: MEDIUM
