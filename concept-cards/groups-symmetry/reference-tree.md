---
# === CORE IDENTIFICATION ===
concept: Reference Tree
slug: reference-tree

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
  - maximal orbit-tree

# === TYPED RELATIONSHIPS ===
prerequisites:
  - tree
  - group-action-on-a-graph
extends: []
related:
  - nielsen-schreier-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a reference tree in the context of group actions on trees?"
---

# Quick Definition

A reference tree Lambda for a group G acting on a tree Gamma is a maximal subtree that contains at most one edge and one vertex from each orbit. It contains exactly one vertex from each orbit (Theorem 28.2).

# Core Definition

"Consider the collection T of all trees inside Gamma which contain no more than one edge and one vertex from each orbit. An element Lambda of T which is maximal with respect to the partial order given by inclusion will be called a reference tree" (Armstrong, Ch. 28, p. 183). Theorem 28.2 establishes: "A reference tree contains precisely one vertex from each orbit."

# Prerequisites

- **Tree** -- A reference tree is a subtree of Gamma
- **Group action on a graph** -- The orbits are defined by the group action

# Key Properties

1. Contains at most one vertex from each vertex orbit
2. Contains at most one edge from each edge orbit
3. Maximality: no larger subtree satisfies these constraints
4. Contains exactly one vertex from each orbit (Theorem 28.2)
5. Existence guaranteed by Zorn's lemma
6. Used to construct a free set of generators in Theorem 28.3

# Construction / Recognition

## Role in the Proof of Theorem 28.3
1. Choose a reference tree Lambda for the free action of G on the tree Gamma
2. Let A_* be edges of Gamma not in Lambda but with initial vertex in Lambda
3. For each alpha in A_*, find the unique g_alpha sending the Lambda-vertex in the orbit of t(alpha) to t(alpha)
4. From each pair g_alpha, g_alpha^{-1}, select one to form the set X
5. X is a free set of generators for G

# Context & Application

The reference tree is the key technical construction in Armstrong's proof that free actions on trees produce free groups (Theorem 28.3). It provides a systematic way to identify the generators of the group from the geometry of the action.

# Examples

**Example 1** (p. 183, Figure 28.4, Example (v)): For Z x Z_2 acting on an infinite tree, a reference tree is shown in the diagram. Armstrong notes there are twelve possible reference trees containing the vertex 0.

# Relationships

## Builds Upon
- **Tree** -- A reference tree is a subtree
- **Group action on a graph** -- Defined relative to orbits of the action

## Enables
- **Nielsen-Schreier theorem** -- The proof constructs free generators using a reference tree

# Common Errors

- **Error**: Assuming a reference tree is unique
  **Correction**: There may be many reference trees; Armstrong's example has twelve

# Common Confusions

- **Confusion**: Thinking a reference tree contains one edge from each orbit
  **Clarification**: A reference tree contains at most one edge from each orbit; it may contain no edges from some orbits

# Source Reference

Chapter 28: Trees and the Nielsen-Schreier Theorem, pages 183-184 (pdf pp. 183-184). Definition on p. 183; Theorem 28.2 on p. 184.

# Verification Notes

- Definition: Directly quoted from Armstrong p. 183
- Theorem 28.2: Proved on p. 184
- Confidence: HIGH -- explicit definition and theorem
- Cross-references: Verified against planned extractions
- Uncertainties: None
