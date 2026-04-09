---
concept: Matching in General Graphs
slug: matching-in-general-graphs
category: matching-and-covering
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Matching, Covering and Packing"
chapter_number: 2
pdf_page: 49
section: "2.2 Matching in general graphs"
extraction_confidence: medium
aliases: []
prerequisites:
  - matching
  - tuttes-theorem
extends:
  - matching
related:
  - halls-marriage-theorem
  - factor-critical-graph
contrasts_with: []
answers_questions:
  - "How does matching theory differ for general vs bipartite graphs?"
---

# Quick Definition
Matching theory in general (non-bipartite) graphs is significantly more complex than in bipartite graphs. Tutte's theorem replaces Hall's theorem, and factor-critical graphs replace the simple bipartite structure.

# Core Definition
Section 2.2 extends matching theory from bipartite graphs to general graphs. The key differences: (1) Hall's marriage condition is replaced by Tutte's condition q(G-S) <= |S|; (2) The structural decomposition involves factor-critical components rather than simple bipartitions; (3) The Gallai-Edmonds structure theorem provides the canonical decomposition.

# Prerequisites
- **Matching** — general matchings
- **Tutte's theorem** — characterizes 1-factor existence

# Key Properties
1. Tutte's condition replaces the marriage condition
2. Factor-critical components replace the bipartite structure
3. Konig's theorem fails for general graphs (Exercise 18)
4. The Gallai-Edmonds structure describes all maximum matchings
5. Algorithms are more complex (Edmonds' blossom algorithm)

# Context & Application
The transition from bipartite to general matching theory is one of the major themes of Section 2.2. While many bipartite results have analogues, the non-bipartite case requires fundamentally new ideas (odd components, factor-criticality).

# Examples
**Example** (Exercise 18): In K3, max matching = 1 but min vertex cover = 2, showing Konig's theorem fails for non-bipartite graphs.

# Relationships
## Builds Upon
- **Matching**, **Tutte's theorem**

## Related
- **Hall's marriage theorem** — the bipartite predecessor
- **Factor-critical graph** — key structure in general matching

# Source Reference
Chapter 2, Section 2.2, pp. 49-54 (pdf pp. 49-54).

# Verification Notes
- Synthesized from Section 2.2
- Confidence: MEDIUM — overview concept, not a single definition
