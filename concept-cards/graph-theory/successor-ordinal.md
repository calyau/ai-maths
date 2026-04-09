---
concept: Successor Ordinal
slug: successor-ordinal

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

aliases:
  - "successor"

prerequisites:
  - well-ordered-set
  - ordinal
extends: []
related:
  - limit-element
  - transfinite-induction
contrasts_with:
  - limit-element

answers_questions:
  - "What is a successor ordinal?"
  - "What is the successor of an element in a well-ordered set?"
---

# Quick Definition
In a well-ordered set, every non-maximal element x has a unique successor: the minimal element of {y | x < y}. An ordinal that is a successor of another ordinal is a successor ordinal.

# Core Definition
Every element x of a well-ordered set X has a successor (unless x is maximal in X): the unique minimal element of {y in X | x < y}. In transfinite induction, the successor case and limit case are handled separately (Diestel, p. 358).

# Prerequisites
- **Well-ordered set**, **ordinal** — successors are defined in well-ordered sets

# Key Properties
1. The successor of x is the smallest element strictly greater than x
2. Not every element has a predecessor (limits)
3. In transfinite induction, the successor step generalizes the induction step of ordinary induction

# Relationships
## Builds Upon
- **well-ordered-set**, **ordinal**

## Contrasts With
- **limit-element** — a limit has no predecessor; a successor's predecessor exists

# Source Reference
Appendix A: Infinite Sets, page 358 (pdf p. 368).

# Verification Notes
- Direct from p. 358
- Confidence: HIGH
