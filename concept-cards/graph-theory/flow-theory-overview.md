---
concept: Flow Theory (Overview)
slug: flow-theory-overview
category: network-flows
subcategory: algebraic-flows
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Flows"
chapter_number: 6
pdf_page: 150
section: null
extraction_confidence: high
aliases:
  - "algebraic flow theory"
prerequisites:
  - graph
  - edge
  - vertex
related:
  - circulation
  - flow-in-network
  - h-flow
  - k-flow
  - flow-colouring-duality
answers_questions:
  - "What is a flow in a network?"
  - "How does Diestel organize flow theory?"
---

# Quick Definition
Diestel's flow theory begins with circulations (algebraic objects on directed edges satisfying antisymmetry and Kirchhoff's law), then specializes to network flows, then develops group-valued flows and their connection to colourings.

# Core Definition
Chapter 6 develops flow theory in a distinctive algebraic sequence:
1. **Circulations** (6.1): The most general concept — Kirchhoff's law everywhere
2. **Network flows** (6.2): Relax Kirchhoff's law at source/sink; max-flow min-cut theorem
3. **Group-valued flows** (6.3): H-flows, k-flows, flow polynomial; Tutte's equivalence theorems
4. **k-flows for small k** (6.4): 2-, 3-, 4-flows characterized
5. **Flow-colouring duality** (6.5): chi(G) = phi(G*) for plane graphs
6. **Tutte's conjectures** (6.6): 3-, 4-, 5-flow conjectures; Seymour's 6-flow theorem (Diestel, pp. 139-162)

# Prerequisites
- **Graph**, **Edge**, **Vertex** — Basic graph theory

# Key Properties
1. Circulations first, then network flows — the algebraic approach
2. Group-valued flows reduce to integer-valued k-flows
3. Flow-colouring duality connects flows to chromatic theory for planar graphs
4. Every bridgeless graph has a 6-flow (the main result)

# Source Reference
Chapter 6: Flows, pages 139-162 (pdf pages 150-172).

# Verification Notes
- Confidence: HIGH — chapter structure overview
