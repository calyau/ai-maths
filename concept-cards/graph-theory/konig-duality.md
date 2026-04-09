---
concept: "Konig Duality"
slug: konig-duality
category: matching-and-covering
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Matching, Covering and Packing"
chapter_number: 2
pdf_page: 54
section: "2.3 Packing and covering"
extraction_confidence: medium
aliases:
  - "matching-cover duality"
  - "min-max duality"
prerequisites:
  - konigs-theorem
  - matching
  - vertex-cover
extends:
  - konigs-theorem
related:
  - mengers-theorem
  - erdos-posa-property
  - gallais-theorem
contrasts_with: []
answers_questions:
  - "What is the duality between matchings and covers?"
---

# Quick Definition
Konig duality is the principle that in bipartite graphs, the maximum matching equals the minimum vertex cover, establishing a min-max duality between packing (matchings) and covering (vertex covers).

# Core Definition
**Konig duality** refers to the min-max relationship max matching = min vertex cover in bipartite graphs (Konig's theorem, Theorem 2.1.1). More broadly, it refers to the general principle that packing and covering numbers in graphs are related by duality (Diestel, Section 2.3 context).

# Prerequisites
- **Konig's theorem** — the foundational result
- **Matching** — the packing side
- **Vertex cover** — the covering side

# Key Properties
1. In bipartite graphs: max matching = min vertex cover (exact equality)
2. In general graphs: max matching <= min vertex cover (inequality may be strict)
3. Generalizes to the Erdos-Posa framework for arbitrary subgraph classes
4. Related to LP duality and total unimodularity

# Context & Application
Konig duality is the template for many min-max results in combinatorics: Menger's theorem, the max-flow min-cut theorem, and the Erdos-Posa property all follow this pattern of "max packing = min cover."

# Examples
**Example**: In K_{3,3}, max matching = 3 = min vertex cover. In K3 (non-bipartite), max matching = 1 but min vertex cover = 2.

# Relationships
## Builds Upon
- **Konig's theorem**, **matching**, **vertex cover**

## Related
- **Menger's theorem** — min separator = max disjoint paths
- **Erdos-Posa property** — packing-covering duality for cycles
- **Gallai's theorem** — vertex cover + independent set = |V|

# Source Reference
Chapter 2, Sections 2.1 and 2.3.

# Verification Notes
- Synthesized from the duality framework of Sections 2.1 and 2.3
- Confidence: MEDIUM — the principle is fundamental but not given a single name in the text
