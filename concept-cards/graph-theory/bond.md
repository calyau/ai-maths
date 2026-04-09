---
concept: Bond
slug: bond

category: algebraic-graph-theory
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 35
section: "1.9 Some linear algebra"

extraction_confidence: high

aliases:
  - "minimal cut"

prerequisites:
  - graph
  - cut
  - connected-graph
extends:
  - cut
related:
  - cut-space
  - cycle
contrasts_with: []

answers_questions:
  - "What is a bond in a graph?"
---

# Quick Definition
A bond is a minimal non-empty cut. In a connected graph, bonds are the minimal cuts, which are exactly the cuts where both sides of the partition induce connected subgraphs.

# Core Definition
A minimal non-empty cut in G is a bond. Bonds are for C* what cycles are for C: the minimal non-empty elements. If G is connected, its bonds are just its minimal cuts, and a cut in a connected graph is minimal if and only if both sides of the corresponding vertex partition induce connected subgraphs (Diestel, p. 25).

# Prerequisites
- **Graph**, **cut**, **connected-graph**

# Key Properties
1. Every cut is a disjoint union of bonds (Lemma 1.9.4)
2. In a connected graph: a cut is a bond iff both sides induce connected subgraphs
3. Bonds and disjoint unions suffice to generate C*

# Relationships
## Builds Upon
- **cut**, **connected-graph**

## Related
- **cycle** — bonds are the cut-space analog of cycles in the cycle space

# Source Reference
Chapter 1: The Basics, Section 1.9, page 25 (pdf p. 35). Lemma 1.9.4.

# Verification Notes
- Direct from p. 25
- Confidence: HIGH
