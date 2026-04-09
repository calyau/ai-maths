---
concept: Bipartite Matching Algorithm
slug: bipartite-matching-algorithm
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
  - "augmenting path algorithm"
prerequisites:
  - matching
  - m-augmenting-path
  - maximum-matching
extends: []
related:
  - konigs-theorem
  - halls-marriage-theorem
contrasts_with: []
answers_questions:
  - "How do you find a maximum matching in a bipartite graph?"
---

# Quick Definition
The augmenting path algorithm finds a maximum matching by repeatedly finding and applying augmenting paths until none remain.

# Core Definition
The **augmenting path algorithm** for bipartite matching works as follows: start with any matching M (e.g., empty), search for an M-augmenting path, and if one is found, augment M along it. Repeat until no augmenting path exists. The resulting matching is maximum (Diestel, p. 44, Exercise 1).

# Prerequisites
- **Matching** — the object being optimized
- **M-augmenting path** — the tool for improvement
- **Maximum matching** — the goal

# Key Properties
1. Each augmentation increases |M| by exactly 1
2. The algorithm terminates (|M| <= |V|/2)
3. The final matching is guaranteed maximum (by the augmenting path characterization)
4. For bipartite graphs, augmenting paths can be found efficiently via BFS/DFS
5. The overall complexity is O(|V| * |E|) for simple implementations, O(sqrt(|V|) * |E|) for Hopcroft-Karp

# Construction / Recognition
## Algorithm Steps
1. Initialize M = empty matching
2. Search for an M-augmenting path P (e.g., via BFS from unmatched vertices in A)
3. If P found: M := M symmetric-difference E(P); go to step 2
4. If no P exists: return M (it is maximum)

# Context & Application
This algorithm is the practical realization of the theory developed in Section 2.1. The reduction of maximum matching to augmenting path finding (Exercise 1) is the key theoretical insight enabling efficient algorithms.

# Examples
**Example** (p. 44): Starting from any matching, alternating paths from unmatched vertices in A are searched. Each successful search yields an augmenting path that increases the matching.

# Relationships
## Builds Upon
- **Matching**, **M-augmenting path**, **maximum matching**

## Related
- **Konig's theorem** — the proof constructs both optimal matching and minimum cover
- **Hall's marriage theorem** — the first proof is algorithmic

# Source Reference
Chapter 2, Section 2.1, pp. 44-46 (pdf pp. 44-46). Exercise 1, p. 51.

# Verification Notes
- From pp. 44-46 and Exercise 1
- Confidence: HIGH — algorithm described and correctness established
