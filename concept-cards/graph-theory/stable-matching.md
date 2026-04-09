---
concept: Stable Matching
slug: stable-matching
category: matching-and-covering
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Matching, Covering and Packing"
chapter_number: 2
pdf_page: 48
section: "2.1 Matching in bipartite graphs"
extraction_confidence: high
aliases:
  - "stable marriage"
prerequisites:
  - matching
  - bipartite-graph
extends:
  - matching
related:
  - halls-marriage-theorem
contrasts_with: []
answers_questions:
  - "What is a stable matching?"
  - "Does every bipartite graph with preferences have a stable matching?"
---

# Quick Definition
A matching M is stable (with respect to a set of preferences) if no unmatched edge e has both of its endpoints preferring e over their current matching edges.

# Core Definition
Given a family of linear orderings (<=_v) on E(v) for each vertex v (a set of **preferences**), a matching M in G is **stable** if for every edge e in E \ M there exists an edge f in M such that e and f share a common vertex v with e <_v f. The **stable marriage theorem** (Gale & Shapley 1962) states: for every set of preferences, G has a stable matching (Diestel, Theorem 2.1.4, p. 48).

# Prerequisites
- **Matching** — stability is a property of a matching
- **Bipartite graph** — the theorem is stated for bipartite graphs

# Key Properties
1. A matching is unstable if some edge e not in M would be preferred by both its endpoints over their current edges
2. Every bipartite graph with preferences has a stable matching (Theorem 2.1.4)
3. The proof is algorithmic: the Gale-Shapley algorithm constructs a stable matching
4. Non-bipartite graphs may have no stable matching (Exercise 11)
5. All stable matchings of a given bipartite graph cover the same vertices (Exercise 12)

# Construction / Recognition
## Gale-Shapley Algorithm (from proof)
1. Start with the empty matching
2. Find an unmatched vertex a in A that is acceptable to some b in B
3. Add to M the best edge ab (according to a's preferences) where a is acceptable to b
4. If b was already matched, discard the old edge at b
5. Repeat until no unmatched vertex in A is acceptable to any vertex in B
6. The result is a stable matching

# Context & Application
Stable matchings model situations where participants have preferences, such as college admissions or organ donor matching. The Gale-Shapley algorithm earned the 2012 Nobel Prize in Economics for its practical applications.

# Examples
**Example** (p. 48): The proof constructs a sequence of matchings starting from the empty matching, each better for vertices in B than the previous one, until a stable matching is reached.

# Relationships
## Builds Upon
- **Matching**, **bipartite graph**

## Enables
- Applications in economics, market design, and assignment problems

## Related
- **Hall's marriage theorem** — both concern matchings in bipartite graphs

# Common Errors
- **Error**: Assuming stability implies maximum size
  **Correction**: A stable matching need not be a maximum matching (Exercise 10)

# Common Confusions
- **Confusion**: Confusing stability with optimality (maximum size)
  **Clarification**: Stability is about local incentive-compatibility (no blocking pair), not global size maximization

# Source Reference
Chapter 2, Section 2.1, Theorem 2.1.4, pp. 48-49 (pdf pp. 48-49).

# Verification Notes
- Definition and theorem from pp. 48-49
- Confidence: HIGH — explicitly defined with full proof
