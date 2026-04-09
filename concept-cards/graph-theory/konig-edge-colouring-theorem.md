---
concept: "Konig's Edge Colouring Theorem"
slug: konig-edge-colouring-theorem
category: graph-colouring
subcategory: edge-colouring
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Colouring"
chapter_number: 5
pdf_page: 122
section: "5.3 Colouring edges"
extraction_confidence: high
aliases:
  - "Proposition 5.3.1"
  - "Konig 1916"
prerequisites:
  - chromatic-index
  - edge-colouring
extends: []
related:
  - vizing-theorem
  - class-one-class-two
contrasts_with: []
answers_questions:
  - "What is the chromatic index of a bipartite graph?"
---

# Quick Definition
Every bipartite graph G satisfies chi'(G) = Delta(G). That is, bipartite graphs are always class 1.

# Core Definition
**Proposition 5.3.1** (Konig 1916): "Every bipartite graph G satisfies chi'(G) = Delta(G)" (Diestel, p. 119).

# Prerequisites
- **Chromatic index** and **Edge colouring**

# Key Properties
1. Bipartite graphs achieve the trivial lower bound chi' = Delta
2. The proof is by induction on ||G||, using alternating path arguments
3. Extends to list-chromatic index: ch'(G) = Delta(G) for bipartite G (Galvin's theorem)

# Context & Application
Konig's theorem shows that bipartite graphs have the best possible edge colouring behaviour. This contrasts with the general case where chi' can be Delta + 1. The proof technique (alternating colour paths) is foundational for Vizing's theorem.

# Relationships
## Enables
- **Class one/class two** -- Bipartite graphs are always class 1
- **Galvin's theorem** -- List version for bipartite graphs

## Related
- **Vizing's theorem** -- General bound chi' in {Delta, Delta+1}

# Source Reference
Chapter 5, Section 5.3, Proposition 5.3.1, page 119.

# Verification Notes
- Full proof given p. 119
- Confidence: HIGH -- named classical theorem with proof
