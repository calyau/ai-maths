---
concept: Integrality Theorem
slug: integrality-theorem
category: network-flows
subcategory: fundamental-theorems
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.1 Flows in Directed Graphs"
extraction_confidence: high
aliases:
  - "integral flow theorem"
  - "Theorem 2"
prerequisites:
  - max-flow-min-cut-theorem
  - capacity-of-edge
extends:
  - max-flow-min-cut-theorem
related:
  - augmenting-path
  - mengers-theorem
contrasts_with: []
answers_questions:
  - "When does a maximum flow have integer values?"
---

# Quick Definition
If the capacity function is integral (all capacities are integers), then there exists a maximal flow that is also integral, with integer flow on every edge.

# Core Definition
**Theorem 2**: If the capacity function is integral then there is a maximal flow that is also integral (Bollobás, p. 77). The proof follows from the augmenting path algorithm: starting from the zero flow (which is integral), each augmentation preserves integrality since the augmentation amount is the minimum of positive integers.

# Prerequisites
- **Max-flow min-cut theorem** — The integrality theorem is a consequence
- **Capacity of an edge** — Must be integral for the theorem to apply

# Key Properties
1. Does not claim uniqueness: there may be non-integral maximal flows too
2. The algorithm constructively produces an integral maximal flow
3. The existence of an integral maximal flow also implies the existence of a maximal *acyclic* flow
4. Essential for deducing Menger's theorem from the max-flow min-cut theorem

# Construction / Recognition
1. Start with the zero flow (integral)
2. Apply the augmenting path algorithm
3. At each step, the augmentation amount $\varepsilon$ is an integer (minimum of positive integers)
4. The resulting maximal flow is integral

# Context & Application
The integrality theorem is the bridge between continuous flow theory and combinatorial applications. When using max-flow min-cut to prove results about paths and matchings, the integrality theorem ensures that the optimal flow decomposes into unit flows along paths.

# Examples
**Example** (p. 77): In the proof of Menger's theorem (Theorem 5), edges are given capacity 1. The integrality theorem ensures a maximal flow with current 0 or 1 in each edge, which decomposes into independent paths.

# Relationships
## Builds Upon
- **max-flow-min-cut-theorem** — The integrality theorem extends it

## Enables
- **mengers-theorem** — Uses integral flows to find independent paths
- **halls-theorem** — Uses integral flows in bipartite graphs

## Related
- **augmenting-path** — The constructive proof uses augmenting paths

# Common Errors
- **Error**: Assuming every maximal flow is integral when capacities are integral
  **Correction**: The theorem guarantees *existence* of an integral maximal flow, not uniqueness

# Common Confusions
- **Confusion**: Thinking the integrality theorem requires all capacities to be finite
  **Clarification**: The theorem applies when the capacity function is integral; some edges may have infinite capacity

# Source Reference
Chapter III, Section III.1, page 77. Theorem 2.

# Verification Notes
- Definition source: Direct theorem statement from p. 77
- Confidence rationale: Explicitly stated and proved
- Uncertainties: None
- Cross-reference status: Verified
