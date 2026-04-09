---
concept: Topological Minor
slug: topological-minor

category: graph-fundamentals
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 29
section: "1.7 Contraction and minors"

extraction_confidence: high

aliases:
  - "TX"
  - "topological subgraph"

prerequisites:
  - graph
  - subgraph
  - subdivision
extends: []
related:
  - minor
  - subdivision
  - contraction
contrasts_with:
  - minor

answers_questions:
  - "What is a topological minor?"
  - "What distinguishes a minor from a topological minor?"
---

# Quick Definition
X is a topological minor of Y if Y contains a subdivision of X as a subgraph. That is, we can find X in Y after replacing edges of X by independent paths.

# Core Definition
If we replace the edges of X with independent paths between their ends (so that none of these paths has an inner vertex on another path or in X), we call the graph G obtained a subdivision of X and write G = TX. If G = TX is the subgraph of another graph Y, then X is a topological minor of Y (Diestel, p. 20).

# Prerequisites
- **Graph**, **subgraph** — the subdivision must be a subgraph
- **Subdivision** — the key construction

# Key Properties
1. Every topological minor is also an (ordinary) minor (Proposition 1.7.2(i))
2. If Delta(X) <= 3, then every MX contains a TX (Proposition 1.7.2(ii))
3. The topological-minor relation is a partial ordering (Proposition 1.7.3)
4. Branch vertices retain their degree from X; subdividing vertices have degree 2

# Context & Application
The topological minor relation is finer than the minor relation. Kuratowski's theorem characterizes planar graphs by forbidden topological minors K^5 and K_{3,3}.

# Examples
**Example** (p. 20): Fig. 1.7.3 shows Y containing G = TX, so X is a topological minor of Y.
**Example** (p. 21): Fig. 1.7.4 shows a subdivision of K^4 viewed as an MK^4.

# Relationships
## Builds Upon
- **graph**, **subgraph**, **subdivision**

## Related
- **minor** — every topological minor is a minor

## Contrasts With
- **minor** — minor allows arbitrary contractions of connected subsets; topological minor only replaces edges by paths

# Common Confusions
- **Confusion**: Thinking every minor is a topological minor
  **Clarification**: A minor of X need not be a topological minor unless Delta(X) <= 3

# Source Reference
Chapter 1: The Basics, Section 1.7, pages 20-21 (pdf pp. 30-31). Propositions 1.7.2, 1.7.3.

# Verification Notes
- Direct from pp. 20-21
- Confidence: HIGH
