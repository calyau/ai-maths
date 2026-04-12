---
# === CORE IDENTIFICATION ===
concept: Group Action on a Graph
slug: group-action-on-a-graph

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
  - graph action
  - group acting on a tree

# === TYPED RELATIONSHIPS ===
prerequisites:
  - graph
  - group
extends: []
related:
  - tree
  - reference-tree
  - nielsen-schreier-theorem
  - cayley-graph
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does it mean for a group to act on a graph?"
  - "What is a free action on a tree?"
---

# Quick Definition

An action of a group G on a graph Gamma is a compatible action on both the edges and vertices, preserving the graph structure: reversal, initial vertices, and terminal vertices. The action is free if no non-identity element fixes any vertex.

# Core Definition

"An action of a group G on a graph Gamma is an action of G on A and on V such that g(alpha-bar) = g(alpha)-bar, g(i(alpha)) = i(g(alpha)) and g(alpha) is not alpha-bar for each g in G and alpha in A. In other words the elements of G permute the edges and vertices of Gamma in a way that is compatible with the structure of Gamma as a graph, and no element of G is allowed to reverse an edge" (Armstrong, Ch. 28, p. 181). "We shall say that G acts freely on Gamma if the stabilizer of each vertex is just the trivial subgroup {e} of G" (Armstrong, p. 181).

# Prerequisites

- **Graph** -- The object being acted upon
- **Group** -- The group performing the action

# Key Properties

1. g(alpha-bar) = g(alpha)-bar (reversal is preserved)
2. g(i(alpha)) = i(g(alpha)) (initial vertices are preserved)
3. g(alpha) is not alpha-bar (no element reverses an edge)
4. Terminal vertices are automatically preserved: g(t(alpha)) = t(g(alpha))
5. Free action: stabilizer of every vertex is trivial
6. Key theorem (28.3): if G acts freely on a tree, then G is a free group

# Construction / Recognition

## To Define a Group Action on a Graph
1. Define how G acts on the vertex set V
2. Define how G acts on the edge set A
3. Verify g(alpha-bar) = g(alpha)-bar for all g, alpha
4. Verify g(i(alpha)) = i(g(alpha)) for all g, alpha
5. Verify g(alpha) is not alpha-bar for all g, alpha (no edge reversal)

# Context & Application

Group actions on graphs (and especially on trees) are the geometric foundation for Armstrong's proof of the Nielsen-Schreier theorem. The key insight is that acting freely on a tree forces the group to be free. This approach, following Serre, replaces the original algebraic proof with a more conceptual geometric argument.

# Examples

**Example 1** (p. 181): A cyclic group of order 3 acts on a Y-shaped tree by rotation. The stabilizer of the central vertex is all of G, so this action is not free.

**Example 2** (p. 181): The infinite cyclic group Z acts freely on the integer line (vertices = Z, edges connecting consecutive integers). The generator sends alpha_r to alpha_{r+1}.

**Example 3** (p. 181): The infinite dihedral group acts on the integer line, but not freely: each vertex has a stabilizer of order 2.

**Example 4** (p. 182): The Cayley graph construction Gamma(G, X): vertices are elements of G, edges connect g to gz for generators z in X. G acts freely on Gamma(G, X) by left multiplication.

# Relationships

## Enables
- **Reference tree** -- Used to analyze group actions on trees
- **Nielsen-Schreier theorem** -- Proved via free actions on trees

## Related
- **Tree** -- The most important case is actions on trees
- **Cayley graph** -- A canonical graph on which G acts freely

# Common Errors

- **Error**: Forgetting the condition that no element reverses an edge
  **Correction**: The condition g(alpha) is not alpha-bar is essential; without it, the theory breaks down

# Common Confusions

- **Confusion**: Confusing "free action" with "faithful action"
  **Clarification**: Free means every vertex stabilizer is trivial; faithful means the only element acting as the identity is e. Free implies faithful but not conversely

# Source Reference

Chapter 28: Trees and the Nielsen-Schreier Theorem, pages 181-182 (pdf pp. 181-182). Definition and examples.

# Verification Notes

- Definition: Directly quoted from Armstrong p. 181
- Examples: All from source text
- Confidence: HIGH -- explicit definition with examples
- Cross-references: Verified against planned extractions
- Uncertainties: None
