---
concept: Fractional Independence Number
slug: fractional-independence-number
category: perfect-graphs
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Colouring"
chapter_number: 5
pdf_page: 180
section: "V.5 Perfect Graphs"
extraction_confidence: high
aliases:
  - "α*(G)"
prerequisites:
  - perfect-graph
  - independence-number
extends:
  - independence-number
related:
  - perfect-graph-theorem
contrasts_with: []
answers_questions:
  - "What is the fractional independence number?"
  - "How does it characterize perfect graphs?"
---

# Quick Definition
The fractional independence number α*(G) is the maximum of Σf(v) over functions f: V(G)→[0,1] with Σ_{v∈K} f(v) ≤ 1 for every clique K. A graph is perfect iff α*(H) = α(H) for every induced subgraph H.

# Core Definition
The fractional independence number α*(G) = max Σ_{v∈G} f(v), where the maximum is over all functions f: V(G) → [0,1] such that Σ_{v∈K} f(v) ≤ 1 for every clique K ⊆ G. This is a linear programming relaxation of the independence number. **Lovász** proved that a graph is perfect if, and only if, α*(H) = α(H) for every induced subgraph H (Bollobás, p. 180).

# Prerequisites
- **Perfect graph** — characterized by this equality
- **Independence number** — α*(G) ≥ α(G) always

# Key Properties
1. α*(G) ≥ α(G) for every graph (relaxation)
2. G is perfect iff α*(H) = α(H) for all induced subgraphs H
3. α*(G) can be computed in polynomial time (linear programming)
4. For perfect graphs, α can therefore be computed in polynomial time

# Relationships
## Builds Upon
- **Independence number** — α* is the LP relaxation of α

## Related
- **Perfect graph theorem** — related characterization

# Source Reference
Chapter V: Colouring, Section V.5, page 180.

# Verification Notes
- Definition source: Direct from p. 180
- Confidence rationale: Explicitly defined with characterization
- Uncertainties: None
- Cross-reference status: Verified
