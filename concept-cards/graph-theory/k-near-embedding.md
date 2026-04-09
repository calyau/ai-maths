---
concept: k-Near Embedding
slug: k-near-embedding
category: graph-minors
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Minors, Trees and WQO"
chapter_number: 12
pdf_page: 350
section: "12.4 Tree-width and forbidden minors"
extraction_confidence: high
aliases:
  - "k-nearly embeddable"
prerequisites:
  - path-decomposition
  - tree-decomposition
extends: []
related:
  - excluded-kn-structure-theorem
contrasts_with: []
answers_questions:
  - "What is a k-near embedding in a surface?"
---

# Quick Definition
A graph H is k-nearly embeddable in a surface S if H has an apex set X of at most k vertices such that H - X decomposes as H_0 union H_1 union ... union H_k, where H_0 embeds in S minus k discs and each H_i (i >= 1) is a vortex of bounded path-width sewn along a cuff.

# Core Definition
A graph H is *k-nearly embeddable* in a surface S if H has a set X of at most k vertices such that H - X can be written as H_0 union H_1 union ... union H_k where: (N1) H_0 embeds in S minus k discs; (N2) H_1, ..., H_k are pairwise disjoint vortices; (N3) each H_i (i >= 1) has a linear decomposition of width <= k indexed by the cuff (Diestel, p. 350).

# Prerequisites
- **Path-decomposition** — Vortices have bounded path-width
- **Tree-decomposition** — Context for the structure theorem

# Key Properties
1. X is the "apex set" of removed vertices
2. H_0 is the "nearly planar" part
3. H_1, ..., H_k are "vortices" of bounded path-width
4. This structure describes all graphs in Forb(K^n)

# Relationships
## Related
- **Excluded K^n structure theorem** — Uses k-near embeddings

# Source Reference
Chapter 12, Section 12.4, page 350.

# Verification Notes
- Definition from p. 350
- Confidence: HIGH — explicit formal definition
