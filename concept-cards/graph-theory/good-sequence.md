---
concept: Good Sequence
slug: good-sequence
category: graph-minors
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Minors, Trees and WQO"
chapter_number: 12
pdf_page: 326
section: "12.1 Well-quasi-ordering"
extraction_confidence: high
aliases:
  - "good pair"
prerequisites:
  - well-quasi-ordering
extends: []
related:
  - bad-sequence
contrasts_with:
  - bad-sequence
answers_questions:
  - "What is a good sequence in WQO theory?"
---

# Quick Definition
A sequence containing a good pair (indices i < j with x_i <= x_j) is a good sequence. A quasi-ordering is a WQO iff every infinite sequence is good.

# Core Definition
A pair (x_i, x_j) with i < j and x_i <= x_j is a *good pair*. A sequence containing a good pair is a *good sequence*. A quasi-ordering on X is a well-quasi-ordering if and only if every infinite sequence in X is good (Diestel, p. 326).

# Prerequisites
- **Well-quasi-ordering** — Good sequences characterize WQOs

# Relationships
## Contrasts With
- **Bad sequence** — A sequence with no good pair

# Source Reference
Chapter 12, Section 12.1, page 326.

# Verification Notes
- Definition from p. 326
- Confidence: HIGH — explicit definition
