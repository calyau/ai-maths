---
concept: Star-Comb Lemma
slug: star-comb-lemma
category: infinite-graphs
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Infinite Graphs"
chapter_number: 8
pdf_page: 214
section: "8.2 Paths, trees, and ends"
extraction_confidence: high
aliases: []
prerequisites:
  - comb
  - ray
  - infinite-graph
extends: []
related:
  - end-of-a-graph
  - normal-spanning-tree
contrasts_with: []
answers_questions:
  - "What is the star-comb lemma?"
---

# Quick Definition
The star-comb lemma states that for any infinite set U of vertices in a connected graph G, either G contains a comb with all teeth in U, or G contains a subdivision of an infinite star with all leaves in U.

# Core Definition
**Lemma 8.2.2** (Star-Comb Lemma): Let U be an infinite set of vertices in a connected graph G. Then G contains either a comb with all teeth in U or a subdivision of an infinite star with all leaves in U (Diestel, p. 214).

# Prerequisites
- **Comb** — One of the two alternatives in the lemma
- **Ray** — The spine of a comb is a ray
- **Infinite graph** — The lemma applies to connected graphs with infinite vertex sets

# Key Properties
1. In locally finite graphs, the lemma always yields a comb (never a star)
2. A subdivided infinite star witnesses a vertex of infinite degree "close to" U
3. A comb witnesses that U converges to an end of G
4. The proof uses Zorn's lemma and Proposition 8.2.1

# Context & Application
The star-comb lemma is one of the most frequently used tools in infinite graph theory. It allows finding detailed structural information about how an infinite set of vertices is distributed in a graph. It is applied repeatedly in the study of ends, normal spanning trees, and topological properties of infinite graphs.

# Examples
**Example 1** (p. 214): Applied in a locally finite graph, the lemma gives a comb, which is used to prove that normal rays reflect the end structure (Lemma 8.2.3).

# Relationships
## Builds Upon
- **Comb** — One alternative
- **Infinite star subdivision** — The other alternative

## Enables
- **Lemma 8.2.3** — Every end contains exactly one normal ray of a normal spanning tree
- **Topological end space** results

# Source Reference
Chapter 8, Section 8.2, page 214 (Lemma 8.2.2).

# Verification Notes
- Statement directly from p. 214
- Confidence: HIGH — named lemma with full proof in source
