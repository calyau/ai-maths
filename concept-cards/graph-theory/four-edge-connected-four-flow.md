---
concept: 4-Edge-Connected Implies 4-Flow
slug: four-edge-connected-four-flow
category: network-flows
subcategory: algebraic-flows
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Flows"
chapter_number: 6
pdf_page: 160
section: "6.4 k-Flows for small k"
extraction_confidence: high
aliases:
  - "Proposition 6.4.4"
prerequisites:
  - four-flow
  - k-flow
related:
  - six-flow-theorem
answers_questions:
  - "When does a graph have a 4-flow?"
---

# Quick Definition
Every 4-edge-connected graph has a 4-flow (Proposition 6.4.4).

# Core Definition
**Proposition 6.4.4**: Every 4-edge-connected graph has a 4-flow. The proof uses two edge-disjoint spanning trees T_1, T_2 (which exist by Corollary 2.4.2 in 4-edge-connected graphs). For each non-tree edge e, the fundamental cycle C_{i,e} in T_i + e carries a Z_4-circulation of value i-bar. Combining these ensures all edges get non-zero values in Z_4. (Diestel, pp. 150-151)

# Prerequisites
- **Four-flow** — The proposition proves 4-flow existence
- **k-flow** — Understanding the concept

# Key Properties
1. Sufficient condition: 4-edge-connectivity
2. The proof uses edge-disjoint spanning trees
3. Z_4-flows of values 1-bar and 2-bar are combined

# Source Reference
Chapter 6, Section 6.4, Proposition 6.4.4, pages 150-151 (pdf pages 160-161).

# Verification Notes
- Confidence: HIGH — proposition with proof
