---
concept: Moore Graph
slug: moore-graph
category: extremal-graph-theory
subcategory: extremal-structures
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Extremal Problems"
chapter_number: 4
pdf_page: 110
section: "IV.1 Paths and Cycles"
extraction_confidence: high
aliases:
  - "Moore graph of degree δ and girth g"
prerequisites:
  - girth
extends: []
related:
  - petersen-graph
  - heawood-graph
contrasts_with: []
answers_questions:
  - "What is a Moore graph?"
---

# Quick Definition
A Moore graph is a graph achieving equality in the girth-degree-order bound of Theorem 1 — it has the minimum possible number of vertices for its degree and girth.

# Core Definition
Let $G_0$ be a graph achieving equality in Theorem 1 (the bound $n_0(g, \delta)$). Then $G_0$ is regular of degree $\delta$; if $g = 2d+1$, it has diameter $d$, and if $g = 2d$, every vertex is within distance $d-1$ of each pair of adjacent vertices. We call $G_0$ a Moore graph of degree $\delta$ and girth $g$ (or diameter $d$ if $g = 2d+1$) (Bollobás, p. 113).

# Prerequisites
- **Girth** — Moore graphs achieve the girth bound

# Key Properties
1. Regular of degree $\delta$
2. For odd girth $2d+1$: diameter exactly $d$
3. For even girth $2d$: every vertex within distance $d-1$ of adjacent pairs
4. Extremely rare; investigated further using algebraic methods in Chapter VIII

# Construction / Recognition
1. Check that $G$ is $\delta$-regular with girth $g$
2. Verify $|G| = n_0(g, \delta)$ (the Moore bound)

# Context & Application
Moore graphs are extremal objects in the degree-girth problem. They are rare and have rich algebraic structure.

# Examples
**Example** (p. 113): The Heawood graph (incidence graph of the Fano plane) is a Moore graph of degree 3 and girth 6.

**Example** (p. 113): The Petersen graph is a Moore graph of degree 3 and diameter 2 (girth 5).

# Relationships
## Builds Upon
- **girth** — Moore graphs achieve the girth bound

## Related
- **petersen-graph** — A Moore graph
- **heawood-graph** — A Moore graph

# Source Reference
Chapter IV, Section IV.1, page 113.

# Verification Notes
- Definition source: Direct from p. 113
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
