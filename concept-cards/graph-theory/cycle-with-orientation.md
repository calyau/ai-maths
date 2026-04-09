---
concept: Cycle with Orientation
slug: cycle-with-orientation
category: network-flows
subcategory: algebraic-flows
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Flows"
chapter_number: 6
pdf_page: 162
section: "6.5 Flow-colouring duality"
extraction_confidence: high
aliases:
  - "oriented cycle"
prerequisites:
  - directed-edge
related:
  - circulation
  - flow-colouring-duality
answers_questions:
  - "What is a cycle with orientation?"
---

# Quick Definition
A cycle with orientation is a cycle C = v_0 ... v_{l-1} v_0 together with a consistent choice of direction along its edges, yielding a set of directed edge triples.

# Core Definition
If C = v_0 ... v_{l-1} v_0 is a cycle with edges e_i = v_i v_{i+1} (and v_l := v_0), a **cycle with orientation** is C-arrow := { (e_i, v_i, v_{i+1}) | i < l }. Every cycle has exactly two orientations. A function f sums to f(C-arrow) := sum of f(e-arrow) over e-arrow in C-arrow. (Diestel, p. 152)

# Prerequisites
- **Directed edge** — Orientations assign directions to cycle edges

# Key Properties
1. Every cycle has exactly two orientations
2. f(C-arrow) = -f(C-arrow-back) by antisymmetry
3. For a circulation related to a dual graph, f(C-arrow) = 0 for every oriented cycle (Lemma 6.5.2)
4. Central to the flow-colouring duality proof

# Relationships
## Enables
- **Flow-colouring duality** — The proof uses the condition f(C-arrow) = 0 for all oriented cycles

# Source Reference
Chapter 6: Flows, Section 6.5, page 152 (pdf page 162).

# Verification Notes
- Confidence: HIGH — formally defined
