---
concept: "Menger's Theorem (Flow Version)"
slug: menger-theorem-flow-version
category: network-flows
subcategory: network-flows
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Flows"
chapter_number: 6
pdf_page: 153
section: "6.2 Flows in networks"
extraction_confidence: high
aliases:
  - "Menger from max-flow"
prerequisites:
  - max-flow-min-cut-theorem
  - integral-flow-theorem
related:
  - flow-in-network
answers_questions:
  - "How does Menger's theorem follow from max-flow min-cut?"
---

# Quick Definition
Menger's theorem can be derived from the max-flow min-cut theorem by constructing an auxiliary network where integral flow units correspond to internally disjoint paths.

# Core Definition
The max-flow min-cut theorem implies Menger's theorem (3.3.5) "without much difficulty" (Exercise 3). For the edge version: set all capacities to 1; then the maximum number of edge-disjoint s-t paths equals the minimum edge cut. For the vertex version: construct an auxiliary graph splitting each internal vertex v into v_in and v_out with a capacity-1 edge between them. (Diestel, p. 141)

# Prerequisites
- **Max-flow min-cut theorem** — The theorem from which Menger's theorem is derived
- **Integral flow theorem** — Integral flows decompose into unit flows along paths

# Key Properties
1. The edge version follows directly from max-flow min-cut with unit capacities
2. The vertex version requires an auxiliary graph construction
3. Demonstrates the "natural power" of the network flow approach

# Relationships
## Builds Upon
- **Max-flow min-cut theorem**, **Integral flow theorem**

# Source Reference
Chapter 6, Section 6.2, Exercise 3, page 160 (pdf page 170). Referenced on p. 141.

# Verification Notes
- Confidence: HIGH — standard derivation mentioned in text, details in exercise
