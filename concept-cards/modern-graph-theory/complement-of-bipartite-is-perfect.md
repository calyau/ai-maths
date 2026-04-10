---
concept: Complement of a Bipartite Graph is Perfect
slug: complement-of-bipartite-is-perfect
category: perfect-graphs
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Colouring"
chapter_number: 5
pdf_page: 176
section: "V.5 Perfect Graphs"
extraction_confidence: high
aliases:
  - "Theorem V.15"
  - "Gallai-König theorem"
prerequisites:
  - perfect-graph
extends: []
related:
  - perfect-graph-theorem
contrasts_with: []
answers_questions:
  - "Are complements of bipartite graphs perfect?"
---

# Quick Definition
The complement of every bipartite graph is perfect. This was the first result on perfect graphs (Gallai-König, 1932), preceding Berge's definition by 28 years.

# Core Definition
**Theorem 15** (Bollobás, p. 176): The complement of a bipartite graph is perfect. The proof: in a colouring of G̅ (G bipartite), every colour class is either a vertex or an edge of G. So χ(G̅) = min vertex cover of G = α(G) = ω(G̅) by König's theorem (Corollary III.10).

# Prerequisites
- **Perfect graph** — the property being established

# Key Properties
1. For bipartite G: χ(G̅) = ω(G̅)
2. Follows from König's min-cover = max-matching duality
3. First result on perfect graphs (1932), before the concept was named

# Relationships
## Related
- **Perfect graph theorem** — later showed all complements of perfect graphs are perfect

# Source Reference
Chapter V: Colouring, Section V.5, Theorem 15, page 176.

# Verification Notes
- Definition source: Direct theorem statement from p. 176
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
