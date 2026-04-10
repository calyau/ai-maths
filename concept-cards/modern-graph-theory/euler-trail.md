---
concept: Euler Trail
slug: euler-trail
category: paths-and-cycles
subcategory: hamilton-euler
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Fundamentals"
chapter_number: 1
pdf_page: 9
section: "I.3 Hamilton Cycles and Euler Circuits"
extraction_confidence: high
aliases:
  - Eulerian trail
prerequisites:
  - graph
  - trail
  - euler-circuit
extends:
  - trail
related:
  - euler-circuit
  - eulerian-graph
contrasts_with:
  - hamilton-path
answers_questions:
  - "What is an Euler trail?"
---

# Quick Definition

An Euler trail is a trail containing all edges of a graph. A connected graph has an Euler trail iff it has at most two vertices of odd degree.

# Core Definition

"A trail containing all edges is an Euler trail" (Bollobás, p. 25). A connected graph has an Euler trail if and only if it has exactly 0 or 2 vertices of odd degree. When there are 0 odd-degree vertices, the Euler trail is closed (an Euler circuit). When there are exactly 2, the trail runs between these two vertices.

# Prerequisites

- **Graph** — Euler trails are defined within graphs
- **Trail** — An Euler trail is a trail
- **Euler circuit** — A closed Euler trail

# Key Properties

1. Traverses every edge exactly once
2. May have different start and end vertices (unlike Euler circuit)
3. Exists iff the graph is connected and has 0 or 2 odd-degree vertices
4. Euler trails with start $\neq$ end have exactly 2 odd-degree vertices

# Construction / Recognition

1. Check connectivity
2. Count vertices of odd degree
3. If 0: Euler circuit exists; if 2: Euler trail between the two odd-degree vertices

# Context & Application

The Königsberg bridge problem asks for an Euler trail: a walk crossing every bridge exactly once. Since the associated multigraph has 4 vertices of odd degree, no such trail exists.

# Examples

**Example** (pp. 25-26): The Königsberg bridge multigraph has 4 vertices of odd degree, so no Euler trail (or circuit) exists.

# Relationships

## Builds Upon
- **Trail** — An Euler trail is a trail through all edges

## Related
- **Euler circuit** — A closed Euler trail

## Contrasts With
- **Hamilton path** — Visits all vertices; Euler trail uses all edges

# Common Errors

- **Error**: Assuming an Euler trail must start and end at the same vertex
  **Correction**: An Euler trail can have distinct endpoints (when exactly 2 odd-degree vertices exist)

# Common Confusions

- **Confusion**: Confusing Euler trail with Euler circuit
  **Clarification**: An Euler circuit is a closed Euler trail (same start and end)

# Source Reference

Chapter I: Fundamentals, Section I.3, pages 25-26.

# Verification Notes

- Definition source: Direct from p. 25
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
