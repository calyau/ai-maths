---
concept: Edge Density Between Sets
slug: edge-density
category: regularity-method
subcategory: definitions
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Extremal Problems"
chapter_number: 4
pdf_page: 110
section: "IV.5 Szemerédi's Regularity Lemma"
extraction_confidence: high
aliases:
  - "d(X,Y)"
  - "bipartite density"
prerequisites: []
extends: []
related:
  - epsilon-uniform-pair
  - graph-density
contrasts_with: []
answers_questions:
  - "What is the edge density between two vertex sets?"
---

# Quick Definition
The edge density $d(X,Y)$ between disjoint vertex sets $X$ and $Y$ is $e(X,Y)/(|X||Y|)$, the ratio of actual to possible edges.

# Core Definition
Given a graph $G = (V,E)$ and disjoint non-empty sets $X, Y \subset V$, denote by $e(X,Y) = e_G(X,Y)$ the number of $X$-$Y$ edges, and write $d(X,Y) = d_G(X,Y) = e(X,Y)/(|X||Y|)$ for the density of the $X$-$Y$ edges (Bollobás, p. 139).

# Prerequisites
This is a foundational concept with no prerequisites within this source.

# Key Properties
1. $0 \le d(X,Y) \le 1$
2. $d(X,Y) = 0$ iff no edges between $X$ and $Y$
3. $d(X,Y) = 1$ iff every vertex of $X$ is joined to every vertex of $Y$
4. Key quantity for $\varepsilon$-uniformity

# Context & Application
Edge density is the fundamental quantity in the regularity lemma framework.

# Examples
**Example** (p. 139): For a random bipartite graph $G(X,Y,p)$, $d(X,Y) \approx p$.

# Relationships
## Enables
- **epsilon-uniform-pair** — Defined in terms of density stability

## Related
- **graph-density** — Overall graph density

# Source Reference
Chapter IV, Section IV.5, page 139.

# Verification Notes
- Definition source: Direct from p. 139
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
