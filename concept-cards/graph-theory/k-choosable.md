---
concept: k-Choosable Graph
slug: k-choosable
category: graph-colouring
subcategory: list-colouring
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Colouring"
chapter_number: 5
pdf_page: 122
section: "5.4 List colouring"
extraction_confidence: high
aliases:
  - "k-list-colourable"
  - "k-choosable"
prerequisites:
  - list-colouring
  - choice-number
extends: []
related:
  - thomassen-five-choosable
contrasts_with:
  - k-colourable
answers_questions:
  - "What does it mean for a graph to be k-choosable?"
---

# Quick Definition
A graph G is k-choosable (k-list-colourable) if for every assignment of lists of size k to its vertices, there is a proper colouring from those lists. Equivalently, ch(G) <= k.

# Core Definition
"The graph G is called k-list-colourable, or k-choosable, if, for every family (S_v)_{v in V} with |S_v| = k for all v, there is a vertex colouring of G from the lists S_v" (Diestel, p. 121).

# Prerequisites
- **List colouring**, **Choice number**

# Key Properties
1. k-choosable implies k-colourable (but not conversely)
2. Every planar graph is 5-choosable (Thomassen)
3. Planar graphs are NOT always 4-choosable
4. k-choosable iff ch(G) <= k

# Relationships
## Contrasts With
- **k-colourable** -- k-choosable is strictly stronger

# Source Reference
Chapter 5, Section 5.4, page 121.

# Verification Notes
- Definition from p. 121
- Confidence: HIGH
