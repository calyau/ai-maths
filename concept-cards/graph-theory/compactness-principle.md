---
concept: Compactness Principle
slug: compactness-principle
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
  - "compactness"
  - "compactness argument"
prerequisites:
  - konigs-infinity-lemma
  - infinite-graph
extends: []
related:
  - locally-finite-graph
contrasts_with: []
answers_questions:
  - "What is the compactness principle in graph theory?"
  - "How do I transfer finite graph theorems to infinite graphs?"
---

# Quick Definition
The compactness principle is a proof technique for infinite graphs that transfers results from finite to infinite settings, typically by applying König's infinity lemma to compatible choices on nested finite subgraphs.

# Core Definition
Compactness proofs offer a formalized way to make correct choices in certain standard cases where a wrong choice may lead to a dead end after finitely many steps. For countable graphs, compactness proofs are formalized by König's infinity lemma (8.1.2). For arbitrary graphs, one appeals directly to Tychonoff's theorem (Diestel, p. 210).

# Prerequisites
- **König's infinity lemma** — Formalizes compactness for countable graphs
- **Infinite graph** — The setting for compactness arguments

# Key Properties
1. Used to transfer theorems from finite to infinite graphs
2. For countable graphs: use König's infinity lemma
3. For uncountable graphs: use Tychonoff's theorem (topological compactness)
4. Requires compatible choices: each finite choice must be extendable

# Construction / Recognition
## Standard Compactness Proof Pattern
1. Enumerate finite induced subgraphs G_0, G_1, ... covering G
2. For each G_n, find all valid choices (e.g., k-colourings) forming a set V_n
3. Define adjacency: a choice in V_n is adjacent to its restriction in V_{n-1}
4. Apply König's infinity lemma to get a compatible infinite sequence
5. The limit of this sequence is the desired object for all of G

# Context & Application
The compactness principle is one of the three basic proof techniques specific to infinite combinatorics (along with Zorn's lemma and transfinite induction). Its standard use is to transfer theorems from finite to infinite graphs.

# Examples
**Example 1** (p. 211): Theorem 8.1.3 (de Bruijn-Erdős, 1951): if every finite subgraph of G is k-colourable, then G is k-colourable. Proved by compactness.

# Relationships
## Builds Upon
- **König's infinity lemma** — The countable case

## Enables
- Transfer of finite chromatic number results to infinite graphs
- Unfriendly partition conjecture for locally finite graphs

# Source Reference
Chapter 8, Section 8.1, pages 210-213.

# Verification Notes
- Synthesized from discussion on pp. 210-213
- Confidence: HIGH — technique explicitly described and illustrated
