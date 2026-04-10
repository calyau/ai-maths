---
# === CORE IDENTIFICATION ===
concept: Schreier System
slug: schreier-system

# === CLASSIFICATION ===
category: algebraic-graph-theory
subcategory: group-computation
tier: intermediate

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Graphs, Groups and Matrices"
chapter_number: 8
pdf_page: 264
section: "VIII.1 Cayley and Schreier Diagrams"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Schreier transversal

# === TYPED RELATIONSHIPS ===
prerequisites:
  - schreier-diagram
extends: []
related:
  - reidemeister-schreier-process
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Schreier system of coset representatives?"
---

# Quick Definition

A Schreier system for $B \bmod A$ is a set of coset representatives obtained from a spanning tree of the Schreier diagram: the representative of coset $H$ is the product of edge colors along the unique tree path from $B$ to $H$.

# Core Definition

Select a spanning tree of the Schreier diagram. Decorate $B$ by 1 (identity) and tree edges by 1. For each vertex $H$, the unique tree path from $B$ to $H$ determines the coset representative $h = abc\cdots$ (product of edge colors). These representatives form a Schreier system for $B \bmod A$ (Bollobas, p. 264).

# Prerequisites

- **Schreier diagram** -- The spanning tree is selected from it

# Key Properties

1. Each coset has exactly one representative in the system
2. The chord decorations (non-tree edges) generate $B$
3. The decoration of a chord $HK$ equals the product of colors around the cycle $B$-$H$-$K$-$B$

# Construction / Recognition

## To Build a Schreier System
1. Choose a spanning tree of the Schreier diagram
2. Assign representative 1 to the root vertex $B$
3. For each other vertex $H$: the representative is the product of edge colors along the tree path from $B$ to $H$

# Context & Application

Schreier systems provide canonical coset representatives needed for the Reidemeister-Schreier process. They are the foundation for computational subgroup analysis.

# Examples

**Example** (p. 264, Fig. VIII.9): The chord decorations in a decorated Schreier diagram give generators of $B$.

# Relationships

## Builds Upon
- **Schreier diagram** -- Source of the spanning tree

## Enables
- **Reidemeister-Schreier process** -- Uses the Schreier system

## Related
- **Reidemeister-Schreier process** -- The main application

## Contrasts With
- None

# Common Errors

- **Error**: Choosing different spanning trees and expecting the same generators
  **Correction**: Different spanning trees give different (but related) generating sets for $B$

# Common Confusions

- **Confusion**: Thinking the Schreier system depends only on the subgroup
  **Clarification**: It depends on the choice of spanning tree of the Schreier diagram

# Source Reference

Chapter VIII, Section VIII.1, page 264.

# Verification Notes

- Definition source: Direct from p. 264
- Confidence rationale: Explicit description
- Uncertainties: None
- Cross-reference status: Verified
