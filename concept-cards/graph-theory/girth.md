---
concept: Girth
slug: girth

category: paths-and-cycles
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 17
section: "1.3 Paths and cycles"

extraction_confidence: high

aliases:
  - "g(G)"

prerequisites:
  - graph
  - cycle
extends: []
related:
  - circumference
  - diameter
contrasts_with:
  - circumference

answers_questions:
  - "What is the girth of a graph?"
---

# Quick Definition
The girth g(G) of a graph G is the minimum length of a cycle in G. If G has no cycle, g(G) := infinity.

# Core Definition
The minimum length of a cycle (contained) in a graph G is the girth g(G) of G. If G does not contain a cycle, we set the girth to infinity (Diestel, p. 8).

# Prerequisites
- **Graph**, **cycle** — girth measures the shortest cycle

# Key Properties
1. g(G) >= 3 if G has a cycle (since minimum cycle length is 3)
2. g(G) = infinity for forests/trees
3. g(G) <= 2 * diam G + 1 (Proposition 1.3.2)
4. If delta(G) >= 3 then g(G) < 2 * log |G| (Corollary 1.3.5)

# Context & Application
Girth measures how "locally tree-like" a graph is. Large girth with large minimum degree forces large order.

# Relationships
## Builds Upon
- **cycle**

## Contrasts With
- **circumference** — the maximum cycle length

# Source Reference
Chapter 1: The Basics, Section 1.3, page 8 (pdf p. 18).

# Verification Notes
- Direct from p. 8
- Confidence: HIGH
