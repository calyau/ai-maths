---
concept: Tutte Polynomial and Jones Polynomial Connection
slug: tutte-polynomial-and-jones-polynomial
category: knot-theory
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 376
section: "X.6 Polynomials of Knots and Links"
extraction_confidence: high
aliases: []
prerequisites:
  - jones-polynomial
  - tutte-polynomial
  - alternating-link-diagram
extends: []
related:
  - tait-conjecture-crossing-number
contrasts_with: []
answers_questions:
  - "How do knot polynomials relate to the Tutte polynomial?"
---

# Quick Definition
For a connected alternating oriented link diagram $L$ with $a$ A-regions, $b$ B-regions, and writhe $w$, the Jones polynomial equals $V_L(t) = (-1)^w t^{(b-a+3w)/4} T_{G^+(L)}(-t, -1/t)$.

# Core Definition
Theorem 21 (p. 376): "Let $L$ be a connected alternating oriented link diagram with $a$ A-regions, $b$ B-regions, and writhe $w$. Then the Jones polynomial of $L$ is given by the Tutte polynomial of $G^+(L)$: $V_L(t) = (-1)^w t^{(b-a+3w)/4} T_{G^+(L)}(-t, -1/t)$."

# Prerequisites
- **Jones polynomial** — The link invariant being expressed
- **Tutte polynomial** — The graph polynomial providing the expression
- **Alternating link diagram** — The class where the connection holds

# Key Properties
1. Only applies to alternating link diagrams
2. $G^+(L)$ is the plane graph associated to the A-shading of $L$
3. The connection "is not only skin deep" (p. 340)
4. Enables proving Tait's conjecture on crossing numbers

# Context & Application
This is the deepest connection between graph theory and knot theory in the chapter, showing that for alternating links, a topological invariant (Jones polynomial) is determined by a combinatorial invariant (Tutte polynomial of an associated graph).

# Examples
**Example**: The Jones polynomial of the trefoil can be computed from $T_{K_3}(-t, -1/t)$.

# Relationships
## Builds Upon
- **jones-polynomial**, **tutte-polynomial**, **alternating-link-diagram**

## Enables
- **tait-conjecture-crossing-number** — Proved using this connection

# Source Reference
Chapter X, Section X.6, Theorem 21, page 376.

# Verification Notes
- Definition source: Direct from Theorem 21
- Confidence rationale: Explicit theorem
- Uncertainties: None
- Cross-reference status: Verified
