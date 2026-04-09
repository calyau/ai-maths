---
concept: Class One and Class Two Graphs
slug: class-one-class-two
category: graph-colouring
subcategory: edge-colouring
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Colouring"
chapter_number: 5
pdf_page: 122
section: "5.3 Colouring edges"
extraction_confidence: high
aliases:
  - "class 1"
  - "class 2"
prerequisites:
  - vizing-theorem
  - chromatic-index
extends:
  - vizing-theorem
related:
  - konig-edge-colouring-theorem
contrasts_with: []
answers_questions:
  - "What are class 1 and class 2 graphs?"
---

# Quick Definition
A graph is class 1 if chi'(G) = Delta(G), and class 2 if chi'(G) = Delta(G) + 1. By Vizing's theorem, every graph falls into one of these two classes.

# Core Definition
"Graphs satisfying chi' = Delta are called (imaginatively) class 1, those with chi' = Delta + 1 are class 2" (Diestel, p. 121).

# Prerequisites
- **Vizing's theorem** -- Establishes that chi' is Delta or Delta + 1
- **Chromatic index** -- Class is determined by chi'

# Key Properties
1. Every graph is either class 1 or class 2 (Vizing's theorem)
2. All bipartite graphs are class 1 (Konig's theorem)
3. Odd cycles are class 2
4. The Petersen graph is class 2
5. Determining the class is NP-complete in general

# Relationships
## Builds Upon
- **Vizing's theorem**

## Related
- **Konig's theorem** -- Bipartite implies class 1

# Source Reference
Chapter 5, Section 5.3, page 121.

# Verification Notes
- Definition from p. 121
- Confidence: HIGH -- explicit definition
