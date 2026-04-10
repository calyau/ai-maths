---
concept: Line Graphs of Bipartite Graphs are Perfect
slug: line-graph-bipartite-perfect
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
  - "Theorem V.16"
prerequisites:
  - perfect-graph
  - edge-colouring-bipartite-graphs
extends: []
related:
  - complement-of-bipartite-is-perfect
contrasts_with: []
answers_questions:
  - "Are line graphs of bipartite graphs perfect?"
---

# Quick Definition
If G is bipartite, then both L(G) and L̅(G) are perfect. This follows from χ'(G) = Δ(G) for bipartite G and König's matching-cover duality.

# Core Definition
**Theorem 16** (Bollobás, p. 177): Let G be a bipartite graph with line graph H = L(G). Then H and H̅ are perfect. For H: ω(H) = Δ(G) = χ'(G) = χ(H). For H̅: ω(H̅) = max matching = min vertex cover = χ(H̅) by König's theorem.

# Prerequisites
- **Perfect graph** — the property being established
- **Edge colouring of bipartite graphs** — provides χ'(G) = Δ(G)

# Key Properties
1. L(G) is perfect for bipartite G
2. L̅(G) is also perfect for bipartite G
3. Combines edge colouring theory with König's duality

# Relationships
## Related
- **Complement of bipartite is perfect** — analogous result
- **Galvin's theorem** — extends: list-chromatic index of L(G) also equals Δ

# Source Reference
Chapter V: Colouring, Section V.5, Theorem 16, page 177.

# Verification Notes
- Definition source: Direct theorem statement from p. 177
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
