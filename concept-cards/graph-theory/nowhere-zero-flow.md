---
concept: Nowhere-Zero Flow
slug: nowhere-zero-flow
category: network-flows
subcategory: algebraic-flows
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Flows"
chapter_number: 6
pdf_page: 155
section: "6.3 Group-valued flows"
extraction_confidence: high
aliases:
  - "nowhere zero"
prerequisites:
  - circulation
  - directed-edge
related:
  - h-flow
  - k-flow
  - flow-number
answers_questions:
  - "What does it mean for a flow to be nowhere zero?"
---

# Quick Definition
A function f: E-arrow -> H is nowhere zero if f(e-arrow) != 0 for all directed edges e-arrow.

# Core Definition
A function f: E-arrow -> H is **nowhere zero** if f(e-arrow) != 0 for all e-arrow in E-arrow. An H-circulation that is nowhere zero is called an H-flow. By Corollary 6.1.2, a graph with an H-flow cannot have a bridge, since circulations are always zero on bridges. (Diestel, p. 145)

# Prerequisites
- **Circulation** — Nowhere-zero is a property added to circulations
- **Directed edge** — The function is defined on directed edges

# Key Properties
1. The set of H-flows is NOT closed under addition (two H-flows may sum to zero on some edge)
2. A graph with an H-flow cannot have a bridge
3. The number of H-flows depends only on |H|, not on H itself (Theorem 6.3.1)

# Relationships
## Enables
- **H-flow** — An H-flow is a nowhere-zero H-circulation
- **k-flow** — A k-flow is a nowhere-zero Z-circulation with bounded values

# Source Reference
Chapter 6: Flows, Section 6.3, page 145 (pdf page 155).

# Verification Notes
- Confidence: HIGH — explicitly defined
