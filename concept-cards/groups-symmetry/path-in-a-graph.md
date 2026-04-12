---
# === CORE IDENTIFICATION ===
concept: Path in a Graph
slug: path-in-a-graph

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
  - edge path
  - round trip

# === TYPED RELATIONSHIPS ===
prerequisites:
  - graph
extends: []
related:
  - tree
  - geodesic
  - fundamental-group-of-a-graph
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a path in a graph?"
  - "What is a round trip?"
---

# Quick Definition

A path in a graph Gamma joining vertex u to vertex v is an ordered string of edges alpha_1 alpha_2 ... alpha_n such that the terminal vertex of each edge is the initial vertex of the next. A round trip is the special case alpha alpha-bar (an edge followed by its reverse).

# Core Definition

"A path in Gamma joining vertex u to vertex v is an ordered string of edges alpha_1 alpha_2 ... alpha_n such that i(alpha_1) = u, i(alpha_{k+1}) = t(alpha_k) for 1 <= k <= n-1, and t(alpha_n) = v. The special case alpha alpha-bar where an edge is followed by its reverse is called a round trip" (Armstrong, Ch. 28, p. 180).

# Prerequisites

- **Graph** -- Paths are defined within graphs

# Key Properties

1. A path is a finite ordered sequence of consecutive edges
2. Consecutive means: the terminal vertex of one edge equals the initial vertex of the next
3. A round trip is an edge followed by its reverse: alpha alpha-bar
4. In a tree, every closed path (from a vertex to itself) must contain a round trip
5. The geodesic is a path with no round trips
6. Any path between two vertices in a tree can be obtained from the geodesic by adding round trips

# Construction / Recognition

## To Verify a Sequence is a Path
1. Check that each entry is an edge of Gamma
2. Check i(alpha_1) = u (starts at u)
3. Check t(alpha_k) = i(alpha_{k+1}) for each consecutive pair
4. Check t(alpha_n) = v (ends at v)

# Context & Application

Paths and round trips are fundamental to the definition of trees and the proof of the Nielsen-Schreier theorem. The concept of a round trip (backtracking) distinguishes trees from graphs with cycles: a tree is exactly a connected graph where every closed path contains a round trip.

# Examples

**Example 1** (p. 180): The round trip alpha alpha-bar starts at i(alpha), goes to t(alpha), and returns to i(alpha).

**Example 2** (Exercise 28.2, p. 186): In a tree, any path from u to v that is not the geodesic can be built from the geodesic by inserting round trips.

# Relationships

## Enables
- **Tree** -- Trees are defined via the behavior of paths
- **Geodesic** -- The unique round-trip-free path
- **Fundamental group of a graph** -- Built from equivalence classes of closed paths

# Common Errors

- **Error**: Assuming every closed path is a round trip
  **Correction**: A round trip is specifically alpha alpha-bar; a closed path may traverse many edges

# Common Confusions

- **Confusion**: Confusing "path" with "simple path" (no repeated vertices)
  **Clarification**: Armstrong's paths can revisit vertices; simplicity is not required

# Source Reference

Chapter 28: Trees and the Nielsen-Schreier Theorem, page 180 (pdf p. 180).

# Verification Notes

- Definition: Directly quoted from Armstrong p. 180
- Confidence: HIGH -- explicit definition
- Cross-references: Verified against planned extractions
- Uncertainties: None
