---
concept: Plane Duality in Flow-Colouring
slug: plane-dual-flow-colouring
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
  - "oriented cycle-cut duality"
  - "Lemma 6.5.1"
  - "Lemma 6.5.2"
prerequisites:
  - circulation
  - flow-colouring-duality
related:
  - cycle-with-orientation
answers_questions:
  - "How does the cycle-cut duality connect flows and colourings?"
---

# Quick Definition
Lemma 6.5.1 establishes a direction-preserving bijection between directed edges of G and G*, and Lemma 6.5.2 shows that circulations on G* correspond to functions on G summing to zero along oriented cycles.

# Core Definition
**Lemma 6.5.1**: For plane dual multigraphs G, G*, there exists a bijection e-arrow -> e-arrow* from E-arrow to E-arrow* such that: (i) the underlying edge of e-arrow* is e*; (ii) for any cycle C in G with F* = E*(X, X-bar), there is an orientation of C with the right correspondence.

**Lemma 6.5.2**: (i) g satisfies (F1) iff f does. (ii) g is a circulation on G* iff f satisfies (F1) and f(C-arrow) = 0 for every oriented cycle C.

These lemmas form the technical foundation for the flow-colouring duality theorem (6.5.3). (Diestel, pp. 152-155)

# Prerequisites
- **Circulation** — The lemmas relate circulations on G* to functions on G
- **Flow-colouring duality** — These lemmas are prerequisites for the main theorem

# Key Properties
1. Based on the orientability of the plane
2. The bijection turns clockwise to match cycle orientations with cut directions
3. "f sums to zero along cycles" is the key bridge between flows and colourings

# Source Reference
Chapter 6, Section 6.5, Lemmas 6.5.1 and 6.5.2, pages 152-155 (pdf pages 162-165).

# Verification Notes
- Confidence: HIGH — technical lemmas with proofs (Lemma 6.5.1 stated without proof due to topological prerequisites)
