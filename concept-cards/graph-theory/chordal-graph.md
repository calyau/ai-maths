---
concept: Chordal Graph
slug: chordal-graph
category: graph-colouring
subcategory: perfect-graphs
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Colouring"
chapter_number: 5
pdf_page: 122
section: "5.5 Perfect graphs"
extraction_confidence: high
aliases:
  - "triangulated graph"
prerequisites:
  - graph
extends: []
related:
  - perfect-graph
  - interval-graph
  - comparability-graph
contrasts_with: []
answers_questions:
  - "What is a chordal graph?"
  - "Are chordal graphs perfect?"
---

# Quick Definition
A graph is chordal (or triangulated) if each of its cycles of length >= 4 has a chord. Equivalently, it contains no induced cycles other than triangles.

# Core Definition
"A graph is chordal (or triangulated) if each of its cycles of length at least 4 has a chord, i.e. if it contains no induced cycles other than triangles" (Diestel, p. 127).

# Prerequisites
- **Graph** -- Defined for graphs

# Key Properties
1. No induced cycle of length >= 4
2. Can be constructed by recursively pasting along complete subgraphs, starting from complete graphs (Proposition 5.5.1)
3. Every chordal graph is perfect (Proposition 5.5.2)
4. Every interval graph is chordal (Exercise 39)
5. The proof of perfection uses pasting along complete subgraphs

# Construction / Recognition
## Characterization (Proposition 5.5.1)
A graph is chordal if and only if it can be constructed recursively by pasting along complete subgraphs, starting from complete graphs.

## To Recognize a Chordal Graph
1. Check if every cycle of length >= 4 has a chord
2. Equivalently: find a perfect elimination ordering

# Context & Application
Chordal graphs are one of the most important classes of perfect graphs. They arise in sparse matrix factorization, database theory, and many optimization problems. Their recursive structure (pasting along cliques) makes them amenable to inductive proofs.

# Examples
**Example** (p. 127): Every complete graph is chordal (trivially, no induced cycle of length >= 4).

**Example** (p. 127-128, Fig. 5.5.1): The proof shows that pasting two chordal graphs along a complete subgraph preserves chordality.

# Relationships
## Enables
- **Perfect graph** -- All chordal graphs are perfect

## Related
- **Interval graph** -- Subclass of chordal graphs
- **Comparability graph** -- Another perfect class

# Common Confusions
- **Confusion**: Thinking "chordal" means "every cycle has a chord"
  **Clarification**: "Chordal" means every cycle of length >= 4 has a chord; triangles (length 3) need not (and cannot) have chords

# Source Reference
Chapter 5, Section 5.5, pages 127-128. Propositions 5.5.1 and 5.5.2.

# Verification Notes
- Definition from p. 127
- Proofs of Propositions 5.5.1 and 5.5.2 given
- Confidence: HIGH -- explicit definition with characterization theorem
