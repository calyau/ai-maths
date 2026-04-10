---
# === CORE IDENTIFICATION ===
concept: Schreier Diagram
slug: schreier-diagram

# === CLASSIFICATION ===
category: algebraic-graph-theory
subcategory: group-graphs
tier: intermediate

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Graphs, Groups and Matrices"
chapter_number: 8
pdf_page: 259
section: "VIII.1 Cayley and Schreier Diagrams"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Schreier graph
  - Schreier coset diagram

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cayley-diagram
  - group-presentation
extends:
  - cayley-diagram
related:
  - schreier-system
  - reidemeister-schreier-process
  - nielsen-schreier-theorem
contrasts_with:
  - cayley-diagram

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Schreier diagram?"
  - "How do Schreier diagrams relate to Cayley diagrams?"
---

# Quick Definition

The Schreier diagram of a group $A$ modulo a subgroup $B$ describes the action of generators on the right cosets of $B$; its vertices are cosets and edges are colored by generators.

# Core Definition

Given a group $A$, a set $S$ of elements of $A$, and a subgroup $B$ of $A$, the Schreier diagram of $A$ mod $B$ is a directed multigraph whose vertices are the right cosets of $B$, with an edge of color $s \in S$ from coset $Bx$ to coset $Bxs$ (Bollobas, p. 259). A Cayley diagram is a Schreier diagram where $B$ is the trivial subgroup.

# Prerequisites

- **Cayley diagram** -- The Schreier diagram generalizes this
- **Group presentation** -- Needed to apply defining relations

# Key Properties

1. Vertices are right cosets of $B$ in $A$
2. Regular coloring: for each vertex and color, exactly one edge starts and one ends
3. Some edges may be loops (when $Bxs = Bx$)
4. The number of vertices equals the index $[A:B]$
5. Can be constructed analogously to Cayley diagrams, with the added condition that elements of $B$ fix the vertex for $B$

# Construction / Recognition

## To Construct a Schreier Diagram
1. Start with vertex 1 representing coset $B$
2. For elements of $B$ that are generators, draw loops at vertex 1
3. For each generator not in $B$, create edges to new vertices
4. Apply defining relations at each vertex
5. Identify vertices when forced by conditions (a) and (b)

# Context & Application

Schreier diagrams are especially useful for determining the index of a subgroup (number of vertices) and for finding generators and presentations of subgroups via the Reidemeister-Schreier process. They can be decorated with coset representatives to read off additional structural information.

# Examples

**Example** (pp. 263--265): For $A = \langle a, b \mid a^2 = b^5 = (ba)^3 = 1\rangle$ and $B = \langle b\rangle$, the Schreier diagram has 12 vertices, showing $[A:B] = 12$ and $A \cong A_5$ (the alternating group on 5 symbols).

# Relationships

## Builds Upon
- **Cayley diagram** -- Special case when $B$ is trivial
- **Group presentation** -- Needed for construction

## Enables
- **Schreier system** -- Coset representatives from a spanning tree
- **Reidemeister-Schreier process** -- Presentation of the subgroup
- **Nielsen-Schreier theorem** -- Proof that subgroups of free groups are free

## Related
- **Schreier system** -- Representatives from the diagram

## Contrasts With
- **Cayley diagram** -- Cayley uses the trivial subgroup; Schreier uses a general subgroup

# Common Errors

- **Error**: Forgetting that generators in $B$ create loops at the vertex for $B$
  **Correction**: If $b \in B$ and $b$ is a generator, the edge colored $b$ at vertex $B$ is a loop

# Common Confusions

- **Confusion**: Thinking the Schreier diagram is always connected
  **Clarification**: If $S$ does not generate $A$ together with $B$, the diagram may be disconnected

# Source Reference

Chapter VIII: Graphs, Groups and Matrices, Section VIII.1, pages 259--266.

# Verification Notes

- Definition source: Direct from p. 259
- Confidence rationale: Explicit definition with worked example
- Uncertainties: None
- Cross-reference status: Verified
