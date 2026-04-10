---
concept: Existence of Stable Matchings
slug: stable-matching-existence
category: matchings
subcategory: stable-matchings
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.5 Stable Matchings"
extraction_confidence: high
aliases:
  - "Theorem 16"
  - "Gale-Shapley theorem"
prerequisites:
  - stable-matching
  - gale-shapley-algorithm
extends: []
related:
  - stable-matching-equal-cardinality
contrasts_with: []
answers_questions:
  - "Does a stable matching always exist?"
---

# Quick Definition
For every assignment of preferences in a bipartite graph, there exists a stable matching.

# Core Definition
**Theorem 16** (Gale-Shapley, 1962): For every assignment of preferences in a bipartite graph, there is a stable matching. The proof is constructive via the Gale-Shapley algorithm (Bollobás, p. 95).

# Prerequisites
- **Stable matching** — The object whose existence is proved
- **Gale-Shapley algorithm** — The constructive proof

# Key Properties
1. Existence holds for any bipartite graph with any preference orderings
2. The proof is constructive
3. The algorithm produces a specific stable matching (the $V_1$-optimal one)

# Construction / Recognition
Run the Gale-Shapley algorithm; it always terminates with a stable matching.

# Context & Application
This is the foundational result of stable matching theory. It guarantees that stable matchings exist regardless of the preference structure.

# Examples
**Example** (p. 96): The algorithm produces a matching $M$. For any $aB \notin M$: either $a$ never proposed to $B$ (so $a$ has a better partner) or $B$ refused $a$ for someone better (so $B$ has a better partner). Hence $M$ is stable.

# Relationships
## Builds Upon
- **gale-shapley-algorithm** — The constructive proof

## Enables
- **stable-matching-equal-cardinality** — All stable matchings have same cardinality

# Source Reference
Chapter III, Section III.5, page 95. Theorem 16.

# Verification Notes
- Definition source: Direct theorem statement from p. 95
- Confidence rationale: Explicitly stated with constructive proof
- Uncertainties: None
- Cross-reference status: Verified
