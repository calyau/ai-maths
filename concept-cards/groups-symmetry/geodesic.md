---
# === CORE IDENTIFICATION ===
concept: Geodesic
slug: geodesic

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
  - shortest path in a tree

# === TYPED RELATIONSHIPS ===
prerequisites:
  - tree
extends: []
related:
  - graph
  - nielsen-schreier-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a geodesic in a tree?"
---

# Quick Definition

A geodesic from vertex u to vertex v in a tree is the unique path joining u to v that does not contain any round trips. It is the shortest path between the two vertices.

# Core Definition

"If Gamma is a tree and if u, v are distinct vertices of Gamma, there is only one path which joins u to v and which does not contain any round trips. This path is the geodesic uv from u to v. Any other path joining u to v can be obtained from this geodesic by successively adding round trips" (Armstrong, Ch. 28, p. 180).

# Prerequisites

- **Tree** -- Geodesics are defined in trees

# Key Properties

1. Unique: only one round-trip-free path exists between any two vertices in a tree
2. Every other path between the same vertices is obtained by adding round trips to the geodesic
3. Geodesics are used extensively in the proof of Theorem 28.3
4. If g fixes two vertices u, v, then g fixes the entire geodesic between them (Exercise 28.3)

# Construction / Recognition

## To Find the Geodesic
1. Find any path from u to v
2. Remove all round trips (pairs alpha alpha-bar)
3. The result is the unique geodesic

# Context & Application

Geodesics are the key technical tool in Armstrong's proof of Theorem 28.3 (groups acting freely on trees are free). The proof constructs a free set of generators by tracing geodesics from a basepoint to its translates.

# Examples

**Example 1** (p. 180): In any tree, the geodesic from u to v is the unique backtracking-free path.

**Example 2** (Exercise 28.2, p. 186): Any path from u to v can be built from the geodesic by inserting round trips -- this is proved by induction.

# Relationships

## Builds Upon
- **Tree** -- Geodesics exist uniquely in trees

## Related
- **Nielsen-Schreier theorem** -- Geodesics are central to the proof

# Common Errors

- **Error**: Assuming geodesics exist in general graphs
  **Correction**: In graphs with cycles, there may be multiple round-trip-free paths between vertices

# Common Confusions

- **Confusion**: Confusing geodesic in a tree with geodesic in a metric space
  **Clarification**: Here "geodesic" means the unique backtracking-free path in a tree; in metric spaces it means a distance-minimizing curve

# Source Reference

Chapter 28: Trees and the Nielsen-Schreier Theorem, pages 180-181 (pdf pp. 180-181).

# Verification Notes

- Definition: Directly quoted from Armstrong p. 180
- Confidence: HIGH -- explicit definition
- Cross-references: Verified against planned extractions
- Uncertainties: None
