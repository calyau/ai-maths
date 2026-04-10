---
concept: Bridge in a Multigraph
slug: bridge-in-multigraph
category: tutte-polynomial
subcategory: null
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 341
section: "X.1 Basic Properties of the Tutte Polynomial"
extraction_confidence: high
aliases:
  - "isthmus"
prerequisites: []
extends: []
related:
  - loop-in-multigraph
  - deletion-contraction
  - tutte-polynomial
contrasts_with:
  - loop-in-multigraph
answers_questions:
  - "How do I compute the Tutte polynomial using deletion-contraction?"
---

# Quick Definition
An edge $e$ of a multigraph $G$ is a bridge if $G - e$ has more components than $G$, i.e., removing $e$ disconnects some component. In the Tutte polynomial recursion: $T_G = x T_{G-e}$ when $e$ is a bridge.

# Core Definition
An edge $e$ is a bridge if $k(G-e) = k(G) + 1$, equivalently $r(G-e) = r(G) - 1$. For bridges: $T_G = x T_{G-e}$ and $T_{G-e} = T_{G/e}$ (since deletion and contraction give equivalent graphs).

# Prerequisites
This is foundational.

# Key Properties
1. Removing a bridge increases the component count by 1
2. $T_G = x T_{G-e}$ (bridge contributes factor $x$)
3. $T_{G-e} = T_{G/e}$ when $e$ is a bridge
4. Bridges are always internally active (in spanning tree expansion)
5. Bridges carry no flow: $q_G(A) = 0$ if $G$ has a bridge

# Relationships
## Related
- **loop-in-multigraph** — Dual concept
- **deletion-contraction** — Bridge case of the recursion
- **tutte-polynomial** — Bridge gives factor $x$

## Contrasts With
- **loop-in-multigraph** — Loop gives factor $y$; bridge gives $x$

# Source Reference
Chapter X, Section X.1, pages 341-343.

# Verification Notes
- Definition source: Direct from pp. 341-343
- Confidence rationale: Implicit in recursion; well-established concept
- Uncertainties: None
- Cross-reference status: Verified
