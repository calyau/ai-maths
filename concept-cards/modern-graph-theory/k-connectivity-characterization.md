---
concept: k-Connectivity Characterization via Independent Paths
slug: k-connectivity-characterization
category: connectivity
subcategory: fundamental-results
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.2 Connectivity and Menger's Theorem"
extraction_confidence: high
aliases:
  - "Corollary 6"
prerequisites:
  - mengers-theorem
  - k-connected-graph
  - k-edge-connected-graph
extends:
  - mengers-theorem
related:
  - vertex-connectivity
  - edge-connectivity
contrasts_with: []
answers_questions:
  - "What is graph connectivity?"
  - "How does vertex connectivity relate to edge connectivity?"
---

# Quick Definition
A graph is $k$-connected iff it has at least two vertices and any two vertices can be joined by $k$ independent paths. Similarly for $k$-edge-connected with edge-disjoint paths.

# Core Definition
**Corollary 6**: For $k \ge 2$, a graph is $k$-connected iff it has at least two vertices and any two vertices can be joined by $k$ independent paths. Also, for $k \ge 2$, a graph is $k$-edge-connected iff it has at least two vertices and any two vertices can be joined by $k$ edge-disjoint paths (Bollobás, p. 84).

# Prerequisites
- **Menger's theorem** — This corollary follows directly
- **k-connected graph** — The property being characterized
- **k-edge-connected graph** — The edge version

# Key Properties
1. Provides an equivalent definition of $k$-connectivity in terms of paths
2. Works for both vertex and edge connectivity
3. The "any two vertices" condition is global, unlike Menger's local result

# Construction / Recognition
To verify $k$-connectivity:
1. Check $|V| \ge 2$
2. For every pair of vertices, verify existence of $k$ independent paths
3. Menger's theorem reduces this to checking minimum separators

# Context & Application
This corollary reformulates connectivity as a path-existence property, which is often more useful in applications than the separation-based definition.

# Examples
**Example**: $K_n$ is $(n-1)$-connected because any two vertices can be joined by $n-1$ independent paths (one through each remaining vertex).

# Relationships
## Builds Upon
- **mengers-theorem** — Direct corollary

## Enables
- Structural results about highly connected graphs

# Common Errors
- **Error**: Requiring exactly $k$ independent paths rather than at least $k$
  **Correction**: The characterization requires at least $k$ independent paths for every pair

# Common Confusions
- **Confusion**: Thinking this only applies for specific pairs of vertices
  **Clarification**: The condition must hold for *every* pair of vertices

# Source Reference
Chapter III, Section III.2, page 84. Corollary 6.

# Verification Notes
- Definition source: Direct from p. 84
- Confidence rationale: Explicitly stated corollary
- Uncertainties: None
- Cross-reference status: Verified
