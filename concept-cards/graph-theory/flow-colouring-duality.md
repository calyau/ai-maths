---
concept: Flow-Colouring Duality
slug: flow-colouring-duality
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
  - "colouring-flow duality"
  - "duality theorem for flows and colourings"
prerequisites:
  - k-flow
  - flow-number
  - circulation
related:
  - five-flow-conjecture
  - four-flow-conjecture
  - three-flow-conjecture
answers_questions:
  - "How do flows relate to colourings (flow-colouring duality)?"
  - "What is the connection between flows on a planar graph and colourings of its dual?"
---

# Quick Definition
For every dual pair G, G* of plane multigraphs, the chromatic number of G equals the flow number of G*: chi(G) = phi(G*).

# Core Definition
**Theorem 6.5.3** (Tutte 1954): For every dual pair G, G* of plane multigraphs,

chi(G) = phi(G*).

The proof shows that G is k-colourable if and only if G* has a k-flow, by establishing a correspondence: a k-colouring c: V -> Z_k of G defines a Z_k-flow g on G* via g(e*-arrow) = c(w) - c(v) for e = vw, and vice versa. This correspondence uses Lemma 6.5.2, which connects circulations on G* to functions on G that sum to zero along cycles. (Diestel, pp. 152-156)

# Prerequisites
- **k-flow** — The theorem equates flow number with chromatic number
- **Flow number** — phi(G*) appears on one side of the equality
- **Circulation** — The proof works through the connection between circulations and cycles

# Key Properties
1. Holds specifically for plane (planar) multigraphs and their duals
2. Transforms colouring problems into flow problems and vice versa
3. k-flows on G* correspond bijectively to k-colourings of G
4. All three Tutte flow conjectures become true for planar graphs via this duality

# Context & Application
This is one of the deepest results in Chapter 6. It reveals that k-flow theory is a natural generalization of map colouring problems. The duality theorem motivates Tutte's flow conjectures: each conjecture translates to a known colouring result for planar graphs.

- 3-flow conjecture translates to Grotzsch's theorem (triangle-free planar graphs are 3-colourable)
- 4-flow conjecture translates to the four colour theorem (since Petersen graph is not planar)
- 5-flow conjecture translates to the five colour theorem

# Examples
**Example** (p. 156): A k-colouring c of G defines f(e, v, w) = c(w) - c(v), which via the duality bijection e -> e* yields a k-flow on G*.

# Relationships
## Builds Upon
- **k-flow**, **Flow number**

## Enables
- Motivation for **Five-flow conjecture**, **Four-flow conjecture**, **Three-flow conjecture**

# Common Confusions
- **Confusion**: Thinking flow-colouring duality holds for all graphs
  **Clarification**: The duality chi(G) = phi(G*) is specific to PLANE multigraphs and their duals; it does not hold for non-planar graphs

# Source Reference
Chapter 6: Flows, Section 6.5 "Flow-colouring duality," pages 152-156 (pdf pages 162-166). Theorem 6.5.3.

# Verification Notes
- Theorem statement: Directly from p. 155
- Proof outline: Summarized from pp. 155-156
- Confidence: HIGH — central theorem of the section, fully proved
