---
concept: Map Colouring Problem
slug: map-colouring-problem
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
extraction_confidence: high
aliases:
  - "four colour problem"
  - "map colouring"
prerequisites:
  - vertex-colouring
  - planar-graph
extends: []
related:
  - four-colour-theorem
  - five-colour-theorem
contrasts_with: []
answers_questions:
  - "How does graph colouring relate to map colouring?"
  - "What is the map colouring problem?"
---

# Quick Definition
The map colouring problem asks: how many colours are needed to colour the countries of a map so that adjacent countries have different colours? This translates directly to colouring the dual planar graph, resolved by the four colour theorem (at most 4 colours suffice).

# Core Definition
The map colouring problem asks for the maximum chromatic number of planar graphs. The four colour theorem resolves this: chi(G) <= 4 for every planar graph G (Diestel, pp. 111-112).

# Prerequisites
- **Vertex colouring** -- Maps are coloured via their dual graphs
- **Planar graph** -- Maps correspond to planar graphs

# Key Properties
1. Countries of a map correspond to vertices of a planar graph
2. Adjacent countries (sharing a border) correspond to adjacent vertices
3. The four colour theorem implies every map needs at most 4 colours
4. The problem was raised by Francis Guthrie in 1852

# Context & Application
The map colouring problem is the historical origin of graph colouring theory. First posed in 1852, it led to one of the longest-standing open problems in mathematics, resolved only in 1977 by Appel and Haken with computer assistance.

# Relationships
## Enables
- **Four colour theorem** -- The resolution of this problem

# Source Reference
Chapter 5, introduction, pages 111-112. Notes pp. 137-138.

# Verification Notes
- Historical context from Notes
- Confidence: HIGH
