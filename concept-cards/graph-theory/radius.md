---
concept: Radius
slug: radius

category: paths-and-cycles
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 19
section: "1.3 Paths and cycles"

extraction_confidence: high

aliases:
  - "rad G"
  - "central vertex"

prerequisites:
  - graph
  - distance
extends: []
related:
  - diameter
contrasts_with:
  - diameter

answers_questions:
  - "What is the radius of a graph?"
  - "What is a central vertex?"
---

# Quick Definition
The radius rad G is the minimum over all vertices v of the maximum distance from v to any other vertex. A vertex achieving this minimum is central.

# Core Definition
A vertex is central in G if its greatest distance from any other vertex is as small as possible. This distance is the radius of G, denoted by rad G. Formally, rad G = min over x in V(G) of max over y in V(G) of d_G(x, y) (Diestel, p. 9).

# Prerequisites
- **Graph**, **distance** — radius is defined in terms of distances

# Key Properties
1. rad G <= diam G <= 2 * rad G
2. A central vertex minimizes eccentricity

# Context & Application
Radius identifies the "center" of a graph. Proposition 1.3.3 bounds the order of a graph with given radius and maximum degree.

# Relationships
## Builds Upon
- **distance**

## Contrasts With
- **diameter** — maximum over all pairs; radius minimizes over vertices

# Source Reference
Chapter 1: The Basics, Section 1.3, page 9 (pdf p. 19).

# Verification Notes
- Direct from p. 9
- Confidence: HIGH
