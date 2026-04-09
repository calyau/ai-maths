---
concept: Distance
slug: distance

category: paths-and-cycles
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 18
section: "1.3 Paths and cycles"

extraction_confidence: high

aliases:
  - "d(x,y)"
  - "graph distance"

prerequisites:
  - graph
  - path
extends: []
related:
  - diameter
  - radius
  - girth
contrasts_with: []

answers_questions:
  - "What is the distance between two vertices?"
  - "What does d(x,y) mean in a graph?"
---

# Quick Definition
The distance d(x, y) between two vertices x and y in G is the length of a shortest x-y path; if no such path exists, d(x, y) := infinity.

# Core Definition
The distance d_G(x, y) in G of two vertices x, y is the length of a shortest x-y path in G; if no such path exists, we set d(x, y) := infinity (Diestel, p. 8).

# Prerequisites
- **Graph** — distance is measured in a graph
- **Path** — distance is defined as the length of a shortest path

# Key Properties
1. d(x, y) >= 0 for all x, y
2. d(x, y) = 0 if and only if x = y
3. d(x, y) = d(y, x) (symmetry)
4. d(x, z) <= d(x, y) + d(y, z) (triangle inequality)
5. d(x, y) = infinity if x and y are in different components

# Context & Application
Distance defines a metric on the vertex set of a connected graph. It connects to diameter, radius, and girth.

# Relationships
## Builds Upon
- **path**

## Enables
- **diameter** — the greatest distance
- **radius** — the minimum eccentricity

# Source Reference
Chapter 1: The Basics, Section 1.3, page 8 (pdf p. 18).

# Verification Notes
- Direct from p. 8
- Confidence: HIGH
