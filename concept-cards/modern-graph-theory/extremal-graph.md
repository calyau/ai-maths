---
concept: Extremal Graph
slug: extremal-graph
category: extremal-graph-theory
subcategory: basic-definitions
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Extremal Problems"
chapter_number: 4
pdf_page: 110
section: "IV Extremal Problems"
extraction_confidence: high
aliases:
  - "EX(n; F)"
prerequisites: []
extends: []
related:
  - extremal-function
  - forbidden-subgraph-problem
contrasts_with: []
answers_questions:
  - "What is an extremal graph?"
---

# Quick Definition
For a given graph parameter bound, an extremal graph is one achieving equality — the graph at the boundary of what is possible.

# Core Definition
If, for a given class of graphs, a certain graph parameter is at most some number $f$, then the graphs for which equality holds are the extremal graphs of the inequality. In the forbidden subgraph problem, a graph is extremal if it does not contain $F$ and has $ex(n; F)$ edges; the set of extremal graphs is $EX(n; F)$ (Bollobás, p. 110).

# Prerequisites
This is a foundational concept with no prerequisites within this source.

# Key Properties
1. Uniqueness is understood up to isomorphism
2. Extremal graphs saturate the bound
3. For the forbidden subgraph problem: $G \in EX(n;F)$ iff $G$ has $n$ vertices, $ex(n;F)$ edges, and $F \not\subset G$

# Construction / Recognition
1. Determine the extremal bound for the parameter
2. Find all graphs achieving this bound
3. These are the extremal graphs

# Context & Application
"Extremal problems are at the very heart of graph theory" (p. 110). The chapter focuses on the forbidden subgraph problem: given $F$, determine $ex(n;F)$ and $EX(n;F)$.

# Examples
**Example** (p. 110): An acyclic graph of order $n$ has at most $n-1$ edges; the extremal graphs are trees of order $n$.

**Example** (p. 110): A graph without odd cycles has at most $\lfloor n^2/4 \rfloor$ edges; the unique extremal graph is $K_{\lfloor n/2 \rfloor, \lceil n/2 \rceil}$.

# Relationships
## Enables
- **extremal-function** — The function $ex(n;F)$
- **forbidden-subgraph-problem** — The central problem

# Source Reference
Chapter IV, introductory section, pages 110-111.

# Verification Notes
- Definition source: Direct from p. 110
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
