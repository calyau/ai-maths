---
concept: Infinite Graph
slug: infinite-graph
category: infinite-graphs
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Infinite Graphs"
chapter_number: 8
pdf_page: 206
section: "8.1 Basic notions, facts and techniques"
extraction_confidence: high
aliases:
  - "infinite graph"
prerequisites:
  - graph
  - vertex
  - edge
extends:
  - graph
related:
  - locally-finite-graph
  - ray
  - end-of-a-graph
  - transfinite-induction
  - zorns-lemma
contrasts_with: []
answers_questions:
  - "What is an infinite graph?"
  - "What must I know before studying infinite graphs?"
---

# Quick Definition
An infinite graph is a graph whose vertex set is infinite. The terminology is exactly the same as for finite graphs, except for aspects unique to infinity such as the eventual behaviour of infinite paths captured by the notion of ends.

# Core Definition
A graph G = (V, E) is infinite if V is infinite. Graphs are finite, infinite, countable, etc., according to the cardinality of their vertex set. The chapter focuses primarily on countable infinite graphs, where set-theoretic issues do not arise. The study of infinite graphs highlights phenomena that always appear when graphs are infinite, particularly when they are "only just" infinite with countably many vertices and perhaps only finitely many edges at each vertex (Diestel, Ch. 8, p. 206).

# Prerequisites
- **Graph** — An infinite graph is a graph with an infinite vertex set
- **Vertex** and **Edge** — The basic components that compose the graph
- **Transfinite induction** and **Zorn's lemma** — Key proof techniques specific to infinite combinatorics

# Key Properties
1. An infinite graph may be countable or uncountable
2. Problems that become interesting only for uncountable graphs tend to belong to combinatorial set theory rather than graph theory
3. Many basic structural features of graphs (paths) are intrinsically countable
4. The three most basic proof techniques specific to infinite graph theory are Zorn's lemma, transfinite induction, and compactness
5. The notion of an end captures the eventual behaviour of infinite paths, having no finite counterpart

# Construction / Recognition
## To Recognize an Infinite Graph
1. Check whether the vertex set V is infinite
2. The edge set may be finite or infinite regardless

# Context & Application
Infinite graph theory extends finite graph theory but introduces genuinely new phenomena. The most fundamental such phenomenon is the notion of ends, which captures convergence of infinite paths to "points at infinity." The chapter alternates between easier sections (8.1, 8.3, 8.5) and more substantial ones (8.2, 8.4).

# Examples
**Example 1** (p. 206): A ray and a double ray are the simplest infinite graphs.

**Example 2** (p. 206): An infinitely connected graph (k-connected for every k) contains a subdivision of the complete graph on countably many vertices.

# Relationships
## Builds Upon
- **Graph** — An infinite graph is the infinite version of a graph

## Enables
- **Ray**, **double ray**, **end-of-a-graph** — Concepts unique to infinite graphs
- **Compactness principle** — A proof technique for transferring finite results to infinite graphs
- **Normal spanning tree** — A structural tool central to infinite graph theory

## Related
- **Locally finite graph** — An infinite graph where all vertices have finite degree
- **Transfinite induction** — A key proof technique

# Common Errors
- **Error**: Assuming infinite intersection of a nested sequence of uncountable sets must be uncountable
  **Correction**: The intersection may be empty

- **Error**: Assuming a maximal set of disjoint rays can be found greedily
  **Correction**: A badly chosen ray can meet infinitely many others; careful simultaneous construction is needed

# Common Confusions
- **Confusion**: Believing that results for finite graphs automatically extend to infinite graphs
  **Clarification**: Some do (via compactness), but many require substantial new ideas or even fail

- **Confusion**: Thinking the most interesting infinite graphs are uncountable
  **Clarification**: Most fundamental phenomena already occur for countable graphs

# Source Reference
Chapter 8: Infinite Graphs, Section 8.1, pages 206-215 (pdf pp. 206-215). See also the appendix for set-theoretic prerequisites.

# Verification Notes
- Definition synthesized from introductory discussion on p. 206
- Key properties extracted from pp. 206-210
- Confidence: HIGH — chapter introduction explicitly describes the scope and nature of infinite graphs
