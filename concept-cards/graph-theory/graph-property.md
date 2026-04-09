---
concept: Graph Property
slug: graph-property

category: graph-fundamentals
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 11
section: "1.1 Graphs"

extraction_confidence: high

aliases: []

prerequisites:
  - graph
  - graph-isomorphism
extends: []
related:
  - graph-invariant
contrasts_with:
  - graph-invariant

answers_questions:
  - "What is a graph property?"
---

# Quick Definition
A graph property is a class of graphs that is closed under isomorphism.

# Core Definition
A class of graphs that is closed under isomorphism is called a graph property. For example, "containing a triangle" is a graph property: if G contains three pairwise adjacent vertices then so does every graph isomorphic to G (Diestel, p. 3).

# Prerequisites
- **Graph** — graph properties are classes of graphs
- **Graph isomorphism** — closure under isomorphism is the defining condition

# Key Properties
1. If G has a graph property and G' is isomorphic to G, then G' also has the property
2. Graph properties depend only on structure, not on labeling

# Context & Application
The distinction between properties (which depend only on structure) and non-structural attributes (which depend on labeling) is fundamental.

# Examples
**Example** (p. 3): "Containing a triangle" is a graph property.

# Relationships
## Builds Upon
- **graph**, **graph-isomorphism**

## Contrasts With
- **graph-invariant** — a property is a Boolean (has/doesn't have); an invariant is a value

# Source Reference
Chapter 1: The Basics, Section 1.1, page 3 (pdf p. 13).

# Verification Notes
- Direct from p. 3
- Confidence: HIGH
