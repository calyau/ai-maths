---
concept: Petersen Graph (Flow Perspective)
slug: petersen-graph-flow
category: network-flows
subcategory: algebraic-flows
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Flows"
chapter_number: 6
pdf_page: 166
section: "6.6 Tutte's flow conjectures"
extraction_confidence: high
aliases: []
prerequisites:
  - snark
  - four-flow
related:
  - four-flow-conjecture
  - five-flow-conjecture
answers_questions:
  - "Why is the Petersen graph important in flow theory?"
---

# Quick Definition
The Petersen graph is the smallest snark: it is cubic, bridgeless, but has no 4-flow (equivalently, not 3-edge-colourable). It serves as the obstruction in Tutte's 4-flow conjecture.

# Core Definition
The **Petersen graph** (Fig. 6.6.1) is a bridgeless graph without a 4-flow: since it is cubic but not 3-edge-colourable, it cannot have a 4-flow by Proposition 6.4.5(ii). Tutte's 4-flow conjecture states that the Petersen graph must be present as a minor in every graph without a 4-flow. The Petersen graph has been shown to be the smallest snark. (Diestel, pp. 156-157)

# Prerequisites
- **Snark** — The Petersen graph is the prototypical snark
- **Four-flow** — It lacks a 4-flow

# Key Properties
1. Cubic (3-regular), bridgeless
2. Not 3-edge-colourable
3. Flow number phi = 5 (has a 5-flow but no 4-flow)
4. The smallest snark
5. Central to the 4-flow conjecture

# Examples
**Example** (p. 157, Fig. 6.6.1): The Petersen graph illustrated.

# Source Reference
Chapter 6, Section 6.6, pages 156-157 (pdf pages 166-167). Fig. 6.6.1.

# Verification Notes
- Confidence: HIGH — extensively discussed
