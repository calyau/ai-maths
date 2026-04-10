---
concept: Graph Density
slug: graph-density
category: extremal-graph-theory
subcategory: graph-parameters
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Extremal Problems"
chapter_number: 4
pdf_page: 110
section: "IV.4 The Structure of Graphs"
extraction_confidence: high
aliases:
  - "density"
  - "upper density"
prerequisites: []
extends: []
related:
  - erdos-stone-theorem
contrasts_with: []
answers_questions:
  - "What is the density of a graph?"
---

# Quick Definition
The density of a graph $G$ of order $n$ is $e(G)/\binom{n}{2}$. The upper density of an infinite graph is the supremum of densities of its large finite subgraphs.

# Core Definition
The density of a graph $G$ of order $n$ is defined to be $e(G)/\binom{n}{2}$. The upper density of an infinite graph $G$ is the supremum of the densities of arbitrarily large finite subgraphs of $G$ (Bollobás, p. 138).

# Prerequisites
This is a foundational concept with no prerequisites within this source.

# Key Properties
1. Density is between 0 and 1
2. $K_n$ has density 1
3. The upper density of an infinite graph takes values $0, 1/2, 2/3, 3/4, \ldots, 1$ (Corollary 25)
4. Not every value in $[0,1]$ is an upper density

# Context & Application
Corollary 25 (from Erdős-Stone): the upper density function takes only values $1-1/r$ for $r = 1,2,\ldots$ or $0$.

# Examples
**Example** (p. 138): The complete $r$-partite graph with infinite classes has upper density $1-1/r$.

# Relationships
## Related
- **erdos-stone-theorem** — Determines possible upper densities

# Source Reference
Chapter IV, Section IV.4, page 138. Corollary 25.

# Verification Notes
- Definition source: Direct from p. 138
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
