---
concept: Circulations Are Zero on Bridges
slug: bridge-flow-zero
category: network-flows
subcategory: algebraic-flows
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Flows"
chapter_number: 6
pdf_page: 151
section: "6.1 Circulations"
extraction_confidence: high
aliases:
  - "Corollary 6.1.2"
prerequisites:
  - circulation
  - net-flow-across-cut
related:
  - h-flow
  - flow-number
answers_questions:
  - "What happens to a circulation on a bridge?"
---

# Quick Definition
If f is a circulation and e = xy is a bridge in G, then f(e, x, y) = 0. A graph with an H-flow (nowhere-zero circulation) therefore cannot have a bridge.

# Core Definition
**Corollary 6.1.2**: If f is a circulation and e = xy is a bridge in G, then f(e, x, y) = 0. Since bridges form cuts by themselves, Proposition 6.1.1 (net flow across any cut is zero) implies the circulation must be zero on the bridge. (Diestel, p. 141)

Consequence: A graph admitting an H-flow cannot have a bridge, since H-flows are nowhere zero.

# Prerequisites
- **Circulation** — The property applies to circulations
- **Net flow across cut** — Bridges form single-edge cuts

# Key Properties
1. Immediate from Proposition 6.1.1
2. Implies: H-flows exist only on bridgeless graphs
3. Implies: phi(G) = infinity iff G has a bridge

# Source Reference
Chapter 6, Section 6.1, Corollary 6.1.2, page 141 (pdf page 151).

# Verification Notes
- Confidence: HIGH — corollary with simple proof
