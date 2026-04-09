---
concept: Augmenting Path Characterization
slug: augmenting-path-characterization
category: matching-and-covering
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Matching, Covering and Packing"
chapter_number: 2
pdf_page: 44
section: "2.1 Matching in bipartite graphs"
extraction_confidence: high
aliases:
  - "Berge's theorem"
  - "optimality criterion"
prerequisites:
  - m-augmenting-path
  - maximum-matching
extends: []
related:
  - konigs-theorem
contrasts_with: []
answers_questions:
  - "When is a matching maximum?"
---

# Quick Definition
A matching M is maximum if and only if there is no M-augmenting path.

# Core Definition
A matching is maximum (optimal) if and only if no augmenting path exists with respect to it. This characterization (Exercise 1, p. 51; attributed to Berge) reduces the maximum matching problem to finding augmenting paths (Diestel, p. 44).

# Prerequisites
- **M-augmenting path** — the absence of which characterizes optimality
- **Maximum matching** — the property being characterized

# Key Properties
1. Forward: if M is not maximum, an augmenting path exists
2. Backward: if no augmenting path exists, M is maximum
3. The proof uses the symmetric difference of M with a larger matching M'
4. This is the theoretical foundation for matching algorithms
5. Applies to both bipartite and general graphs

# Context & Application
This characterization is fundamental to all matching algorithms. The augmenting path method works by repeatedly finding and applying augmenting paths until none remain, at which point the matching is guaranteed to be maximum.

# Examples
**Example** (p. 44): Starting with any matching M, the algorithm finds augmenting paths and applies them. When no augmenting path exists, M is maximum.

# Relationships
## Builds Upon
- **M-augmenting path**, **maximum matching**

## Related
- **Konig's theorem** — another characterization of maximum matchings (in bipartite graphs)

# Source Reference
Chapter 2, Section 2.1, Exercise 1, p. 51 (pdf p. 51). Discussed on p. 44.

# Verification Notes
- From p. 44 and Exercise 1
- Confidence: HIGH — standard result
