---
concept: "König's Theorem"
slug: konigs-theorem
category: matchings
subcategory: fundamental-theorems
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.3 Matching"
extraction_confidence: high
aliases:
  - "Corollary 10"
  - "König-Egerváry theorem"
prerequisites:
  - halls-theorem
  - deficiency-version-halls-theorem
extends:
  - halls-theorem
related:
  - matching
  - independent-vertices
contrasts_with: []
answers_questions:
  - "What is the relationship between maximum matching and minimum cover in bipartite graphs?"
---

# Quick Definition
In a bipartite graph, the maximum number of independent edges equals $m + n$ minus the maximum number of independent vertices, and also equals the minimum number of edges and vertices covering all vertices.

# Core Definition
**Corollary 10**: Let $G = G_2(m,n)$ be a bipartite graph. Write $h$ for the maximal number of independent edges, $i$ for the maximal number of independent vertices, and $j$ for the minimal number of edges and vertices covering all the vertices. Then $i = j = m + n - h$ (Bollobás, p. 87).

# Prerequisites
- **Hall's theorem** — The foundation
- **Deficiency version of Hall's theorem** — Used in the proof

# Key Properties
1. Three seemingly different quantities are all equal
2. Connects matching number, independence number, and covering number
3. Specific to bipartite graphs (fails for general graphs)

# Construction / Recognition
1. Find a maximum matching of size $h$
2. Independence number is $i = m + n - h$
3. Minimum cover size is $j = m + n - h$

# Context & Application
König's theorem is a cornerstone of bipartite graph theory, connecting matching duality with covering problems.

# Examples
**Example** (p. 87): The proof shows that edges and vertices in a cover can be reorganized so that the edges are independent, giving $j = m + n - h$.

# Relationships
## Builds Upon
- **halls-theorem** — Used in the proof
- **deficiency-version-halls-theorem** — Provides the key inequality

## Related
- **matching** — Matching number $h$

# Source Reference
Chapter III, Section III.3, page 87. Corollary 10.

# Verification Notes
- Definition source: Direct from p. 87
- Confidence rationale: Explicitly stated with proof
- Uncertainties: None
- Cross-reference status: Verified
