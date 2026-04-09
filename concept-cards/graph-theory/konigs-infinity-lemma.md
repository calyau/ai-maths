---
concept: "König's Infinity Lemma"
slug: konigs-infinity-lemma
category: infinite-graphs
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Infinite Graphs"
chapter_number: 8
pdf_page: 210
section: "8.1 Basic notions, facts and techniques"
extraction_confidence: high
aliases:
  - "infinity lemma"
  - "König's lemma"
prerequisites:
  - ray
  - infinite-graph
extends: []
related:
  - compactness-principle
  - locally-finite-graph
contrasts_with: []
answers_questions:
  - "What is König's infinity lemma?"
  - "How do compactness proofs work in infinite graph theory?"
---

# Quick Definition
König's infinity lemma states that if V_0, V_1, ... is an infinite sequence of disjoint non-empty finite sets, and every vertex in V_n (n >= 1) has a neighbour in V_{n-1}, then the graph contains a ray v_0v_1... with v_n in V_n for all n.

# Core Definition
**Lemma 8.1.2** (König's Infinity Lemma): Let V_0, V_1, ... be an infinite sequence of disjoint non-empty finite sets, and let G be a graph on their union. Assume that every vertex v in a set V_n with n >= 1 has a neighbour f(v) in V_{n-1}. Then G contains a ray v_0v_1... with v_n in V_n for all n (Diestel, p. 210).

# Prerequisites
- **Ray** — The lemma produces a ray
- **Infinite graph** — The setting is an infinite graph partitioned into finite layers

# Key Properties
1. The sets V_n must be finite (essential for the proof)
2. The neighbour relation goes "downward" from V_n to V_{n-1}
3. The proof uses a pigeonhole argument: since V_0 is finite but infinitely many paths end there, infinitely many agree on v_0, then v_1, etc.
4. This is the foundation of compactness proofs for countable graphs

# Construction / Recognition
## How the Proof Works
1. Infinitely many paths from higher levels end at the same vertex v_0 in V_0 (pigeonhole)
2. Of these, infinitely many agree on their penultimate vertex v_1 in V_1
3. Continue: at each step, infinitely many paths agree on v_n
4. The sequence v_0, v_1, ... is well-defined and forms a ray

# Context & Application
The infinity lemma is the tool that formalizes "compactness" proofs in countable graph theory. It is used to transfer theorems from finite to infinite graphs. The standard application: prove something for finite induced subgraphs, use the infinity lemma to pass to a limit.

# Examples
**Example 1** (p. 211): Used to prove Theorem 8.1.3 (de Bruijn-Erdős): if every finite subgraph of G is k-colourable, then so is G.

**Example 2** (p. 213): Used to prove the unfriendly partition conjecture for locally finite graphs.

# Relationships
## Enables
- **Compactness principle** — König's lemma formalizes compactness for countable graphs
- **De Bruijn-Erdős theorem** — Every graph whose finite subgraphs are k-colourable is k-colourable

## Related
- **Tychonoff's theorem** — The topological version of compactness used for arbitrary graphs

# Source Reference
Chapter 8, Section 8.1, page 210 (Lemma 8.1.2).

# Verification Notes
- Statement and proof directly from p. 210
- Confidence: HIGH — named lemma with full proof
