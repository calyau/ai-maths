---
concept: Diameter and Radius
slug: diameter-and-radius
category: graph-fundamentals
subcategory: basic-definitions
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Fundamentals"
chapter_number: 1
pdf_page: 9
section: "I.2 Paths, Cycles, and Trees"
extraction_confidence: high
aliases:
  - diameter
  - radius
  - "diam G"
  - "rad G"
prerequisites:
  - graph
  - distance
  - connected-graph
extends:
  - distance
related:
  - spanning-tree
contrasts_with: []
answers_questions:
  - "What are the diameter and radius of a graph?"
---

# Quick Definition

The diameter $\text{diam}\,G = \max_{x,y} d(x,y)$ is the greatest distance between any two vertices. The radius $\text{rad}\,G = \min_x \max_y d(x,y)$ is the smallest eccentricity over all vertices.

# Core Definition

"$\text{diam}\,G = \max_{x,y} d(x,y)$ is called the diameter of $G$ and $\text{rad}\,G = \min_x \max_y d(x,y)$ is the radius of $G$" (Bollobás, p. 18).

# Prerequisites

- **Graph** — Defined for graphs
- **Distance** — Uses the distance function $d(x,y)$
- **Connected graph** — Meaningful for connected graphs

# Key Properties

1. $\text{rad}\,G \le \text{diam}\,G \le 2\,\text{rad}\,G$
2. Both are measured in terms of edge count (shortest path length)
3. A vertex $x$ achieving $\max_y d(x,y) = \text{rad}\,G$ is called a centre of $G$

# Construction / Recognition

To compute: find all pairwise distances (e.g., by BFS from each vertex). The diameter is the maximum; the radius is the minimum over vertices of their maximum distance to any other vertex.

# Context & Application

Diameter and radius measure the "spread" of a graph. A spanning tree can be constructed from a centre vertex with radius equal to the graph's radius.

# Examples

**Example** (p. 18): If a spanning tree $T$ is constructed from a vertex $x$ with $k = \text{rad}\,G$, then $T$ also has radius $k$.

# Relationships

## Builds Upon
- **Distance** — Diameter and radius are extremes of the distance function

## Enables
- Efficient spanning tree constructions
- Bounds on graph properties

# Common Errors

- **Error**: Confusing diameter (max-max) with radius (min-max)
  **Correction**: Diameter maximizes over all pairs; radius minimizes the eccentricity

# Common Confusions

- **Confusion**: Thinking diameter equals twice the radius
  **Clarification**: Only the inequality $\text{rad}\,G \le \text{diam}\,G \le 2\,\text{rad}\,G$ holds; equality is not guaranteed

# Source Reference

Chapter I: Fundamentals, Section I.2, page 18.

# Verification Notes

- Definition source: Direct from p. 18
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
