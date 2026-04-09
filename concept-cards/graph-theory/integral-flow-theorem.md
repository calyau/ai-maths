---
concept: Integral Flow Theorem
slug: integral-flow-theorem
category: network-flows
subcategory: network-flows
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Flows"
chapter_number: 6
pdf_page: 154
section: "6.2 Flows in networks"
extraction_confidence: high
aliases:
  - "integrality theorem"
prerequisites:
  - max-flow-min-cut-theorem
  - flow-in-network
  - capacity-function
related:
  - menger-theorem-flow-version
answers_questions:
  - "When can we find an integral maximum flow?"
---

# Quick Definition
In every network with integral capacity function, there exists an integral flow of maximum total value.

# Core Definition
**Corollary 6.2.3**: In every network (with integral capacity function) there exists an integral flow of maximum total value. This follows directly from the proof of the max-flow min-cut theorem, since the flow constructed by the Ford-Fulkerson algorithm is integral at every step. (Diestel, p. 144)

# Prerequisites
- **Max-flow min-cut theorem** — The integral flow theorem is a corollary
- **Flow in network** — Must understand integral flows
- **Capacity function** — Requires integral capacities

# Key Properties
1. Integral capacities guarantee the existence of an integral maximum flow
2. The Ford-Fulkerson construction produces an integral flow
3. Critical for applications to combinatorial problems (matchings, connectivity)

# Relationships
## Builds Upon
- **Max-flow min-cut theorem** — Direct corollary

## Enables
- **Menger's theorem (flow version)** — Uses integral flows to construct disjoint paths

# Source Reference
Chapter 6: Flows, Section 6.2, Corollary 6.2.3, page 144 (pdf page 154).

# Verification Notes
- Confidence: HIGH — stated as a corollary with clear proof reference
