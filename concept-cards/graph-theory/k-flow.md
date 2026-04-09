---
concept: k-Flow
slug: k-flow
category: network-flows
subcategory: algebraic-flows
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Flows"
chapter_number: 6
pdf_page: 157
section: "6.3 Group-valued flows"
extraction_confidence: high
aliases:
  - "nowhere-zero k-flow"
prerequisites:
  - circulation
  - nowhere-zero-flow
extends:
  - h-flow
related:
  - flow-number
  - two-flow
  - three-flow
  - four-flow
  - six-flow-theorem
contrasts_with:
  - h-flow
answers_questions:
  - "What is a k-flow?"
  - "How are k-flows related to group-valued flows?"
---

# Quick Definition
A k-flow on a multigraph G is a Z-valued circulation f such that 0 < |f(e-arrow)| < k for every directed edge; equivalently, an integer-valued nowhere-zero flow with values bounded by k.

# Core Definition
Let k >= 1 be an integer and G = (V, E) a multigraph. A Z-flow f on G such that 0 < |f(e-arrow)| < k for all e-arrow in E-arrow is called a **k-flow**. Any k-flow is also an l-flow for all l > k. (Diestel, p. 147)

**Theorem 6.3.3** (Tutte 1950): A multigraph admits a k-flow if and only if it admits a Z_k-flow. This means the general question about H-flows for arbitrary groups reduces to k-flows.

# Prerequisites
- **Circulation** — A k-flow is a Z-circulation with bounded non-zero values
- **Nowhere-zero flow** — The non-zero requirement is essential

# Key Properties
1. Values are integers with 0 < |f(e-arrow)| < k
2. Every k-flow is an l-flow for all l > k
3. Existence of k-flow is equivalent to existence of Z_k-flow (Theorem 6.3.3)
4. A graph has a k-flow for some k if and only if it is bridgeless
5. Z_k-flows are often easier to construct than k-flows (by summing partial flows)

# Context & Application
k-flows are the integer-valued version of group-valued flows, and by Tutte's theorem they capture all the information. The question of determining the least k for which a k-flow exists (the flow number) leads to deep open problems.

# Examples
**Example** (p. 149): A graph has a 1-flow (the empty set) iff it has no edges.

**Example** (p. 150): K^4 has flow number 4; all K^n for odd n > 1 have flow number 2.

# Relationships
## Builds Upon
- **H-flow** — k-flows are the integer-valued special case

## Enables
- **Flow number** — Defined as the least k admitting a k-flow
- **Two-flow**, **Three-flow**, **Four-flow** — Specific cases

## Contrasts With
- **H-flow** — H-flows take values in arbitrary abelian groups; k-flows use integers with bounded absolute value

# Source Reference
Chapter 6: Flows, Section 6.3, pages 147-149 (pdf pages 157-159). Theorem 6.3.3.

# Verification Notes
- Confidence: HIGH — explicit definition and major theorem
