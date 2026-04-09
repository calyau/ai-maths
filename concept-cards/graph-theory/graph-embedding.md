---
concept: Graph Embedding
slug: graph-embedding

category: graph-fundamentals
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 30
section: "1.7 Contraction and minors"

extraction_confidence: high

aliases:
  - "embedding"

prerequisites:
  - graph
  - subgraph
  - induced-subgraph
  - minor
  - topological-minor
extends: []
related: []
contrasts_with: []

answers_questions:
  - "What is a graph embedding?"
---

# Quick Definition
An embedding of G in H is an injective map from V(G) to V(H) that preserves the desired structure: adjacency (subgraph embedding), adjacency and non-adjacency (induced subgraph), paths (topological minor), or connected sets (minor).

# Core Definition
An embedding of G in H is an injective map phi: V(G) -> V(H) that preserves the kind of structure we are interested in. phi embeds G in H 'as a subgraph' if it preserves adjacency, 'as an induced subgraph' if it preserves both adjacency and non-adjacency. If phi maps edges to independent paths, it embeds G 'as a topological minor'. An embedding 'as a minor' maps vertices to disjoint connected vertex sets (Diestel, p. 21).

# Prerequisites
- **Graph**, **subgraph**, **induced-subgraph**, **minor**, **topological-minor**

# Key Properties
1. Subgraph embedding: preserves adjacency
2. Induced subgraph embedding: preserves adjacency and non-adjacency
3. Topological minor embedding: maps edges to independent paths
4. Minor embedding: maps vertices to disjoint connected sets

# Context & Application
Embeddings unify the various containment relations under a common framework.

# Relationships
## Builds Upon
- **graph**, **subgraph**, **induced-subgraph**, **minor**, **topological-minor**

# Source Reference
Chapter 1: The Basics, Section 1.7, page 21 (pdf p. 31).

# Verification Notes
- Direct from p. 21
- Confidence: HIGH
