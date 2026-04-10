---
concept: Imperfect Graph
slug: imperfect-graph
category: perfect-graphs
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Colouring"
chapter_number: 5
pdf_page: 180
section: "V.5 Perfect Graphs"
extraction_confidence: high
aliases:
  - "critically imperfect graph"
prerequisites:
  - perfect-graph
extends: []
related:
  - perfect-graph-conjecture
contrasts_with:
  - perfect-graph
answers_questions:
  - "What graphs are not perfect?"
---

# Quick Definition
A graph is imperfect if some induced subgraph H has χ(H) > ω(H). A graph is critically imperfect if it is imperfect but every proper induced subgraph is perfect.

# Core Definition
A graph G is **imperfect** if it is not perfect, i.e., there exists an induced subgraph H with χ(H) > ω(H). A graph is **critically imperfect** if it is imperfect but every proper induced subgraph is perfect. Known examples: odd cycles C_{2k+1} (k ≥ 2) and their complements. The Strong Perfect Graph Conjecture (Berge, 1960; proved 2006) states these are the only critically imperfect graphs (Bollobás, p. 180).

# Prerequisites
- **Perfect graph** — imperfect is the negation

# Key Properties
1. A graph with an odd hole (C_{2k+1}, k ≥ 2) as induced subgraph is imperfect
2. A graph with an odd antihole (complement of odd hole) as induced subgraph is imperfect
3. Every triangle-free non-bipartite graph is imperfect (ω = 2, χ ≥ 3)
4. The only known critically imperfect graphs are odd holes and odd antiholes

# Relationships
## Contrasts With
- **Perfect graph** — imperfect graphs violate χ = ω for some induced subgraph

## Related
- **Perfect graph conjecture** — characterizes imperfect graphs by forbidden subgraphs

# Source Reference
Chapter V: Colouring, Section V.5, page 180.

# Verification Notes
- Definition source: Direct from p. 180
- Confidence rationale: Explicitly discussed
- Uncertainties: None
- Cross-reference status: Verified
