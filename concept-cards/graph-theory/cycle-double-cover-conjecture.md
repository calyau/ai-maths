---
concept: Cycle Double Cover Conjecture
slug: cycle-double-cover-conjecture
category: network-flows
subcategory: algebraic-flows
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Flows"
chapter_number: 6
pdf_page: 170
section: "Exercises"
extraction_confidence: medium
aliases: []
prerequisites:
  - four-flow
related:
  - five-flow-conjecture
  - snark
answers_questions:
  - "What is the cycle double cover conjecture?"
---

# Quick Definition
The cycle double cover conjecture asserts that every bridgeless multigraph has a family of cycles such that every edge lies on exactly two of these cycles. It is true for graphs with a 4-flow.

# Core Definition
A family of (not necessarily distinct) cycles in a graph G is a **cycle double cover** of G if every edge of G lies on exactly two of these cycles. The **cycle double cover conjecture** asserts that every bridgeless multigraph has a cycle double cover. Exercise 13 asks to prove it for graphs with a 4-flow. (Diestel, p. 160)

# Prerequisites
- **Four-flow** — The conjecture is proved for 4-flow graphs

# Key Properties
1. Related to the 5-flow conjecture (snarks are the hard cases for both)
2. True for graphs with a 4-flow
3. Another major open problem connected to flow theory

# Source Reference
Chapter 6, Exercise 13, page 160 (pdf page 170).

# Verification Notes
- Confidence: MEDIUM — mentioned in exercises, not main text
