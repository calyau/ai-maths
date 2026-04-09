---
concept: k-Connected
slug: k-connected

category: connectivity
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 20
section: "1.4 Connectivity"

extraction_confidence: high

aliases:
  - "k-connectivity"
  - "vertex connectivity"
  - "connectivity kappa(G)"

prerequisites:
  - graph
  - connected-graph
  - separator
extends:
  - connected-graph
related:
  - edge-connectivity
  - separation
contrasts_with:
  - edge-connectivity

answers_questions:
  - "What is a k-connected graph?"
  - "What is the connectivity kappa(G)?"
  - "What distinguishes vertex connectivity from edge connectivity?"
---

# Quick Definition
A graph G is k-connected if |G| > k and G - X remains connected for every set X of fewer than k vertices. The connectivity kappa(G) is the greatest k for which G is k-connected.

# Core Definition
G is called k-connected (for k in N) if |G| > k and G - X is connected for every set X of vertices with |X| < k. In other words, no two vertices of G are separated by fewer than k other vertices. Every (non-empty) graph is 0-connected, and the 1-connected graphs are precisely the non-trivial connected graphs. The greatest integer k such that G is k-connected is the connectivity kappa(G) of G. Thus, kappa(G) = 0 if and only if G is disconnected or a K^1, and kappa(K^n) = n - 1 for all n >= 1 (Diestel, p. 11).

# Prerequisites
- **Graph**, **connected-graph** — k-connectivity strengthens connectivity
- **Separator** — k-connectivity means no separator of size < k

# Key Properties
1. Every graph is 0-connected
2. 1-connected = non-trivially connected
3. kappa(G) <= lambda(G) <= delta(G) (Proposition 1.4.2)
4. kappa(K^n) = n - 1
5. kappa(G) = 0 iff G is disconnected or K^1

# Construction / Recognition
G is k-connected if and only if |G| > k and no set of fewer than k vertices separates G.

# Context & Application
Connectivity measures the robustness of a graph. Menger's theorem (Chapter 3) characterizes k-connectivity in terms of independent paths. Mader's theorem (1.4.3) shows that large average degree forces a highly connected subgraph.

# Relationships
## Builds Upon
- **connected-graph**, **separator**

## Contrasts With
- **edge-connectivity** — removes edges instead of vertices

# Common Confusions
- **Confusion**: Confusing vertex connectivity (kappa) with edge connectivity (lambda)
  **Clarification**: kappa counts vertex removals; lambda counts edge removals. kappa(G) <= lambda(G) always holds.

# Source Reference
Chapter 1: The Basics, Section 1.4, page 11 (pdf p. 21). Proposition 1.4.2.

# Verification Notes
- Direct from p. 11
- Confidence: HIGH
