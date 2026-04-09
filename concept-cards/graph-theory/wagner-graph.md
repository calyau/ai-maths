---
concept: Wagner Graph
slug: wagner-graph
category: extremal-graph-theory
subcategory: minors
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Extremal Graph Theory"
chapter_number: 7
pdf_page: 184
section: "7.3 Hadwiger's conjecture"
extraction_confidence: high
aliases:
  - "W"
  - "Mobius-Kantor graph"
prerequisites:
  - graph
related:
  - wagner-theorem
  - hadwiger-conjecture
answers_questions:
  - "What is the Wagner graph?"
---

# Quick Definition
The Wagner graph W is the unique graph that, together with plane triangulations, forms the building blocks for edge-maximal graphs without K^5 minor. It has chi(W) = 3.

# Core Definition
The **Wagner graph** W is a specific graph on 8 vertices that appears as an irreducible building block in Wagner's structure theorem (Theorem 7.3.4) for K^5-minor-free graphs. It has chromatic number chi(W) = 3. Three representations are shown in Fig. 7.3.1. (Diestel, p. 175)

# Prerequisites
- **Graph** — W is a specific graph

# Key Properties
1. One of two building block types for K^5-minor-free graphs (the other being plane triangulations)
2. chi(W) = 3 (which helps prove Hadwiger for r = 5 using 4CT)
3. Not planar (contains K^5-minor-free structure that is non-planar)

# Examples
**Example** (p. 175, Fig. 7.3.1): Three representations of the Wagner graph W.

# Source Reference
Chapter 7, Section 7.3, page 175 (pdf page 184). Fig. 7.3.1.

# Verification Notes
- Confidence: HIGH — named graph with figure
