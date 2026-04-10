---
concept: Planar Graph
slug: planar-graph
category: planar-graphs
subcategory: planarity
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Fundamentals"
chapter_number: 1
pdf_page: 9
section: "I.4 Planar Graphs"
extraction_confidence: high
aliases:
  - planar
prerequisites:
  - graph
extends: []
related:
  - plane-graph
  - eulers-formula
  - kuratowskis-theorem
contrasts_with: []
answers_questions:
  - "What is a planar graph?"
---

# Quick Definition

A graph is planar if it can be drawn in the plane with no two edges crossing. Equivalently, its topological realization $R(G)$ is homeomorphic to a subset of $\mathbb{R}^2$.

# Core Definition

A graph is planar if "it can be drawn in the plane in such a way that no two edges intersect" (Bollobás, p. 29). More rigorously, it has a drawing where vertices correspond to distinct points and edges to simple Jordan curves connecting endvertices, with curves either disjoint or meeting only at common endpoints. Equivalently, "a graph $G$ is planar if $R(G)$ is homeomorphic to a subset of $\mathbb{R}^2$" (p. 29).

# Prerequisites

- **Graph** — Planarity is a property of graphs

# Key Properties

1. A planar graph of order $n \ge 3$ has at most $3n - 6$ edges (Theorem 16)
2. A planar graph of girth $g$ has at most $\frac{g}{g-2}(n-2)$ edges (Theorem 16)
3. $K_5$ and $K_{3,3}$ are nonplanar
4. Every planar graph can be drawn with straight line segments as edges
5. Every planar graph can be drawn with piecewise linear edges

# Construction / Recognition

## To verify planarity
1. Check edge count: $e(G) \le 3n - 6$ (necessary but not sufficient)
2. Check for $TK_5$ or $TK_{3,3}$ subdivisions (Kuratowski's theorem)
3. Or check for $K_5$ or $K_{3,3}$ minors (Wagner's theorem)

# Context & Application

Planar graphs arise naturally in geographical map colouring, circuit board design, and any setting where connections must be made without crossings. The four-colour theorem states that every planar graph is 4-colourable.

# Examples

**Example** (p. 31): $K_5$ is nonplanar since $e(K_5) = 10 > 3(5) - 6 = 9$.

**Example** (p. 31): $K_{3,3}$ is nonplanar since its girth is 4 and $e(K_{3,3}) = 9 > \frac{4}{2}(6-2) = 8$.

# Relationships

## Builds Upon
- **Graph**

## Enables
- **Plane graph** — A specific planar embedding
- **Euler's formula** — Applies to plane graphs
- **Kuratowski's theorem** — Characterizes planarity
- **Wagner's theorem** — Characterizes planarity via minors

# Common Errors

- **Error**: Using the edge bound $e \le 3n - 6$ as sufficient for planarity
  **Correction**: This bound is necessary but not sufficient; many nonplanar graphs satisfy it

# Common Confusions

- **Confusion**: Confusing "planar graph" with "plane graph"
  **Clarification**: A planar graph can be drawn in the plane; a plane graph is a specific drawing in the plane

# Source Reference

Chapter I: Fundamentals, Section I.4, pages 29-32.

# Verification Notes

- Definition source: Direct from p. 29
- Confidence rationale: Explicitly defined with multiple characterizations
- Uncertainties: None
- Cross-reference status: Verified
