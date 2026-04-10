---
concept: Coxeter Graph
slug: coxeter-graph
category: root-systems
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "The Structure of Semisimple Lie Algebras and Algebraic Groups in Characteristic Zero"
chapter_number: 3
pdf_page: 301
section: "Classification of root systems by Dynkin diagrams"
extraction_confidence: high
aliases: []
prerequisites:
  - root-system
  - base-of-root-system
extends: []
related:
  - dynkin-diagram
  - cartan-matrix
contrasts_with:
  - dynkin-diagram
answers_questions:
  - "What is a Coxeter graph?"
---

# Quick Definition

The Coxeter graph of a root system has nodes indexed by simple roots, with distinct nodes α, β joined by n(α,β)·n(β,α) edges (where n(α,β) = ⟨α, β^∨⟩).

# Core Definition

Choose a base S for a root system R. The **Coxeter graph** of (V, R) is the graph whose nodes are indexed by the elements of S; two distinct nodes are joined by n(α,β)·n(β,α) edges. Up to indexing of nodes, it is independent of the choice of S (Milne, §1h, p. 301).

The Coxeter graph is connected if and only if the root system is indecomposable (Proposition 1.16).

# Prerequisites

- **Root system** — The graph encodes root system structure
- **Base of root system** — Nodes correspond to simple roots

# Key Properties

1. Independent of choice of base (up to node relabeling)
2. Connected iff root system is indecomposable
3. Does not distinguish B_n from C_n (both give the same Coxeter graph)

# Examples

**Example 1** (p. 301): For rank 2 systems, the number of edges between the two nodes is 0 (A₁×A₁), 1 (A₂), 2 (B₂), or 3 (G₂).

# Relationships

## Enables
- **Dynkin diagram** — Obtained by adding arrows to the Coxeter graph

## Contrasts With
- **Dynkin diagram** — The Dynkin diagram carries more information (root length distinction)

# Source Reference

Chapter III, Section 1h, pages 301–302.

# Verification Notes

- Definition source: Direct from §1h
- Confidence: HIGH
- Uncertainties: None
