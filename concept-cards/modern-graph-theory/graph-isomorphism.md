---
concept: Graph Isomorphism
slug: graph-isomorphism
category: graph-fundamentals
subcategory: basic-definitions
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Fundamentals"
chapter_number: 1
pdf_page: 9
section: "I.1 Definitions"
extraction_confidence: high
aliases:
  - isomorphic graphs
prerequisites:
  - graph
  - adjacency
extends: []
related:
  - graph-order-and-size
contrasts_with: []
answers_questions:
  - "When are two graphs isomorphic?"
---

# Quick Definition

Two graphs are isomorphic if there is a bijection between their vertex sets that preserves adjacency. Isomorphic graphs are considered structurally identical.

# Core Definition

"Two graphs are isomorphic if there is a correspondence between their vertex sets that preserves adjacency. Thus $G = (V, E)$ is isomorphic to $G' = (V', E')$ if there is a bijection $\phi: V \to V'$ such that $xy \in E$ iff $\phi(x)\phi(y) \in E'$" (Bollobás, p. 11). Isomorphic graphs have the same order and size. The notation $G \cong H$ or simply $G = H$ is used.

# Prerequisites

- **Graph** — Isomorphism is a relation between graphs
- **Adjacency** — The bijection must preserve adjacency

# Key Properties

1. Isomorphic graphs have the same order, size, and degree sequence
2. Isomorphism is an equivalence relation (reflexive, symmetric, transitive)
3. In practice, isomorphic graphs are not distinguished unless vertices are labelled
4. A bijection $\phi$ must satisfy: $xy \in E$ if and only if $\phi(x)\phi(y) \in E'$

# Construction / Recognition

## To verify isomorphism
1. Check that the two graphs have the same order and size
2. Find a bijection $\phi: V(G) \to V(H)$ preserving adjacency
3. Verify $xy \in E(G)$ iff $\phi(x)\phi(y) \in E(H)$ for all vertex pairs

# Context & Application

Graph isomorphism is the fundamental notion of structural equivalence in graph theory. Most graph properties are isomorphism-invariant, meaning they depend only on the abstract structure, not on vertex labels.

# Examples

**Example** (p. 11): Fig. I.3 shows all graphs up to isomorphism of order at most 4 and size 3.

# Relationships

## Builds Upon
- **Graph**, **Adjacency**

## Enables
- Classifying graphs up to structural equivalence
- Counting non-isomorphic graphs of given order and size

# Common Errors

- **Error**: Concluding two graphs are isomorphic because they have the same degree sequence
  **Correction**: Equal degree sequences are necessary but not sufficient for isomorphism

# Common Confusions

- **Confusion**: Thinking isomorphic graphs must have the same vertex labels
  **Clarification**: Isomorphism is about structural equivalence; the vertex labels may differ entirely

# Source Reference

Chapter I: Fundamentals, Section I.1 Definitions, page 11.

# Verification Notes

- Definition source: Direct from p. 11
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
