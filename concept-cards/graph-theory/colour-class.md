---
concept: Colour Class
slug: colour-class
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
  - "color class"
  - "independent set in colouring"
prerequisites:
  - vertex-colouring
extends: []
related:
  - chromatic-number
contrasts_with: []
answers_questions:
  - "What is a colour class in a graph colouring?"
---

# Quick Definition
A colour class in a k-colouring is the set of all vertices assigned the same colour. Each colour class is an independent set, and a k-colouring is a partition of the vertex set into k colour classes.

# Core Definition
"Note that a k-colouring is nothing but a vertex partition into k independent sets, now called colour classes" (Diestel, p. 111).

# Prerequisites
- **Vertex colouring** -- Colour classes arise from a colouring

# Key Properties
1. Each colour class is an independent set
2. A k-colouring partitions V into exactly k non-empty colour classes
3. The size of the largest colour class is at most alpha(G)
4. chi(G) >= |V|/alpha(G) follows from this

# Relationships
## Builds Upon
- **Vertex colouring**

## Related
- **Chromatic number** -- Number of colour classes in an optimal colouring

# Source Reference
Chapter 5, page 111.

# Verification Notes
- Definition quoted from p. 111
- Confidence: HIGH -- explicit definition
