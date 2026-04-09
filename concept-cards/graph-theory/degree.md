---
concept: Degree
slug: degree

category: graph-fundamentals
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 15
section: "1.2 The degree of a vertex"

extraction_confidence: high

aliases:
  - "valency"
  - "d(v)"

prerequisites:
  - graph
  - vertex
  - edge
  - incident
extends: []
related:
  - neighborhood
  - minimum-degree
  - maximum-degree
  - average-degree
  - regular-graph
contrasts_with: []

answers_questions:
  - "What is the degree of a vertex?"
  - "What does d(v) mean?"
---

# Quick Definition
The degree d(v) of a vertex v is the number of edges at v, which equals the number of neighbours of v.

# Core Definition
The degree (or valency) d_G(v) = d(v) of a vertex v is the number |E(v)| of edges at v; by our definition of a graph, this is equal to the number of neighbours of v. A vertex of degree 0 is isolated (Diestel, p. 5).

# Prerequisites
- **Graph**, **vertex**, **edge** — degree is a property of a vertex in a graph
- **Incident** — degree counts incident edges

# Key Properties
1. d(v) = |E(v)| = |N(v)|
2. d(v) is a non-negative integer
3. A vertex of degree 0 is called isolated
4. In a graph on n vertices, 0 <= d(v) <= n - 1

# Construction / Recognition
To determine d(v), count the edges incident with v, or equivalently, count the neighbors of v.

# Context & Application
Degree is one of the most fundamental local properties of a vertex. It features in many results including the Handshaking Lemma.

# Relationships
## Builds Upon
- **graph**, **vertex**, **edge**, **incident**

## Enables
- **minimum-degree**, **maximum-degree**, **average-degree** — aggregate degree measures
- **regular-graph** — all degrees equal
- **handshaking-lemma** — sum of degrees equals twice the number of edges

# Source Reference
Chapter 1: The Basics, Section 1.2, page 5 (pdf p. 15).

# Verification Notes
- Direct from p. 5
- Confidence: HIGH
