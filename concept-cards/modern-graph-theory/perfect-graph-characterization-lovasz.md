---
concept: Lovász's Characterization of Perfect Graphs
slug: perfect-graph-characterization-lovasz
category: perfect-graphs
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Colouring"
chapter_number: 5
pdf_page: 179
section: "V.5 Perfect Graphs"
extraction_confidence: high
aliases:
  - "Hajnal-Simonovits conjecture (proved)"
prerequisites:
  - perfect-graph
  - perfect-graph-theorem
extends:
  - perfect-graph-theorem
related:
  - fractional-independence-number
contrasts_with: []
answers_questions:
  - "How can perfect graphs be characterized?"
---

# Quick Definition
A graph G is perfect if and only if |H| ≤ ω(H)·ω(H̅) for every induced subgraph H. This necessary condition (from the inequality χ ≥ |G|/α) is also sufficient.

# Core Definition
If H is an induced subgraph of a perfect graph, then ω(H) = χ(H) ≥ |H|/α(H) = |H|/ω(H̅), so |H| ≤ ω(H)·ω(H̅). Hajnal and Simonovits conjectured this trivial necessary condition is also sufficient. **Lovász (1972)** proved it: a graph is perfect iff |H| ≤ ω(H)·ω(H̅) for every induced subgraph H. Note the perfect graph theorem follows immediately since the condition is symmetric in G and G̅. Gasparian (1996) found a shorter proof (Bollobás, p. 179).

# Prerequisites
- **Perfect graph** — the class being characterized
- **Perfect graph theorem** — a consequence of this result

# Key Properties
1. |H| ≤ ω(H)·ω(H̅) for all induced H ⟺ G is perfect
2. The condition is clearly self-complementary, immediately implying the PGT
3. Lovász proved this in 1972; Gasparian found a shorter proof in 1996

# Relationships
## Builds Upon
- **Perfect graph theorem** — implied by this characterization

## Related
- **Fractional independence number** — another characterization: G perfect iff α* = α for all induced subgraphs

# Source Reference
Chapter V: Colouring, Section V.5, pages 179–180.

# Verification Notes
- Definition source: Direct from pp. 179–180
- Confidence rationale: Explicitly stated
- Uncertainties: None
- Cross-reference status: Verified
