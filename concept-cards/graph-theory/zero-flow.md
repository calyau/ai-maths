---
concept: Zero Flow
slug: zero-flow
category: network-flows
subcategory: algebraic-flows
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Flows"
chapter_number: 6
pdf_page: 150
section: "6.1 Circulations"
extraction_confidence: high
aliases:
  - "trivial flow"
prerequisites:
  - circulation
related:
  - flow-in-network
  - h-flow
contrasts_with:
  - nowhere-zero-flow
answers_questions:
  - "What is the zero flow?"
---

# Quick Definition
The zero flow assigns value 0 to every directed edge; it is the trivial H-circulation for any abelian group H, and serves as the starting point for the Ford-Fulkerson algorithm.

# Core Definition
The function f: E-arrow -> H defined by f(e-arrow) = 0 for all e-arrow in E-arrow is the **zero flow** (or zero circulation). It trivially satisfies both (F1) and (F2). In the network flow setting, f_0 = 0 is the initial flow in the Ford-Fulkerson algorithm. (Diestel, p. 143)

# Prerequisites
- **Circulation** — The zero flow is a circulation

# Key Properties
1. Always a valid H-circulation for any abelian group H
2. Starting point for the Ford-Fulkerson algorithm
3. NOT an H-flow (since H-flows must be nowhere zero)

# Relationships
## Contrasts With
- **Nowhere-zero flow** — The zero flow is the opposite: zero everywhere

# Source Reference
Chapter 6, Sections 6.1-6.2, pages 140, 143.

# Verification Notes
- Confidence: HIGH — trivially defined
