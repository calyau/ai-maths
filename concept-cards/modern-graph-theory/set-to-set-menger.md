---
concept: Set-to-Set Version of Menger's Theorem
slug: set-to-set-menger
category: connectivity
subcategory: fundamental-theorems
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.2 Connectivity and Menger's Theorem"
extraction_confidence: high
aliases:
  - "generalized Menger's theorem"
prerequisites:
  - mengers-theorem
extends:
  - mengers-theorem
related:
  - multiple-sources-sinks-max-flow
contrasts_with: []
answers_questions:
  - "How does Menger's theorem generalize to sets of vertices?"
---

# Quick Definition
For arbitrary vertex sets $S$ and $T$, the maximum number of vertex-disjoint $S$-$T$ paths (including endpoints) equals $\min\{|W| : G - W \text{ has no } S\text{-}T \text{ path}\}$.

# Core Definition
If $S$ and $T$ are arbitrary subsets of vertices of $G$, then the maximal number of vertex-disjoint $S$-$T$ paths (including endvertices!) equals $\min\{|W| : W \subset V(G), G - W \text{ has no } S\text{-}T \text{ path}\}$. This follows by adding super-source $s$ and super-sink $t$ joined to $S$ and $T$ respectively (Bollobás, p. 84).

# Prerequisites
- **Menger's theorem** — The two-vertex version

# Key Properties
1. Paths are fully vertex-disjoint (including endpoints in $S$ and $T$)
2. Reduces to standard Menger by adding super-source and super-sink
3. Generalizes to edge-disjoint version similarly

# Context & Application
Useful when the "sources" and "sinks" are sets rather than individual vertices.

# Examples
**Example** (p. 84): Add $s$ joined to all of $S$ and $t$ joined to all of $T$. Apply Menger's theorem to $s$ and $t$ in the new graph.

# Relationships
## Builds Upon
- **mengers-theorem** — Generalized to sets

## Related
- **multiple-sources-sinks-max-flow** — Flow version of the same generalization

# Source Reference
Chapter III, Section III.2, page 84.

# Verification Notes
- Definition source: Direct from p. 84
- Confidence rationale: Explicitly stated
- Uncertainties: None
- Cross-reference status: Verified
