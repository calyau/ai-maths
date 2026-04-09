---
concept: Pseudo-Random Graph
slug: pseudo-random-graph
category: extremal-graph-theory
subcategory: regularity
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Extremal Graph Theory"
chapter_number: 7
pdf_page: 186
section: "7.4 Szemeredi's regularity lemma"
extraction_confidence: medium
aliases:
  - "quasi-random graph"
prerequisites:
  - epsilon-regular-pair
related:
  - regularity-lemma
  - embedding-lemma
answers_questions:
  - "What is a pseudo-random graph?"
---

# Quick Definition
Concrete graphs whose structure resembles that expected of a random graph are called pseudo-random. The bipartite graphs spanned by an epsilon-regular pair are pseudo-random.

# Core Definition
**Pseudo-random graphs** are concrete graphs whose structure resembles the structure expected of a random graph. For example, the bipartite graphs spanned by an epsilon-regular pair of vertex sets in a graph are pseudo-random: their edges are distributed uniformly (up to epsilon deviations) between subsets. (Diestel, p. 272, footnote 4, and p. 184)

# Prerequisites
- **Epsilon-regular pair** — Regular pairs exhibit pseudo-random behaviour

# Key Properties
1. Edge distribution is approximately uniform
2. Epsilon-regular pairs are the primary example in this context
3. The regularity lemma approximates any graph by a collection of pseudo-random bipartite graphs
4. Pseudo-random graphs contain any given bounded-degree subgraph (embedding lemma)

# Context & Application
The connection between regularity and pseudo-randomness is a major theme in modern combinatorics. The regularity lemma provides pseudo-random approximations, and the embedding lemma exploits pseudo-randomness to find subgraphs.

# Source Reference
Chapter 7, Section 7.4, page 176 (pdf page 186). Chapter 9 notes, page 272.

# Verification Notes
- Confidence: MEDIUM — described conceptually but not formally defined in the main text
