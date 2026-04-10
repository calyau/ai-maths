---
concept: Loop in a Multigraph
slug: loop-in-multigraph
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
  - "self-loop"
prerequisites: []
extends: []
related:
  - bridge-in-multigraph
  - deletion-contraction
  - tutte-polynomial
contrasts_with:
  - bridge-in-multigraph
answers_questions:
  - "How do I compute the Tutte polynomial using deletion-contraction?"
---

# Quick Definition
A loop is an edge whose two endpoints are the same vertex. In the Tutte polynomial recursion: $T_G = y T_{G-e}$ when $e$ is a loop. Note $G/e = G - e$ for loops.

# Core Definition
A loop $\ell$ is an edge incident to a single vertex twice. "If $\ell$ is a loop then $G/\ell = G - \ell$" (Bollobás, p. 341). For loops: $T_G = y T_{G-e}$. Loops contribute to nullity: $n(G-e) = n(G) - 1$.

# Prerequisites
This is foundational.

# Key Properties
1. $G/e = G - e$ for a loop $e$
2. $T_G = y T_{G-e}$ (loop contributes factor $y$)
3. $p_G(x) = 0$ if $G$ has a loop (no proper colouring possible)
4. Loops are always externally active (in spanning tree expansion)
5. Loops contribute to nullity but not rank

# Relationships
## Related
- **bridge-in-multigraph** — Dual concept
- **deletion-contraction** — Loop case of the recursion

## Contrasts With
- **bridge-in-multigraph** — Bridge gives factor $x$; loop gives $y$

# Source Reference
Chapter X, Section X.1, pages 341-343.

# Verification Notes
- Definition source: Direct from pp. 341-343
- Confidence rationale: Explicit treatment
- Uncertainties: None
- Cross-reference status: Verified
