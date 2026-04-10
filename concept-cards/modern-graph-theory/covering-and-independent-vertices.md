---
concept: Covering and Independent Vertices
slug: covering-and-independent-vertices
category: matchings
subcategory: basic-definitions
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.3 Matching"
extraction_confidence: high
aliases:
  - "vertex cover"
  - "independent vertices"
  - "covering"
prerequisites:
  - matching
extends: []
related:
  - konigs-theorem
contrasts_with: []
answers_questions:
  - "What does it mean for edges and vertices to cover all vertices?"
---

# Quick Definition
An edge $e$ covers its endpoints; a vertex covers itself. A set of edges and vertices covers all vertices if every vertex is either an endpoint of a selected edge or is itself selected.

# Core Definition
If an edge $e$ is incident with a vertex $x$, then $e$ covers $x$, and $x$ covers $e$. Furthermore, a vertex is said to cover itself. A set of independent vertices is a set of pairwise nonadjacent vertices (Bollobás, p. 87).

# Prerequisites
- **Matching** — Independent edges cover some vertices

# Key Properties
1. In a bipartite graph: max independent vertices = $m + n - h$ = min cover size (Corollary 10)
2. König's theorem connects matching, independence, and covering numbers

# Context & Application
The covering/independence duality is central to König's theorem (Corollary 10).

# Examples
**Example** (p. 87): In Corollary 10, $i = j = m + n - h$ where $h$ is max matching, $i$ is max independent set, $j$ is min cover.

# Relationships
## Related
- **konigs-theorem** — Connects these quantities

# Source Reference
Chapter III, Section III.3, page 87.

# Verification Notes
- Definition source: Direct from p. 87
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
