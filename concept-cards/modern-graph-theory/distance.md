---
concept: Distance
slug: distance
category: graph-fundamentals
subcategory: basic-definitions
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Fundamentals"
chapter_number: 1
pdf_page: 9
section: "I.1 Definitions"
extraction_confidence: high
aliases:
  - graph distance
  - "$d(x, y)$"
prerequisites:
  - graph
  - path
extends: []
related:
  - connected-graph
  - diameter-and-radius
contrasts_with: []
answers_questions:
  - "How is distance defined in a graph?"
---

# Quick Definition

The distance $d(x, y)$ between vertices $x$ and $y$ is the minimal length of an $x$-$y$ path. If no such path exists, $d(x, y) = \infty$.

# Core Definition

"Given vertices $x$ and $y$, their distance $d(x, y)$ is the minimal length of an $x$-$y$ path. If there is no $x$-$y$ path then $d(x, y) = \infty$" (Bollobás, p. 14).

# Prerequisites

- **Graph** — Distance is defined within a graph
- **Path** — Distance is the length of a shortest path

# Key Properties

1. $d(x, x) = 0$ for all $x$
2. $d(x, y) = d(y, x)$ (symmetry)
3. $d(x, z) \le d(x, y) + d(y, z)$ (triangle inequality)
4. $d(x, y) = \infty$ iff $x$ and $y$ are in different components
5. $d(x, y) < \infty$ iff $x$ and $y$ are in the same component

# Construction / Recognition

To compute $d(x, y)$: find a shortest $x$-$y$ path (e.g., by breadth-first search).

# Context & Application

Distance is a metric on the vertex set of a connected graph. It defines the diameter and radius of a graph and is used to construct spanning trees via distance layers $V_i = \{y : d(x, y) = i\}$.

# Examples

**Example** (p. 18): In the spanning tree construction, $V_i = \{y \in G : d(x, y) = i\}$ defines the distance layers from a chosen root vertex $x$.

# Relationships

## Builds Upon
- **Graph**, **Path**

## Enables
- **Connected graph** — Connected iff $d(x, y) < \infty$ for all pairs
- **Diameter and radius** — Defined in terms of distances
- **Spanning tree** — Can be constructed from distance layers

# Common Errors

- **Error**: Counting vertices instead of edges when computing distance
  **Correction**: Distance is the number of edges on a shortest path, not the number of vertices

# Common Confusions

- **Confusion**: Thinking distance must be finite
  **Clarification**: $d(x, y) = \infty$ when $x$ and $y$ are in different components

# Source Reference

Chapter I: Fundamentals, Section I.1 Definitions, page 14.

# Verification Notes

- Definition source: Direct from p. 14
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
