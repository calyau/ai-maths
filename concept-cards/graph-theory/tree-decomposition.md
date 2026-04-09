---
concept: Tree-Decomposition
slug: tree-decomposition
category: graph-minors
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Minors, Trees and WQO"
chapter_number: 12
pdf_page: 329
section: "12.3 Tree-decompositions"
extraction_confidence: high
aliases:
  - "tree decomposition"
prerequisites:
  - graph
extends: []
related:
  - tree-width
  - bramble
  - path-decomposition
  - lean-tree-decomposition
contrasts_with:
  - path-decomposition
answers_questions:
  - "What is a tree-decomposition?"
  - "How do I construct a tree-decomposition?"
  - "What distinguishes a tree-decomposition from a path-decomposition?"
---

# Quick Definition
A tree-decomposition of a graph G is a pair (T, V) where T is a tree and V = (V_t)_{t in T} is a family of vertex sets (parts/bags) indexed by T, such that: (T1) every vertex of G is in some V_t, (T2) every edge has both ends in some V_t, and (T3) for t1, t2, t3 with t2 on the t1-t3 path in T, V_{t1} cap V_{t3} is a subset of V_{t2}.

# Core Definition
Let G be a graph, T a tree, and V = (V_t)_{t in T} a family of vertex sets V_t subset V(G) indexed by T. The pair (T, V) is a *tree-decomposition* of G if:
- (T1) V(G) = union of V_t over t in T
- (T2) for every edge e of G, there exists t in T such that both ends of e lie in V_t
- (T3) V_{t1} cap V_{t3} subset V_{t2} whenever t2 lies on the t1-t3 path in T
The subgraphs G[V_t] and sets V_t are the *parts* (or *bags*) of the decomposition (Diestel, pp. 329-330).

# Prerequisites
- **Graph** — Tree-decompositions apply to graphs

# Key Properties
1. The most important feature: separation properties transfer from T to G (Lemma 12.3.1)
2. V_{t1} cap V_{t2} separates the parts of G corresponding to the two components of T - t1t2
3. Passed on to subgraphs (Lemma 12.3.2) and contractions (Lemma 12.3.3)
4. Any complete subgraph is contained in some part (Lemma 12.3.5)
5. Condition (T3) equivalently: for every vertex v, the set {t | v in V_t} induces a subtree of T

# Construction / Recognition
## To Construct a Tree-Decomposition
1. Find natural separators in G (e.g., clique separators)
2. Build T by organizing the pieces separated by these separators
3. Each part V_t should contain the separator vertices and the vertices of one piece
4. Verify (T1), (T2), (T3)

## Alternative Construction
1. Find an enumeration t_1, ..., t_n of parts satisfying: for each k >= 2, there is j < k with V_{t_k} cap (union_{i<k} V_{t_i}) subset V_{t_j}
2. Connect each t_k to such a t_j to form T

# Context & Application
Tree-decompositions capture how "tree-like" a graph is. They permit generalizations of tree properties (like Kruskal's theorem) and play a crucial role in the proof of the graph minor theorem. They are also fundamental in algorithmic graph theory.

# Examples
**Example 1** (p. 329, Fig. 12.3.1): Visual illustration of parts and the edges/parts ruled out by (T2) and (T3).

**Example 2** (p. 330, Fig. 12.3.2): How V_{t1} cap V_{t2} separates the graph.

# Relationships
## Enables
- **Tree-width** — The minimum width of any tree-decomposition
- **Bramble** — Dual obstruction to small tree-width
- **Graph minor theorem** — Uses tree-decompositions extensively

## Contrasts With
- **Path-decomposition** — A tree-decomposition whose tree is a path

# Common Errors
- **Error**: Forgetting condition (T3) — the "subtree property"
  **Correction**: For every vertex v, the nodes t with v in V_t must form a connected subtree of T

# Common Confusions
- **Confusion**: Thinking parts must be disjoint
  **Clarification**: Parts typically overlap; the overlaps are exactly the separators

# Source Reference
Chapter 12, Section 12.3, pages 329-336.

# Verification Notes
- Definition from pp. 329-330
- Properties from Lemmas 12.3.1-12.3.5
- Confidence: HIGH — central concept with explicit formal definition
