---
# === CORE IDENTIFICATION ===
concept: Graph
slug: graph

# === CLASSIFICATION ===
category: combinatorial-group-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Trees and the Nielsen-Schreier Theorem"
chapter_number: 28
pdf_page: 180
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - directed graph
  - combinatorial graph

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
extends: []
related:
  - tree
  - group-action-on-a-graph
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a graph in the sense used for the Nielsen-Schreier theorem?"
---

# Quick Definition

A graph Gamma consists of a set A of directed edges and a set V of vertices, with a reversal function alpha -> alpha-bar and initial/terminal vertex functions i and t, satisfying alpha-bar-bar = alpha, alpha-bar is not alpha, and i(alpha-bar) = t(alpha).

# Core Definition

"A graph Gamma consists of two sets A (directed edges) and V (vertices) together with two functions A -> A, alpha -> alpha-bar and A -> V x V, alpha -> (i(alpha), t(alpha)) which satisfy alpha-bar-bar = alpha, alpha-bar is not alpha and i(alpha-bar) = t(alpha) for each alpha in A. The vertices i(alpha), t(alpha) are the initial and terminal vertices of the directed edge alpha, and alpha-bar is the reverse of alpha" (Armstrong, Ch. 28, p. 180).

# Prerequisites

- **Group** -- Graphs provide the setting for group actions in this chapter

# Key Properties

1. Each edge alpha has a reverse alpha-bar with alpha-bar-bar = alpha
2. alpha-bar is not alpha (no edge is its own reverse)
3. i(alpha-bar) = t(alpha) (reversal swaps initial and terminal vertices)
4. Each "physical" edge represents a pair of directed edges (alpha and alpha-bar)
5. Paths are ordered strings of edges alpha_1 alpha_2 ... alpha_n with i(alpha_{k+1}) = t(alpha_k)

# Construction / Recognition

## To Construct a Graph
1. Specify the vertex set V
2. Specify the edge set A as pairs of directed edges
3. Define the reversal: for each edge alpha, specify alpha-bar
4. Define i(alpha) and t(alpha) for each edge
5. Verify the three axioms hold

# Context & Application

Armstrong's definition of graph is designed for the theory of group actions on trees. The directed edges with explicit reversal allow clean statements about paths and geodesics. This is the framework used by Serre for proving the Nielsen-Schreier theorem via group actions on trees.

# Examples

**Example 1** (p. 180, Figure 28.1): Armstrong provides pictures using dots for vertices and arcs for edges, noting that simplified diagrams use single arcs to represent edge pairs.

**Example 2** (p. 182, Example (iv)): Given a group G and generating set X, the Cayley graph Gamma(G, X) has vertex set G and edges (g, z) where z or z^{-1} is in X.

# Relationships

## Enables
- **Tree** -- A tree is a graph satisfying additional conditions
- **Group action on a graph** -- Groups can act on graphs by permuting edges and vertices

# Common Errors

- **Error**: Forgetting that each "edge" in a simplified diagram represents two directed edges
  **Correction**: Always remember the pair alpha, alpha-bar when reasoning formally

# Common Confusions

- **Confusion**: Confusing this definition with the graph-theory definition where edges are unordered pairs
  **Clarification**: Armstrong uses directed edges with explicit reversal, which is more suited to group actions

# Source Reference

Chapter 28: Trees and the Nielsen-Schreier Theorem, pages 180-181 (pdf pp. 180-181). Definition at the start of the chapter.

# Verification Notes

- Definition: Directly quoted from Armstrong p. 180
- Confidence: HIGH -- explicit formal definition
- Cross-references: Verified against planned extractions
- Uncertainties: None
