---
# === CORE IDENTIFICATION ===
concept: Cayley Graph is Tree Theorem
slug: cayley-graph-is-tree-theorem

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
  - "Theorem 28.1"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cayley-graph
  - free-group
  - tree
extends: []
related:
  - nielsen-schreier-theorem
  - free-action-on-tree-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When is the Cayley graph of a group a tree?"
---

# Quick Definition

The Cayley graph Gamma(G, X) is a tree if and only if X is a free set of generators for G. This connects the algebraic concept of freeness to the geometric property of being a tree.

# Core Definition

"(28.1) Theorem. If X is a free set of generators for G, then Gamma(G, X) is a tree" (Armstrong, Ch. 28, p. 183). The proof shows: a closed path in Gamma(G, X) corresponds to a word z_1 z_2 ... z_n = e in G. Since X is free, the word must reduce to the empty word, so it contains a pair z z^{-1}, which corresponds to a round trip in the graph.

# Prerequisites

- **Cayley graph** -- Gamma(G, X) is the graph in question
- **Free group** -- G must be free with free generators X
- **Tree** -- The conclusion

# Key Properties

1. Free generators yield a tree; non-free generators yield a graph with cycles
2. The proof uses uniqueness of reduced word representation
3. Closed paths correspond to words equal to the identity
4. In a free group, such words must contain cancellable pairs, giving round trips
5. This theorem is one of the two ingredients for the Nielsen-Schreier theorem

# Construction / Recognition

## Proof (Armstrong, p. 183)
1. Take a closed path alpha_1 ... alpha_n from vertex g back to g
2. This gives a word z_1 z_2 ... z_n with e = z_1 z_2 ... z_n
3. Since X is free, the only reduced word for e is the empty word
4. Therefore z_1 ... z_n must contain an adjacent pair z z^{-1}
5. This corresponds to a round trip alpha alpha-bar in the path
6. Hence Gamma(G, X) is a tree

# Context & Application

This theorem provides the bridge between algebra and geometry in Armstrong's proof strategy. Combined with Theorem 28.3 (free action on a tree implies free group), it yields the Nielsen-Schreier theorem: a subgroup of F acts freely on the tree Gamma(F, X), hence is free.

# Examples

**Example 1** (p. 182, Figure 28.3): The Cayley graph of F_2 on {x, y} is an infinite tree where each vertex has degree 4.

**Example 2** (p. 182): The Cayley graph of Z_n on {generator} is an n-gon, which is NOT a tree (since the generator is not free -- it satisfies x^n = e).

# Relationships

## Builds Upon
- **Cayley graph** -- The graph Gamma(G, X)
- **Free group** -- The algebraic condition

## Enables
- **Nielsen-Schreier theorem** -- One of the two key ingredients

## Related
- **Free action on tree theorem** -- The other key ingredient

# Common Errors

- **Error**: Assuming the converse without proof (if Gamma(G,X) is a tree then X is free)
  **Correction**: The converse is also true but requires separate argument; Armstrong states the forward direction

# Common Confusions

- **Confusion**: Thinking all Cayley graphs are trees
  **Clarification**: Only Cayley graphs of free groups with free generators are trees; finite groups always have non-tree Cayley graphs

# Source Reference

Chapter 28: Trees and the Nielsen-Schreier Theorem, Theorem 28.1 and proof, page 183 (pdf p. 183).

# Verification Notes

- Theorem: Directly quoted from Armstrong p. 183
- Proof: Complete in source
- Confidence: HIGH -- named theorem with complete proof
- Cross-references: Verified against planned extractions
- Uncertainties: None
