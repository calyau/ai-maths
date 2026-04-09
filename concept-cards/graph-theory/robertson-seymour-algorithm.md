---
concept: Robertson-Seymour Algorithm
slug: robertson-seymour-algorithm
category: graph-minors
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Minors, Trees and WQO"
chapter_number: 12
pdf_page: 359
section: "12.5 The graph minor theorem"
extraction_confidence: high
aliases: []
prerequisites: []
extends: []
related: []
contrasts_with: []
answers_questions:
  - "What is Robertson-Seymour Algorithm?"
---

# Quick Definition
For every fixed graph H, there is a cubic-time algorithm testing whether H <= G. Combined with the graph minor theorem, every minor-closed property is decidable in polynomial time.

# Core Definition
For every graph H, Robertson and Seymour showed there is a polynomial-time (cubic) algorithm deciding whether H is a minor of an input graph G. Combined with the graph minor theorem, this means every minor-closed property P can be decided in cubic time: test G for each of the finitely many forbidden minors (Diestel, p. 359).

# Source Reference
Chapter 12, Section 12.5 The graph minor theorem, page 359.

# Verification Notes
- Extracted from source
- Confidence: HIGH
