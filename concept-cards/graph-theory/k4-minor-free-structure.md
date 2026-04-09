---
concept: "K^4-Minor-Free Graph Structure"
slug: k4-minor-free-structure
category: extremal-graph-theory
subcategory: minors
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Extremal Graph Theory"
chapter_number: 7
pdf_page: 183
section: "7.3 Hadwiger's conjecture"
extraction_confidence: high
aliases:
  - "Proposition 7.3.1"
prerequisites:
  - hadwiger-conjecture
related:
  - hadwiger-conjecture-small-r
  - wagner-theorem
answers_questions:
  - "What do graphs without a K^4 minor look like?"
---

# Quick Definition
A graph with at least 3 vertices is edge-maximal without a K^4 minor iff it can be constructed recursively from triangles by pasting along K^2s. All such graphs have exactly 2|G|-3 edges.

# Core Definition
**Proposition 7.3.1**: A graph with at least three vertices is edge-maximal without a K^4 minor if and only if it can be constructed recursively from triangles by pasting along K^2s.

**Corollary 7.3.2**: Every edge-maximal graph G without a K^4 minor has 2|G| - 3 edges.

**Corollary 7.3.3**: Hadwiger's conjecture holds for r = 4. (Since pasting along complete graphs preserves the maximum chromatic number, all K^4-minor-free graphs are 3-colourable.) (Diestel, pp. 173-174)

# Prerequisites
- **Hadwiger's conjecture** — This provides the r = 4 case

# Key Properties
1. Simple recursive construction from triangles
2. Every edge-maximal K^4-minor-free graph has exactly 2n-3 edges (all are "extremal")
3. These graphs are always 3-colourable
4. Uses the equivalence of MK^4 and TK^4 (since Delta(K^4) = 3)

# Relationships
## Enables
- Hadwiger's conjecture for r = 4

# Source Reference
Chapter 7, Section 7.3, Proposition 7.3.1, pages 173-174 (pdf pages 183-184).

# Verification Notes
- Confidence: HIGH — proposition with proof
