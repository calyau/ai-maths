---
concept: "Veblen's Theorem"
slug: veblens-theorem
category: paths-and-cycles
subcategory: cycle-decomposition
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
  - edge partition into cycles
  - cycle decomposition theorem
prerequisites:
  - graph
  - cycle
  - vertex-degree
extends: []
related:
  - euler-circuit
  - eulerian-graph
contrasts_with: []
answers_questions:
  - "When can a graph's edges be partitioned into cycles?"
---

# Quick Definition

Veblen's theorem (1912) states that the edge set of a graph can be partitioned into cycles if and only if every vertex has even degree.

# Core Definition

"**Theorem 1.** The edge set of a graph can be partitioned into cycles if, and only if, every vertex has even degree" (Bollobás, p. 12). The proof constructs cycles greedily: find a maximal path, which must close into a cycle since all degrees are even, then remove its edges and repeat.

# Prerequisites

- **Graph** — The theorem applies to graphs
- **Cycle** — The partition is into cycles
- **Vertex degree** — The condition involves degree parity

# Key Properties

1. Necessity: if edges partition into cycles, each vertex in $k$ cycles has degree $2k$
2. Sufficiency: a greedy algorithm finds cycles one at a time
3. Also valid for multigraphs (with loops as 1-cycles, double edges as 2-cycles)
4. Directed version: edges partition into directed cycles iff $d^+(v) = d^-(v)$ for all $v$
5. Essentially equivalent to Theorem 12 (Euler's theorem) for connected graphs

# Construction / Recognition

1. Find a maximal path; it closes into a cycle (since all degrees $\ge 2$)
2. Remove the cycle's edges
3. The remaining graph still has all even degrees
4. Repeat until no edges remain

# Context & Application

This is the first theorem proved in the book. It is "practically the same" as Euler's theorem (Theorem 12): every Euler circuit partitions edges into cycles, and a connected graph whose edges partition into cycles has an Euler circuit by concatenation.

# Examples

**Example** (p. 12): The proof shows that if every vertex has even degree and $e(G) > 0$, then a maximal-length path from any vertex must close into a cycle.

# Relationships

## Builds Upon
- **Graph**, **Cycle**, **Vertex degree**

## Enables
- **Euler circuit** — For connected graphs, cycle decomposition implies Euler circuit existence

# Common Errors

- **Error**: Applying the theorem to graphs with odd-degree vertices
  **Correction**: All vertices must have even degree for the edge partition to exist

# Common Confusions

- **Confusion**: Thinking the cycle decomposition is unique
  **Clarification**: The decomposition may not be unique; the theorem guarantees existence, not uniqueness

# Source Reference

Chapter I: Fundamentals, Section I.1 Definitions, Theorem 1, pages 12-13.

# Verification Notes

- Definition source: Direct theorem statement from p. 12
- Confidence rationale: Explicitly stated with proof
- Uncertainties: None
- Cross-reference status: Verified
