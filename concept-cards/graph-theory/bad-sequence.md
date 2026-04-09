---
concept: Bad Sequence
slug: bad-sequence
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
aliases: []
prerequisites:
  - well-quasi-ordering
extends: []
related:
  - good-sequence
contrasts_with:
  - good-sequence
answers_questions:
  - "What is a bad sequence?"
---

# Quick Definition
An infinite sequence is bad if it contains no good pair, i.e., there are no indices i < j with x_i <= x_j. A quasi-ordering is a WQO iff it has no bad sequence.

# Core Definition
An infinite sequence is *bad* if it is not good, i.e., it contains no good pair (Diestel, p. 326). The "minimal bad sequence" technique — choosing each element of a bad sequence to be minimal given the previous elements — is a powerful proof method in WQO theory.

# Prerequisites
- **Well-quasi-ordering** — Bad sequences are the obstruction to WQO

# Key Properties
1. A WQO has no bad sequences
2. The "minimal bad sequence" argument: assume a bad sequence exists, choose elements minimally, derive contradiction
3. This technique is used in the proofs of Higman's lemma and Kruskal's theorem

# Relationships
## Contrasts With
- **Good sequence** — The opposite concept

# Source Reference
Chapter 12, Section 12.1, page 326.

# Verification Notes
- Definition from p. 326
- Confidence: HIGH — explicit definition
