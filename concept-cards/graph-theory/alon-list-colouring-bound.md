---
concept: "Alon's Theorem (Average Degree Forces Choosability)"
slug: alon-list-colouring-bound
category: graph-colouring
subcategory: list-colouring
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Colouring"
chapter_number: 5
pdf_page: 122
section: "5.4 List colouring"
extraction_confidence: medium
aliases:
  - "Theorem 5.4.1"
  - "Alon 1993"
prerequisites:
  - choice-number
extends: []
related:
  - chromatic-number
  - colouring-number
contrasts_with: []
answers_questions:
  - "Does large average degree force large choice number?"
---

# Quick Definition
There exists a function f: N -> N such that all graphs G with average degree d(G) >= f(k) satisfy ch(G) >= k. Large average degree forces large choice number.

# Core Definition
**Theorem 5.4.1** (Alon 1993): "There exists a function f: N -> N such that, given any integer k, all graphs G with average degree d(G) >= f(k) satisfy ch(G) >= k" (Diestel, p. 122).

# Prerequisites
- **Choice number**

# Key Properties
1. Contrasts with chromatic number: K_{n,n} has chi = 2 but arbitrarily large average degree
2. Large average degree forces large ch but NOT large chi
3. Proved using probabilistic methods (Chapter 11)

# Context & Application
This theorem highlights a fundamental difference between the chromatic number and the choice number. While chi is not forced up by local density (bipartite graphs can have high average degree), ch IS. This makes ch more sensitive to graph structure.

# Relationships
## Related
- **Chromatic number** -- NOT forced up by average degree
- **Colouring number** -- Also forces ch up

# Source Reference
Chapter 5, Section 5.4, Theorem 5.4.1, page 122.

# Verification Notes
- Theorem stated; proof in Chapter 11
- Confidence: MEDIUM -- proof not given in Ch. 5
