---
concept: Minor-Closed Property
slug: minor-closed-property
category: graph-minors
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Minors, Trees and WQO"
chapter_number: 12
pdf_page: 337
section: "12.4 Tree-width and forbidden minors"
extraction_confidence: high
aliases:
  - "minor-closed class"
prerequisites:
  - graph-minor
extends: []
related:
  - forbidden-minor
  - kuratowski-set
  - graph-minor-theorem
contrasts_with: []
answers_questions:
  - "What is a minor-closed property?"
---

# Quick Definition
A graph property P is minor-closed if whenever G is in P and G' is a minor of G, then G' is also in P. Equivalently, P can be expressed by forbidden minors.

# Core Definition
A graph property P is *minor-closed* if G' <= G and G in P implies G' in P. Every minor-closed property can be expressed by forbidden minors: P = Forb(complement of P) (Proposition 12.4.1, Diestel, p. 337).

# Prerequisites
- **Graph minor** — The ordering under which the property is closed

# Key Properties
1. P is minor-closed iff P = Forb(H) for some set H
2. By the graph minor theorem, P = Forb(K_P) where K_P is finite
3. Examples: planarity, embeddability in any surface, bounded tree-width, being a forest

# Context & Application
Minor-closed properties are ubiquitous in graph theory. The graph minor theorem implies that each has a finite characterization by forbidden minors, and each can be tested in polynomial time.

# Relationships
## Enables
- **Kuratowski set** — Unique smallest set of forbidden minors
- Polynomial-time decidability (by the graph minor theorem + Robertson-Seymour algorithm)

# Source Reference
Chapter 12, Section 12.4, page 337.

# Verification Notes
- Definition from p. 337
- Confidence: HIGH — explicit definition
