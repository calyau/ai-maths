---
concept: Edge-Disjoint Paths
slug: edge-disjoint-paths
category: connectivity
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Connectivity"
chapter_number: 3
pdf_page: 76
section: "3.3 Menger's theorem"
extraction_confidence: high
aliases: []
prerequisites:
  - path
extends:
  - path
related:
  - mengers-theorem-edge-version
  - independent-paths
contrasts_with:
  - independent-paths
answers_questions:
  - "What are edge-disjoint paths?"
---

# Quick Definition
Two paths are edge-disjoint if they share no edges (but may share vertices).

# Core Definition
Paths are **edge-disjoint** if no two of them share an edge. Edge-disjoint paths may share vertices but not edges. The maximum number of edge-disjoint a-b paths equals the minimum edge cut between a and b (Corollary 3.3.5(ii)).

# Prerequisites
- **Path** — edge-disjoint paths are paths with a disjointness condition

# Key Properties
1. Edge-disjoint paths share no edges
2. They may share vertices (unlike independent/vertex-disjoint paths)
3. Max edge-disjoint paths = min edge cut (Menger's edge theorem)
4. Weaker than vertex-disjoint: vertex-disjoint implies edge-disjoint but not vice versa

# Context & Application
Edge-disjoint paths are the natural objects for edge-connectivity. They represent redundant communication channels that share no links (but may share nodes).

# Examples
**Example**: In the graph with vertices a,b,c and edges ab, ac, bc, the two paths a-b and a-c-b are edge-disjoint but share vertex a.

# Relationships
## Builds Upon
- **Path**

## Related
- **Menger's theorem (edge version)** — counts max edge-disjoint paths

## Contrasts With
- **Independent paths** — share no vertices (stronger condition)

# Source Reference
Chapter 3, Section 3.3.

# Verification Notes
- Standard concept in Section 3.3
- Confidence: HIGH
