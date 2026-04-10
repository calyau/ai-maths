---
# === CORE IDENTIFICATION ===
concept: Automorphism Group of a Graph
slug: automorphism-group-graph

# === CLASSIFICATION ===
category: algebraic-graph-theory
subcategory: graph-symmetry
tier: intermediate

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Graphs, Groups and Matrices"
chapter_number: 8
pdf_page: 277
section: "VIII.3 Strongly Regular Graphs"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Aut(G)
  - graph automorphism group

# === TYPED RELATIONSHIPS ===
prerequisites:
  - adjacency-matrix
extends: []
related:
  - cayley-diagram
  - strongly-regular-graph
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the automorphism group of a graph?"
---

# Quick Definition

The automorphism group $\text{Aut}(G)$ is the group of permutations of $V(G)$ preserving adjacency. Every abstract finite group can be represented as $\text{Aut}(G)$ for some graph $G$.

# Core Definition

The automorphism group of a graph $G$ is $\text{Aut}(G)$, the group of permutations of vertices preserving adjacency. Each $\pi \in \text{Aut}(G)$ induces a permutation matrix $P$ that commutes with the adjacency matrix: $AQ = QA$. The eigenspaces of $A$ are invariant under $P$. Every abstract group is representable as $\text{Aut}(G)$ for some graph (Bollobas, p. 277).

# Prerequisites

- **Adjacency matrix** -- Automorphisms commute with $A$

# Key Properties

1. Each automorphism permutes eigenvectors within eigenspaces
2. If all eigenvalues are simple, $P^2 = I$ for every automorphism $P$
3. If all eigenvalues are simple and $|V| \ge 3$, $\text{Aut}(G)$ cannot be vertex-transitive
4. Every finite group is realizable as $\text{Aut}(G)$ (via Cayley diagram replacement)

# Construction / Recognition

## To Realize a Group as Aut(G)
1. Take the Cayley diagram of the group with some generators
2. Replace directed colored edges by suitable subgraphs encoding direction and color
3. The resulting graph has automorphism group isomorphic to the original group

# Context & Application

Graph automorphisms connect group theory to graph theory. Strongly regular graphs often have large automorphism groups, and sporadic simple groups are often related to strongly regular graphs.

# Examples

**Example 1** (p. 277, Fig. VIII.10): A graph with $\text{Aut}(G) \cong S_3$, constructed from the Cayley diagram.

**Example 2** (p. 283): A strongly regular graph with parameters (162, 105, 81) whose automorphism group contains the McLaughlin group.

# Relationships

## Builds Upon
- **Adjacency matrix** -- Automorphisms commute with $A$

## Enables
- Understanding of graph symmetry in spectral terms

## Related
- **Cayley diagram** -- Source for realizing groups
- **Strongly regular graph** -- Often have large automorphism groups

## Contrasts With
- None

# Common Errors

- **Error**: Assuming $\text{Aut}(G)$ is always trivial
  **Correction**: Many graphs (especially regular ones) have non-trivial automorphisms

# Common Confusions

- **Confusion**: Thinking the automorphism group determines the graph
  **Clarification**: Many non-isomorphic graphs can have the same (abstract) automorphism group

# Source Reference

Chapter VIII, Section VIII.3, pages 277--278.

# Verification Notes

- Definition source: Direct from p. 277
- Confidence rationale: Explicit discussion
- Uncertainties: None
- Cross-reference status: Verified
