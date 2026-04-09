---
concept: k-Constructible Graph
slug: k-constructible-graph
category: graph-colouring
subcategory: vertex-colouring
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Colouring"
chapter_number: 5
pdf_page: 122
section: "5.2 Colouring vertices"
extraction_confidence: high
aliases:
  - "Hajos construction"
  - "Hajos graph"
prerequisites:
  - chromatic-number
extends: []
related:
  - chromatic-number
contrasts_with: []
answers_questions:
  - "How can all graphs of chromatic number >= k be constructed?"
---

# Quick Definition
The k-constructible graphs are defined recursively: K^k is k-constructible; if G is k-constructible and xy are non-adjacent, then (G+xy)/xy is; and a specific "Hajos join" of two k-constructible graphs is. A graph has chi >= k iff it contains a k-constructible subgraph.

# Core Definition
**Theorem 5.2.6** (Hajos 1961): "chi(G) >= k if and only if G has a k-constructible subgraph" (Diestel, p. 118). The three construction rules are: (i) K^k is k-constructible, (ii) adding and contracting a non-edge, (iii) the Hajos join operation.

# Prerequisites
- **Chromatic number** -- Characterizes graphs with chi >= k

# Key Properties
1. All k-constructible graphs (and their supergraphs) are at least k-chromatic
2. Conversely, every graph with chi >= k contains a k-constructible subgraph
3. Provides a "certificate" for high chromatic number

# Context & Application
Hajos's theorem provides a constructive characterization of high chromatic number, complementing the NP-hardness of determining chi(G). It shows that chi >= k can always be "explained" by a recursive construction starting from K^k.

# Relationships
## Related
- **Chromatic number** -- Characterizes chi >= k

# Source Reference
Chapter 5, Section 5.2, Theorem 5.2.6, pages 117-118.

# Verification Notes
- Full proof given pp. 118-119
- Confidence: HIGH -- named theorem with proof
