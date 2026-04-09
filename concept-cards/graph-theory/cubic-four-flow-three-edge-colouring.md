---
concept: Cubic 4-Flow and 3-Edge-Colouring Equivalence
slug: cubic-four-flow-three-edge-colouring
category: network-flows
subcategory: algebraic-flows
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Flows"
chapter_number: 6
pdf_page: 161
section: "6.4 k-Flows for small k"
extraction_confidence: high
aliases:
  - "Proposition 6.4.5(ii)"
prerequisites:
  - four-flow
  - k-flow
related:
  - snark
  - four-flow-conjecture
answers_questions:
  - "How are 4-flows related to edge colourings in cubic graphs?"
---

# Quick Definition
A cubic graph has a 4-flow if and only if it is 3-edge-colourable (Proposition 6.4.5(ii)). This connects flow theory to edge-colouring theory.

# Core Definition
**Proposition 6.4.5(ii)**: A cubic graph has a 4-flow if and only if it is 3-edge-colourable. The proof uses the Klein four-group Z_2^2: since a = -a in Z_2^2, the three non-zero elements form the colour set, and (F2) at each cubic vertex is equivalent to proper 3-edge-colouring. (Diestel, p. 152)

**Corollary 6.4.6**: Every cubic 3-edge-colourable graph is bridgeless.

# Prerequisites
- **Four-flow** — The equivalence concerns 4-flows
- **k-flow** — General flow concepts

# Key Properties
1. Establishes a bridge between flow theory and edge-colouring
2. Uses the Klein four-group Z_2^2 = Z_2 x Z_2
3. The Petersen graph: cubic, not 3-edge-colourable, hence no 4-flow (snark)
4. A cubic bridgeless graph without a 4-flow is called a snark

# Relationships
## Related
- **Snark** — Defined as cubic bridgeless without 4-flow (i.e., not 3-edge-colourable)
- **Four-flow conjecture** — Every snark contains the Petersen graph as a minor

# Source Reference
Chapter 6, Section 6.4, Proposition 6.4.5(ii), page 152 (pdf page 162). Corollary 6.4.6.

# Verification Notes
- Confidence: HIGH — characterization with proof
