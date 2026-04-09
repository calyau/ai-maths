---
concept: Finite Set
slug: finite-set

category: set-theory-foundations
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Infinite Sets"
chapter_number: null
pdf_page: 367
section: null

extraction_confidence: high

aliases: []

prerequisites:
  - cardinality
extends: []
related:
  - infinite-set
  - countable-set
contrasts_with:
  - infinite-set

answers_questions:
  - "What is a finite set?"
---

# Quick Definition
A set A is finite if |A| = n for some natural number n.

# Core Definition
The natural numbers are defined inductively as n := {0, ..., n-1}, starting with 0 := the empty set. A set A is finite if there is a natural number n such that |A| = n; otherwise it is infinite (Diestel, p. 357).

# Prerequisites
- **Cardinality** — finiteness is defined via cardinality

# Key Properties
1. A finite set has |A| = n for some n in N
2. Every subset of a finite set is finite
3. A finite union of finite sets is finite

# Relationships
## Builds Upon
- **cardinality**

## Contrasts With
- **infinite-set** — a set that is not finite

# Source Reference
Appendix A: Infinite Sets, page 357 (pdf p. 367).

# Verification Notes
- Direct from p. 357
- Confidence: HIGH
