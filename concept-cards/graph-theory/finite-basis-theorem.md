---
concept: Finite Basis Theorem
slug: finite-basis-theorem
category: graph-minors
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Minors, Trees and WQO"
chapter_number: 12
pdf_page: 352
section: "12.5 The graph minor theorem"
extraction_confidence: high
aliases:
  - "Corollary 12.5.2"
prerequisites:
  - graph-minor-theorem
  - kuratowski-set
extends:
  - graph-minor-theorem
related:
  - minor-closed-property
contrasts_with: []
answers_questions:
  - "Why does every minor-closed property have finitely many forbidden minors?"
---

# Quick Definition
The finite basis theorem (Corollary 12.5.2 of the graph minor theorem) states that the Kuratowski set for any minor-closed graph property is finite.

# Core Definition
**Corollary 12.5.2**: The Kuratowski set for any minor-closed graph property is finite (Diestel, p. 352). This follows immediately from the graph minor theorem: the elements of K_P are pairwise incomparable under <=, and the graph minor theorem says no infinite antichain exists.

# Prerequisites
- **Graph minor theorem** — The finite basis theorem is a direct corollary
- **Kuratowski set** — The set whose finiteness is asserted

# Key Properties
1. Every minor-closed property has a finite characterization by forbidden minors
2. This implies embeddability in any surface has finitely many forbidden minors (Corollary 12.5.3)
3. Combined with Robertson-Seymour's algorithm, every minor-closed property is decidable in cubic time

# Context & Application
This is the most immediately applicable consequence of the graph minor theorem. It turns the abstract WQO result into a concrete structural consequence: finite forbidden minor characterizations always exist.

# Relationships
## Builds Upon
- **Graph minor theorem** — The finite basis theorem is a corollary

## Enables
- Finite forbidden minor characterizations for all minor-closed properties

# Source Reference
Chapter 12, Section 12.5, page 352 (Corollary 12.5.2).

# Verification Notes
- Statement from p. 352
- Confidence: HIGH — explicit corollary
