---
concept: Independent Paths
slug: independent-paths
category: connectivity
subcategory: path-structures
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.2 Connectivity and Menger's Theorem"
extraction_confidence: high
aliases:
  - "internally disjoint paths"
  - "vertex-disjoint paths"
prerequisites:
  - graph-connectivity
extends: []
related:
  - mengers-theorem
  - edge-disjoint-paths
contrasts_with:
  - edge-disjoint-paths
answers_questions:
  - "What must I know before understanding Menger's theorem?"
---

# Quick Definition
Two $s$-$t$ paths are independent if they share only the vertices $s$ and $t$ (their internal vertices are disjoint).

# Core Definition
Two $s$-$t$ paths are independent if they have only the vertices $s$ and $t$ in common. This is the vertex-disjoint version of path independence used in the vertex form of Menger's theorem (Bollobás, p. 82).

# Prerequisites
- **Graph connectivity** — Independent paths arise in connectivity theory

# Key Properties
1. Independent paths share only their endpoints
2. The maximum number of independent $s$-$t$ paths equals the minimum vertex separator (Menger's theorem)
3. Distinct from edge-disjoint paths, which may share internal vertices

# Construction / Recognition
1. Find two $s$-$t$ paths $P_1$ and $P_2$
2. Check that $V(P_1) \cap V(P_2) = \{s, t\}$
3. If so, the paths are independent

# Context & Application
Independent paths are the key objects in the vertex form of Menger's theorem. The number of independent paths between two vertices characterizes the vertex connectivity between them.

# Examples
**Example** (p. 82): In the proof of Menger's theorem, integral flows through vertex-split graphs decompose into independent paths between $s$ and $t$.

# Relationships
## Builds Upon
- **graph-connectivity** — Paths exist in connected graphs

## Enables
- **mengers-theorem** — Counts independent paths

## Contrasts With
- **edge-disjoint-paths** — Share no edges but may share vertices

# Common Errors
- **Error**: Allowing independent paths to share internal vertices
  **Correction**: Independent paths share only $s$ and $t$; all internal vertices are distinct

# Common Confusions
- **Confusion**: Confusing independent paths with edge-disjoint paths
  **Clarification**: Independent = vertex-disjoint (except endpoints); edge-disjoint = no shared edges (vertices may repeat)

# Source Reference
Chapter III, Section III.2, page 82.

# Verification Notes
- Definition source: Direct from p. 82
- Confidence rationale: Explicitly defined before Menger's theorem
- Uncertainties: None
- Cross-reference status: Verified
