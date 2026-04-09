---
concept: Deficiency
slug: deficiency
category: matching-and-covering
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Matching, Covering and Packing"
chapter_number: 2
pdf_page: 52
section: "2.2 Matching in general graphs"
extraction_confidence: high
aliases:
  - "d(G)"
  - "matching deficiency"
prerequisites:
  - tuttes-condition
  - odd-component
  - maximum-matching
extends: []
related:
  - tutte-berge-formula
  - gallai-edmonds-structure
contrasts_with: []
answers_questions:
  - "What is the deficiency of a graph?"
---

# Quick Definition
The deficiency d(G) = max_S(q(G-S) - |S|) measures how far a graph is from having a 1-factor. The maximum matching size is (|V| - d(G))/2.

# Core Definition
For a set T of vertices, define d(T) = d_G(T) = q(G-T) - |T|. The **deficiency** d(G) = max_T d(T) measures the worst-case excess of odd components over |T|. The maximum matching size is (|V| - d(G))/2 (Diestel, p. 52, context of Theorem 2.2.3 proof).

# Prerequisites
- **Tutte's condition** — d(G) = 0 iff Tutte's condition holds
- **Odd component** — q(G-T) counts odd components
- **Maximum matching** — size determined by deficiency

# Key Properties
1. d(G) >= 0 always (take T = empty set, q(G) >= 0)
2. d(G) = 0 iff G has a 1-factor (Tutte's theorem)
3. max matching = (|V| - d(G))/2
4. The set S maximizing d(T) is used in the Gallai-Edmonds decomposition
5. d(G) equals the number of unmatched vertices in a maximum matching

# Context & Application
Deficiency provides a quantitative measure of how far a graph is from having a perfect matching. The Tutte-Berge formula expresses the maximum matching size in terms of deficiency.

# Examples
**Example**: If G = K3 (triangle), d(G) = q(G - empty) - 0 = 1 (one odd component). Max matching = (3-1)/2 = 1.

# Relationships
## Builds Upon
- **Tutte's condition**, **odd component**

## Related
- **Tutte-Berge formula** — max matching = (|V| - d(G))/2
- **Gallai-Edmonds structure** — S maximizing d(T) gives the decomposition

# Source Reference
Chapter 2, Section 2.2, p. 52 (pdf p. 52).

# Verification Notes
- From the proof of Theorem 2.2.3
- Confidence: HIGH — explicitly used in the proof
