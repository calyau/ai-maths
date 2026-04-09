---
concept: k-Mesh
slug: k-mesh
category: graph-minors
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Minors, Trees and WQO"
chapter_number: 12
pdf_page: 339
section: "12.4 Tree-width and forbidden minors"
extraction_confidence: high
aliases:
  - "premesh"
prerequisites:
  - externally-k-connected
  - tree-width
extends: []
related:
  - grid-theorem
contrasts_with: []
answers_questions:
  - "What is a k-mesh?"
---

# Quick Definition
A premesh (A, B) in G has G = A union B where A contains a tree T of max degree <= 3 with V(A cap B) in T. If V(A cap B) is externally k-connected in B, the premesh is a k-mesh. Its order is |A cap B|.

# Core Definition
An ordered pair (A, B) of subgraphs of G is a *premesh* if G = A union B and A contains a tree T with max degree <= 3, every vertex of A cap B lies in T with degree <= 2, and T has a leaf in A cap B. The *order* is |A cap B|. If V(A cap B) is externally k-connected in B, it is a *k-mesh* (Diestel, p. 339).

# Prerequisites
- **Externally k-connected** — The connectivity condition for k-meshes
- **Tree-width** — k-meshes relate to tree-width bounds

# Key Properties
1. Lemma 12.4.5: If G has no k-mesh of order h, then tw(G) < h + k - 1
2. Used as intermediate structures in the proof of the grid theorem
3. The tree T organizes the boundary vertices

# Source Reference
Chapter 12, Section 12.4, pages 339-340 (Lemma 12.4.5).

# Verification Notes
- Definition from p. 339
- Confidence: HIGH — explicit definition
