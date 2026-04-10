---
concept: Independence Number
slug: independence-number
category: vertex-coloring
subcategory: null
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Colouring"
chapter_number: 5
pdf_page: 153
section: "V.1 Vertex Colouring"
extraction_confidence: high
aliases:
  - "α(G)"
  - "maximum independent set size"
prerequisites: []
extends: []
related:
  - chromatic-number
  - clique-number
  - colour-class
contrasts_with:
  - clique-number
answers_questions:
  - "What is the independence number of a graph?"
---

# Quick Definition
The independence number α(G) is the maximum size of an independent set in G — a set of vertices with no two adjacent.

# Core Definition
The independence number α(G) is the maximal size of an independent set in G. It provides a lower bound on the chromatic number via χ(G) ≥ |G|/α(G), since every colour class has at most α(G) vertices (Bollobás, p. 153).

# Prerequisites
This is a foundational concept with no prerequisites within this source.

# Key Properties
1. χ(G) ≥ |G|/α(G)
2. α(G) = ω(G̅) (independence number equals clique number of complement)
3. α(Kₙ) = 1 and α(K̄ₙ) = n
4. Each colour class in any colouring has at most α(G) vertices

# Construction / Recognition
## To Find α(G)
1. Search for independent sets of increasing size
2. The largest independent set found gives α(G)
3. Computing α(G) is NP-hard in general

# Context & Application
The independence number is dual to the clique number via complementation. It provides the second basic lower bound on chromatic number and plays a central role in the theory of perfect graphs.

# Examples
**Example** (p. 153): If G has no independent set of size h+1, then every colour class has at most h vertices, giving χ(G) ≥ ⌈|G|/h⌉.

# Relationships
## Enables
- Lower bound χ(G) ≥ |G|/α(G)
- **Perfect graph** theory (via complementation)

## Related
- **Chromatic number** — bounded below by |G|/α(G)
- **Colour class** — each colour class is an independent set of size ≤ α(G)

## Contrasts With
- **Clique number** — α(G) = ω(G̅); maximum independent set vs. maximum clique

# Common Errors
- **Error**: Confusing α(G) with the size of a maximal (not maximum) independent set
  **Correction**: α(G) is the maximum, not just any maximal independent set

# Common Confusions
- **Confusion**: Mixing up independence number of G with clique number of G
  **Clarification**: α(G) = ω(G̅), not ω(G); they are dual via complementation

# Source Reference
Chapter V: Colouring, Section V.1, page 153.

# Verification Notes
- Definition source: Direct from p. 153
- Confidence rationale: Explicitly defined with notation α(G)
- Uncertainties: None
- Cross-reference status: Verified
