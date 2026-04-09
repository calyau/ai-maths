---
concept: Double Ray
slug: double-ray
category: infinite-graphs
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Infinite Graphs"
chapter_number: 8
pdf_page: 206
section: "8.1 Basic notions, facts and techniques"
extraction_confidence: high
aliases:
  - "two-way infinite path"
prerequisites:
  - graph
  - infinite-graph
  - ray
extends:
  - ray
related:
  - end-of-a-graph
contrasts_with:
  - ray
answers_questions:
  - "What is a double ray?"
---

# Quick Definition
A double ray is a two-way infinite path: an infinite graph with vertices ..., x_{-1}, x_0, x_1, ... and edges ..., x_{-1}x_0, x_0x_1, x_1x_2, .... It is the unique infinite 2-regular connected graph.

# Core Definition
A *double ray* is an infinite graph (V, E) of the form V = {..., x_{-1}, x_0, x_1, ...}, E = {..., x_{-1}x_0, x_0x_1, x_1x_2, ...}, where the x_n are assumed distinct (Diestel, p. 206). Up to isomorphism, there is only one double ray, and it is the unique infinite 2-regular connected graph.

# Prerequisites
- **Graph** — A double ray is a graph
- **Infinite graph** — A double ray is infinite
- **Ray** — A double ray contains two rays as subrays

# Key Properties
1. Up to isomorphism, there is exactly one double ray
2. Every vertex has degree exactly 2
3. It is the unique infinite 2-regular connected graph
4. A double ray contains two rays (one in each direction)
5. The two tails of a double ray may or may not belong to the same end

# Construction / Recognition
## To Construct a Double Ray
1. Start with vertex x_0
2. Extend in both directions: add x_1, x_{-1}, then x_2, x_{-2}, etc.
3. Add edges x_nx_{n+1} for all integers n

# Context & Application
Double rays arise naturally when considering infinite paths. In topological end space theory, a double ray whose two tails belong to different ends forms an arc in |G| between those two ends.

# Examples
**Example 1** (p. 213): The 2-way infinite ladder has two ends; each end contains one tail of the horizontal double rays.

# Relationships
## Builds Upon
- **Ray** — A double ray consists of two rays sharing a finite initial segment

## Related
- **End of a graph** — The two tails of a double ray may belong to the same or different ends

## Contrasts With
- **Ray** — A ray is infinite in only one direction

# Common Confusions
- **Confusion**: Assuming the two tails of a double ray always belong to different ends
  **Clarification**: They may belong to the same end if no finite separator separates them

# Source Reference
Chapter 8, Section 8.1, page 206.

# Verification Notes
- Definition directly from p. 206
- Confidence: HIGH — explicit formal definition
