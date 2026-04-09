---
concept: "Tutte's Condition"
slug: tuttes-condition
category: matching-and-covering
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Matching, Covering and Packing"
chapter_number: 2
pdf_page: 49
section: "2.2 Matching in general graphs"
extraction_confidence: high
aliases:
  - "Tutte condition"
  - "1-factor condition"
prerequisites:
  - odd-component
extends: []
related:
  - tuttes-theorem
  - marriage-condition
contrasts_with:
  - marriage-condition
answers_questions:
  - "What is Tutte's condition for a 1-factor?"
---

# Quick Definition
Tutte's condition states that q(G-S) <= |S| for all S contained in V(G), where q counts odd components. It is necessary and sufficient for a graph to have a 1-factor.

# Core Definition
If G has a 1-factor, then q(G-S) <= |S| for all S contained in V(G), since every odd component of G-S will send a factor edge to S. This inequality is called **Tutte's condition** (Diestel, p. 49).

# Prerequisites
- **Odd component** — q(G-S) counts odd components of G-S

# Key Properties
1. Necessary for a 1-factor (each odd component sends >= 1 edge to S)
2. Also sufficient (Tutte's theorem, 1947)
3. Involves checking all subsets S of V(G)
4. Generalizes the marriage condition to non-bipartite graphs
5. For S = empty set, requires q(G) = 0 (even number of vertices in each component, or equivalently, even order of G)

# Construction / Recognition
## To Verify Tutte's Condition
1. For every subset S of V(G)
2. Compute G-S (remove vertices in S and their incident edges)
3. Count q(G-S), the number of odd components
4. Verify q(G-S) <= |S|

# Context & Application
Tutte's condition is the non-bipartite analogue of the marriage condition. While the marriage condition characterizes matchings of A in bipartite graphs, Tutte's condition characterizes the existence of 1-factors in arbitrary graphs.

# Examples
**Example** (p. 50, Fig. 2.2.1): With q = 3 odd components and |S| = 3, Tutte's condition holds as 3 <= 3.

# Relationships
## Builds Upon
- **Odd component** — the condition counts odd components

## Enables
- **Tutte's theorem** — Tutte's condition is necessary and sufficient for a 1-factor

## Contrasts With
- **Marriage condition** — the bipartite analogue: |N(S)| >= |S| for all S in A

# Common Errors
- **Error**: Checking only S = V(G) or S = empty set
  **Correction**: Tutte's condition must hold for every subset S

# Common Confusions
- **Confusion**: Thinking Tutte's condition is only necessary
  **Clarification**: It is both necessary and sufficient (Tutte's theorem)

# Source Reference
Chapter 2, Section 2.2, p. 49 (pdf p. 49).

# Verification Notes
- Definition from p. 49
- Confidence: HIGH — explicitly defined and named
