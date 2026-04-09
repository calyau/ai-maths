---
concept: Circumference
slug: circumference

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

aliases: []

prerequisites:
  - graph
  - cycle
extends: []
related:
  - girth
  - hamilton-cycle
contrasts_with:
  - girth

answers_questions:
  - "What is the circumference of a graph?"
---

# Quick Definition
The circumference of a graph G is the maximum length of a cycle in G. If G has no cycle, the circumference is zero.

# Core Definition
The maximum length of a cycle in G is its circumference. If G does not contain a cycle, the circumference is set to zero (Diestel, p. 8).

# Prerequisites
- **Graph**, **cycle**

# Key Properties
1. Circumference = 0 for acyclic graphs
2. Circumference = |G| if and only if G has a Hamilton cycle

# Relationships
## Builds Upon
- **cycle**

## Related
- **hamilton-cycle** — a cycle of maximum possible length

## Contrasts With
- **girth** — the minimum cycle length

# Source Reference
Chapter 1: The Basics, Section 1.3, page 8 (pdf p. 18).

# Verification Notes
- Direct from p. 8
- Confidence: HIGH
