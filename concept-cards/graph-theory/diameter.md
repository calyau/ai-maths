---
concept: Diameter
slug: diameter

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
  - "diam G"

prerequisites:
  - graph
  - distance
extends: []
related:
  - radius
  - girth
contrasts_with:
  - radius

answers_questions:
  - "What is the diameter of a graph?"
---

# Quick Definition
The diameter of a graph G is the greatest distance between any two vertices in G, denoted diam G.

# Core Definition
The greatest distance between any two vertices in G is the diameter of G, denoted by diam G (Diestel, p. 8).

# Prerequisites
- **Graph** — diameter is a graph property
- **Distance** — diameter is the maximum distance

# Key Properties
1. rad G <= diam G <= 2 * rad G
2. g(G) <= 2 * diam G + 1 for graphs containing a cycle (Proposition 1.3.2)

# Context & Application
Diameter measures how "spread out" a graph is. Proposition 1.3.2 shows that diameter and girth are related.

# Relationships
## Builds Upon
- **distance**

## Related
- **radius** — rad G <= diam G <= 2 * rad G
- **girth** — g(G) <= 2 * diam G + 1

## Contrasts With
- **radius** — radius uses minimum eccentricity, diameter uses maximum

# Source Reference
Chapter 1: The Basics, Section 1.3, page 8 (pdf p. 18). Proposition 1.3.2.

# Verification Notes
- Direct from p. 8
- Confidence: HIGH
