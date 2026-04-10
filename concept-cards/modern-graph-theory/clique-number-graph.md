---
concept: Clique Number
slug: clique-number-graph
category: extremal-graph-theory
subcategory: graph-parameters
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Extremal Problems"
chapter_number: 4
pdf_page: 110
section: "IV.2 Complete Subgraphs"
extraction_confidence: high
aliases:
  - "ω(G)"
  - "omega(G)"
prerequisites:
  - extremal-function
extends: []
related:
  - turans-theorem
contrasts_with: []
answers_questions:
  - "What is the clique number of a graph?"
---

# Quick Definition
The clique number $\omega(G)$ is the maximum order of a complete subgraph of $G$.

# Core Definition
A maximal complete subgraph of a graph is a clique, and the clique number $\omega(G)$ of a graph $G$ is the maximal order of a clique in $G$. Turán's theorem states that if $m \ge t_{r-1}(n)$ then $\omega(G) \ge r$ (Bollobás, p. 121).

# Prerequisites
- **Extremal function** — Clique number relates to extremal bounds

# Key Properties
1. $\omega(G) \ge r$ if $e(G) > t_{r-1}(n)$ (Turán's theorem)
2. $\omega(G) = 1$ iff $G$ has no edges
3. Determines the forbidden subgraph structure

# Construction / Recognition
1. Find the largest complete subgraph
2. Its order is $\omega(G)$

# Context & Application
Turán's theorem gives a lower bound on $\omega(G)$ from edge count.

# Examples
**Example** (p. 121): If $G$ has $n$ vertices and $m \ge t_{r-1}(n)$ edges, then $\omega(G) \ge r$.

# Relationships
## Related
- **turans-theorem** — Lower bounds on clique number

# Source Reference
Chapter IV, Section IV.2, page 121.

# Verification Notes
- Definition source: Direct from p. 121
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
