---
concept: "Excluded K^n Structure Theorem"
slug: excluded-kn-structure-theorem
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
  - "Robertson-Seymour structure theorem"
prerequisites:
  - tree-decomposition
  - graph-minor
  - tree-width
extends: []
related:
  - graph-minor-theorem
  - path-decomposition
contrasts_with: []
answers_questions:
  - "What is the structure of graphs without a K^n minor?"
---

# Quick Definition
For every n, every graph without a K^n minor has a tree-decomposition whose torsos are k-nearly embeddable in a surface in which K^n is not embeddable, for some k depending on n (Robertson-Seymour, 2003).

# Core Definition
**Theorem 12.4.11** (Robertson & Seymour 2003): For every n there exists k such that every graph G not containing K^n as a minor has a tree-decomposition whose torsos are k-nearly embeddable in a surface in which K^n is not embeddable (Diestel, p. 350).

# Prerequisites
- **Tree-decomposition** — The structural tool
- **Graph minor** — The excluded minor condition
- **Tree-width** — The torsos have bounded structure

# Key Properties
1. The torsos are "nearly" embeddable in bounded-genus surfaces
2. "k-nearly embeddable" allows: an apex set of <= k vertices, an embedding in a surface minus k discs, and vortices of bounded path-width along cuffs
3. Separators in the tree-decomposition have bounded size
4. This is the key structural result used in the proof of the graph minor theorem
5. Extends to infinite graphs (Diestel-Thomas 1999)

# Context & Application
This theorem describes the global structure of all K^n-free graphs. It is central to the proof of the graph minor theorem and to algorithmic applications (Robertson-Seymour cubic-time minor testing).

# Relationships
## Builds Upon
- **Tree-decomposition** — The decomposition framework

## Enables
- **Graph minor theorem** — Uses this structure theorem in its proof

# Source Reference
Chapter 12, Section 12.4, pages 350-351 (Theorem 12.4.11).

# Verification Notes
- Statement from pp. 350-351
- Confidence: HIGH — named theorem, stated without proof
