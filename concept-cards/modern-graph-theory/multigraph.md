---
concept: Multigraph
slug: multigraph
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
  - multi-graph
prerequisites:
  - graph
extends:
  - graph
related:
  - directed-graph
  - hypergraph
contrasts_with:
  - graph
answers_questions:
  - "What is a multigraph?"
---

# Quick Definition

A multigraph allows both multiple edges (several edges joining the same pair of vertices) and loops (edges joining a vertex to itself), unlike a simple graph which forbids both.

# Core Definition

"By definition a graph does not contain a loop, an 'edge' joining a vertex to itself; neither does it contain multiple edges, that is, several 'edges' joining the same two vertices. In a multigraph both multiple edges and multiple loops are allowed; a loop is a special edge" (Bollobás, p. 15). A loop contributes 2 to the degree of its vertex.

# Prerequisites

- **Graph** — A multigraph generalizes a graph

# Key Properties

1. Multiple edges between the same pair of vertices are allowed
2. Loops (edges from a vertex to itself) are allowed
3. A loop contributes 2 to the degree of its vertex
4. Theorem 1 (cycle partition) is valid for multigraphs
5. Euler's theorem (Theorem 12) applies naturally to multigraphs

# Construction / Recognition

A multigraph is recognized by the presence of loops or multiple edges. If neither is present, it is a simple graph.

# Context & Application

Multigraphs arise naturally in many contexts: the Königsberg bridge problem uses a multigraph (Fig. I.15), and electrical networks are best modelled as multigraphs. Bollobás notes: "sometimes multigraphs are the natural context for our results, and it is artificial to restrict ourselves to (simple) graphs."

# Examples

**Example** (p. 25-26): The Königsberg bridges form a multigraph with 4 vertices, some joined by multiple edges.

# Relationships

## Builds Upon
- **Graph** — A multigraph generalizes a graph

## Enables
- **Euler circuit** — Euler's theorem applies to multigraphs
- **Electrical network** — Naturally modelled as multigraphs

## Contrasts With
- **Graph** — A simple graph forbids loops and multiple edges

# Common Errors

- **Error**: Forgetting that a loop contributes 2 to the degree
  **Correction**: A loop at vertex $v$ contributes 2 to $d(v)$, maintaining the handshaking lemma

# Common Confusions

- **Confusion**: Thinking "graph" and "multigraph" are synonymous
  **Clarification**: In Bollobás's usage, "graph" means simple graph by default

# Source Reference

Chapter I: Fundamentals, Section I.1 Definitions, pages 15-16.

# Verification Notes

- Definition source: Direct from pp. 15-16
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
