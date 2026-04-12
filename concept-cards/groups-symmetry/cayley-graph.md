---
# === CORE IDENTIFICATION ===
concept: Cayley Graph
slug: cayley-graph

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
  - "Gamma(G, X)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - graph
  - group
extends:
  - graph
related:
  - group-action-on-a-graph
  - free-group
  - tree
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Cayley graph of a group?"
  - "When is a Cayley graph a tree?"
---

# Quick Definition

The Cayley graph Gamma(G, X) of a group G with generating set X has vertices G and directed edges (g, z) for each g in G and generator z in X (or z^{-1} in X). G acts freely on its Cayley graph by left multiplication.

# Core Definition

"Given a group G and a set X of generators for G we can construct a graph Gamma(G, X) as follows. ... Let A be the collection of all ordered pairs (g, z) where g comes from G and either z or z^{-1} belongs to X. Take V = G and define (g,z)-bar = (gz, z^{-1}), i((g,z)) = g, t((g,z)) = gz" (Armstrong, Ch. 28, p. 182). G acts freely on Gamma(G, X) by left multiplication: g'((g, z)) = (g'g, z).

# Prerequisites

- **Graph** -- The Cayley graph is a graph
- **Group** -- G and its generating set X

# Key Properties

1. Vertices are the elements of G
2. Edges connect g to gz for each generator z in X
3. G acts freely on Gamma(G, X) by left translation
4. Any two vertices can be joined by a path (the graph is connected)
5. If X is a free set of generators, Gamma(G, X) is a tree (Theorem 28.1)
6. For a finite cyclic group of order n with one generator, Gamma(G, X) is an n-gon

# Construction / Recognition

## To Build Gamma(G, X)
1. Set V = G (one vertex per group element)
2. For each g in G and each z in X (assuming z^2 is not e): create edge (g, z) from g to gz
3. Define reversal: (g, z)-bar = (gz, z^{-1})
4. G acts by left multiplication: g'(g, z) = (g'g, z)

## When Gamma(G, X) is a Tree (Theorem 28.1)
The Cayley graph is a tree if and only if X is a free set of generators for G.

# Context & Application

The Cayley graph connects group theory to graph theory and is the bridge to the Nielsen-Schreier theorem. Armstrong uses Theorem 28.1 (Cayley graph of a free group is a tree) combined with Theorem 28.3 (free action on a tree implies free group) to prove Nielsen-Schreier.

# Examples

**Example 1** (p. 182): For a finite cyclic group of order n with one generator, Gamma(G, X) is a polygon with n sides, acted on by rotation.

**Example 2** (p. 182, Figure 28.3): For F_2 = F({x, y}), the Cayley graph is an infinite tree where each vertex has degree 4 (edges for x, x^{-1}, y, y^{-1}).

# Relationships

## Builds Upon
- **Graph** -- The Cayley graph is a graph

## Enables
- **Nielsen-Schreier theorem** -- Free group Cayley graphs are trees; subgroups act freely on these trees

## Related
- **Free group** -- Cayley graph of a free group is a tree
- **Group action on a graph** -- G acts freely on its Cayley graph

# Common Errors

- **Error**: Assuming the Cayley graph depends only on G
  **Correction**: The Cayley graph depends on the choice of generating set X; different X give different graphs

# Common Confusions

- **Confusion**: Thinking the Cayley graph is always a tree
  **Clarification**: The Cayley graph is a tree only when X is a free set of generators (Theorem 28.1); for a cyclic group, the Cayley graph is a polygon

# Source Reference

Chapter 28: Trees and the Nielsen-Schreier Theorem, pages 182-183 (pdf pp. 182-183). Example (iv) and Theorem 28.1.

# Verification Notes

- Definition: Directly quoted from Armstrong p. 182
- Theorem 28.1: Stated and proved on p. 183
- Confidence: HIGH -- explicit construction and theorem
- Cross-references: Verified against planned extractions
- Uncertainties: None
