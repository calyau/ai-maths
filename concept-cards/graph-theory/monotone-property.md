---
concept: Monotone Property
slug: monotone-property
category: random-graphs
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Random Graphs"
chapter_number: 11
pdf_page: 315
section: "11.3 Properties of almost all graphs"
extraction_confidence: high
aliases:
  - "increasing property"
prerequisites:
  - random-graph-gnp
  - graph-property
extends: []
related:
  - threshold-function
contrasts_with: []
answers_questions:
  - "What is a monotone (increasing) graph property?"
---

# Quick Definition
An increasing (monotone) property is a graph property closed under the addition of edges. All non-trivial increasing properties have threshold functions (Bollobás-Thomason, 1987).

# Core Definition
A graph property is *increasing* if it is closed under the addition of edges. Properties of the form {G | G superset H} for fixed H are common increasing properties; connectedness is another. Bollobás & Thomason (1987) showed that all increasing properties, trivial exceptions aside, have threshold functions (Diestel, p. 315).

# Prerequisites
- **Random graph G(n,p)** — Context for threshold analysis
- **Graph property** — Monotone properties are a class of graph properties

# Relationships
## Enables
- **Threshold function** — All non-trivial increasing properties have one

# Source Reference
Chapter 11, Section 11.3, page 315.

# Verification Notes
- Definition from p. 315
- Confidence: HIGH — explicit definition
