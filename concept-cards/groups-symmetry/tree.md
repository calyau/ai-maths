---
# === CORE IDENTIFICATION ===
concept: Tree
slug: tree

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - graph
extends:
  - graph
related:
  - geodesic
  - group-action-on-a-graph
  - nielsen-schreier-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a tree in the context of group actions?"
  - "How does a tree differ from a general graph?"
---

# Quick Definition

A tree is a connected graph in which every path from a vertex to itself must contain a round trip (an edge followed by its reverse). Equivalently, a tree has no cycles.

# Core Definition

"A graph is a tree if any two distinct vertices may be joined by a path, and if every path which joins a vertex to itself has to contain a round trip" (Armstrong, Ch. 28, p. 180). The "round trip" alpha alpha-bar is an edge followed by its reverse. In a tree, distinct vertices are connected by a unique path without round trips (the geodesic).

# Prerequisites

- **Graph** -- A tree is a special type of graph

# Key Properties

1. Connected: any two distinct vertices can be joined by a path
2. Acyclic: every closed path contains a round trip
3. Between any two distinct vertices there is a unique path without round trips (the geodesic)
4. Any other path between the same vertices is obtained from the geodesic by adding round trips (Exercise 28.2)
5. If G acts freely on a tree, then G is free (Theorem 28.3)

# Construction / Recognition

## To Verify a Graph is a Tree
1. Check connectivity: any two vertices can be joined by a path
2. Check acyclicity: show every closed path contains an edge alpha followed by alpha-bar

# Context & Application

Trees are the central geometric objects in Armstrong's proof of the Nielsen-Schreier theorem. The key theorem (28.3) states that a group acting freely on a tree is free. This geometric approach follows Serre's treatment and gives an elegant proof of Nielsen-Schreier.

# Examples

**Example 1** (p. 180, Figure 28.2): Armstrong illustrates trees vs. non-trees using simplified diagrams.

**Example 2** (p. 181, Example (ii)): The real line with integers as vertices is a tree; the infinite cyclic group acts freely on it.

**Example 3** (p. 182, Figure 28.3): The Cayley graph of the free group F_2 on generators {x, y} is a tree (Theorem 28.1).

# Relationships

## Builds Upon
- **Graph** -- A tree is a connected acyclic graph

## Enables
- **Nielsen-Schreier theorem** -- Proved using group actions on trees
- **Geodesic** -- The unique shortest path in a tree

## Related
- **Group action on a graph** -- Groups acting freely on trees are free
- **Reference tree** -- A subtree used in the proof of Theorem 28.3

# Common Errors

- **Error**: Assuming a tree must be finite
  **Correction**: Trees can be infinite; the Cayley graph of F_2 is an infinite tree

# Common Confusions

- **Confusion**: Confusing "round trip" with "cycle"
  **Clarification**: A round trip is specifically an edge followed by its reverse (alpha alpha-bar); a "cycle" in general graph theory need not contain such backtracking

# Source Reference

Chapter 28: Trees and the Nielsen-Schreier Theorem, pages 180-183 (pdf pp. 180-183). Definition on p. 180; Theorem 28.1 on p. 183.

# Verification Notes

- Definition: Directly quoted from Armstrong p. 180
- Confidence: HIGH -- explicit definition
- Cross-references: Verified against planned extractions
- Uncertainties: None
