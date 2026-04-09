---
concept: Bridge
slug: bridge

category: connectivity
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 20
section: "1.4 Connectivity"

extraction_confidence: high

aliases:
  - "cut edge"

prerequisites:
  - graph
  - edge
  - connected-graph
extends: []
related:
  - cut-vertex
  - separator
  - cycle
contrasts_with:
  - cut-vertex

answers_questions:
  - "What is a bridge in a graph?"
---

# Quick Definition
A bridge is an edge whose removal disconnects its endpoints; equivalently, it is an edge that does not lie on any cycle.

# Core Definition
An edge separating its ends is a bridge. Thus, the bridges in a graph are precisely those edges that do not lie on any cycle (Diestel, p. 11).

# Prerequisites
- **Graph**, **edge**, **connected-graph**

# Key Properties
1. A bridge e is an edge such that G - e has more components than G
2. An edge is a bridge if and only if it does not lie on any cycle
3. In a tree, every edge is a bridge

# Examples
**Example** (p. 11): Fig. 1.4.2 shows a bridge e = xy.

# Relationships
## Builds Upon
- **edge**, **connected-graph**

## Related
- **cut-vertex** — a vertex whose removal disconnects
- **cycle** — an edge on a cycle is not a bridge

## Contrasts With
- **cut-vertex** — bridges are edges; cut vertices are vertices

# Source Reference
Chapter 1: The Basics, Section 1.4, page 11 (pdf p. 21). See Fig. 1.4.2.

# Verification Notes
- Direct from p. 11
- Confidence: HIGH
