---
concept: Light and Heavy Sets
slug: light-heavy-set
category: connectivity
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Connectivity"
chapter_number: 3
pdf_page: 84
section: "3.5 Linking pairs of vertices"
extraction_confidence: high
aliases:
  - "light set"
  - "heavy set"
prerequisites:
  - graph
extends: []
related:
  - thomas-wollan-theorem
contrasts_with: []
answers_questions:
  - "What are light and heavy sets in the Thomas-Wollan proof?"
---

# Quick Definition
A set U of vertices is light in G if ||U||+ <= 8k|U| (where ||U||+ counts edges with at least one end in U). A set is heavy if it is not light.

# Core Definition
Call a set U in V(G) **light** in G if ||U||+ <= 8k|U|, where ||U||+ denotes the number of edges of G with at least one end in U. A set of vertices is **heavy** if it is not light (Diestel, p. 84).

# Prerequisites
- **Graph** — light/heavy is defined for vertex sets in a graph

# Key Properties
1. Light sets have bounded edge density (at most 8k per vertex)
2. Heavy sets have high edge density
3. In the proof of Theorem 3.5.3: V \ X is assumed heavy
4. Small X-separations can only split light parts away from X
5. These conditions enable induction: if a part splits away, it is light, preserving the heavy assumption for the remaining graph

# Context & Application
Light and heavy sets are the key technical innovation in the Thomas-Wollan proof. They replace the exponential bound of Theorem 3.5.2 with a linear one by tracking edge density.

# Examples
**Example** (p. 84): The condition epsilon(G) >= 8k ensures ||V \ X||+ > 8k|V \ X|, so V \ X is heavy.

# Relationships
## Related
- **Thomas-Wollan theorem** — proof relies on light/heavy distinction

# Source Reference
Chapter 3, Section 3.5, p. 84 (pdf p. 84).

# Verification Notes
- Definition from p. 84
- Confidence: HIGH — explicitly defined
